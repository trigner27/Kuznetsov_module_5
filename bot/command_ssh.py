from fabric import Connection
from dotenv import load_dotenv
import logging
import paramiko
import os

logging.basicConfig(filename='Log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

host = os.getenv('RM_HOST')
user_name = os.getenv('RM_USER')
user_password = os.getenv('RM_PASSWORD')
port = os.getenv('RM_PORT')


def get_release():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('lsb_release -a')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return ex


def get_uname():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('uname -a')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_uptime():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('uptime')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_df():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('df -h')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_free():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('free -h')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_mpstat():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('top -b -n 1')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_w():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('w')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_auths():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('last -n 10')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_critical():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('cat /var/log/syslog | grep -i "critical" | tail -n 5')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_ps():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('ps aux')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_ss():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('netstat -tuln')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_apt_list():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('dpkg --get-selections')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_apt_list_arg(packet):
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run(f'apt show {packet}')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'
def get_services():
    try:
        with Connection(host=host, user=user_name, port = port, connect_kwargs={'password': user_password}) as conn:
            result = conn.run('service --status-all')
            result = result.stdout.strip()
        return result
    except Exception as ex:
        logging.error("Ошибка при работе по ssh: %s", ex)
        return 'Ошибка при работе по ssh'

