FROM python:3.11.0-alpine3.17
ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN  pip install -r requirements.txt
ADD . ./app
WORKDIR /app
CMD ["uvicorn", "--workers", "3", "--host", "0.0.0.0", "--port", "8000", "main:app"]
EXPOSE 8000
