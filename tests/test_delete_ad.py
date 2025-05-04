import allure
import pytest
from src import ResponseCodes, ResponseMessage


@allure.feature('Обновление объявлений')
class TestAdDelete:

    @allure.story('Успешное удаление объявления')
    def test_delete_ad_success(self, create_new_user, api_ad, create_test_ad):
        token = create_new_user
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
        ad_id = create_test_ad(token)

        response = api_ad.delete_ad(ad_id=ad_id, headers=headers)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.OK
        assert response_data['message'] == ResponseMessage.SUCCESSFUL_DELETE
