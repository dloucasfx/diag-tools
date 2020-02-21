FROM python:3.6-slim
ADD azureResourceMgm.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./azureResourceMgm.py" ]
