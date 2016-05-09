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


class LegacyFeature(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LegacyFeature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'description': 'str',
            'enabled_locally': 'bool',
            'enabled': 'bool',
            'disallowed_as_of_version': 'str',
            'end_of_life_version': 'str',
            'documentation_url': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'enabled_locally': 'enabled_locally',
            'enabled': 'enabled',
            'disallowed_as_of_version': 'disallowed_as_of_version',
            'end_of_life_version': 'end_of_life_version',
            'documentation_url': 'documentation_url',
            'url': 'url'
        }

        self._id = None
        self._name = None
        self._description = None
        self._enabled_locally = None
        self._enabled = None
        self._disallowed_as_of_version = None
        self._end_of_life_version = None
        self._documentation_url = None
        self._url = None

    @property
    def id(self):
        """
        Gets the id of this LegacyFeature.
        Unique Id

        :return: The id of this LegacyFeature.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LegacyFeature.
        Unique Id

        :param id: The id of this LegacyFeature.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LegacyFeature.
        Name

        :return: The name of this LegacyFeature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LegacyFeature.
        Name

        :param name: The name of this LegacyFeature.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LegacyFeature.
        Description

        :return: The description of this LegacyFeature.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LegacyFeature.
        Description

        :param description: The description of this LegacyFeature.
        :type: str
        """
        
        self._description = description

    @property
    def enabled_locally(self):
        """
        Gets the enabled_locally of this LegacyFeature.
        Whether this feature has been enabled by a user

        :return: The enabled_locally of this LegacyFeature.
        :rtype: bool
        """
        return self._enabled_locally

    @enabled_locally.setter
    def enabled_locally(self, enabled_locally):
        """
        Sets the enabled_locally of this LegacyFeature.
        Whether this feature has been enabled by a user

        :param enabled_locally: The enabled_locally of this LegacyFeature.
        :type: bool
        """
        
        self._enabled_locally = enabled_locally

    @property
    def enabled(self):
        """
        Gets the enabled of this LegacyFeature.
        Whether this feature is currently enabled

        :return: The enabled of this LegacyFeature.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this LegacyFeature.
        Whether this feature is currently enabled

        :param enabled: The enabled of this LegacyFeature.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def disallowed_as_of_version(self):
        """
        Gets the disallowed_as_of_version of this LegacyFeature.
        Looker version where this feature became a legacy feature

        :return: The disallowed_as_of_version of this LegacyFeature.
        :rtype: str
        """
        return self._disallowed_as_of_version

    @disallowed_as_of_version.setter
    def disallowed_as_of_version(self, disallowed_as_of_version):
        """
        Sets the disallowed_as_of_version of this LegacyFeature.
        Looker version where this feature became a legacy feature

        :param disallowed_as_of_version: The disallowed_as_of_version of this LegacyFeature.
        :type: str
        """
        
        self._disallowed_as_of_version = disallowed_as_of_version

    @property
    def end_of_life_version(self):
        """
        Gets the end_of_life_version of this LegacyFeature.
        Future Looker version where this feature will be removed

        :return: The end_of_life_version of this LegacyFeature.
        :rtype: str
        """
        return self._end_of_life_version

    @end_of_life_version.setter
    def end_of_life_version(self, end_of_life_version):
        """
        Sets the end_of_life_version of this LegacyFeature.
        Future Looker version where this feature will be removed

        :param end_of_life_version: The end_of_life_version of this LegacyFeature.
        :type: str
        """
        
        self._end_of_life_version = end_of_life_version

    @property
    def documentation_url(self):
        """
        Gets the documentation_url of this LegacyFeature.
        URL for documentation about this feature

        :return: The documentation_url of this LegacyFeature.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """
        Sets the documentation_url of this LegacyFeature.
        URL for documentation about this feature

        :param documentation_url: The documentation_url of this LegacyFeature.
        :type: str
        """
        
        self._documentation_url = documentation_url

    @property
    def url(self):
        """
        Gets the url of this LegacyFeature.
        Link to get this item

        :return: The url of this LegacyFeature.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this LegacyFeature.
        Link to get this item

        :param url: The url of this LegacyFeature.
        :type: str
        """
        
        self._url = url

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

