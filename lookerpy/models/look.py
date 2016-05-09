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


class Look(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Look - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'title': 'str',
            'user': 'UserIdOnly',
            'query_id': 'int',
            'description': 'str',
            'short_url': 'str',
            'space': 'SpaceBase',
            'public': 'bool',
            'public_slug': 'str',
            'user_id': 'int',
            'space_id': 'int',
            'model': 'str',
            'public_url': 'str',
            'embed_url': 'str',
            'image_embed_url': 'str',
            'google_spreadsheet_formula': 'str',
            'excel_file_url': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'user': 'user',
            'query_id': 'query_id',
            'description': 'description',
            'short_url': 'short_url',
            'space': 'space',
            'public': 'public',
            'public_slug': 'public_slug',
            'user_id': 'user_id',
            'space_id': 'space_id',
            'model': 'model',
            'public_url': 'public_url',
            'embed_url': 'embed_url',
            'image_embed_url': 'image_embed_url',
            'google_spreadsheet_formula': 'google_spreadsheet_formula',
            'excel_file_url': 'excel_file_url'
        }

        self._id = None
        self._title = None
        self._user = None
        self._query_id = None
        self._description = None
        self._short_url = None
        self._space = None
        self._public = None
        self._public_slug = None
        self._user_id = None
        self._space_id = None
        self._model = None
        self._public_url = None
        self._embed_url = None
        self._image_embed_url = None
        self._google_spreadsheet_formula = None
        self._excel_file_url = None

    @property
    def id(self):
        """
        Gets the id of this Look.
        Unique Id

        :return: The id of this Look.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Look.
        Unique Id

        :param id: The id of this Look.
        :type: int
        """
        
        self._id = id

    @property
    def title(self):
        """
        Gets the title of this Look.
        Look Title

        :return: The title of this Look.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Look.
        Look Title

        :param title: The title of this Look.
        :type: str
        """
        
        self._title = title

    @property
    def user(self):
        """
        Gets the user of this Look.
        User

        :return: The user of this Look.
        :rtype: UserIdOnly
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Look.
        User

        :param user: The user of this Look.
        :type: UserIdOnly
        """
        
        self._user = user

    @property
    def query_id(self):
        """
        Gets the query_id of this Look.
        Query Id

        :return: The query_id of this Look.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this Look.
        Query Id

        :param query_id: The query_id of this Look.
        :type: int
        """
        
        self._query_id = query_id

    @property
    def description(self):
        """
        Gets the description of this Look.
        Description

        :return: The description of this Look.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Look.
        Description

        :param description: The description of this Look.
        :type: str
        """
        
        self._description = description

    @property
    def short_url(self):
        """
        Gets the short_url of this Look.
        Short Url

        :return: The short_url of this Look.
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """
        Sets the short_url of this Look.
        Short Url

        :param short_url: The short_url of this Look.
        :type: str
        """
        
        self._short_url = short_url

    @property
    def space(self):
        """
        Gets the space of this Look.
        Space of this Look

        :return: The space of this Look.
        :rtype: SpaceBase
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this Look.
        Space of this Look

        :param space: The space of this Look.
        :type: SpaceBase
        """
        
        self._space = space

    @property
    def public(self):
        """
        Gets the public of this Look.
        Is Public

        :return: The public of this Look.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this Look.
        Is Public

        :param public: The public of this Look.
        :type: bool
        """
        
        self._public = public

    @property
    def public_slug(self):
        """
        Gets the public_slug of this Look.
        Public Slug

        :return: The public_slug of this Look.
        :rtype: str
        """
        return self._public_slug

    @public_slug.setter
    def public_slug(self, public_slug):
        """
        Sets the public_slug of this Look.
        Public Slug

        :param public_slug: The public_slug of this Look.
        :type: str
        """
        
        self._public_slug = public_slug

    @property
    def user_id(self):
        """
        Gets the user_id of this Look.
        (Write-only) User Id

        :return: The user_id of this Look.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Look.
        (Write-only) User Id

        :param user_id: The user_id of this Look.
        :type: int
        """
        
        self._user_id = user_id

    @property
    def space_id(self):
        """
        Gets the space_id of this Look.
        (Write-only) Space Id

        :return: The space_id of this Look.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """
        Sets the space_id of this Look.
        (Write-only) Space Id

        :param space_id: The space_id of this Look.
        :type: int
        """
        
        self._space_id = space_id

    @property
    def model(self):
        """
        Gets the model of this Look.
        Model

        :return: The model of this Look.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this Look.
        Model

        :param model: The model of this Look.
        :type: str
        """
        
        self._model = model

    @property
    def public_url(self):
        """
        Gets the public_url of this Look.
        Public Url

        :return: The public_url of this Look.
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """
        Sets the public_url of this Look.
        Public Url

        :param public_url: The public_url of this Look.
        :type: str
        """
        
        self._public_url = public_url

    @property
    def embed_url(self):
        """
        Gets the embed_url of this Look.
        Embed Url

        :return: The embed_url of this Look.
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """
        Sets the embed_url of this Look.
        Embed Url

        :param embed_url: The embed_url of this Look.
        :type: str
        """
        
        self._embed_url = embed_url

    @property
    def image_embed_url(self):
        """
        Gets the image_embed_url of this Look.
        Image Embed Url

        :return: The image_embed_url of this Look.
        :rtype: str
        """
        return self._image_embed_url

    @image_embed_url.setter
    def image_embed_url(self, image_embed_url):
        """
        Sets the image_embed_url of this Look.
        Image Embed Url

        :param image_embed_url: The image_embed_url of this Look.
        :type: str
        """
        
        self._image_embed_url = image_embed_url

    @property
    def google_spreadsheet_formula(self):
        """
        Gets the google_spreadsheet_formula of this Look.
        Google Spreadsheet Formula

        :return: The google_spreadsheet_formula of this Look.
        :rtype: str
        """
        return self._google_spreadsheet_formula

    @google_spreadsheet_formula.setter
    def google_spreadsheet_formula(self, google_spreadsheet_formula):
        """
        Sets the google_spreadsheet_formula of this Look.
        Google Spreadsheet Formula

        :param google_spreadsheet_formula: The google_spreadsheet_formula of this Look.
        :type: str
        """
        
        self._google_spreadsheet_formula = google_spreadsheet_formula

    @property
    def excel_file_url(self):
        """
        Gets the excel_file_url of this Look.
        Excel File Url

        :return: The excel_file_url of this Look.
        :rtype: str
        """
        return self._excel_file_url

    @excel_file_url.setter
    def excel_file_url(self, excel_file_url):
        """
        Sets the excel_file_url of this Look.
        Excel File Url

        :param excel_file_url: The excel_file_url of this Look.
        :type: str
        """
        
        self._excel_file_url = excel_file_url

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

