FROM centos:latest
MAINTAINER keldwud <keldwud@gmail.com>

RUN yum -y update && yum install -y \
  python \
  python-pip

ENV MYVALUE my-value

#EXPOSE 80

COPY clock.py /opt/clock.py
COPY test_clock.py /opt/test_clock.py

WORKDIR /opt

CMD ["/usr/bin/python /opt/test_clock.py","FOREGROUND"]
