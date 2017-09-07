FROM centos

ENV ALL tmp

MAINTAINER "praveen"

RUN yum install httpd -y


COPY run.sh /${ALL}/

COPY index.html  /var/www/html/

RUN chmod -v +x /${ALL}/run.sh

CMD ["bash","/tmp/run.sh"]


