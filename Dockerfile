FROM ubuntu:16.04
MAINTAINER Alex Baden / Neurodata (neurodata.io)

RUN apt-get update
RUN apt-get -y upgrade

# install dependencies
RUN apt-get -y install \
  python-all-dev \
  python-pip \
  git vim \
  supervisor

RUN apt-get -y --fix-missing install nginx 

# install MySQL independently
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get -y install \
  mysql-server mysql-client \
  libmysqlclient-dev \
  python-mysqldb

# copy in website
RUN mkdir -p /var/www/ndwebsite
COPY . /var/www/ndwebsite/
WORKDIR /var/www/ndwebsite

# install django / python requirements
RUN pip install -r setup/requirements.txt
RUN pip install uwsgi

ENV PASSWORD 'YOUR_PASSWORD_HERE'
# create mysql users
RUN service mysql start && mysql -u root -i -e "create user 'neurodata'@'localhost' identified by '$PASSWORD';" &&\
  mysql -u root -i -e "grant all privileges on *.* to 'neurodata'@'localhost' with grant option;" &&\
  mysql -u neurodata -p$PASSWORD -i -e "CREATE DATABASE ndwebsite;" &&\
  python manage.py migrate

# colllect static files
RUN python manage.py collectstatic

# configure nginx and supervisor
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY setup/nginx-default.conf /etc/nginx/sites-available/default
COPY setup/supervisor.conf /etc/supervisor/conf.d/

# Expose the port (note: if you change the port here, you need to change it in CMD below)
EXPOSE 80

CMD ["supervisord", "-n"]


# setup entrypoint
#COPY setup/docker_entrypoint.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/docker_entrypoint.sh
#ENTRYPOINT ["docker_entrypoint.sh"]

# default command
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]