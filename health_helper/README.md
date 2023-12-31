
<h2>Описание</h2>

Это Django-приложение предназначено для диагностики сердечных заболеваний. Пользователи могут вводить свои медицинские данные через веб-форму, после чего приложение использует предварительно обученную модель машинного обучения для предсказания риска сердечного заболевания.

<h2>Особенности</h2>

Ввод пользовательских медицинских данных через веб-форму.
Использование модели RandomForest для предсказания риска сердечных заболеваний.
Отображение результата предсказания и точности модели на веб-странице.

<h2>Технологии</h2>

Python
Django
Pandas
Scikit-Learn

<h2>Установка и Запуск</h2>

<h2>Требования</h2>
<li>Python 3.6+
<li>Django 3.1+
<li>Pandas
<li>Scikit-Learn
<h2>Установка</h2>
Клонируйте репозиторий:
bash

git clone [URL репозитория]
Перейдите в директорию проекта:
bash

cd [название проекта]
Установите необходимые зависимости:
bash

pip install -r requirements.txt
Запуск
Запустите сервер разработки Django:
bash

python manage.py runserver
Откройте веб-браузер и перейдите по адресу:


http://127.0.0.1:8000/ так же есть возможность запустить через docker файл 
<h2>Использование</h2>

Заполните форму на главной странице своими медицинскими данными.
Нажмите кнопку "Отправить" для получения результатов анализа.
Результаты анализа, включая предсказание и точность модели, будут отображены на странице.
