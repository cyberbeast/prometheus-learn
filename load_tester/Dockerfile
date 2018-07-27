FROM python:3.6-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD tester.py /var/app/tester.py

CMD python /var/app/tester.py