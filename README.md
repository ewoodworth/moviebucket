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

# The Stack What/Why

## Flow
- Database
- Backend/API
- Frontend

## Infra
- User/Pass is quick to setup but becomes yet one more thing to maintain which means it will break and it will be your fault. (will instantiate w/this, but aim to use OAuth asap)
- OAuth is a bigger pain initially but more robust in the long run
  - MVP: You get to look at your own records sharing is no-one or everyone
  - Eventually: Share records with select users/groups of users

# Setup a Dev Environment
- Docker

# Deploy to Production
- AWS
