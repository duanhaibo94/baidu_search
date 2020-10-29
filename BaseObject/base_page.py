# -*- coding:UTF-8 -*-
from selenium import  webdriver
import time
class Base_method(object):
    #新建对象就自动创建浏览器并且最大化窗口
    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        self.driver = driver
        self.driver.maximize_window()
    #打开网页功能
    def open(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
    # 关闭网页功能
    def close(self):
        time.sleep(3)
        self.driver.close()
    # 定位元素功能
    def locateElement(self,type,value):
        if type=="id":
            el = self.driver.find_element_by_id(value)
        elif type=="name":
            el = self.driver.find_element_by_name(value)
        elif type=="class_name":
            el = self.driver.find_element_by_class_name(value)
        elif type=="tag_name":
            el = self.driver.find_element_by_tag_name(value)
        elif type=="link_text":
            el = self.driver.find_element_by_link_text(value)
        elif type=="partial_link_text":
            el = self.driver.find_element_by_partial_link_text(value)
        elif type=="xpath":
            el = self.driver.find_element_by_xpath(value)
        elif type=="css_selector":
            el = self.driver.find_element_by_css_selector(value)
        return el

    def getScreen(self,file_name):
        # picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        picture_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        picture_url = self.driver.get_screenshot_as_file(file_name + picture_time + '.png')
        # print("%s：截图成功！！！" % picture_url)
        if picture_url==True:
            print("截图成功")
        else:
            print("截图失败")

    # 删除对象时自动执行的方法
    def __del__(self):
        self.driver.close()

if __name__ == "__main__":
    url = "https://www.baidu.com"
    brower = Base_method(webdriver.Chrome())
    brower.getScreen('C:\\Users\\Administrator\\Desktop\\python_selenium\\webtest\\PO\\BaseObject')