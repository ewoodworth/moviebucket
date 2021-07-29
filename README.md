# moviebucket
Movie database with HTTP user interface.

## MVP
Timed task, 72 hours
1 hr planning, 2 X 3 hr builds, 1 hr cleanup/proofreading

1. The service must create, list, update, and delete movies in the collection.
2. Each movie in the collection needs the following attributes:
a. Title [text; length between 1 and 50 characters]
b. Format [text; allowable values “VHS”, “DVD”, “Streaming”] 
c. Length [time; value between 0 and 500 minutes]
d. Release Year [integer; value between 1800 and 2100]
e. Rating [integer; value between 1 and 5]
3. The service must be accessible over http. You can implement an API, a command line interface (curl, node, etc.) and/or a basic web-based GUI.
4. Add an authentication method to restrict access to the service.

## Eventually
1. Sophisitcated Authorization
2. Dockerize the dev environment


# Deploy to Production
Initial Setup Per this Tutorial: https://medium.com/@abhishekmeena_68076/how-to-deploy-the-flask-django-app-on-aws-ec2-with-gunicorn-ngnix-with-free-ssl-certificate-566b2ada3b6a

- ssh to EC2 CLI
- git pull
- pip install -r requirements.txt

# The Stack What/Why

## Flow
### Database
- Postgresql: Versitle, powerful, scaleable, free. We don't need anything exotic or domain-specific for the tasks in the MVP
### Backend/API
- Python/Flask: Familiar, Flask also is SUPER well documented for database interactions and less overhead than Django
### Frontend
- MVP: Curl commands
- Eventually: React or somesuch. React + OAuth is a better user experience and safer than trying to keep track of whether you scrubbed your variables properly and stored your login credentials safely for Javascript/AJAX.

## Infra
### Auth
- User/Pass is quick to setup but becomes yet one more thing to maintain which means it will break and it will be your fault. (will instantiate w/this, but aim to use OAuth asap)
- OAuth is a bigger pain initially but more robust in the long run
  - MVP: You get to look at your own records sharing is no-one or everyone
  - Eventually: Share records with select users/groups of users

# Setup an EC2 Instance (notes I wish I'd taken last time I did this)
## Locally
- stick the aws generated keypair in the local dir IMMEDIATELY
- ssh in
## On the EC2
- sudo apt update
- sudo apt install python3-venv
- python3 -m venv venv
- source venv/bin/activate
- ssh-keygen
- Move pub key to GitHub instance with tag as EC2 usecase
- git clone git@github.com:ewoodworth/moviebucket.git
- sudo apt install gunicorn3

