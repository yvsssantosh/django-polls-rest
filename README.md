# Polls API using Django REST
This repository defines the basic working of Polls API.

Let's first clone our sample django application from

```
git clone https://github.com/yvsssantosh/django-polls-rest.git
```

Just to make sure we're on master branch, run the command `git checkout master`

To test the application locally, let's create a virtual environment, and test the server
```
# Creating a virtual environment
mkvirtualenv pollsapi

# Installing current project requirements
pip install -r requirements.txt

# Connect to postgres
export POSTGRES_USER=postgres
export POSTGRES_DB=postgres
export POSTGRES_PASSWORD=postgres
export POLLSAPI_PG_HOST=127.0.0.1

# Running migrations
python manage.py migrate

# Start the local server
python manage.py runserver 0.0.0.0:8000
```

To deploy this application using Kubernetes on GKE, with Ingress Load Balancing, visit https://github.com/yvsssantosh/django-on-k8s/