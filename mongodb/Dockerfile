FROM python:2.7-slim
ADD connectionTest.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./connectionTest.py" ]
