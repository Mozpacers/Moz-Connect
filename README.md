# Moz-Connect
Connecting Contributors to Mozilla

## For Developers
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
