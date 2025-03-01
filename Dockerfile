FROM python:3.9

WORKDIR /scores

COPY Scores.txt utils.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main_score.py"]


