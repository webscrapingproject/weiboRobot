# weiboRobot

A bot to automatically collect data and publishing posts on Weibo 

## 1. Prerequisites

- Chrome
- selemium
- python3.7

## 2. Getting started 
### 2.1 Install Dependencies
```
git clone https://github.com/webscrapingproject/weiboRobot.git
cd weiboRobot
pip install -r requirements.txt
```
### 2.2 Options
```
python run.py -a <account> -p <password> -o <option(bing,geo,wea,ast)>
```

```
<account>	 accounts name of Sina Weibo
<password> 	password
<option> 	select on of the following data sources
bing 	Bing Image of the Day
geo  	National Geographic Photo of the Day
wea 	3-day weather forecast
ast 	NASA Image of the Day
```
## 3. Run via docker
```
docker run univeroner/weiborobot:latest python run.py -a <account> -p <password> -o <option(bing,geo,wea,ast)>
```

(Note: Captcha is currently unbreakable when deployed on servers without a graphical interface)
