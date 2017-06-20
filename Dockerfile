FROM centos:latest
MAINTAINER keldwud <keldwud@gmail.com>

RUN yum -y update && yum install -y python python-pip

ENV MYVALUE my-value

#EXPOSE 80

CMD ["/usr/bin/python /home/user/test_ball-clock.py","-D","FOREGROUND"]
