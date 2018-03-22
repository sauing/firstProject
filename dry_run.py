# try:
#     assert False, "Hello!"
# except AssertionError as e:
#     e.args += ("this is the assertion error",)
#     raise
#
#
#
# ############################
#     def add_company_phonebook(self):
#         try:
#             status=self.boss_page.commonfunctionality.add_company_phonebook()
#         except:
#             print(e)
#             raise
#
#
#     def add_company_phonebook_verify(self):
#         try:
#             status1=self.boss_page.commonfunctionality.add_company_phonebook_verify()
#         except:
#             print(e)
#             raise
#         return status1
#
#
# #####################################3
# #Common Functionality
#
#
#
# ################
#     def switch_page_company_phonebook(self,*option):
#         """
#         To switch to company phonebook page
#         :return:
#         """
#         try:
#             status=False
#             time.sleep(2)
#             self.action_ele.mouse_hover("home_tab")
#             time.sleep(1)
#             self.action_ele.click_element("company_phonebook")
#             self.action_ele.explicit_wait("add_button")
#             status=True
#         except Exception,e:
#             print(e)
#             self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
#
#         return status
#
#     def add_company_phonebook(self):
#         """
#         To add contact in company phone book
#         :return:
#         """
#         try:
#
#             status=False
#             self.action_ele.click_element("add_button")
#             time.sleep(2)
#             self.action_ele.explicit_wait("add_phonebook_ok_button")
#             self.name="Test"
#             import random,string
#             letter="".join(random.choice(string.ascii_letters))
#             self.name=(letter.join("_"+self.name))
#             self.action_ele.input_text("first_name",self.name)
#             self.action_ele.input_text("last_name","user")
#             self.action_ele.click_element("add_phonebook_ok_button")
#             time.sleep(5)
#             status=True
#         except Exception,e:
#             print(e)
#             self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
#         return status
#
#     def add_company_phonebook_verify(self):
#         """
#         verify the contact has been added
#         :return:
#         """
#         try:
#             status=False
#             self.action_ele.input_text("name_text_field",self.name)
#             time.sleep(1)
#             phonebook_names=self._browser.elements_finder("grid_data")
#             for name in range(len(phonebook_names)):
#                 if phonebook_names[name].text=="Test":
#                     status=True
#         except Exception,e:
#             print(e)
#             self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
#         return status


# x=iter(range(5))
# for each in x:
#     print each

# def func(myfunc):
#     def func1():
#         return myfunc() +1
#     return func1
#
# @func
# def myfunc():
#     return 3
#
# print myfunc()


# def outer():
#     print "outer"
#     def inner():
#         print "inner"
#     return inner
#
# outer()()

# class class1(object):
#     def sound(self):
#         print "Hey Manisha"
#
#
# class class2(object):
#     def sound(self):
#         print "Hey Ayushi"
#
#
# def makeSound(animalType):
#     animalType.sound()
#
#
# Obj1 = class1()
# Obj = class2()
#
# makeSound(Obj1)
# makeSound(Obj)


# class outer(object):
#     def __init__(self):
#         self.cup="Empty"
#
#     def breakfast(self):
#         print self.cup
#         self.cup="coffee"
#         print self.cup
#     @classmethod
#     def lunch(self):
#         self.cup="juice"
#         print self.cup
#     @staticmethod
#     def snacks():
#         cup = "Tea"
#         print cup
# obj=outer()
# obj.breakfast()
# print obj.breakfast
# obj.lunch()
# print obj.lunch
# obj.snacks()
# print obj.snacks


# class parent():
#     def __init__(self):
#         print "Parent Class"
#
#     def func(self):
#         print "Parent Function"
#
# class child1(parent):
#     def __init__(self):
#         print "Child Class"
#
#     def func1(self):
#         print "Child Function"
#
# obj=child1()
# obj.func()
# obj.func1()

#print child1.__mro__
# #obj.func()


# import os
# import pdb;pdb.Pdb().set_trace()
# lis=os.listdir(os.getcwd())
# last_file= sorted(lis, key=os.path.getmtime,reverse=True)
# print last_file[0]

# print lis
# for each in lis:
#     print os.stat(each).st_mtime

#print os.stat(os.listdir(os.getcwd())).st_atime


