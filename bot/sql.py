import logging
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os

user=os.getenv('DB_USER')
password=os.getenv('DB_PASSWORD')
host=os.getenv('DB_HOST')
port=os.getenv('DB_PORT')
database=os.getenv('DB_DATABASE')

load_dotenv()

logging.basicConfig(filename='app_sql.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def sozd_table():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                        """CREATE TABLE IF NOT EXISTS users_email(
                            id serial PRIMARY KEY,
                            email varchar(255) NOT NULL);"""
                    )
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(
                        """CREATE TABLE IF NOT EXISTS users_phone(
                            id serial PRIMARY KEY,
                            phone_number BIGINT NOT NULL);"""
                    )
            connection.commit()
        data = 'OK'
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data =error  # 'Ошибка при создании бд.'
    finally:
        return data
def get_emails():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT email FROM users_email;"
            )
            data = cursor.fetchall()
            if len(data) == 0: data = None
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data = 'Ошибка при работе с PostgreSQL'
    finally:
        return data


def get_phone_numbers():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT phone_number from users_phone;"
            )
            data = cursor.fetchall()
            if len(data) == 0: data = None
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data = 'Ошибка при работе с PostgreSQL'
    finally:
        return data

def email_insert(arg):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users_email (email) VALUES ('{arg}');"""
            )
            connection.commit()
            data = 'Успех'
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data = 'Ошибка при работе с PostgreSQL'
    finally:
        return data



def phone_insert(arg):
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO users_phone (phone_number) VALUES ({arg});"""
            )
            connection.commit()
            data = 'Успех'
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data = 'Ошибка при работе с PostgreSQL'
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return data



def get_repl_logs():
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT pg_read_file(pg_current_logfile());"""
            )
            connection.commit()
            data = cursor.fetchall()
            data = str(data).replace('\\n', '\n').replace('\\t', '\t')[2:-1]
            answer = ''
            for str1 in data.split('\n'):
               if 'replication command' in str1:
                  answer += str1 + '\n'
            if len(answer) == 0:
            	data = 'События репликации не обнаружены'
            else:
            	data = answer
    except (Exception, Error) as error:
        logging.error("Ошибка при работе с PostgreSQL: %s", error)
        data = 'Ошибка при работе с PostgreSQL'
    finally:
        if connection is not None:
            cursor.close()
            connection.close()
        return data
