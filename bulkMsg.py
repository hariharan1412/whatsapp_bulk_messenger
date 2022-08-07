from logging import root
from selenium import webdriver
from selenium.webdriver.webkitgtk import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tkinter import *
import pandas as pd
from tkinter.filedialog import askopenfile


class bulk:

    def BulkMsg(self):
         
        options = webdriver.ChromeOptions()

        driver_path = "./chromedriver.exe"
        self.web = webdriver.Chrome(executable_path=driver_path)

        self.web.implicitly_wait(20)
        print(self.file_path.name)
        phoneNumber= pd.read_csv(self.file_path.name)


        phoneNo = phoneNumber['phoneNumber'].tolist()
        self.msg = self.Message.get()

        wts = ' https://web.whatsapp.com/send?phone=+91'
        msg = '&text=' + self.msg

        for phone in phoneNo:
            try:
                url = wts+str(phone)+msg
                print(url)
                
                time.sleep(5)
                self.web.get(url)
                self.web.implicitly_wait(20)
                self.web.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()

            except:
                pass

        time.sleep(10)

    
    def open_file(self):
        self.file_path = askopenfile(mode='r' , filetypes=[('csv Files' , '*csv')])
        print(self.file_path)

    def bulkMain(self):
                
        root = Tk()

        root.geometry("500x400")

        label1 = Label(root , text = " BULK MESSENGER  " , font='times 15')
        label1.place(x=160 , y=50)

        label1 = Label(root , text = " Enter Message : ")
        label1.place(x=80 , y=100)

        self.Message= Entry(root)
        self.Message.place(x=200 , y=100)
        
        label2 = Label(root , text = " Select the CSV file : ")
        label2.place(x=80 , y=160)

        dlbtn = Button( root, text ='Choose File ', command = self.open_file) 
        dlbtn.place(x=200 , y=150)

        b1 = Button(root , text  = " START " , command=bulk.BulkMsg , width=12 )
        b1.place(x=200 , y=200)

        root.mainloop()

bulk = bulk()