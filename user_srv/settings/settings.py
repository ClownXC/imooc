from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class ReconnectMysqlDatabase(ReconnectMixin, PooledMySQLDatabase):
    pass


MYSQL_DB = "mxshop_user_srv"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "3494269"
DB = ReconnectMysqlDatabase(database=MYSQL_DB,
                            host=MYSQL_HOST,
                            port=MYSQL_PORT,
                            user=MYSQL_USERNAME,
                            password=MYSQL_PASSWORD)
