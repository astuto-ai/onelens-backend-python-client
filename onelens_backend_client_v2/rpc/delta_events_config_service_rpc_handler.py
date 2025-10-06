# DeltaEventsConfigServiceRpcHandler API


from onelens_backend_client_v2.api_client import ApiClient


class DeltaEventsConfigServiceRpcHandler:
    """NOTE: This class is auto generated. Do not edit the class manually."""

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client
