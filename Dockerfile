FROM castyr/spacy_en:latest
MAINTAINER Justin Phillips "justin_phillips@ultimatesoftware.com"
ADD . /app
COPY ./src/ /app/
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
USER flask
EXPOSE 5000
CMD python /app/app.py