h1 Проект Polls (skillfactory)
=====================
Для того чтобы запусть проект у себе на компьютере(на примере ubuntu) нужно:
***
1. Установить и настроить postgresql:
    Выполняется в терминале
    * sudo apt install postgresql postgresql-contrib
    * sudo -u postgres psql
    * CREATE DATABASE db_name;
    * CREATE USER username WITH PASSWORD 'password';
    * GRANT ALL PRIVILEGES ON DATABASE db_name TO username;

2. Далее устанавливаем виртуальное окружение:
    * pip3 install virtualenv
    * mkdir project
    * python3.8 -m venv venv
    * source venv/bin/activate
    * cd ..

3. Далее скачиваем с github и настраиваем сам проект:
    * git clone https://github.com/kotbegemot1/hropros_beckend.git
    * cd hropros
    * nano .env
        копируем следующие настройки:
        SECRET_KEY='et3%q!e%d0810%(mc2#p!*owxn36eb!2vyt6+o-*(es8&b&lc&'
        DB_NAME='db_name'
        DB_USER='username'
        DB_PASSWORD='password'
        DB_HOST=127.0.0.1
        DB_PORT=5432
    * cd ..
    * pip install -r requirements.txt
    * ./manage.py migrate
    * ./manage.py createsuperuser