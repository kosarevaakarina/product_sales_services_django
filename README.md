# Сервис для продажи товаров для дома "Skystore"

## Описание
* Интерфейс системы содержит следующие экраны: каталог товаров, категории товаров, создание пользователя, удаление
  пользователя, редактирование пользователя.
* Реализовано приложение для ведения блога.
* Права доступа разделены для различных пользователей.
* Модель пользователя расширена для регистрации по почте, а также верификации.
* Настроено кеширование
* Реализована валидация данных
* Интерфейс реализован с помощью UI Kit Bootstrap

## Технологии

* Python
* Bootstrap
* Django
* PostgreSQL
* Redis
* Pillow

## Сущности

- Product (продукты)
- Category (категории продуктов)
- Blog (блог)
- Contact (форма для обратной связи)
- Version (версии продуктов)
- User (авторизованные пользователи)

## Настройка сервиса
_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_

```
python3 -m venv venv
```
```
source venv/bin/activate
```

_Установить зависимости:_

```
pip install -r requirements.txt
```

_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_

_Выполнить миграции:_

```
python3 manage.py migrate
```

_Для заполнения БД запустить команду:_

```
python3 manage.py fill
```

_Для создания администратора запустить команду:_

```
python3 manage.py csu
```

_Для заполнения БД запустить команду:_

```
python3 manage.py fill
```

_Для запуска приложения:_

```
python3 manage.py runserver
```



