for enter myenv virtual environment type in cmd :::  '.\myenv\Scripts\activate

for exit myenv virtual environment type in cmd :::: 'deactivate'


for run django project type in cmd ::::  'python manage.py runserver' (mainly run the manage.py file in python)

python -m pip freeze >.\requirements.txt 
or
pip freeze >.\requirements.txt 
for put all pip packages name with version in requirements.txt file

create environment variable folder using this command 'python -m virtualenv myenv
environment folder present inside the main file as a sibling of requirements.txt file

pip install -r .\requirements.txt install all packages mention in requirements.txt file

inbuilt theme used by telusko download from following url https://github.com/sahaib9747/TeluskoTutorial-TravelloTheme

copy manage.py file from mysite folder to DJANGOTELUSKO folder and then run python manage.py startapp travello in DJANGOTELUSKO directory to create a new project inside DJANGOTELUSKO directory

required pip package::

asgiref==3.5.0
Django==3.2.12
pytz==2022.1
sqlparse==0.4.2
typing_extensions==4.1.1



this django code are do following Telusko Youtube channel

video complete :17,18th 


to solve the problem and properly make app(separate project component in django): https://youtu.be/L7D50lzcG5s

inside parent mysite folder create a folder name static where i store all image css file and js file need our website

for import external css file link or js file link we need to use {% <folderName> <rest url> %} this type pattern but in case of image we directly add folderName to the rest url like add parent folder to a file name

-------------------------------------------------------------------------------model create and migration

install python package psycopg2(pip install psycopg2) it help to connect django to postgreSql database 
install pillow package(pip install pillow) which need to migrate django model
to migrate django model need execute this command python manage.py makemigrations in cmd after migration complete where the schema generated the file location is display in the cmd with filename

and then run the python manage.py sqlmigrate travello 0001 command that create a sql querry based on the python model created and 0001 indicate the file name where the django orm model are store 

then run following commant python manage.py migrate it actually execute the sql command in postgreSql database 



see all table in postGreSql database through pgAdmin  Schemas => public => Tables


