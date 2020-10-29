# -*- coding:UTF-8 -*-
from selenium import  webdriver
from time import sleep
from base_page import Base_method
class common(Base_method):
    #点击元素功能
    def click(self,type,value):
        # 调用locateElement定位元素,调用click()进行点击操作
        self.locateElement(type, value).click()

    # 对定位到元素进行输入
    def input_data(self, type, value,data):
        # 调用locateElement定位元素
        self.locateElement(type, value).send_keys(data)

    # 获取定位到的元素中的文本内容<a>text</a>
    def getText(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回文本内容
        return el.text

    # 获取定位到的元素中的标签值
    def getAttribute(self, type, value,name):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回文本内容
        return el.get_attribute(name)


#如果是引用该类则不执行该方法
if __name__ == "__main__":
    url = "https://www.baidu.com"
    test = common(webdriver.Chrome())
    test.open(url)
    test.input_data("id","kw","Howell")
    test.click("id","su")
    sleep(3)
    test.getScreen('C:\\Users\\Administrator\\Desktop\\python_selenium\\webtest\\PO\\login')
