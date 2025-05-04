import allure
import pytest
from src import ResponseCodes, ResponseMessage


@allure.feature('Регистрация пользователя')
class TestUserRegistration:

    @allure.story('Успешная регистрация нового пользователя')
    def test_registration_success(self, api_user, user_data):
        response = api_user.create_user(data=user_data)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.CREATED
        assert 'user' in response_data
        assert 'access_token' in response_data

    @allure.story('Регистрация с уже существующим email')
    def test_registration_w_exist_email(self, api_user, user_data, create_new_user):
        response = api_user.create_user(data=user_data)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.BAD_REQUEST
        assert response_data['message'] == ResponseMessage.EMAIL_BUSY
