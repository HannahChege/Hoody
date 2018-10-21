# TITLE
HOODWATCH WEBSITE
# BUILT BY
 HANNNAH NJERI
# DESCRIPTION
This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
The application is build with Django Framework in Pthyon.

# USER STORIES
As a user I would like to:

`Sign in with the application to start using.
`Set up a profile about me and a general location and my neighborhood name.
`Find a list of different businesses in my neighborhood.
`Find Contact Information for the health department and Police authorities near my neighborhood.
`Create Posts that will be visible to everyone in my neighborhood.
`Change My neighborhood when I decide to move out.
`Only view details of a single neighborhood.

 # INSTALATION REQUIREMENTS
installations required
python version should be 3.6 -Django version 1.11 pip install django==1.11
Additionally, you’ll need to make sure you have pip available. You can check this by running:
pip --Version
`Install Pipenv pip install --user pipenv
`install virtualenv and then test it
python3.6 pip install --user --upgrade pip
python3.6 -m virtualenv env
source env/bin/activate
Inorder to clone , follow the procedure below;

On GitHub, navigate to the main page of the repository.
Under the repository name, click Clone or downlonload.
click the paste button.
Open Terminal.
Change the current working directory to the location where - you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 2.
git clonehttps://github.com/HannahChege/Hoody.git Press Enter.
#CREATING A DATABASE

psql
CREATE DATABASE hood;
connect to the database \c hood;
check if tables have been created \dt
#RUN MIGRATIONS

python3.6 manage.py migrate
python3.6 manage.py makemigrations hood
#RUNNING THE APP

python3.6 manage.py runserver
#TESTING

python3.6 manage.py test hood
# TECHNOLOGIES USED
- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- Postgressql
- Heroku
# Prerequisites 
`python3.6 pip virtualenv 
`Cloning In your terminal:

`$git clone https://github.com/HannahChege/Hoody 
`$cd Hood
`Running the Application 
`Creating the virtual environment

`$python3.6 -m venv --without-pip virtual $ 
`source virtual/bin/env 
`Installing Django. 
`(virtual)$ pip install django==1.11
`Confirm that you do have Django.
`To achieve this, activate your python shell and run python3.6 on your terminal.
`Under your shell input this code:
 >>> import django
>>> django.get_version()
'1.11.5'
`Start a Django server.
`(virtual)$ python3.6 manage.py runserver
`Performing system checks...

`System check identified no issues (0 silenced).
September 28, 2018 - 12:01:08
Django version 1.11, using settings '.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 Technologies Used 
`Python3.6  

License Copyright (c) 2018
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
License Copyright (c) 2018 
HannahChege
