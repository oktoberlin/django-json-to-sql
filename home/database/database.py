import pymysql

# database information
user_db = 'root'
pass_db = ''
host_db = 'localhost'
port_db = 3306
name_db = 'jsonhmm'

# connecting server database Jakarta to pythons
db = pymysql.connect(user=user_db,password=pass_db,host=host_db,port=port_db,database=name_db)