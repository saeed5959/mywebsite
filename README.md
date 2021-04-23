# my first website

**https://saeediranian.herokuapp.com/**
~~~~
Back-end:Django(Python)
Front-end:HTML&CSS
~~~~

####it is a personal site that has some below features :
~~~~
1)login/signup 
2)user panel
3)payment gateway(IDPAY)

~~~~
####these three files are related to heroku deploying
~~~~
Procfile
requirements.txt
runtime.txt

~~~~
####How to use?
~~~~
1)clone this repository
git clone https://github.com/saeed5959/mywebsite

2)go to repository's path
cd python-django

3)Create virtualenv named build
virtualenv -p python3 build
source build/bin/activate

2)install all needed packages and migrate and run
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver