from email.mime import image
import random
from selenium import webdriver
from selenium.webdriver.common.by import By 
from tkinter import *
from tkinter.filedialog import askopenfile
import time

class spam:

    def searchPerson(self):
                
        options = webdriver.ChromeOptions()
        
        driver_path = "./chromedriver.exe"
        self.web = webdriver.Chrome(executable_path=driver_path)

        self.web.get('https://web.whatsapp.com/')
        self.web.implicitly_wait(20)

        print(self.person.get() , self.msgBox.get() , self.countBox.get())

        self.contact = self.person.get()
        self.search = self.web.find_elements_by_class_name('copyable-text')

        self.search[0].click()

        self.search[0].send_keys(self.contact)
        
        self.web.find_element_by_xpath("//span[@title='"+ self.contact +"']").click()
    
    def spamMsg(self):

        self.searchPerson()
        self.contact=self.person.get()

        msg = self.msgBox.get()

        count =self.countBox.get()
        
        
        for i in range(int(count)):
            self.web.find_element_by_xpath("//div[@title='Type a message']").click()
            self.web.find_element(By.XPATH, "//div[@title='Type a message']").send_keys(msg)

            self.web.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[2]/button[1]/span[1]").click()

    def spamMain(self):
                
        root = Tk()

        root.geometry("500x400")

        label1 = Label(root , text = " Enter The Person Name to be searched : " , font='times 15')
        label1.pack()

        self.person = Entry(root)
        self.person.pack()


        label2 = Label(root , text = " Enter The Message you want to sent : " , font='times 15' )
        label2.pack()

        self.msgBox = Entry(root)
        self.msgBox.pack()


        label3 = Label(root , text = " Enter The Number of Times : " , font='times 15')
        label3.pack()

        self.countBox = Entry(root)
        self.countBox.pack()

        b1 = Button(root , text  = " Do It " , command=spam.spamMsg , width=12 )
        b1.pack()

        root.mainloop()

spam = spam()