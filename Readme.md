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
4.1) Run vagrant using
	```
	"vagrant init ubuntu/bionic64"
	then "vagrant up"
	and then get into vagrant using "vagrant ssh" (can also be used to get back in after exiting)
	```
4.2) Use "cd /vagrant" to get into the Atom folder of Vagrant, now check the files using "ls" (now you can see the sync by adding or deleting in any place, very cool sync)

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
