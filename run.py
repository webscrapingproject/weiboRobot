# coding=utf-8
from weibo import *
import sys,getopt
sys.path.append("..")
from postSource.bing import *
from postSource.astro import *
from postSource.weatherCast import *
from postSource.Geogra import *

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ha:p:o:",["help","account=","password=","option="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print('Usage : python run.py -a <account> -p <password> -o <option(bing,geo,wea,ast)>')
            sys.exit()
        elif opt in ("-a", "--account"):
            email = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-o", "--option"):
            option = arg
    robot=weibo_robot()
    robot.login(email,password)
    test=robot.login_successfully()
    print("first: ",test)
    if(test==False):
        robot.crack()
        test=robot.login_successfully()
        print("second: ",test)
    # 重新登录
    while(test==False):
        robot.__del__()
        robot=weibo_robot()
        robot.login(email,password)
        if (robot.login_successfully() == False):
            robot.crack()
    robot.jump()
    def bing():
        bing=bingWallpaper()
        robot.newPost(bing[0],bing[1])
    def wea():
        wea=weatherCast()
        robot.newPost(wea[0],wea[1])
    def ast():
        ast=astro()
        robot.newPost(ast[0],ast[1])
    def geo():
        geo=geogra()
        robot.newPost(geo[0], geo[1])
    eval(option)()
    robot.__del__()
    print('success!')
if __name__ == '__main__':
    main(sys.argv[1:])
