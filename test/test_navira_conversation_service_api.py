# coding: utf-8

"""
onelens-backend

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from onelens_backend_client.api.navira_conversation_service_api import (
    NaviraConversationServiceApi,
)


class TestNaviraConversationServiceApi(unittest.TestCase):
    """NaviraConversationServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NaviraConversationServiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_thread(self) -> None:
        """Test case for create_thread

        Create Thread
        """
        pass

    def test_get_agent_types(self) -> None:
        """Test case for get_agent_types

        Get Agent Types
        """
        pass

    def test_get_all_threads(self) -> None:
        """Test case for get_all_threads

        Get All Threads
        """
        pass

    def test_get_messages(self) -> None:
        """Test case for get_messages

        Get Messages
        """
        pass

    def test_get_state(self) -> None:
        """Test case for get_state

        Get State
        """
        pass

    def test_get_thread_by_id(self) -> None:
        """Test case for get_thread_by_id

        Get Thread By Id
        """
        pass

    def test_send_message(self) -> None:
        """Test case for send_message

        Send Message
        """
        pass

    def test_update_state(self) -> None:
        """Test case for update_state

        Update State
        """
        pass


if __name__ == "__main__":
    unittest.main()
