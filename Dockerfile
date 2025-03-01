FROM python:3.9

WORKDIR /scores

COPY main_score.py utils.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 30000

CMD ["python", "main_score.py"]



