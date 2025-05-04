from faker import Faker


def generate_user_data():
    fake = Faker('ru_RU')
    data = {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password()
    }
    return data


def generate_ad_data():
    fake = Faker('ru_RU')
    data = {
        'name': fake.sentence(nb_words=4),
        'category': 'Авто',
        'condition': 'Новый',
        'city': 'Москва',
        'description': fake.paragraph(nb_sentences=5),
        'price': fake.random_int(min=1000, max=10000)
    }
    return data
