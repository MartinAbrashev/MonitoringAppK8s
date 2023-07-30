FROM python:3.9.17-slim-bullseye  

# define base image

WORKDIR /app       
#define workdir of the container

COPY requirements.txt .   
#copy req.txt from the current folder to /app

RUN pip3 install --no-cache-dir -r requirements.txt   
#installing -r req.txt , with no cache 

COPY . .  
# copy everything inside this dir to /app dir /// copy the code from here, inside the image 

ENV FLASK_RUN_HOST=0.0.0.0   
#setting the container host to 0.0.0.0, no restrict for the app 

EXPOSE 5000 
#expose the port that the container will listen on it 

CMD ["flask" , "run"]  
# start the flask app

