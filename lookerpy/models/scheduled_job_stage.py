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


class ScheduledJobStage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScheduledJobStage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'scheduled_job_id': 'int',
            'node_id': 'int',
            'stage': 'str',
            'started_at': 'datetime',
            'completed_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'scheduled_job_id': 'scheduled_job_id',
            'node_id': 'node_id',
            'stage': 'stage',
            'started_at': 'started_at',
            'completed_at': 'completed_at'
        }

        self._id = None
        self._scheduled_job_id = None
        self._node_id = None
        self._stage = None
        self._started_at = None
        self._completed_at = None

    @property
    def id(self):
        """
        Gets the id of this ScheduledJobStage.
        Unique Id

        :return: The id of this ScheduledJobStage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledJobStage.
        Unique Id

        :param id: The id of this ScheduledJobStage.
        :type: int
        """
        
        self._id = id

    @property
    def scheduled_job_id(self):
        """
        Gets the scheduled_job_id of this ScheduledJobStage.
        Job this stage describes

        :return: The scheduled_job_id of this ScheduledJobStage.
        :rtype: int
        """
        return self._scheduled_job_id

    @scheduled_job_id.setter
    def scheduled_job_id(self, scheduled_job_id):
        """
        Sets the scheduled_job_id of this ScheduledJobStage.
        Job this stage describes

        :param scheduled_job_id: The scheduled_job_id of this ScheduledJobStage.
        :type: int
        """
        
        self._scheduled_job_id = scheduled_job_id

    @property
    def node_id(self):
        """
        Gets the node_id of this ScheduledJobStage.
        Node Id stage was run on

        :return: The node_id of this ScheduledJobStage.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this ScheduledJobStage.
        Node Id stage was run on

        :param node_id: The node_id of this ScheduledJobStage.
        :type: int
        """
        
        self._node_id = node_id

    @property
    def stage(self):
        """
        Gets the stage of this ScheduledJobStage.
        Stage

        :return: The stage of this ScheduledJobStage.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """
        Sets the stage of this ScheduledJobStage.
        Stage

        :param stage: The stage of this ScheduledJobStage.
        :type: str
        """
        
        self._stage = stage

    @property
    def started_at(self):
        """
        Gets the started_at of this ScheduledJobStage.
        Time when the stage was started

        :return: The started_at of this ScheduledJobStage.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this ScheduledJobStage.
        Time when the stage was started

        :param started_at: The started_at of this ScheduledJobStage.
        :type: datetime
        """
        
        self._started_at = started_at

    @property
    def completed_at(self):
        """
        Gets the completed_at of this ScheduledJobStage.
        Time whent the stage was completed

        :return: The completed_at of this ScheduledJobStage.
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """
        Sets the completed_at of this ScheduledJobStage.
        Time whent the stage was completed

        :param completed_at: The completed_at of this ScheduledJobStage.
        :type: datetime
        """
        
        self._completed_at = completed_at

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
