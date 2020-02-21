FROM python:3.6-slim
ADD azureResourceMgmt.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./azureResourceMgmt.py" ]
