import mysql.connector as sql
from datetime import datetime
from Functions.Encryption.encryption import decrypt

def connectToDatabase():
    databaseParameters = {
        "user": decrypt(cipherText = b'encryptedUsername'),
        "password": decrypt(cipherText = b'encryptedPassword'),
        "host":decrypt(cipherText = b'encryptedHostnameOrIP'),
        "database":decrypt(cipherText = b'encryptedDatabaseName'),
        "port":int(decrypt(cipherText = b'encryptedPortInteger')),
        "raise_on_warnings": True
    }

    dbSession = sql.connect(**databaseParameters)
    return dbSession

def writeToDatabase(database, tableName: str, logs: list):
    for log in logs:
        values = list(log.values())
        sqlValues = ""
        for i, element in enumerate(values):
            if i == (len(values)-1) and (not isinstance(element, str) or element == "NULL"):
                sqlValues += str(element)
            elif i == (len(values)-1):
                sqlValues += "\"" + str(element) + "\""
            elif not isinstance(element, str) or element == "NULL":
                sqlValues += str(element) + ", "
            else:
                sqlValues += "\"" + str(element) + "\", "

        sqlQuery = ("INSERT INTO " + tableName + " (" + (", ".join(log.keys())) + ") VALUES (" + sqlValues + ")")
        database.execute(sqlQuery)

def prepareSql(database):
    currentYear = datetime.today().strftime("%Y")
    currentYearTable = "tableName" + currentYear
    database.execute("SHOW TABLES")
    result = database.fetchall()

    tables = []
    for element in result:
        for table in element:
            tables.append(table)

    if currentYearTable in tables:
        return currentYearTable, "Already existed."
    
    else:
        database.execute("CREATE TABLE " + currentYearTable + " (date DATETIME, stringVar VARCHAR(128), ipVar VARCHAR(45), booleanVar TINYINT, longTextVar TEXT)")
        print("Created " + currentYearTable + " table.")
        return currentYearTable, "Created new."
    