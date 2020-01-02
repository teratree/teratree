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
alias manage.py='docker-compose -f `pwd`/docker-compose.yml run --rm web python3 manage.py'
manage.py startapp experiment
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
```

or is you are importing data from within the container:

```
manage.py loaddata /code/data.json
```

You can connect to the PostgreSQL database with:

```
alias psql='docker-compose -f `pwd`/docker-compose.yml run --rm web psql'
psql -h db -U postgres postgres
```

(You will need to run `psql -h db -U postgres postgres -c 'DELETE FROM wagtailcore_site CASCADE; DELETE FROM wagtailcore_grouppagepermission CASCADE; DELETE FROM wagtailcore_page CASCADE;'` first if you are loading an entire dataset from a freshly migrated database since wagtail adds some data you need to remove first)

That means to import from a dump you run:

```
alias psql='docker-compose -f `pwd`/docker-compose.yml run --rm web psql'
alias manage.py='docker-compose -f `pwd`/docker-compose.yml run --rm web python3 manage.py'
alias aws='docker-compose -f `pwd`/docker-compose.yml run --rm aws'
manage.py migrate
psql -h db -U postgres postgres -c 'DELETE FROM wagtailcore_site CASCADE; DELETE FROM wagtailcore_grouppagepermission CASCADE; DELETE FROM wagtailcore_page CASCADE;'
manage.py loaddata /code/dump-live.json
# The /media directory in the container is mounted to ./web/media
aws s3 sync s3://teratree-media /media
```

NOTE: You have to be running *exactly* the same schemas on a completely empty database for a dump and load to work.

In development remember to clear your browser cache once you've changed static files and run `manage.py collectstatic` by restarting the Docker container. Otherwise the browser will use the cached old version.

### DB

If you are starting with an empty database you'll want to set up database tables and an admin user:

```
manage.py migrate
manage.py createsuperuser
```


### Syntax Formatting

```
autopep8 --diff --exclude /code/mysite/settings/base.py -r /code/
autopep8 --in-place --exclude /code/mysite/settings/base.py -r /code/
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

Set the deployment target to the Heroku app name:

```
export DEPLOYMENT_TARGET=teratree-staging
```

Set up your local alias:

```
alias manage.py='docker-compose -f `pwd`/docker-compose.yml run --rm web python3 manage.py'
```

If you are going to deploy data from a local instance, dump it now:

```
manage.py dumpdata --natural-foreign --natural-primary --indent 2 --format json > web/dump.json
```

Or to get the data from the live site:

```
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py dumpdata --natural-foreign --natural-primary --indent 2 --format json > web/dump.json
```

The first time you deploy you need to set create the PostGIS extension and the database tables, then remove unncessary Wagtail data before loading your data:

```
echo 'CREATE EXTENSION postgis;' | heroku pg:psql -a $DEPLOYMENT_TARGET
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py migrate
# Danger, only run this if you are setting up a fresh database
# heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py wipedb
# heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py loaddata /code/web/dump.json
```

Then commit any changes you want to deploy.

Finally run these one at a time, otherwise they might not all get run:

```
# See https://devcenter.heroku.com/articles/local-development-with-docker-compose
heroku login
heroku container:login
git stash
manage.py collectstatic --clear --noinput | grep -v 'Found another file with the destination path'
cd web
heroku container:push -a $DEPLOYMENT_TARGET web
heroku container:release -a $DEPLOYMENT_TARGET web
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py migrate
# The /media directory in the container is mounted to ./web/media
# alias aws='docker-compose -f `pwd`/docker-compose.yml run --rm aws'
# aws s3 sync /media s3://teratree-media
# heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py loaddata /code/dump.json
# heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py createsuperuser
git stash pop
```

Other useful commands:

```
EDITOR=vim heroku config:edit --app $DEPLOYMENT_TARGET
heroku logs --tail --app $DEPLOYMENT_TARGET
```

Resetting:

```
export DATABASE_URL=...
heroku pg:reset -a $DEPLOYMENT_TARGET DATABASE
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py migrate
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/psql $DATABASE_URL -c 'DELETE FROM wagtailcore_site CASCADE; DELETE FROM wagtailcore_grouppagepermission CASCADE; DELETE FROM wagtailcore_page CASCADE;'
heroku run --type=worker -a $DEPLOYMENT_TARGET /usr/bin/python3 manage.py loaddata /code/dump.json
```

Backup:

```
DATABASE_URL=postgres://ngqfyabpszlkoh:d48a4e89269768c6591743021a0291afe496fd30ab7870b611cbf47ffbfca704@ec2-54-217-219-235.eu-west-1.compute.amazonaws.com:5432/ddsjvmq9qd0pie
export DEPLOYMENT_TARGET=teratree
heroku run --type=worker -a $DEPLOYMENT_TARGET pg_dump $DATABASE_URL > web/dump-live-3.sql
mv db db.old
docker-compose up
alias psql='docker-compose -f `pwd`/docker-compose.yml run --rm web psql'
cat web/dump-live-3.sql | psql -h db -U postgres postgres
alias manage.py='docker-compose -f `pwd`/docker-compose.yml run --rm web python3 manage.py'
manage.py migrate
```
