
while True:
    data = input()
    # data = "mysql://user:passwdxxxx@dbserver:3306/datbasename"
    (dbtype, rest) =  data.split(':', 1)
    rest = rest.lstrip("/")
    loginpass, rest = rest.split('@', 1)
    hostport, dbname = rest.split('/', 1)
    host, port = hostport.split(":")
    user, passw = loginpass.split(":")
    print("dbtype", dbtype)
    # print(loginpass)
    # print(hostport)
    # print(rest)
    print("user", user)
    print("passw", passw)
    print("host", host)
    print("port", port)
    print()
    print(f"mysql -u {user} -p{passw} -h {host} -P {port} {dbname}")
    print()
