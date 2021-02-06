# TODO-LIST
API FOR TODO-LIST

## PREREQUISITE 
- pyhton <= v3.6
- pip 21.0.1

## INSTALATION
import `todo api.postman_collection.json' to postman
### MacOS/Linux
1. run `make all` command to execute the Makefile.
### Windows
please run the following command by the order they written:

1. open powershell
2. `virtualenv venv`
3. `.\venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `cd todo`
6.	`python manage.py migrate`
7. `python manage.py test api.tests --noinput`
8. `python manage.py runserver`
