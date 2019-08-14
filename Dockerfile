FROM python:3.7.4
ADD . app/
WORKDIR app/
RUN pip install --upgrade pip
RUN pip install -r github_loader/requirements.txt
EXPOSE 5000
# ENTRYPOINT ["python", "run.py"]
