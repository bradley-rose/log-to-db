__author__ = "Bradley Rose"
__version__ = 0.5
__status__ = "WIP Development"

###########
# IMPORTS #
###########

from Functions.Database.database import prepareSql, connectToDatabase, writeToDatabase
from Functions.fileSelection.singleFile import fileParse

def main():

    # Connect to database
    dbSession = connectToDatabase()
    dbCursor = dbSession.cursor()

    # Validate that table exists, and if it does not, create it.
    tableName, message = prepareSql(dbCursor)
    
    # Parse the log file in chunks 
    chunkOfLogsForSql = fileParse()
    for i, logs in enumerate(chunkOfLogsForSql):
        writeToDatabase(dbCursor, tableName, logs)

    # Close the database session upon completion.
    dbSession.commit()
    dbSession.close()

if __name__ == "__main__":
    main()
