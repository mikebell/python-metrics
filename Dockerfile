FROM python:3

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD src/app.py /

# ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
