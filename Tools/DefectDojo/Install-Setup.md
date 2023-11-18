# DefectDojo

## Installation & Setup

- Clone the repository 

        git clone https://github.com/DefectDojo/django-DefectDojo
        cd django-DefectDojo
- Build Images

        sudo ./dc-build.sh
- Run Containers
    
        sudo ./dc-up-d.sh mysql-rabbitmq --env-file ./docker/environments/mysql-rabbitmq.env
- [Change Admin Password](#change-admin-password)
- Go to `http://localhost:8080` and Login with admin user and your new password
- To see logs:

        docker compose logs initializer

### Setup HTTPS
- Auto Generated Certificate
  - Steps

        cd django-DefectDojo
        rm -f docker-compose.override.yml
        ln -s docker-compose.override.https.yml docker-compose.override.yml
  - Open https://server_ip:8443

- Custom Certificate:
  - TODO

### Scripts

`./dc-build.sh` - Build the docker images, it can take one additional parameter to be used in the build process, e.g. ./dc-build.sh --no-cache.

`./dc-up.sh` - Start the docker containers in the foreground, it needs one of the profile names as a parameter, e.g. ./dc-up.sh postgres-redis.

`./dc-up-d.sh` - Start the docker containers in the background, it needs one of the profile names as a parameter, e.g. ./dc-up-d.sh mysql-rabbitmq

`./dc-stop.sh` - Stop the docker containers, it can take one additional parameter to be used in the stop process.

`./dc-down.sh` - Stop and remove the docker containers, it can take one additional parameter to be used in the stop and remove process.

`./dc-unittest.sh` - Utility script to aid in running a specific unit test class. Requires a profile and test case as parameters.

### Change Admin Password

    docker exec -it django-defectdojo-uwsgi-1 ./manage.py changepassword admin

## Architecture

![DefectDojo-Arch.png](https://github.com/nxenon/DevSecOps/assets/61124903/5fe62fa5-e87b-4522-9c86-cfca447532ce)

### NGINX
The webserver NGINX delivers all static content, e.g. images, JavaScript files or CSS files.

### uWSGI
uWSGI is the application server that runs the DefectDojo platform, written in Python/Django, to serve all dynamic content.

### Message Broker
The application server sends tasks to a Message Broker for asynchronous execution. RabbitMQ is a well established choice.

### Celery Worker
Tasks like deduplication or the JIRA synchronization are performed asynchronously in the background by the Celery Worker.

### Celery Beat
In order to identify and notify users about things like upcoming engagements, DefectDojo runs scheduled tasks. These tasks are scheduled and run using Celery Beat.

### Initializer
The Initializer setups / maintains the database and syncs / runs migrations after version upgrades. It shuts itself down after all tasks are performed.

### Database
The Database stores all the application data of DefectDojo. Currently PostgreSQL and MySQL are supported, with PostgreSQL being the recommended option. Please note the django-watson search engine require one or more MyISAM tables, so you cannot use Azure MySQL or Cloud SQL for MySQL. AWS RDS MySQL supports MyISAM tables.

Databases:
- mysql-rabbitmq 
- mysql-redis 
- postgres-rabbitmq 
- postgres-redis*

        ./dc-up-d.sh mysql-rabbitmq --env-file ./docker/environments/mysql-rabbitmq.env

- env files in env directory:

        ./docker/environments/
