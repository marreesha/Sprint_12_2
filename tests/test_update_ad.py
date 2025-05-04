import allure
import pytest
from src import ResponseCodes, ResponseMessage, TestParameters, generate_user_data


@allure.feature('Обновление объявлений')
class TestAdUpdate:

    @allure.story('Успешное обновление поля объявления')
    @allure.title('Обновление поля "{ad_field}", значение "{new_value}"')
    @pytest.mark.parametrize('ad_field, new_value', TestParameters.AD_FIELDS)
    def test_update_ad_success(self, create_new_user, api_ad, ad_data, create_test_ad, delete_test_ad, ad_field,
                               new_value):
        token = create_new_user
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
        ad_id = create_test_ad(token)
        ad_data[ad_field] = new_value

        response = api_ad.update_ad(ad_id=ad_id, data=ad_data, headers=headers)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.OK
        assert response_data[ad_field] == new_value

        delete_test_ad(token=token, ad_id=ad_id)

    @allure.story('Успешное обновление фото объявления')
    def test_update_ad_image(self, create_new_user, api_ad, ad_data, create_test_ad, delete_test_ad):
        token = create_new_user
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
        ad_id = create_test_ad(token)

        image_path = TestParameters.IMAGE_2
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        files = [('images', (f'image.jpg', image_data, 'image/jpeg'))]

        response = api_ad.update_ad(ad_id=ad_id, data=ad_data, files=files, headers=headers)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.OK

        delete_test_ad(token=token, ad_id=ad_id)

    @allure.story('Попытка обновления другим пользователем')
    def test_update_ad_by_other_user(self, api_user, create_new_user, api_ad, ad_data, create_test_ad,
                                          delete_test_ad):
        # correct_token
        correct_token = create_new_user
        ad_id = create_test_ad(correct_token)

        # wrong_token
        response = api_user.create_user(data=generate_user_data())
        wrong_token = response.json().get('access_token', '').get('access_token', '')
        headers = {'Authorization': f'Bearer {wrong_token}', 'Accept': 'application/json'}

        # ad_data
        ad_data['name'] = 'Попытка обновления другим пользователем'

        response = api_ad.update_ad(ad_id=ad_id, data=ad_data, headers=headers)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.UNAUTHORIZED
        assert response_data['message'] == ResponseMessage.NO_PERMISSION

        delete_test_ad(token=correct_token, ad_id=ad_id)
