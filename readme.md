# Log File to DB
## Purpose
- This automation reads in a large (multi-GB) .gz file and manipulates/outputs the contents to a database.

## Getting Started
### 1. Create a Python virtual environment. 

#### From a Windows machine:

```ps1
cd C:\path\to\log-to-db
mkdir venv
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### From a Linux machine:
```bash
cd /path/to/log-to-db
mkdir venv
python -m venv venv
source /venv/bin/activate
```

### 2. Install necessary libraries
```ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Generate encryption key and encrypt secure strings
1. Open a Python shell from the `log-to-db` directory.
2. Encrypt your database username, password, and any other connection strings. Take a look inside `Functions/Database/database.py`, specifically at the `connectToDatabase()` function for the hardcoded example.
    1. user
    2. password
    3. host
    4. database
    5. port

```python
>>> from Functions.Encryption import encryption
>>> 
>>> # Generate an encryption key
>>> encryption.generateKey()
>>> encryption.encrypt(plaintext = "username")
>>> 
>>> # Your ciphertext will be presented to you in a binary string format like the below
>>> b'secureStringThatsReallyLong'
```

3. Paste your secure string values into `Functions/Database/database.py` in the relevant variables.

> **IMPORTANT NOTE**: It is vital that you secure your encryption key that you generated with `encryption.generateKey()`. This encryption key file is found at `Functions/Encryption/encryptionKey.txt`.
> 
> Assign the lowest possible privileges to this file in particular; otherwise, you might as well just leave your database credentials in plaintext as this encryption key is the only thing guarding your secure strings. The only user object that should have read access to this file is the user that is executing this script. Remove all other permissions with the exception of other Server Administrator groups.

### 4. Run logscan.py

> **NOTE**: This step is under construction. Right now, there must be a log file in the same parent directory as `logscan.py`. This file is currently hardcoded into `Functions/filePicker/singleFile.py` until further definitions have been made. See README Section 3.1 for development notes.

```ps1
python .\logscan.py
```

#### 3.1 TODO: Implement log file picker
Implement log file picker and/or multi-selection tool for eventual multiFile runtime.