from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from tkinter import *
import pandas as pd
from tkinter.filedialog import askopenfile
import os
from selenium.webdriver.common.keys import Keys

# PIP INSTALL openpyxl

os.system('clear')

class alumni:

    def __init__(self) -> None:

        self.attachment = False
        self.chromeDrive = False

    def GUI(self) -> None:
        
        try:
            self.root = Tk()

            self.root.geometry("600x600")
            self.root.title("Whatsapp Bulk Messenger")

            label1 = Label(self.root , text = " BULK MESSENGER  " , font='times 15')
            label1.place(x=210 , y=50)

            label1 = Label(self.root , text = " Enter Message : ")
            label1.place(x=20 , y=140)

            self.msg = Text(self.root, height=11, width=50)
            self.msg.place(x=150 , y=120)                        
            
            label2 = Label(self.root , text = " **Select Chromedriver file : ")
            label2.place(x=10 , y=350)

            dlbtn = Button( self.root, text ='Choose File ', command = self.open_file_driver) 
            dlbtn.place(x=220 , y=345)

            label2 = Label(self.root , text = " *Select Contact file : ")
            label2.place(x=15 , y=400)

            dlbtn = Button( self.root, text ='Choose File ', command = self.open_file) 
            dlbtn.place(x=220 , y=395)

            label2 = Label(self.root , text = " Select Attachment file : ")
            label2.place(x=20 , y=450)

            dlbtn1 = Button( self.root, text ='Choose File ', command = self.open_file_attachment) 
            dlbtn1.place(x=220 , y=445)

            b1 = Button(self.root , text  = " START " , command=self.service , width=12 )
            b1.place(x=250 , y=500)

            self.root.mainloop()
        
        except Exception as e:
            print(" ERROR IN TKINTER : " , e)

    def open_file_driver(self):

        self.file_path_driver = askopenfile(mode ='r', filetypes =[('All file','*')])
        self.chromeDrive = True

    def open_file(self):
      
        self.file_path = askopenfile(mode ='r', filetypes =[('Excel Files', '*.xlsx *.xlsm *.sxc *.ods *.csv *.tsv')])
       
    def open_file_attachment(self):

        self.file_path_attachment = askopenfile(mode ='r', filetypes =[('All files', '*.*')])
        self.attachment = True

    def service(self):
        

        if self.chromeDrive:
            pass

        else:

            raise Exception("PLEASE SELECT YOUR CHROME DRIVER :) ")


        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./User_Data')

        driver_path = self.file_path_driver.name
        
        self.web = webdriver.Chrome(executable_path=driver_path , options=options)

        print(" FILE : " , self.file_path , self.file_path.name)


        self.web.implicitly_wait(20)   

        try:
        
            phoneNumber= pd.read_csv(self.file_path.name)
        
        except:

            phoneNumber= pd.read_excel(self.file_path.name)


        self.Message = self.msg.get("1.0",'end-1c')

        phoneNo = phoneNumber['Contact'].tolist()

        country_code = "+91"
        wts = ' https://web.whatsapp.com/send?phone='+country_code

        print(phoneNo)

        result = []

        for phone in phoneNo:

            try:

                url = wts+str(phone)
                print(url)
                
                self.web.get(url)
                self.web.implicitly_wait(20)
                
                # Type a message
                text_box = self.web.find_element(By.XPATH,"//div[@title='Type a message']")
                text_box.click()
 
                for line in self.Message.split('\n'):
                    ActionChains(self.web).send_keys(line).perform()
                    ActionChains(self.web).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

                self.web.find_element(By.XPATH,"//span[@data-icon='send']").click()


                if self.attachment:
                    #CLIP 
                    self.web.find_element(By.XPATH , "//div[@title='Attach']").click()

                    #PDF 
                    self.web.find_element(By.XPATH , "//input[@type='file']").send_keys(self.file_path_attachment.name)

                    self.web.find_element(By.XPATH,"//span[@data-icon='send']").click()
                    
                time.sleep(3)
                result.append(' sent ')

            except Exception as e:

                result.append(' not sent ')
                print(' ERROR : ', e)


        with open('./log.txt' , '+a') as f:
            for i in zip(phoneNo , result):
                f.writelines(str(i))
                f.writelines('\n')
            
            f.writelines('\n')

        time.sleep(10)
        self.web.quit()        
        self.root.destroy()



if __name__ == "__main__":

    try:
        bot = alumni()  
        bot.GUI()

    except Exception as e:
        print(" OOPS!! Something went wrong : (")
        print(" ERROR : " , e)