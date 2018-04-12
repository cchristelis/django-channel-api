#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------

FROM python:3.5
MAINTAINER Christian Christelis <christian@kartoza.com>

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not with to use caching
RUN apt-get -y update

RUN apt-get install locales && \
    echo "en_ZA.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_ZA.UTF-8

ENV LANG en_ZA.UTF-8
ENV LANGUAGE en_ZA:en
ENV LC_ALL en_ZA.UTF-8

ADD REQUIREMENTS.txt /REQUIREMENTS.txt
RUN pip3 install -r /REQUIREMENTS.txt

# Open port 8080 as we will be running our uwsgi socket on that
EXPOSE 8080

WORKDIR /home/web/django_project


# daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem -b 0.0.0.0 -p 8080 django_project.asgi:channel_layer
CMD ["daphne", "-e", "ssl:443:privateKey=key.pem:certKey=crt.pem", "-b", "0.0.0.0", "-p", "8080", "django_project.asgi:channel_layer"]