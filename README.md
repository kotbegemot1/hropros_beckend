Проект Polls
=====================
Для того, чтобы посмотреть проект не устанавливая к себе на компьютер, можно перейти по ссылке
https://final-proj-sf.herokuapp.com/polls/.

Администатор может создавать опросы в админке и просто на сайте(логин/пароль - admin/admin)

Авторизованный пользователь может просматривать и проходить опросы(логин/пароль - user/password1user)

Неавторизованный пользователь не видит опросов
***
Для того чтобы запусть проект у себе на компьютере(на примере ubuntu) нужно:
-----------------------------------
1. Установить и настроить postgresql:
    * устанавливаем postgresql
        > sudo apt install postgresql postgresql-contrib
    * запускаем из терминала
        > sudo -u postgres psql
    * создаем базу данных
        > CREATE DATABASE db_name;
    * создаем пользователя с паролем
        > CREATE USER username WITH PASSWORD 'password';
    * назначаем ему права
        > GRANT ALL PRIVILEGES ON DATABASE db_name TO username;

2. Далее устанавливаем виртуальное окружение:
    * устанавливаем виртуальное окружение
        > pip3 install virtualenv
    * mkdir project
    * содаем виртуальное окружение для проекта
        > python3.8 -m venv venv
    * активируем его
        > source venv/bin/activate
    * cd ..

3. Далее скачиваем с github и настраиваем сам проект:
    * скачиваем проект
        > git clone https://github.com/kotbegemot1/hropros_beckend.git
    * cd hropros
    * создаем файл .env
        > nano .env
        * и прописываем следующие настройки:
        > SECRET_KEY='et3%q!e%d0810%(mc2#p!*owxn36eb!2vyt6+o-*(es8&b&lc&'
        >
        > DB_NAME='db_name'
        >
        > DB_USER='username'
        >
        > DB_PASSWORD='password'
        >
        > DB_HOST=127.0.0.1
        >
        > DB_PORT=5432
    * cd ..
    * устанавливаем нужные пакеты
        > pip install -r requirements.txt
    * проводим миграции
        > ./manage.py migrate
    * создаем суперюзера и придумываем ему логин и пароль 
        > ./manage.py createsuperuser
    * далее переходим по адресу http://127.0.0.1:8000/ и перед нами проект
