FROM python:3.12
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
COPY ./data /code/data
WORKDIR /code/src
CMD ["fastapi", "run", "api.py", "--port", "80"]