FROM python:3.6-slim
ADD syncMetricType.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS="/keyfile.json"
CMD [ "python", "./syncMetricType.py" ]
