FROM python:3.6
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code
CMD ["python", "app.py"]