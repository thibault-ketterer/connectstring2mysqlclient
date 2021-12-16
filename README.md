# connectstring2mysqlclient
give mysql client command line from connect string

example of use

	$ python connectstring2mysqlclient.py 
	mysql://user:passwdxxxx@dbserver:3306/datbasename
	dbtype mysql
	user user
	passw passwdxxxx
	host dbserver
	port 3306
	
	mysql -u user -ppasswdxxxx -h dbserver -P 3306 datbasename