# import time,os,sys
# from selenium import webdriver
#
# url="https://www.google.com"
# driver = webdriver.Chrome()
#
# driver.get(url)
# driver.find_element_by_xpath("//*[@id='lst-ib']").click()
# driver.find_element_by_xpath("//*[@id='lst-ib']").send_keys("Kirti Pagal")
#
#
# def check_alert():
#     """
#     Check for alert pop up on page
#     :return:
#     """
#     try:
#         browser_obj = self._browser.get_current_browser()
#         WebDriverWait(browser_obj, 3).until(EC.alert_is_present(), "Checking for Alert Pop up")
#         alert = browser_obj.switch_to.alert
#         print alert.text
#         alert.accept()
#     except Exception, e:
#         print e
#         print"No alert"
#         # self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)


# lis=[['2.6'], ['2.5'], ['2.4'], ['2.3'], ['2.2'], ['2.1'], ['2.7.14'], ['2.7.13'], ['2.7.12'], ['2.7.11'], ['2.7.10'], ['2.7.9'], ['2.7.8'], ['2.7.7'],
#      ['2.7.6'], ['2.7.5'], ['2.7.4'], ['2.7.3'], ['2.7.2'], ['2.7.1'], ['2.7'], ['2.6.9'], ['2.6.8'], ['2.6.7'], ['2.6.6'], ['2.6.5'], ['2.6.4'], ['2.6.3'],
#      ['2.6.2'], ['2.6.1'], ['2.6'], ['2.5.4'], ['2.5.3'], ['2.5.2'], ['2.5.1'], ['2.5'], ['2.4.4'], ['2.4.3'], ['2.4.2'], ['2.4.1'], ['2.4'], ['2.3.5'],
#      ['2.3.4'], ['2.3.3'], ['2.3.2'], ['2.3.1'], ['2.3'], ['2.2.3'], ['2.2.2'], ['2.2.1'], ['2.2'], ['2.2'], ['2.1.3'], ['2.1.2'], ['2.1.1'], ['2.1'], ['2.0.1'], ['2.0']]
#
# lis1=[]
# from distutils.version import StrictVersion
# for each in lis:
#     for i in each:
#         lis1.append(i)
# print lis1
# max=lis1[0]
# for i in lis1:
#     if StrictVersion(max) < StrictVersion(i):
#         max=i
# print max

import os

# for dirName,subdirList, fileList in os.walk('.'):
#     print('Found directory: %s' % dirName)
#     for name in fileList:
#         print('\t%s' % name)

#print os.environ.get('path')

# var= os.path.join(os.getcwd(),'tasdfest.txt')  #join path
# print os.path.basename(var)
# print os.path.dirname(var)
# print os.path.split(var)
# print os.path.exists(var)
# print os.path.splitext(var)

# import sys
#
# print sys.argv

# def insertionsort(aList):
#     for i in range(1, len(aList)):
#         tmp = aList[i]
#         k = i
#         while k > 0 and tmp < aList[k - 1]:
#             aList[k] = aList[k - 1]
#             k -= 1
#         aList[k] = tmp
#     print aList
# lis = [9,5,3,2,5,6,7,1]
# print "before swapping"
# print lis
# insertionsort(lis)
#

# func=lambda x: x*x
# print func(9)

# remove_duplicate=lambda interable: list(set(interable))
# print remove_duplicate("hhheeeellollooooo")


# convert_list_toint=lambda iterable:map(int, iterable)
# print convert_list_toint(["11","12","13","15"])

# is_even=lambda num: num%2==0
# even=lambda lis:filter(is_even,lis)
#
# print even(range(15))
#
# even= lambda lis:filter(lambda num:num%2==0,lis)
# print even(range(20))


# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# for f in fib():
#     if f >50:
#         break
#     print f

# def fact(x):
#     factorial = 1
#     while x >0:
#         factorial=factorial*x
#         x-=1
#     print factorial
# fact(5)

# def fact_rec(x):
#     if x==1:
#         return x
#     else:
#         return x*fact_rec(x-1)
#
# print fact_rec(5)


#prime number with best possible time
#import pdb,sys

# import time,math
# def prime(n):
#     if n==1:
#         return "Num is not prime"
#     if n==2 or n%2==0:
#         return "Num is not prime"
#     max = math.sqrt(n)
#     for i in range(3,int(max)+1,2):
#         if i % 2==0:
#             return False
#     return "Num is prime"
# t0=time.time()
# print t0
# for i in range(1,100000):
#     print prime(i)
# t1=time.time()
# print t1
# print t1-t0

# lis=[11,12,13,14,15]
# c=0
# for each in lis:
#     pdb.Pdb(stdout=sys.__stdout__).set_trace()
#     c=c+each
# print c

