from pathlib import Path
from faker import Faker


class ResponseCodes:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500


class ResponseMessage:
    EMAIL_BUSY = 'Почта уже используется'
    NO_PERMISSION = 'Оффер не найден или у вас нет прав на его редактирование'
    SUCCESSFUL_DELETE = 'Объявление удалено успешно'


class TestParameters:
    CATEGORY = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
    IMAGE_1 = Path(__file__).parent.parent / 'helpers' / 'images' / 'image_1.jpg'
    IMAGE_2 = Path(__file__).parent.parent / 'helpers' / 'images' / 'image_2.jpg'

    fake = Faker('ru_RU')
    AD_FIELDS = [
        ('name', fake.sentence(nb_words=4)),
        ('category', 'Книги'),
        ('condition', 'Б/У'),
        ('city', 'Екатеринбург'),
        ('description', fake.paragraph(nb_sentences=5)),
        ('price', fake.random_int(min=1000, max=10000))
    ]


class TorData:
    CATEGORY = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
    CONDITION = ['Новый', 'Б/У']
    CITY = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']
