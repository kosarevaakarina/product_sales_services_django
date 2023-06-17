Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:

python -m venv venv
source venv/bin/activate 
pip install -r requirement.txt

Для запуска приложения:

python3 manage.py runserver

В приложении есть следующие модели:
- Product
- Category
- Blog

Для заполнения моделей данными необходимо выполнить следующую команду:

python3 manage.py fill

Для отправки сообщений в файл .env необходимо добавить почту и пароль:

EMAIL_HOST_USER='mail@yandex.ru'
EMAIL_HOST_PASSWORD='password'

