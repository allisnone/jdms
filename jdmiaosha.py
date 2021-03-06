# _*_coding:utf-8_*_  
from selenium import webdriver
import datetime  
import time


driver = webdriver.Firefox()

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    time.sleep(30)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success')

def miaosha_order(good_id):
    """
    秒杀链接
    """
    #玩客云：https://item.jd.com/4993737.html
    #https://item.jd.com/4993773.html
    url='https://item.jd.com/%s.html'%(good_id)
    driver.get(url)
    driver.find_element_by_id("btn-onkeybuy").click()
    time.sleep(3)
    return
# buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
        time.sleep(0.5)

# entrance
login('usename', 'password')
good_id = 6076915
miaosha_order(good_id)
buy_on_time('2017-01-01 14:00:00')