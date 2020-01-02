FROM alpine:edge as runbase
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
RUN apk update
RUN apk add --update python3 postgresql-client libpq jpeg zlib libffi gdal geos proj proj-datumgrid geoip py3-pillow
RUN ln -s /usr/lib/libproj.so.15.1.0 /usr/lib/libproj.so
RUN pip3 install --upgrade pip

FROM runbase as buildbase
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
RUN apk update
RUN apk add --update build-base postgresql-dev libffi-dev zlib-dev jpeg-dev python3-dev gdal-dev geos-dev proj-dev geoip-dev

FROM buildbase as pipdownload
ENV PYTHONUNBUFFERED 1
COPY ./base-requirements.txt /code/base-requirements.txt
RUN pip3 download -r /code/base-requirements.txt

FROM pipdownload as pip
RUN pip3 install -r /code/base-requirements.txt

FROM pip as piplocal
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

FROM runbase as django
COPY --from=piplocal /usr/lib/python3.7/ /usr/lib/python3.7/
COPY --from=piplocal /usr/bin/ /usr/bin/
ENV PYTHONUNBUFFERED 1
RUN adduser -D -u 1000 django

FROM django as emptydjango
WORKDIR /code/
COPY staticcache/ /code/staticcache/
RUN chown -R django:django /code/staticcache/

FROM emptydjango as staticdjango
USER django
WORKDIR /code/
COPY base-requirements.txt /code/base-requirements.txt
COPY blog/                 /code/blog/
COPY data/                 /code/data/
COPY experience/           /code/experience/
COPY experiment            /code/experiment/
# COPY dump.json           /code/dump.json
# COPY freeze.txt          /code/freeze.txt
COPY homepage/             /code/homepage/
COPY manage.py             /code/manage.py
COPY meeting/              /code/meeting/
COPY requirements.txt      /code/requirements.txt
COPY run.sh                /code/run.sh
# Don't need this for production though
COPY run.sh.local          /code/run.sh.local
COPY teratree/             /code/teratree/
EXPOSE 8000
CMD ["/bin/sh", "/code/run.sh"]
