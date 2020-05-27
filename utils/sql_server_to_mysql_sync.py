# need switch to python2.7 env
from etlalchemy import ETLAlchemyTarget, ETLAlchemySource

mssql_db_source = ETLAlchemySource("mssql+pyodbc://cai:1Q2w3e4r@DO_sql_server")

mysql_db_target = ETLAlchemyTarget("mysql://root@localhost/MD_BData", drop_database=True)

mysql_db_target.addSource(mssql_db_source)
mysql_db_target.migrate()
