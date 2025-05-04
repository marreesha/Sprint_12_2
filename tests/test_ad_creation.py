import allure
import pytest
from src import ResponseCodes, TestParameters


@allure.feature('Создание объявлений')
class TestAdCreation:

    @allure.story('Успешное создание объявления')
    @allure.title('Создание объявления в категории "{category}"')
    @pytest.mark.parametrize('category', TestParameters.CATEGORY)
    def test_create_ad_success(self, api_ad, create_new_user, ad_data, delete_test_ad, category):
        # headers
        token = create_new_user
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}

        # files
        image_path = TestParameters.IMAGE_1
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        files = [('images', (f'image.jpg', image_data, 'image/jpeg'))]

        # data
        ad_data['category'] = category

        response = api_ad.create_ad(data=ad_data, files=files, headers=headers)
        response_code = response.status_code
        response_data = response.json()

        with allure.step('Данные теста'):
            allure.attach(str(response_code), name='response_code')
            allure.attach(str(response_data), name='response_data')

        assert response_code == ResponseCodes.CREATED
        assert response_data['category'] == category

        delete_test_ad(token=token, ad_id=response_data['id'])
