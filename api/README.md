# A REST API for littlelemon website using Django

### How to run this project

step 1: Go on your shell and run "git clone https://github.com/AshishKakran/backend-capstone.git"

step 2: change to backend-capstone/api/ directory

step 3: run "pipenv shell"

step 4: run "pipenv install"

step 5: make sure you have mysql database server up and running with with settings in DATABASES parameters of backend-capstone/api/api/settings.py file.

step 6: run "python manage.py makemigraions &&  python manage.py migrate"

step 7: run "python manage.py runserver"

step 8: go to your browser and enter "localhost:8000/restaurant/"

The api implements two endpoints

/restaurant/menu
/restaurant/booking

You can also use endpoints for authentication provided by djoser library such 
/auth/token/login
/auth/users
