FROM python:3.8
ENV WORKDIR=/var/lib/labor
VOLUME /root/.labor

WORKDIR $WORKDIR

COPY ./ ./

RUN pip install -e .

CMD  [ "python", "labor/test.py" ]
