# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ScheduledJobDestination(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScheduledJobDestination - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'scheduled_job_id': 'int',
            'format': 'str',
            'address': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'scheduled_job_id': 'scheduled_job_id',
            'format': 'format',
            'address': 'address',
            'type': 'type'
        }

        self._id = None
        self._scheduled_job_id = None
        self._format = None
        self._address = None
        self._type = None

    @property
    def id(self):
        """
        Gets the id of this ScheduledJobDestination.
        Unique Id

        :return: The id of this ScheduledJobDestination.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledJobDestination.
        Unique Id

        :param id: The id of this ScheduledJobDestination.
        :type: int
        """
        
        self._id = id

    @property
    def scheduled_job_id(self):
        """
        Gets the scheduled_job_id of this ScheduledJobDestination.
        Id of scheduled job

        :return: The scheduled_job_id of this ScheduledJobDestination.
        :rtype: int
        """
        return self._scheduled_job_id

    @scheduled_job_id.setter
    def scheduled_job_id(self, scheduled_job_id):
        """
        Sets the scheduled_job_id of this ScheduledJobDestination.
        Id of scheduled job

        :param scheduled_job_id: The scheduled_job_id of this ScheduledJobDestination.
        :type: int
        """
        
        self._scheduled_job_id = scheduled_job_id

    @property
    def format(self):
        """
        Gets the format of this ScheduledJobDestination.
        Format requested by the given destination (i.e. PDF, etc.)

        :return: The format of this ScheduledJobDestination.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this ScheduledJobDestination.
        Format requested by the given destination (i.e. PDF, etc.)

        :param format: The format of this ScheduledJobDestination.
        :type: str
        """
        
        self._format = format

    @property
    def address(self):
        """
        Gets the address of this ScheduledJobDestination.
        Address for recipient (only email addresses supported for now)

        :return: The address of this ScheduledJobDestination.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ScheduledJobDestination.
        Address for recipient (only email addresses supported for now)

        :param address: The address of this ScheduledJobDestination.
        :type: str
        """
        
        self._address = address

    @property
    def type(self):
        """
        Gets the type of this ScheduledJobDestination.
        Type of the address (only 'email' is supported for now)

        :return: The type of this ScheduledJobDestination.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ScheduledJobDestination.
        Type of the address (only 'email' is supported for now)

        :param type: The type of this ScheduledJobDestination.
        :type: str
        """
        
        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
