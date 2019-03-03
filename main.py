from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

nr_stagii = 0



class stagiu:

    def __init__(self,element):
        self.pozitie=""
        self.companie=""
        self.oras=""
        self.link=""
        text=element.text
        self.pozitie=text.split('\n')[1]
        self.companie=text.split('\n')[0]
        self.companie=self.companie.split(' ·')[0]
        self.link=get_href(element)
   
    def __str__(self):
        rez=self.pozitie+' la '+self.companie+ '\nlink : '+self.link
        return rez
        
        
def print_stagii_from(URL,oras):
    
    global nr_stagii
    driver.get(URL)
    
    container=driver.find_element_by_id('jobs-grid')
    stagii = container.find_elements_by_tag_name("li")

    for items in stagii:
        if oras in items.text:
            nr_stagii=nr_stagii+1
            obj = stagiu(items)
            print(str(nr_stagii)+'.\nStagiu gasit\nDetalii:')
            print(str(obj)+'\n')


def get_href(stagiu):
    return str(stagiu.find_elements_by_tag_name("a")[0].get_attribute("href"))

def login(driver):
   
    username_text=input("username:")
    print("Este normal ca atunci cand scrieti parola sa nu apara nimic in linia de comanda")
    password_text = getpass.getpass() 
    driver.get('https://junio.ro/dashboard/login/')
    #try:
    username_box= driver.find_element_by_name("username")
    print("username text_box found")

    password_box= driver.find_element_by_name("password")
    print("password text_box found")

    username_box.send_keys(username_text)
    password_box.send_keys(str(password_text))
    driver.find_element_by_css_selector('#login-section > div.form-wrapper > form:nth-child(4) > button').click()

    if(driver.current_url!="https://junio.ro/dashboard/login/"):
        print('conectare reusita\n')
        paginare=driver.find_element_by_css_selector('#page-body > div.container > div > div > nav > ul')
        nr_pagina=0
        pagini=paginare.text.split('\n')
        orase=['București','Iași','Timișoara','Cluj','Sibiu']
        
        nr_oras=-1

        while(int(nr_oras)<0 or int(nr_oras)>4):
            for i in range(4):
                print(str(i+1)+orase[i])
            nr_oras=input('\nnumar oras:')
            nr_oras=int(nr_oras)-1
        
        nr_pagini=int(pagini[len(pagini)-2])
        for i in range(1,nr_pagini+1):
                URL='https://junio.ro/dashboard/students/jobs/?page=' + str(i)+'&type=&industry='
                print(URL)
                #print_stagii_from(URL,orase[int(nr_oras)])
            
    else:
        print("user sau parola gresita")
        login(driver)
    
    
driver = webdriver.Chrome()
login(driver)
print ('\n\nau fost gasite '+str(nr_stagii)+' stagii')
driver.close()
