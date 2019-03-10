
  
FROM joyzoursky/python-chromedriver:3.7-selenium

# copy weibo_robot2
ADD . /code
WORKDIR /code

# install requirements
RUN pip install -r requirements.txt
