FROM python:3.9

WORKDIR /app

COPY Scores.txt utils.py ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main_score.py"]


