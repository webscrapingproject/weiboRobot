# weiboRobot
自动采集数据发微博机器人

## 1. 本地使用
基本要求：Chrome+selemium+python3.7
### 1.1 安装依赖
```
git clone https://github.com/webscrapingproject/weiboRobot.git
cd weiboRobot
 pip install -r requirements.txt
```
### 1.2 用法
```
python run.py -a <account> -p <password> -o <option(bing,geo,wea,ast)>
```
参数解释：
```
<account>	 新浪微博帐号
<password> 	新浪微博密码
<option> 	发布内容选择，仅支持单选
bing 	bing每日图片以及标题
geo  	国家地理每日图片
wea 	中国气象网近3天天气预报
ast 	NASA每日图片以及文字（采集于中国天文馆的翻译）
```
## 2. docker部署
```
docker run univeroner/weiborobot:latest python run.py -a <account> -p <password> -o <option(bing,geo,wea,ast)>

```
注意：目前在无图形界面的服务器上部署时出现验证码无法破解的情况
