# Profiles REST API

(Tested on Windows)

Installation:

1. Download and install Vagrant (for server setup)
2. Download and install VirtualBox
3. Install Atom
6. Install Git
7. Install Mode Header for Google Chrome extension

Why Vagrant not Docker:

Docker: 1. Streamline workflow
2. All developers use supported OS

Vagrant: 1. Just getting started
2. Supported on wider range of OS

Procedure:
1. Install the requirements
2. Create a workspace (folder for storing your work)
3. Using GIT implement the following in your workspace:
```
a) git init
b) git add .
```
c) Check the folder is added or not in Atom
```
d) git commit -am "name of changes in commit"
```
e) Find a public/private key in the folder using
```
"ls ~/.ssh"
```
in GIT bash in the workspace
f) Create a key using
```
"ssh-keygen -t rsa -b 4096 -C "emailID""
```
g) Click enter for default folder and enter a passphrase if you want
h) Check if the file exists using
```
"ls ~/.ssh"
```
i) If exists then open ".pub" file using
```
"cat ~/.ssh/ida_rsa.pub"  #this contains #public key
```
j) Copy this key from ssh-rsa till the emailID given
j) Add that public key in GitHub by going to SSH/GPG keys in settings and add the title as the your PC's name using "hostname" in cmd
k) Open Git bash and push the folder to your GitHub account using the commands:
```
	1.1) git remote add origin https://github.com/GITHUB_ACCOUNT/repository_name.git
	1.2) git push -u origin master (enter your GitHub credentials)
	1.3) After adding/editing some files use:
		1.3.1) git add .
		1.3.2) git commit -m "Changes made title"
		1.3.3) git push origin
```
4. Using Vagrant as virtual space to work after installation:
4.1 Run vagrant using
	```
	"vagrant init ubuntu/bionic64"
	then "vagrant up"
	and then get into vagrant using "vagrant ssh" (can also be used to get back in after exiting)
	```
4.2 Use "cd /vagrant" to get into the Atom folder of Vagrant, now check the files using "ls" (now you can see the sync by adding or deleting in any place, very cool sync)

5. Create any file of python and run it using "python filename.py".
6. Exit the vagrant using "exit"
7. Commit the changes using 1.3 given above

Working on Vagrant:
1. Start the Vagrant server by going to workspace and using:
```
vagrant up and then vagrant ssh
```
2. Setup the virtual environment for python in environment folder using:
```
python -m venv ~/env
```
3. Activate and deactivate using:
```
source ~/env/bin/activate
deactivate
```
Know more on python virtual environment cheatsheet:
```
https://python-guide.readthedocs.io/en/latest/dev/virtualenvs
```
4. See that you've installed the required packages from the ```requirements.txt```
or use:
```
pip install -r requirements.txt
```

Creating a Django Project:

Setting up:

1. Call the Django admin and start new project using
```
django-admin.py startproject profiles_project .	#"." is used to make a folder in root
```
2. Now you can see project folder has been initiated in Atom, create an app(API) using
```
python manage.py startapp profiles_api
```
3. Enable the profile_api in project by going to setting.py in profiles_project and listing the apps required to install for the project and add ```rest_framework```,```rest_framework.authtoken``` and ```profile_api``` in the same format

Running:
1. ```python manage.py runserver 0.0.0.0:8000``` to run our server
2. Goto ```127.0.0.1``` on browser to check whether the project setup was done or not

Creating our user database model:

1. Open ```models.py``` and import ```AbstractBaseUser``` and ```PermissionMixin``` from ```auth.models```

2. Follow the code in ```models.py``` in ```profile_api```

3. Maintain a ```UserProfileManager``` as the admin of the application and create a user, superuser

4. Create migrations and sync DB's:

4.1 Go to Vagrant and in the virtual environment use ```python manage.py makemigrations profile_api``` to create a file in ```profile_api```

4.2 Run the migration using ```python manage.py migrate```

Enabling a Django admin:

1. Create a superuser in cli using ```python manage.py createsuperuser``` and enter the credentials for the data to be safe

2. Enable Django admin (default already created but to register new model in interface) by going to ```admin.py``` and importing ```from profile_api import models``` and registering our model using ```admin.site.register(models.UserProfile)```

3. Test the Django admin by starting the development server and going to local host by:```python manage.py runserver 0.0.0.0:8000``` and opening ```127.0.0.1:8000/admin```

Creating our APIView with GET, POST, PUT, PATCH, DELETE:

1. Go to ```views.py``` and write the code given for Response passed as dictionary

2. Configure the URLs by creating a new file named ```urls.py``` in ```profile_api```

3. Create another ```urls.py``` in profile_api and configure according to code given

4. Test the url by opening ```127.0.0.1:8000/api/hello-view```

5. Add a GET method in ```views.py``` to return a message

5. Add a ```serializers.py``` to profile_api and check the code in the above

6. Add a POST method in ```views.py``` to implement the serializer and to handle requests

7. Add PUT, PATCH and DELETE in ```views.py``` according to the file

Creating a ViewSet for our API:

1. In  ```views.py``` write the ViewSet code by import ViewSet using ```from rest_framework import viewsets```

2. Goto ```urls.py``` in profile_api and import ```DefaultRouter``` and make an include operation of router in the path. Check for base_name variable, sometimes it comes basename.

3. Add Create, Retrieve, Update, Partial_Update and Destroy to ViewSet

Building ProfileAPI:

1. Open ```serializers.py``` and add another class ```UserProfileSerializer``` to add the operations in the class like create, update

2. Create a ViewSet to access through the endpoint in ```views.py``` to allow users create profile

3. Test the create profile using POST and PATCH

4. Create a permission class in ```profile_api``` to prevent users accessing others profile

5. Add authentication and permission to ```views.py```
