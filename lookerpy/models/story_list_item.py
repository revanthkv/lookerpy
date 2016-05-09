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


class StoryListItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoryListItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'file_id': 'str',
            'project': 'ProjectListItem'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'file_id': 'file_id',
            'project': 'project'
        }

        self._id = None
        self._title = None
        self._file_id = None
        self._project = None

    @property
    def id(self):
        """
        Gets the id of this StoryListItem.
        Unique Id

        :return: The id of this StoryListItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoryListItem.
        Unique Id

        :param id: The id of this StoryListItem.
        :type: str
        """
        
        self._id = id

    @property
    def title(self):
        """
        Gets the title of this StoryListItem.


        :return: The title of this StoryListItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this StoryListItem.


        :param title: The title of this StoryListItem.
        :type: str
        """
        
        self._title = title

    @property
    def file_id(self):
        """
        Gets the file_id of this StoryListItem.


        :return: The file_id of this StoryListItem.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """
        Sets the file_id of this StoryListItem.


        :param file_id: The file_id of this StoryListItem.
        :type: str
        """
        
        self._file_id = file_id

    @property
    def project(self):
        """
        Gets the project of this StoryListItem.


        :return: The project of this StoryListItem.
        :rtype: ProjectListItem
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this StoryListItem.


        :param project: The project of this StoryListItem.
        :type: ProjectListItem
        """
        
        self._project = project

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

