FROM couchdb:1.6.1
RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install couchdb
# Credit to Justin Simonelis (https://github.com/jelis) for dockerfile instructions above.

COPY  set_python_views.py /opt/scripts/set_python_views.py
RUN python /opt/scripts/set_python_views.py
