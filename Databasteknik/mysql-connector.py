## USING MYSQL CONNECTOR LIBRARY IN PYTHON
## https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html


import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root2', password='Secondo12@',
                                host='127.0.0.1',
                                database='VM')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


# per eseguire un comando in mysql bisogna prima creare un cursore partendo dal database aperto
cursor = cnx.cursor()

# a questo punto è possibile fare unq query al DB
#cursor.execute("QUERY")

# è anche possibile salvare una query in una variabile e poi rendere questa eseguibile. Ogni riga deve essere
# contenuta tra gli apici "" e contenuta tutta in una ()
query = (
        "SELECT * FROM `VM`.`Domare` LIMIT 1000"
        )
cursor.execute(
        "SELECT * FROM `VM`.`Domare`"
        "WHERE id = %(n)s", ({ 'n': 2 })
        )

for i, j in cursor:
    print(i, j)
cnx.close()
