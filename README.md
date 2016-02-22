# Moz-Connect
Connecting Contributors to Mozilla

## For Developers

### Getting Started
Fork this repo and then carry on these steps to run this app locally.

- Make a virtual environment and activate it

  ```
  $ virtualenv venv
  (venv) $ venv/bin/activate
  ```
- Install the required dependencies from requirements.txt by:

  ```
  (venv) $ pip install -r requirements.txt
  ```

- Now migrate the changes to set up the database by:

  ```
  (venv) $ python manage.py migrate
  ```

- Now run the app by:

  ```
  (venv) $ python manage.py runserver
  ```
The app is now running at [localhost:8000](http://localhost:8000)

### Backing up the database

To make a backup copy of the database, simply do a "dump" and redirect the results to a file.

```
sqlite3 db.sqlite3 .dump > moz-connect-db.bak
```

### Restoring the database
Before restoring, ensure the database is empty. You can rename the destination database and let sqlite create a new one for you.

```
mv db.sqlite3 db.sqlite3.old
sqlite3 db.sqlite3 < moz-connect-db.bak
```

After restoring, verify the results.

```
sqlite3 db.sqlite3 'select * from registrations_person'
```
