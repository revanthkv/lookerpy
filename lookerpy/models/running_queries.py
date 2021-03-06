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


class RunningQueries(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RunningQueries - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'user': 'UserPublic',
            'created_at': 'str',
            'completed_at': 'str',
            'query_id': 'str',
            'source': 'str',
            'node_id': 'str',
            'slug': 'str',
            'query_task_id': 'str',
            'cache_key': 'str',
            'connection_name': 'str',
            'dialect': 'str',
            'connection_id': 'str',
            'message': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'created_at': 'created_at',
            'completed_at': 'completed_at',
            'query_id': 'query_id',
            'source': 'source',
            'node_id': 'node_id',
            'slug': 'slug',
            'query_task_id': 'query_task_id',
            'cache_key': 'cache_key',
            'connection_name': 'connection_name',
            'dialect': 'dialect',
            'connection_id': 'connection_id',
            'message': 'message',
            'status': 'status'
        }

        self._id = None
        self._user = None
        self._created_at = None
        self._completed_at = None
        self._query_id = None
        self._source = None
        self._node_id = None
        self._slug = None
        self._query_task_id = None
        self._cache_key = None
        self._connection_name = None
        self._dialect = None
        self._connection_id = None
        self._message = None
        self._status = None

    @property
    def id(self):
        """
        Gets the id of this RunningQueries.
        Unique Id

        :return: The id of this RunningQueries.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RunningQueries.
        Unique Id

        :param id: The id of this RunningQueries.
        :type: int
        """
        
        self._id = id

    @property
    def user(self):
        """
        Gets the user of this RunningQueries.
        User who initiated the query

        :return: The user of this RunningQueries.
        :rtype: UserPublic
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this RunningQueries.
        User who initiated the query

        :param user: The user of this RunningQueries.
        :type: UserPublic
        """
        
        self._user = user

    @property
    def created_at(self):
        """
        Gets the created_at of this RunningQueries.
        Date/Time Query was initiated

        :return: The created_at of this RunningQueries.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this RunningQueries.
        Date/Time Query was initiated

        :param created_at: The created_at of this RunningQueries.
        :type: str
        """
        
        self._created_at = created_at

    @property
    def completed_at(self):
        """
        Gets the completed_at of this RunningQueries.
        Date/Time Query was completed

        :return: The completed_at of this RunningQueries.
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """
        Sets the completed_at of this RunningQueries.
        Date/Time Query was completed

        :param completed_at: The completed_at of this RunningQueries.
        :type: str
        """
        
        self._completed_at = completed_at

    @property
    def query_id(self):
        """
        Gets the query_id of this RunningQueries.
        Query Id

        :return: The query_id of this RunningQueries.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """
        Sets the query_id of this RunningQueries.
        Query Id

        :param query_id: The query_id of this RunningQueries.
        :type: str
        """
        
        self._query_id = query_id

    @property
    def source(self):
        """
        Gets the source of this RunningQueries.
        Source (look, dashboard, queryrunner, explore, etc.)

        :return: The source of this RunningQueries.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this RunningQueries.
        Source (look, dashboard, queryrunner, explore, etc.)

        :param source: The source of this RunningQueries.
        :type: str
        """
        
        self._source = source

    @property
    def node_id(self):
        """
        Gets the node_id of this RunningQueries.
        Node Id

        :return: The node_id of this RunningQueries.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this RunningQueries.
        Node Id

        :param node_id: The node_id of this RunningQueries.
        :type: str
        """
        
        self._node_id = node_id

    @property
    def slug(self):
        """
        Gets the slug of this RunningQueries.
        Slug

        :return: The slug of this RunningQueries.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this RunningQueries.
        Slug

        :param slug: The slug of this RunningQueries.
        :type: str
        """
        
        self._slug = slug

    @property
    def query_task_id(self):
        """
        Gets the query_task_id of this RunningQueries.
        ID of a Query Task

        :return: The query_task_id of this RunningQueries.
        :rtype: str
        """
        return self._query_task_id

    @query_task_id.setter
    def query_task_id(self, query_task_id):
        """
        Sets the query_task_id of this RunningQueries.
        ID of a Query Task

        :param query_task_id: The query_task_id of this RunningQueries.
        :type: str
        """
        
        self._query_task_id = query_task_id

    @property
    def cache_key(self):
        """
        Gets the cache_key of this RunningQueries.
        Cache Key

        :return: The cache_key of this RunningQueries.
        :rtype: str
        """
        return self._cache_key

    @cache_key.setter
    def cache_key(self, cache_key):
        """
        Sets the cache_key of this RunningQueries.
        Cache Key

        :param cache_key: The cache_key of this RunningQueries.
        :type: str
        """
        
        self._cache_key = cache_key

    @property
    def connection_name(self):
        """
        Gets the connection_name of this RunningQueries.
        Connection

        :return: The connection_name of this RunningQueries.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """
        Sets the connection_name of this RunningQueries.
        Connection

        :param connection_name: The connection_name of this RunningQueries.
        :type: str
        """
        
        self._connection_name = connection_name

    @property
    def dialect(self):
        """
        Gets the dialect of this RunningQueries.
        Dialect

        :return: The dialect of this RunningQueries.
        :rtype: str
        """
        return self._dialect

    @dialect.setter
    def dialect(self, dialect):
        """
        Sets the dialect of this RunningQueries.
        Dialect

        :param dialect: The dialect of this RunningQueries.
        :type: str
        """
        
        self._dialect = dialect

    @property
    def connection_id(self):
        """
        Gets the connection_id of this RunningQueries.
        Connection ID

        :return: The connection_id of this RunningQueries.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this RunningQueries.
        Connection ID

        :param connection_id: The connection_id of this RunningQueries.
        :type: str
        """
        
        self._connection_id = connection_id

    @property
    def message(self):
        """
        Gets the message of this RunningQueries.
        Additional Information(Error message or verbose status)

        :return: The message of this RunningQueries.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this RunningQueries.
        Additional Information(Error message or verbose status)

        :param message: The message of this RunningQueries.
        :type: str
        """
        
        self._message = message

    @property
    def status(self):
        """
        Gets the status of this RunningQueries.
        Status description

        :return: The status of this RunningQueries.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RunningQueries.
        Status description

        :param status: The status of this RunningQueries.
        :type: str
        """
        
        self._status = status

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

