# Moz-Connect
Connecting Contributors to Mozilla

## For Developers

### Getting Started
This doc is targeted for beginners, and we've tried to make it as beginner-friendly as possible.
Fork this repo and then carry on these steps to run this app locally.

- Make a clone of repo in your system and navigate on the root

  ```
  $ git clone https://github.com/<USER-NAME>/Moz-Connect.git
  cd Moz-Connect
  ```

- Make a virtual environment and activate it

  ```
  $ virtualenv venv
  $ source venv/bin/activate
  ```
- Install the required dependencies from requirements.txt by:

  ```
  (venv) $ pip install -r requirements.txt
  ```
- Set environment variables either by using `export` or creating a `.env` file as shown:
  Navigate to moz_connect dir, create a .env file:
  ```
  (venv) $ cd moz_connect
  (venv) $ gedit .env
  ```
  Now paste the following configurations to be set as env variables:
  ```
    DEBUG=True
	SECRET_KEY="my-secret-key"
	DATABASE_URL=sqlite:///db.sqlite3
  ```
  Save the file.

- Now migrate the changes to set up the database by:

  ```
  (venv) cd ..
  (venv) $ python manage.py migrate
  ```
- Create superuser to login to django-admin:

  ```
  (venv) $ python manage.py createsuperuser
  Enter Username
  Enter Email address
  Enter Password
  ```

- Now run the app by:

  ```
  (venv) $ python manage.py runserver
  ```
The app is now running at [localhost:8000](http://localhost:8000)
The django-admin can be checked at [localhost:8000/admin](http://localhost:8000/admin), credentials for login in are same as given while creating superuser.

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
