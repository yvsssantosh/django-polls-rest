# Polls API using Django REST
This repository defines the basic working of Polls API.

Let's first clone our sample django application from

```
git clone https://github.com/yvsssantosh/django-polls-rest.git
```

Just to make sure we're on master branch, run the command `git checkout master`

To test the application locally, let's create a virtual environment, and test the server
```sh
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

# Setup Google Storage to serve Static Files (Optional - Read NOTE below to avoid this)
export GS_ACCESS_KEY_ID=YOUR_GOOGLE_STORAGE_ACCESS_KEY_ID
export GS_SECRET_ACCESS_KEY=YOUR_GOOGLE_STORAGE_SECRET_ACCESS_KEY
export GS_BUCKET_NAME=YOUR_GOOGLE_STORAGE_BUCKET_NAME
# NOTE : If you do not want to setup this, remove the `LAST 6 LINES` under STATIC_FILES_SETTINGS in pollsapi/settings.py & set DEBUG = True in settings.py file

# Start the local server
python manage.py runserver 0.0.0.0:8000
```

To deploy this application using Kubernetes on GKE, with Ingress Load Balancing, visit https://github.com/yvsssantosh/django-on-k8s/