# teratree

Heroku will expect an app called `teratree-staging` to be created, along with a free PostgreSQL instance. The Heroku instance needs the following variables set up:

* `ADMINS` - a comma-separated list of emails to receive error reports
* `ALLOWED_HOSTS` - a comma-separated list of allowed hosts
* `DATABASE_URL` - The database settings. This is set up by Heroku.
* `DJANGO_SETTINGS_MODULE` - `teratree.settings.production`
* `SECRET_KEY` -  a long (32 characters+) random string used for deriving secrets for the session cookies and other things

For media in production you'll need to create an S3 bucket with suitable permissions as described in `web/djangosharedsettings/bucket.py` then set:

* `AWS_STORAGE_BUCKET_NAME` - The name of the S3 bucket
* `AWS_ACCESS_KEY_ID` - The access key ID for the bucket above
* `AWS_SECRET_ACCESS_KEY` - The secret key for the access key above

For email you can use the variables in `web/djangosharedsettings/email.py`. At the moment the system will use the first email specified in `ADMINS`:

* `EMAIL_PORT` - e.g. `465`
* `EMAIL_USE_TLS` - e.g. `"false"`
* `EMAIL_USE_SSL` - e.g. `"true"`
* `SERVER_EMAIL` - e.g. `admin@teratree.example.com`
* `DEFAULT_FROM_EMAIL` - e.g. `admin@teratree.example.com`
* `EMAIL_HOST` - e.g. `smtp.example.com`
* `EMAIL_HOST_PASSWORD`
* `EMAIL_HOST_USER`

For instructions on how to test email sending see `EMAIL.md`.


## Development

1. Install the latest version of Docker
2. Clone the repo to a directory called `teratree` (if you choose a different name, Docker Compose will name the containers in a different way to the names used in the documentation).
3. Copy `docker-compose.yml.example` to `docker-compose.yml` and update it with the settings you want to use for development

   ```
   cp docker-compose.yml.example docker-compose.yml
   ```

4. Run `docker-compose up --build`

Your will be hosted then at http://localhost:8000 (the port may be different if you configured a different `PORT` variable).

```
docker-compose down && docker-compose up --build web db && docker-compose logs -f web db
```

5. Create your first app:

```
docker-compose run --rm web python manage.py startapp experiment
docker-compose run --rm web python manage.py makemigrations
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
```

You can connect to the PostgreSQL database with:

```
docker-compose run --rm web psql -h db -U postgres postgres
```

### DB

If you are starting with an empty database you'll want to set up database tables and an admin user:

```
docker exec -it teratree_web_1 /usr/local/bin/python3 manage.py migrate
docker exec -it teratree_web_1 /usr/local/bin/python3 manage.py createsuperuser
```


### Syntax Formatting

```
docker exec -it teratree_web_1 /usr/local/bin/autopep8 --diff -r /code/
docker exec -it teratree_web_1 /usr/local/bin/autopep8 --in-place -r /code/
```


### Running Tests

Once you've written tests, you can run them like this:

```
docker exec -it teratree_web_1 /usr/local/bin/python3 manage.py test --failfast -k teratree/test
```

You can use VNC Viewer to view Chrome while the tests are running.

https://www.realvnc.com/en/connect/download/viewer/

Load the viewer and enter the address `localhost:5900` while the `chrome` docker container is running to see the testing visaully in browser. You'll need to ignore the warning about the connection being unencrypted. Then enter the password `secret`.


## Deployment

### Release to Heroku

Make sure static files are up to date:

```
docker exec -it teratree_web_1 /usr/local/bin/python3 manage.py collectstatic --noinput --link
```

Set the deployment target to the Heroku app name:

```
export DEPLOYMENT_TARGET=teratree-staging
```

Create a new version number each time. You can find the old number like this:

```
docker images | grep $DEPLOYMENT_TARGET
```

Then export the new version:

```
export BACKEND_VERSION=0.1.1
```

Then commit any changes you want to deploy.

Finally run these one at a time, otherwise they might not all get run:


```
# See https://devcenter.heroku.com/articles/local-development-with-docker-compose
heroku login
heroku container:login
git stash
heroku container:push web
# cd web
# docker build -t $DEPLOYMENT_TARGET:$BACKEND_VERSION .
# docker tag $DEPLOYMENT_TARGET:$BACKEND_VERSION registry.heroku.com/$DEPLOYMENT_TARGET/web
# docker push registry.heroku.com/$DEPLOYMENT_TARGET/web
heroku container:release --app $DEPLOYMENT_TARGET web
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/local/bin/python3 manage.py migrate
git stash pop
```

Other useful commands:

```
heroku config --app $DEPLOYMENT_TARGET
heroku logs --tail --app $DEPLOYMENT_TARGET
```
