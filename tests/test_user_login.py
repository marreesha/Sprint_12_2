import allure
import pytest
from src import ResponseCodes


@allure.feature('Авторизация пользователя')
class TestUserLogin:

    @allure.story('Успешная авторизация пользователя')
    def test_login_success(self, api_user, user_data, create_new_user):
        response =  api_user.login_user(data=user_data)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.CREATED
        assert 'user' in response_data
        assert 'token' in response_data