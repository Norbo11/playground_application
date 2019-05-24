import uuid
import time
import random
import math
import multiprocessing
import logging
from multiprocessing import Queue, Process
from playground_application.models import Driver as DriverModel, Location, FindRideRequest, FindRideResponse

logger = logging.getLogger("ride_hailing_logger")


class Driver(DriverModel):

    def __init__(self):
        super().__init__()

        self.current_location = Location(
            x=random.randint(1, 100),
            y=random.randint(1, 100)
        )

        self.rating = int(random.random() * 5)


class MapLocationService(object):

    def compute_distance_km(self, a, b):
        time.sleep(1)
        print(type(a))
        print(type(b))
        return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))


class DriverAvailabilityService(object):

    def __init__(self, map_location_client):
        self.available_drivers = []
        self.map_location_client = map_location_client

    def add_available_driver(self, driver):
        self.available_drivers.append(driver)

    def remove_available_driver(self, driver):
        self.available_drivers.remove(driver)

    def find_driver_candidates(self, start_location):
        key = lambda driver: self.map_location_client.compute_distance_km(driver.current_location, start_location)
        sorted_by_distance = sorted(self.available_drivers, key=key, reverse=True)

        return sorted_by_distance[:5]


class DriverMatchingService(object):

    def __init__(self, driver_availability_client):
        self.driver_availability_client = driver_availability_client

    def find_driver(self, ride_info):
        candidates = self.driver_availability_client.find_driver_candidates(ride_info.start_location)

        if len(candidates) > 0:
            sorted_by_rating = sorted(candidates, key=lambda driver: driver.rating, reverse=True)
            return sorted_by_rating[0]
        else:
            return None


class DriverOperationsService(object):

    def __init__(self):
        self.rides = []

    def ask_for_ride(self, driver, ride_info):
        time.sleep(random.randint(1, 4))
        return random.random() > 0.5

    def create_ride(self, driver, ride_info):
        ride = {
            'driver': driver,
            'ride_info': ride_info
        }

        return ride


class PricingService(object):

    def __init__(self):
        pass

    def compute_cost_based_on_distance(self, distance_km):
        if distance_km <= 5:
            cost_dollars = 5
        elif distance_km < 15:
            cost_dollars = distance_km
        else:
            cost_dollars = distance_km * 0.7

        return cost_dollars


class RideService(object):

    def __init__(self, driver_matching_client, driver_operations_client, map_location_client, pricing_client):
        self.driver_matching_client = driver_matching_client
        self.driver_operations_client = driver_operations_client
        self.map_location_client = map_location_client
        self.pricing_client = pricing_client

    def find_ride(self, find_ride_request):
        # find_ride_request.id = str(uuid.uuid4())

        distance_km = self.map_location_client.compute_distance_km(find_ride_request.start_location, find_ride_request.end_location)
        estimated_price = self.pricing_client.compute_cost_based_on_distance(distance_km)

        driver_accepted = False
        candidate = None

        drivers_declined = 0

        while driver_accepted is False:
            while candidate is None:
                candidate = self.driver_matching_client.find_driver(find_ride_request)

            driver_accepted = self.driver_operations_client.ask_for_ride(candidate, find_ride_request)
            if not driver_accepted:
                drivers_declined += 1

        logger.info(f"{drivers_declined} drivers declined before a ride could be found")
        ride = self.driver_operations_client.create_ride(candidate, find_ride_request)
        return FindRideResponse(driver=ride['driver'], estimated_cost=estimated_price)


map_location_client = MapLocationService()
driver_availability_client = DriverAvailabilityService(map_location_client)
driver_matching_client = DriverMatchingService(driver_availability_client)
driver_operations_client = DriverOperationsService()
pricing_client = PricingService()
ride_client = RideService(driver_matching_client, driver_operations_client, map_location_client, pricing_client)

driver_availability_client.add_available_driver(Driver())
driver_availability_client.add_available_driver(Driver())
driver_availability_client.add_available_driver(Driver())


def find_ride(body):
    find_ride_request = FindRideRequest.from_dict(body)
    find_ride_response = ride_client.find_ride(find_ride_request)
    return find_ride_response.to_dict()







