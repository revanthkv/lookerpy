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


class SamlMetadataParseResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SamlMetadataParseResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'idp_issuer': 'str',
            'idp_url': 'str',
            'idp_cert': 'str'
        }

        self.attribute_map = {
            'idp_issuer': 'idp_issuer',
            'idp_url': 'idp_url',
            'idp_cert': 'idp_cert'
        }

        self._idp_issuer = None
        self._idp_url = None
        self._idp_cert = None

    @property
    def idp_issuer(self):
        """
        Gets the idp_issuer of this SamlMetadataParseResult.
        Identify Provider Issuer

        :return: The idp_issuer of this SamlMetadataParseResult.
        :rtype: str
        """
        return self._idp_issuer

    @idp_issuer.setter
    def idp_issuer(self, idp_issuer):
        """
        Sets the idp_issuer of this SamlMetadataParseResult.
        Identify Provider Issuer

        :param idp_issuer: The idp_issuer of this SamlMetadataParseResult.
        :type: str
        """
        
        self._idp_issuer = idp_issuer

    @property
    def idp_url(self):
        """
        Gets the idp_url of this SamlMetadataParseResult.
        Identify Provider Url

        :return: The idp_url of this SamlMetadataParseResult.
        :rtype: str
        """
        return self._idp_url

    @idp_url.setter
    def idp_url(self, idp_url):
        """
        Sets the idp_url of this SamlMetadataParseResult.
        Identify Provider Url

        :param idp_url: The idp_url of this SamlMetadataParseResult.
        :type: str
        """
        
        self._idp_url = idp_url

    @property
    def idp_cert(self):
        """
        Gets the idp_cert of this SamlMetadataParseResult.
        Identify Provider Certificate

        :return: The idp_cert of this SamlMetadataParseResult.
        :rtype: str
        """
        return self._idp_cert

    @idp_cert.setter
    def idp_cert(self, idp_cert):
        """
        Sets the idp_cert of this SamlMetadataParseResult.
        Identify Provider Certificate

        :param idp_cert: The idp_cert of this SamlMetadataParseResult.
        :type: str
        """
        
        self._idp_cert = idp_cert

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

