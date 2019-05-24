# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from playground_application.models.base_model_ import Model
from playground_application.models.location import Location
from playground_application import util

from playground_application.models.location import Location  # noqa: E501

class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start_location=None, end_location=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param start_location: The start_location of this InlineObject.  # noqa: E501
        :type start_location: Location
        :param end_location: The end_location of this InlineObject.  # noqa: E501
        :type end_location: Location
        """
        self.openapi_types = {
            'start_location': Location,
            'end_location': Location
        }

        self.attribute_map = {
            'start_location': 'start_location',
            'end_location': 'end_location'
        }

        self._start_location = start_location
        self._end_location = end_location

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start_location(self):
        """Gets the start_location of this InlineObject.


        :return: The start_location of this InlineObject.
        :rtype: Location
        """
        return self._start_location

    @start_location.setter
    def start_location(self, start_location):
        """Sets the start_location of this InlineObject.


        :param start_location: The start_location of this InlineObject.
        :type start_location: Location
        """

        self._start_location = start_location

    @property
    def end_location(self):
        """Gets the end_location of this InlineObject.


        :return: The end_location of this InlineObject.
        :rtype: Location
        """
        return self._end_location

    @end_location.setter
    def end_location(self, end_location):
        """Sets the end_location of this InlineObject.


        :param end_location: The end_location of this InlineObject.
        :type end_location: Location
        """

        self._end_location = end_location