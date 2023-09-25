FROM python:3.9

RUN apt-get update && apt-get install -y nginx

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV=production

EXPOSE 5000

# ENTRYPOINT ["./entrypoint.sh"]
CMD ["/bin/bash", "entrypoint.sh"]
