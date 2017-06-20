FROM centos:latest
MAINTAINER keldwud <keldwud@gmail.com>

RUN yum -y update && yum install -y python python-pip

ENV MYVALUE my-value

#EXPOSE 80

COPY . /clock.py
COPY . /test_clock.py

CMD ["/usr/bin/python /home/user/test_clock.py","FOREGROUND"]
