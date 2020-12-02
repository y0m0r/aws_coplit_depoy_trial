FROM python:3
RUN pip install flask
RUN pip install flask_restful
EXPOSE 3000
ADD helloworld.py /
CMD ["python", "./helloworld.py"]
