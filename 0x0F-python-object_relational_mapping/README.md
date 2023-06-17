The MySQL C API has been wrapped in an object-oriented way. The only MySQL data structures which are implemented are the MYSQL (database connection handle) and MYSQL_RES (result handle) types. In general, any function which takes MYSQL *mysql as an argument is now a method of the connection object, and any function which takes MYSQL_RES *result as an argument is a method of the result object. Functions requiring none of the MySQL data structures are implemented as functions in the module. Functions requiring one of the other MySQL data structures are generally not implemented. Deprecated functions are not implemented. In all cases, the mysql_ prefix is dropped from the name. Most of the conn methods listed are also available as MySQLdb Connection object methods. Their use is non-portable.

MySQL C API function mapping
C API	_mysql
mysql_affected_rows()	conn.affected_rows()
mysql_autocommit()	conn.autocommit()
mysql_character_set_name()	conn.character_set_name()
mysql_close()	conn.close()
mysql_commit()	conn.commit()
mysql_connect()	_mysql.connect()
mysql_data_seek()	result.data_seek()
mysql_debug()	_mysql.debug()
mysql_dump_debug_info	conn.dump_debug_info()
mysql_escape_string()	_mysql.escape_string()
mysql_fetch_row()	result.fetch_row()
mysql_get_character_set_info()	conn.get_character_set_info()
mysql_get_client_info()	_mysql.get_client_info()
mysql_get_host_info()	conn.get_host_info()
mysql_get_proto_info()	conn.get_proto_info()
mysql_get_server_info()	conn.get_server_info()
mysql_info()	conn.info()
mysql_insert_id()	conn.insert_id()
mysql_num_fields()	result.num_fields()
mysql_num_rows()	result.num_rows()
mysql_options()	various options to _mysql.connect()
mysql_ping()	conn.ping()
mysql_query()	conn.query()
mysql_real_connect()	_mysql.connect()
mysql_real_query()	conn.query()
mysql_real_escape_string()	conn.escape_string()
mysql_rollback()	conn.rollback()
mysql_row_seek()	result.row_seek()
mysql_row_tell()	result.row_tell()
mysql_select_db()	conn.select_db()
mysql_set_character_set()	conn.set_character_set()
mysql_ssl_set()	ssl option to _mysql.connect()
mysql_stat()	conn.stat()
mysql_store_result()	conn.store_result()
mysql_thread_id()	conn.thread_id()
mysql_use_result()	conn.use_result()
mysql_warning_count()	conn.warning_count()
CLIENT_*	MySQLdb.constants.CLIENT.*
CR_*	MySQLdb.constants.CR.*
ER_*	MySQLdb.constants.ER.*
FIELD_TYPE_*	MySQLdb.constants.FIELD_TYPE.*
FLAG_*	MySQLdb.constants.FLAG.*

ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. Developers can use the programming language they are comfortable with to work with a database instead of writing SQL statements or stored procedures.

For example, without an ORM a developer would write the following SQL statement to retrieve every row in the USERS table where the zip_code column is 94107:

SELECT * FROM USERS WHERE zip_code=94107;
The equivalent Django ORM query would instead look like the following Python code:

# obtain everyone in the 94107 zip code and assign to users variable
users = Users.objects.filter(zip_code=94107)
The ability to write Python code instead of SQL can speed up web application development, especially at the beginning of a project. The potential development speed boost comes from not having to switch from Python code into writing declarative paradigm SQL statements. While some software developers may not mind switching back and forth between languages, it's typically easier to knock out a prototype or start a web application using a single programming language.

ORMs also make it theoretically possible to switch an application between various relational databases. For example, a developer could use SQLite for local development and MySQL in production. A production application could be switched from MySQL to PostgreSQL with minimal code modifications.

In practice however, it's best to use the same database for local development as is used in production. Otherwise unexpected errors could hit in production that were not seen in a local development environment. Also, it's rare that a project would switch from one database in production to another one unless there was a pressing reason.
