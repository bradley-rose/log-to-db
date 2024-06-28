import json
import gzip
from Functions.Formatting.formatting import logEntryEvaluation, formatForSqlDatabase

def fileParse():
    # Open the GZIP in 10MB chunks
    chunk_size = 10240 * 1024

    with gzip.open("nameOfLogFile.gz","rb") as gzFile:
        chunk = gzFile.read(chunk_size).decode("ascii")
        while chunk:
            
            contents = chunk.split("\n")
            unfinishedElement = contents.pop()
                
            logEntries = []

            for element in contents:
                logEntries.append(json.loads(r'{}'.format(element)))

            filteredLogs = logEntryEvaluation(logEntries)
            # Return the chunk generator and continue to proceed. View line 23 of logscan.py for the for loop.
            yield formatForSqlDatabase(filteredLogs)

            chunk = unfinishedElement + (gzFile.read(chunk_size).decode("ascii"))