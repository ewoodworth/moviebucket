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

### MVP Notes:
2 infrastructure gaps that mean failute to meet mvp. 
1 - gunicorn isn't serving the Flask app off the EC2 instance 
2 - SQLAlchemy fails to instantiate the RDS database on a (very mysterious) failure to authenticate. 

This leaves a lot of the code untested. Gnereally the data model as described should meet the data gathering and authentication requirements (2, 4) THe Flask app should meet the functional requirements (1) and serve content over http (3) The integration errors prevent any component from actually* working.

# Deploy to Production
Initial Setup Per this Tutorial: https://medium.com/@abhishekmeena_68076/how-to-deploy-the-flask-django-app-on-aws-ec2-with-gunicorn-ngnix-with-free-ssl-certificate-566b2ada3b6a

- ssh to EC2 CLI
 
> git pull

> pip install -r requirements.txt

> ansible-vault decrypt config.ini

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

