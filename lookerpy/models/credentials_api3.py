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


class CredentialsApi3(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CredentialsApi3 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'client_id': 'str',
            'created_at': 'str',
            'is_disabled': 'bool',
            'type': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'client_id': 'client_id',
            'created_at': 'created_at',
            'is_disabled': 'is_disabled',
            'type': 'type',
            'url': 'url'
        }

        self._id = None
        self._client_id = None
        self._created_at = None
        self._is_disabled = None
        self._type = None
        self._url = None

    @property
    def id(self):
        """
        Gets the id of this CredentialsApi3.
        Unique Id

        :return: The id of this CredentialsApi3.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CredentialsApi3.
        Unique Id

        :param id: The id of this CredentialsApi3.
        :type: int
        """
        
        self._id = id

    @property
    def client_id(self):
        """
        Gets the client_id of this CredentialsApi3.
        API key client_id

        :return: The client_id of this CredentialsApi3.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CredentialsApi3.
        API key client_id

        :param client_id: The client_id of this CredentialsApi3.
        :type: str
        """
        
        self._client_id = client_id

    @property
    def created_at(self):
        """
        Gets the created_at of this CredentialsApi3.
        Timestamp for the creation of this credential

        :return: The created_at of this CredentialsApi3.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CredentialsApi3.
        Timestamp for the creation of this credential

        :param created_at: The created_at of this CredentialsApi3.
        :type: str
        """
        
        self._created_at = created_at

    @property
    def is_disabled(self):
        """
        Gets the is_disabled of this CredentialsApi3.
        Has this credential been disabled?

        :return: The is_disabled of this CredentialsApi3.
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """
        Sets the is_disabled of this CredentialsApi3.
        Has this credential been disabled?

        :param is_disabled: The is_disabled of this CredentialsApi3.
        :type: bool
        """
        
        self._is_disabled = is_disabled

    @property
    def type(self):
        """
        Gets the type of this CredentialsApi3.
        Short name for the type of this kind of credential

        :return: The type of this CredentialsApi3.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CredentialsApi3.
        Short name for the type of this kind of credential

        :param type: The type of this CredentialsApi3.
        :type: str
        """
        
        self._type = type

    @property
    def url(self):
        """
        Gets the url of this CredentialsApi3.
        Link to get this item

        :return: The url of this CredentialsApi3.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this CredentialsApi3.
        Link to get this item

        :param url: The url of this CredentialsApi3.
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

