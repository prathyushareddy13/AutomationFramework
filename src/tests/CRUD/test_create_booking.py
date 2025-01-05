from logging import Logger

import allure
import pytest
import logging #use to print the logs

from faker.providers.bank.en_PH import logger

from src.constants.apiconstants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import * # to import everything

class Test_create_booking:

    #@pytest.mark.positive
    @allure.title("Creating a booking")
    @allure.description("We are creating a booking request based on the details entered by the user")
    def test_create_booking(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.info("Create Booking Test execution started")
        logger.info("Post request execution started")
        response = post_request(url = APIConstants().create_booking_url(),
                                auth=None,
                                headers=Utils().common_header_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        logger.info("Post request is completed")
        logger.info("Verifying the details created")

        verify_http_status_code(response_data=response,expected_data=200)
        logger.info(response.json())
        logger.info(response.json()["bookingid"])
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])

    #@pytest.mark.negative
    @allure.title("Creating a request with empty payload")
    @allure.description("Verifying the status code by passing the empty payload")
    def test_create_booking_neg(self):
        logger = logging.getLogger(__name__)
        logger.info("Create Booking Test execution started")
        logger.info("Post request execution started")
        response = post_request(url=APIConstants().create_booking_url(),
                                auth=None,
                                headers=Utils().common_header_json(),
                                payload={},
                                in_json=False)
        logger.info("Post request is completed")
        logger.info("Verifying the details created")
        verify_http_status_code(response_data=response, expected_data=500)

    #@pytest.mark.negative
    @allure.title("Creating a request with incorrect payload")
    @allure.description("Verifying the status code by passing the incorrect payload")
    def test_create_booking_neg1(self):
        logger = logging.getLogger(__name__)
        logger.info("Create Booking Test execution started")
        logger.info("Post request execution started")
        response = post_request(url=APIConstants().create_booking_url(),
                                auth=None,
                                headers=Utils().common_header_json(),
                                payload={"name":"Prathyusha"},
                                in_json=False)
        logger.info("Post request is completed")
        logger.info("Verifying the details created")
        verify_http_status_code(response_data=response, expected_data=500)
