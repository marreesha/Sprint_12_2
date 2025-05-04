import allure
from .http_client import HttpMethods
from src import URLS


class ApiAd:

    def __init__(self, api_client):
        self.client = api_client

    @allure.step('Запрос на создание нового объявления')
    def create_ad(self, data, **kwargs):
        return self.client.send_request(HttpMethods.POST, URLS.CREATE_AD_ENDPOINT, data=data, **kwargs)

    @allure.step('Запрос на удаление объявления')
    def delete_ad(self, ad_id, **kwargs):
        return self.client.send_request(HttpMethods.DELETE, f'{URLS.ADS_ENDPOINT}/{ad_id}', **kwargs)

    @allure.step('Запрос на обновление объявления')
    def update_ad(self, ad_id, data, **kwargs):
        return self.client.send_request(HttpMethods.PATCH, f'{URLS.UPDATE_AD_ENDPOINT}/{ad_id}', data=data, **kwargs)