# count=1
#
# def do():
#     global count
#     print count
#     for i in (1,2,3,4):
#         count+=1
# do()
# print count

# import json
# JSON_Datalist = '{"id":"XXXX", "name": "xyz", "user" : { "id": "XXXX", "username":"XYZ", "group":{"id": "XXXX"}}}'
# the_dict = json.loads(JSON_Datalist)
# print the_dict
# print the_dict['user']['username']
# a_dic = json.dumps(JSON_Datalist)
# print type(a_dic)

# import re
# x="This is string to test regular expression and find if any number exist or not in string. 9663107919 and 9035081064 and 918861271413"
# print re.search(r"\d+ \w+ \d+ \w+ \d+",x,re.I).group()

#dictionary compehension
#d = {k: v for k, v in d.items() if k != "x"}

# def test(x,**z):
#     print x
#     #print y
#     print z
#
# dic={"xx":"y"}
# test(7,z="Hello")

# def text(test):
#     #print "Value of text: " +str(test())
#     return "hello"
#
# @text
# def test():
#     return "hi"
#
# print test
# #print text(test)

#Slice
# x=[1,2,3,4,5,6,7,8,9,0]
# print x
# print x[1:]
# print x[::-1]
# print x[::-2]
# print x[1::2]

# x=[x/x for x in range(1,5)]
# print x

# x=[1,2,3,4,5,6,7,8,9,0]
# for each in x[::-4]:
#     print each
#
# x=(1,2,3,4,5)
# y=(6,7,8,9,0)
# z={'name':"Saurabh",'id':4341,'company':"ACL"}
# y={}
# print z.items()
# for k,c in z.items():
#     print str(k)+"->"+str(c)
#     y[k]=c
# print y
# tup=('name','class','roll_no')
# dict=dict.fromkeys(tup)
# print dict
# print zip(x,y)

"""Sorting"""
# lis=[9,3,1,5,7,94,3,2,11,-90,-34]
# print sorted(lis)
# print sorted(lis,key=abs,reverse=True)

# d={'name':"Saurabh",'id':4341,'company':"ACL", "x":"098"}
# d = {k: v for k, v in d.items() if k != "x"}
# print d

# import sys
#
# class a(object):
#     def  __init__(self,cup="Empty",mug="Empty",glass="Empty"):
#         self.cup = cup
#         self.mug = mug
#         self.glass = glass
#         print self.cup,self.mug,self.glass
#     def morning(self):
#         print "morning breakfast"
#         print self.cup
#         print self.glass
#         print self.mug
#
# class b(a):
#     def  __init__(self,cup="chai",mug="kapi",glass="daru"):
#         #super(b, self).__init__()
#         #super(b, self).__init__()
#         self.cup = cup
#         self.mug = mug
#         self.glass = glass
#     def morning(self):
#         print "evening snacks"
#         print self.cup
#         print self.glass
#         print self.mug
# #o=b("tea","milk","beer")
# o=b()
# o.morning()
# a().morning()

#Headless Mode
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#
# driver = webdriver.Chrome(executable_path="C:\Users\sasingh\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
# #driver = webdriver.Chrome(executable_path="C:\Users\sasingh\Downloads\chromedriver_win32\chromedriver.exe")
# driver.get("http://www.duo.com")
# print("Browser Launched")
# magnifying_glass = driver.find_element_by_id("js-open-icon")
# if magnifying_glass.is_displayed():
#     magnifying_glass.click()
#     print("button Clicked")
# else:
#     menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
#     menu_button.click()
#     print("Else part")
#
# search_field = driver.find_element_by_id("site-search")
# search_field.clear()
# search_field.send_keys("Olabode")
# search_field.send_keys(Keys.RETURN)
# assert "Looking Back at Android Security in 2016" in driver.page_source
# driver.close()

# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument("download.default_directory=C:/Downloads")
#
# driver = webdriver.Chrome(chrome_options=options)

os.path.join(os.getenv('USERPROFILE'), 'Downloads')
#to change directory
# import os
# def last_access_file_from_download_flder():
#     oldpath=os.getcwd()
#     os.chdir(os.path.join(os.getenv('USERPROFILE'), 'Downloads'))
#     lis=os.listdir(os.getcwd())
#     last_file= sorted(lis, key=os.path.getatime,reverse=True)
#     os.chdir(oldpath)
#     return last_file[0]


lis=[9,3,1,5,7,94,3,2,11,-90,-34]
print sorted(lis)
print sorted(lis,key=abs,reverse=True)