from datetime import datetime

def formatForSqlDatabase(filteredLogs: dict):
    sqlEntries = []
    for logType in filteredLogs.keys(): 
        for entry in filteredLogs[logType]:
            sqlPayload = {}
            for logKey,dbKey in {
                "variableInLog":"databaseColumnHeader",
                "anotherVariableInLog":"anotherColumnInDB",
                "dateTimeVariable":"dateTimeDbColumnName"
            }.items():
                
                if logKey == "dateTimeVariable":
                    sqlPayload[dbKey] = str(datetime.strptime(entry[logKey], "%Y-%m-%dT%H:%M:%SZ"))
                else:
                    sqlPayload[dbKey] = entry[logKey] if logKey in entry.keys() else "NULL"
                # Implement some logic to store string values of "1" for True and "2" for False as well for the TINYINT booleans.

            sqlEntries.append(sqlPayload)
    return sqlEntries

def logEntryEvaluation(logEntries: list) -> dict:

    categoryOne = []; categoryTwo = []; categoryThree = []; categoryFour = []

    for entry in logEntries:

        if "aKey" in entry.keys() and entry["aKey"] == "aValue":
            categoryOne.append(entry)
        elif entry["anotherKey"] == "anotherValue":
            categoryTwo.append(entry)
        elif entry["aThirdKey"] == "aThirdValue":
            categoryThree.append(entry)
        elif entry["aFourthKey"] == "aFourthValue":
            categoryFour.append(entry)
    
    return {
        "categoryOne":categoryOne, 
        "categoryTwo":categoryTwo, 
        "categoryThree":categoryThree, 
        "categoryFour":categoryFour
    }
