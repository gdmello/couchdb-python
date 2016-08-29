FROM couchdb:1.6.1
RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install couchdb

COPY  set_python_views.py /opt/scripts/set_python_views.py
RUN python /opt/scripts/set_python_views.py
