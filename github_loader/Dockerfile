FROM python:3.7.4
ADD . /app/
WORKDIR /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flaskblog.py"]
EXPOSE 5000
