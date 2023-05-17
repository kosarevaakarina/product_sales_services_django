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

