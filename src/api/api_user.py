import allure
from .http_client import HttpMethods
from src import URLS


class ApiUser:

    def __init__(self, api_client):
        self.client = api_client

    @allure.step('Запрос на создание нового пользователя')
    def create_user(self, data, **kwargs):
        return self.client.send_request(HttpMethods.POST, URLS.SIGNUP_ENDPOINT, json=data, **kwargs)

    @allure.step('Запрос на логин пользователя')
    def login_user(self, data, **kwargs):
        return self.client.send_request(HttpMethods.POST, URLS.SIGNIN_ENDPOINT, json=data, **kwargs)
