#Load the python base image, so we won't need to run commands for python and pip installation.
FROM python:3.6
#Copy the dependencies to the image
COPY ./requirements.txt /requirements.txt
#Define the directory 
WORKDIR /
#Install dependencies
RUN pip3 install -r requirements.txt
COPY . /
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app/app.py" ]