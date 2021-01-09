# Copyright 2021 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# coding: utf-8

"""
    Device Connect

    Device facing API for managing persistent device connections.   # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@mender.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from devices_api.api_client import ApiClient
from devices_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DevicesAPIClient(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def connect(self, **kwargs):  # noqa: E501
        """Connect the device and make it available to the server.   # noqa: E501

        Calling /connect will upgrade the connection to a persistent websocket connection and making the device available to the management api. The device must provide it's identity using the DeviceJWT either as Authorization header or as a cookie named 'JWT'.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str connection: Standard websocket request header.
        :param str upgrade: Standard websocket request header.
        :param str sec_websocket_key: Standard websocket request header.
        :param int sec_websocket_version: Standard websocket request header.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.connect_with_http_info(**kwargs)  # noqa: E501

    def connect_with_http_info(self, **kwargs):  # noqa: E501
        """Connect the device and make it available to the server.   # noqa: E501

        Calling /connect will upgrade the connection to a persistent websocket connection and making the device available to the management api. The device must provide it's identity using the DeviceJWT either as Authorization header or as a cookie named 'JWT'.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.connect_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str connection: Standard websocket request header.
        :param str upgrade: Standard websocket request header.
        :param str sec_websocket_key: Standard websocket request header.
        :param int sec_websocket_version: Standard websocket request header.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'connection',
            'upgrade',
            'sec_websocket_key',
            'sec_websocket_version'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method connect" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'connection' in local_var_params:
            header_params['Connection'] = local_var_params['connection']  # noqa: E501
        if 'upgrade' in local_var_params:
            header_params['Upgrade'] = local_var_params['upgrade']  # noqa: E501
        if 'sec_websocket_key' in local_var_params:
            header_params['Sec-Websocket-Key'] = local_var_params['sec_websocket_key']  # noqa: E501
        if 'sec_websocket_version' in local_var_params:
            header_params['Sec-Websocket-Version'] = local_var_params['sec_websocket_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DeviceJWT']  # noqa: E501

        return self.api_client.call_api(
            '/connect', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
