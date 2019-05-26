import uuid
import time
import random
import math
import multiprocessing
import logging
from datetime import datetime, timedelta

from flask import current_app as flask_app
from multiprocessing import Queue, Process
from playground_application.models import Driver as DriverModel, Location, FindRideRequest, FindRideResponse


class DriverNotFoundException(Exception):
    pass


class GoogleMapsService(object):

    def authenticate(self):
        time.sleep(4)
        return str(uuid.uuid4())

    def compute_distance_km(self, auth_token, a, b):
        time.sleep(0.5)
        return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))


class Driver(DriverModel):

    def __init__(self):
        super().__init__()

        self.current_location = Location(
            x=random.randint(1, 100),
            y=random.randint(1, 100)
        )

        self.rating = int(random.random() * 5)


class MapLocationService(object):

    def __init__(self, google_maps_client):
        self.last_auth_token = None
        self.last_auth_time = datetime.min
        self.google_maps_client = google_maps_client

    def compute_distance_km(self, a, b):
        if datetime.now() - self.last_auth_time > timedelta(hours=1):
            self.last_auth_token = self.google_maps_client.authenticate()
            self.last_auth_time = datetime.now()

        return self.google_maps_client.compute_distance_km(self.last_auth_token, a, b)


class DriverMatchingService(object):

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
        sorted_by_rating = sorted(sorted_by_distance, key=lambda driver: driver.rating, reverse=True)

        return sorted_by_rating


class DriverOperationsService(object):

    def __init__(self):
        self.rides = []

    def ask_for_ride(self, driver, ride_info):
        time.sleep(random.randint(1, 3))
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
        # Estimate the price of the ride
        distance_km = self.map_location_client.compute_distance_km(find_ride_request.start_location, find_ride_request.end_location)
        estimated_price = self.pricing_client.compute_cost_based_on_distance(distance_km)

        driver_accepted = False
        drivers_declined = 0

        # Get driver candidates
        candidates = self.driver_matching_client.find_driver_candidates(find_ride_request.start_location)
        chosen_driver = None

        # Find the first one which accepts
        for candidate in candidates:
            driver_accepted = self.driver_operations_client.ask_for_ride(candidate, find_ride_request)
            if driver_accepted:
                chosen_driver = candidate
                break
            else:
                drivers_declined += 1

        # If we still haven't found a driver
        if chosen_driver == False:
            raise DriverNotFoundException(f"All {len(candidates)} drivers declined the ride")

        # Happy journey!
        flask_app.logger.info(f"{drivers_declined} drivers declined before a ride could be found")
        self.driver_operations_client.create_ride(chosen_driver, find_ride_request)
        return FindRideResponse(driver=chosen_driver, estimated_cost=estimated_price)
















google_maps_client = GoogleMapsService()
map_location_client = MapLocationService(google_maps_client)
driver_matching_client = DriverMatchingService(map_location_client)
driver_operations_client = DriverOperationsService()
pricing_client = PricingService()
ride_client = RideService(driver_matching_client, driver_operations_client, map_location_client, pricing_client)

driver_matching_client.add_available_driver(Driver())
driver_matching_client.add_available_driver(Driver())
driver_matching_client.add_available_driver(Driver())


def find_ride(body):
    find_ride_request = FindRideRequest.from_dict(body)
    find_ride_response = ride_client.find_ride(find_ride_request)
    return find_ride_response.to_dict()







