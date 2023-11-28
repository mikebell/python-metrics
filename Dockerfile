FROM python:3

ADD requirements.txt /opt/

RUN pip install -r /opt/requirements.txt

ADD src/app.py /opt

RUN adduser --uid 1001 python

USER 1001

WORKDIR /opt/

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]