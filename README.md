# connectstring2mysqlclient
## description
It gives **mysql client command line** from **connect string**

Just an handy script

example of use


input `mysql://user:passwdxxxx@dbserver:3306/datbasename`

output `mysql -u user -ppasswdxxxx -h dbserver -P 3306 datbasename`

	$ python connectstring2mysqlclient.py 
	mysql://user:passwdxxxx@dbserver:3306/datbasename
	dbtype mysql
	user user
	passw passwdxxxx
	host dbserver
	port 3306
	
	mysql -u user -ppasswdxxxx -h dbserver -P 3306 datbasename



