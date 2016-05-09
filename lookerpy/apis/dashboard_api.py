# coding: utf-8

"""
DashboardApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DashboardApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def all_dashboards(self, **kwargs):
        """
        get all dashboards
        Get information about all dashboards.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_dashboards(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fieds.
        :return: list[DashboardBase]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_dashboards" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/dashboards'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[DashboardBase]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def copy_dashboards(self, **kwargs):
        """
        copy dashboards to space
        ### Copy dashboards with specified ids to space

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.copy_dashboards(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Dashboard body: dashboard
        :param str space_id: Destination space id.
        :param list[str] dashboard_ids: Dashboard ids to copy.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'space_id', 'dashboard_ids']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_dashboards" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/dashboards/copy'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'space_id' in params:
            query_params['space_id'] = params['space_id']
        if 'dashboard_ids' in params:
            query_params['dashboard_ids'] = params['dashboard_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_dashboard(self, **kwargs):
        """
        create dashboard
        ### Create a dashboard with specified information.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dashboard(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Dashboard body: dashboard
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/dashboards'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_dashboard_prefetch(self, dashboard_id, **kwargs):
        """
        create a prefetch
        ### Create a prefetch for a dashboard with the specified information. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_dashboard_prefetch(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param PrefetchDashboardRequestMapper body: Parameters for prefetch request
        :return: PrefetchDashboardRequestMapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `create_dashboard_prefetch`")


        resource_path = '/dashboards/{dashboard_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchDashboardRequestMapper',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def dashboard(self, dashboard_id, **kwargs):
        """
        get dashboard
        ### Get information about the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.dashboard(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param str fields: Requested fields.
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard`")


        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def dashboard_prefetch(self, dashboard_id, **kwargs):
        """
        get a prefetch
        ### Get a prefetch for a dashboard with the specified information. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.dashboard_prefetch(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param list[PrefetchDashboardFilterValue] dashboard_filters: JSON encoded string of Dashboard filters that were applied to prefetch
        :return: PrefetchMapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'dashboard_filters']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `dashboard_prefetch`")


        resource_path = '/dashboards/{dashboard_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}
        if 'dashboard_filters' in params:
            query_params['dashboard_filters'] = params['dashboard_filters']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchMapper',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def dashboards_move_plan(self, **kwargs):
        """
        plan for moving dashboards to space
        ### Plan for moving dashboards with specified ids.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.dashboards_move_plan(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str space_id: Destination space id.
        :param list[str] dashboard_ids: Dashboard ids to move.
        :return: LookMovePlan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'dashboard_ids']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboards_move_plan" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/dashboards/move_plan'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'space_id' in params:
            query_params['space_id'] = params['space_id']
        if 'dashboard_ids' in params:
            query_params['dashboard_ids'] = params['dashboard_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LookMovePlan',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_dashboard(self, dashboard_id, **kwargs):
        """
        delete dashboard
        ### Delete the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_dashboard(dashboard_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `delete_dashboard`")


        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def move_dashboards(self, body, **kwargs):
        """
        move dashboards to space
        ### Move dashboards with specified ids to space

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_dashboards(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Dashboard body: dashboard (required)
        :param str space_id: Destination space id.
        :param list[str] dashboard_ids: Dashboard ids to move.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'space_id', 'dashboard_ids']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_dashboards" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `move_dashboards`")


        resource_path = '/dashboards/move'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'space_id' in params:
            query_params['space_id'] = params['space_id']
        if 'dashboard_ids' in params:
            query_params['dashboard_ids'] = params['dashboard_ids']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_dashboard(self, dashboard_id, body, **kwargs):
        """
        update dashboard
        ### Update the dashboard with a specific id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_dashboard(dashboard_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str dashboard_id: Id of dashboard (required)
        :param Dashboard body: dashboard (required)
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_dashboard" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params) or (params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `update_dashboard`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_dashboard`")


        resource_path = '/dashboards/{dashboard_id}'.replace('{format}', 'json')
        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Dashboard',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
