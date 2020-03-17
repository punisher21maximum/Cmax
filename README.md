# Cmax
March17_v1

Python : 3.5
Django : 2.0.2

## To run the website
### install in order
1.install python3
sudo apt-get install python3.6 #any python 3 is OK!

2.install virtual environment
sudo pip3 install virtualenv    or  sudo python3 -m pip install virtualenv

3.install django2.0.2
sudo python3 -m pip install django==2.0.2 

### Run in order
1.copy paste the complete website (main newwebsite folder) in folder_X

2.create virtual environment (preferably in same folder_X)
$ virtualenv -p /usr/bin/python3.6 venv #python3.x version same as installed
Note : name of your virtualenv is -> venv

3.activate virtual environment
$ source venv/bin/activate 
or 
$ cd venv 
$ . bin/activate
$ cd ..

4.run convimax
$ ls #should give
newwebsite  venv
$ cd newwebsite
$ ls #should give
db.sqlite3  etx_app  manage.py  manage.pyc  media  newwebsite  others  owner  PayTm  polls
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
open browser and go to
http://localhost:8000/polls/etx/etx_index

### To close running website (server)

1.on terminal press : ctrl+c







