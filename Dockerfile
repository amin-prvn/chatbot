FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./app/req.txt /app
RUN pip install -r req.txt
COPY ./app /app
