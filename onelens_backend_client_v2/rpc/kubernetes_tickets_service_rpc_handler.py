# KubernetesTicketsServiceRpcHandler API

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated


from onelens_backend_client_v2.models import BulkCreateKubernetesTicketsRequest


from onelens_backend_client_v2.models import BulkCreateKubernetesTicketsResponse


from onelens_backend_client_v2.models import BulkUpdateKubernetesTicketsRequest


from onelens_backend_client_v2.models import BulkUpdateKubernetesTicketsResponse


from onelens_backend_client_v2.models import CreateKubernetesTicketRequest


from onelens_backend_client_v2.models import CreateKubernetesTicketResponse


from onelens_backend_client_v2.models import GetKubernetesTicketRequest


from onelens_backend_client_v2.models import GetKubernetesTicketResponse


from onelens_backend_client_v2.models import GetKubernetesTicketByInsightIdRequest


from onelens_backend_client_v2.models import GetKubernetesTicketByInsightIdResponse


from onelens_backend_client_v2.models import GetKubernetesTicketMetadataRequest


from onelens_backend_client_v2.models import GetKubernetesTicketMetadataResponse


from onelens_backend_client_v2.models import SyncKubernetesTicketDataRequest


from onelens_backend_client_v2.models import SyncKubernetesTicketDataResponse


from onelens_backend_client_v2.models import UpdateKubernetesTicketRequest


from onelens_backend_client_v2.models import UpdateKubernetesTicketResponse


from onelens_backend_client_v2.models import UpsertKubernetesTicketsRequest


from onelens_backend_client_v2.models import UpsertKubernetesTicketsResponse


from onelens_backend_client_v2.api_client import ApiClient, RequestSerialized


class KubernetesTicketsServiceRpcHandler:
    """NOTE: This class is auto generated. Do not edit the class manually."""

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def bulk_create_kubernetes_tickets(
        self,
        request: BulkCreateKubernetesTicketsRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BulkCreateKubernetesTicketsResponse:
        """Bulk create kubernetes tickets from a list of insights.



        :param request: (required)
        :type request: BulkCreateKubernetesTicketsRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._bulk_create_kubernetes_tickets_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "BulkCreateKubernetesTicketsResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _bulk_create_kubernetes_tickets_serialize(
        self,
        request: BulkCreateKubernetesTicketsRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/bulk_create_kubernetes_tickets",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def bulk_update_kubernetes_tickets(
        self,
        request: BulkUpdateKubernetesTicketsRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BulkUpdateKubernetesTicketsResponse:
        """Bulk update multiple kubernetes tickets with the same field values.



        :param request: (required)
        :type request: BulkUpdateKubernetesTicketsRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._bulk_update_kubernetes_tickets_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "BulkUpdateKubernetesTicketsResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _bulk_update_kubernetes_tickets_serialize(
        self,
        request: BulkUpdateKubernetesTicketsRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/bulk_update_kubernetes_tickets",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def create_kubernetes_ticket(
        self,
        request: CreateKubernetesTicketRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CreateKubernetesTicketResponse:
        """Create a new kubernetes ticket from an insight.



        :param request: (required)
        :type request: CreateKubernetesTicketRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._create_kubernetes_ticket_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "CreateKubernetesTicketResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _create_kubernetes_ticket_serialize(
        self,
        request: CreateKubernetesTicketRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/create_kubernetes_ticket",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_kubernetes_ticket(
        self,
        request: GetKubernetesTicketRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetKubernetesTicketResponse:
        """Get kubernetes ticket details by ticket_id.



        :param request: (required)
        :type request: GetKubernetesTicketRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_kubernetes_ticket_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetKubernetesTicketResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_kubernetes_ticket_serialize(
        self,
        request: GetKubernetesTicketRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/get_kubernetes_ticket",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_kubernetes_ticket_by_insight_id(
        self,
        request: GetKubernetesTicketByInsightIdRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetKubernetesTicketByInsightIdResponse:
        """Get a kubernetes ticket by its insight_id, returned as InsightData.



        :param request: (required)
        :type request: GetKubernetesTicketByInsightIdRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_kubernetes_ticket_by_insight_id_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetKubernetesTicketByInsightIdResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_kubernetes_ticket_by_insight_id_serialize(
        self,
        request: GetKubernetesTicketByInsightIdRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/get_kubernetes_ticket_by_insight_id",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_kubernetes_ticket_metadata(
        self,
        request: GetKubernetesTicketMetadataRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetKubernetesTicketMetadataResponse:
        """Get kubernetes ticket metadata by ticket_id (no joins).



        :param request: (required)
        :type request: GetKubernetesTicketMetadataRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_kubernetes_ticket_metadata_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "GetKubernetesTicketMetadataResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _get_kubernetes_ticket_metadata_serialize(
        self,
        request: GetKubernetesTicketMetadataRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/get_kubernetes_ticket_metadata",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def sync_kubernetes_ticket_data(
        self,
        request: SyncKubernetesTicketDataRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SyncKubernetesTicketDataResponse:
        """Sync kubernetes ticket data to aggregated_tickets.



        :param request: (required)
        :type request: SyncKubernetesTicketDataRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._sync_kubernetes_ticket_data_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "SyncKubernetesTicketDataResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _sync_kubernetes_ticket_data_serialize(
        self,
        request: SyncKubernetesTicketDataRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/sync_kubernetes_ticket_data",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def update_kubernetes_ticket(
        self,
        request: UpdateKubernetesTicketRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UpdateKubernetesTicketResponse:
        """Update ticket_status, assigned_to, priority, and savings fields.



        :param request: (required)
        :type request: UpdateKubernetesTicketRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._update_kubernetes_ticket_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "UpdateKubernetesTicketResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _update_kubernetes_ticket_serialize(
        self,
        request: UpdateKubernetesTicketRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/update_kubernetes_ticket",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def upsert_kubernetes_tickets(
        self,
        request: UpsertKubernetesTicketsRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]
            ],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UpsertKubernetesTicketsResponse:
        """Upsert Kubernetes Tickets



        :param request: (required)
        :type request: UpsertKubernetesTicketsRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._upsert_kubernetes_tickets_serialize(
            request=request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            "200": "UpsertKubernetesTicketsResponse",
            "422": "HTTPValidationError",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    def _upsert_kubernetes_tickets_serialize(
        self,
        request: UpsertKubernetesTicketsRequest,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the body parameter
        if request is not None:
            _body_params = request

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(
                ["application/json"]
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/rpc/kubernetes_tickets_service/upsert_kubernetes_tickets",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
