FROM python:3.6-slim

WORKDIR Users\kilia\pythonProject\python\miniProjFilm

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","./film.py"]