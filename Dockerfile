# This defines how to build our Docker image - what base image to use, what files to copy, and how to run our app.
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
