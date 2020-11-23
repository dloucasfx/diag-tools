FROM python:3.6-slim
ADD azureResourceMgmt.py /
ADD metrics.py /
ADD metricsUSGOV.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y vim 
CMD [ "python", "./metrics.py" ]
