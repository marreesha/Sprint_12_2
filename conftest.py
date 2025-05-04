import pytest
from src import URLS, generate_user_data, generate_ad_data, TestParameters
from src import ApiClient, ApiUser, ApiAd


@pytest.fixture
def api_user():
    client = ApiClient(URLS.BASE_URL)
    return ApiUser(client)


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def create_new_user(api_user, user_data):
    response = api_user.create_user(data=user_data)
    token = response.json().get('access_token', '').get('access_token', '')
    return token


@pytest.fixture
def api_ad():
    client = ApiClient(URLS.BASE_URL)
    return ApiAd(client)


@pytest.fixture
def ad_data():
    return generate_ad_data()


@pytest.fixture
def create_test_ad(api_ad, ad_data):
    def _wrapper(token):
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
        image_path = TestParameters.IMAGE_1
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        files = [('images', (f'image.jpg', image_data, 'image/jpeg'))]
        response = api_ad.create_ad(data=ad_data, files=files, headers=headers)
        return response.json().get('id', '')

    return _wrapper


@pytest.fixture
def delete_test_ad(api_ad):
    def _wrapper(token, ad_id):
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
        api_ad.delete_ad(ad_id=ad_id, headers=headers)

    return _wrapper
