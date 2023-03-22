from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

class  SauceExample :
     
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        sleep(2)

   
    def login(self, username, password):
        self.driver.refresh()
        sleep(2)

        username_input = self.driver.find_element(By.ID, "user-name")  
        password_input = self.driver.find_element(By.ID, "password")  
        sleep(2)
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(2)

        login_btn = self.driver.find_element(By.ID, "login-button") 
        sleep(2)

        login_btn.click()
        sleep(2)

    def username_and_password_are_blank(self) :
        tester.login("", "")
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)

        result = error_message.text == "Epic sadface: Username is required" 
        if result:
            print("1st test successful..")
        else :
            print("1st test failed..")

    def just_the_password_is_blank(self):
        tester.login("locked_out_user", "")
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)

        result = error_message.text == "Epic sadface: Password is required"
        if result:
            print("2nd test successful..")
        else :
            print("2nd test failed..")

    def lockedUsername_and_password_check(self):
        tester.login("locked_out_user", "secret_sauce")
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        result = error_message.text == "Epic sadface: Sorry, this user has been locked out."

        if result:
            print("3rd test successful..")
        else :
            print("3rd test failed..")
     
    def x_icon(self):
        tester.login("", "")
        error_message = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)

        result = error_message.text == "Epic sadface: Username is required" 
        if result:
            error_message_x = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            sleep(2)

            error_message_x.click()
            sleep(2)

            try:
                username_icon = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg")
                password_icon = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg")
                sleep(2)
            except:
                print("4th test successful..")
        else:
            print("4th test failed..")

        
    def standardUsername_and_password_check(self):
        tester.login("standard_user", "secret_sauce")
        current_url = self.driver.current_url
        result= current_url== "https://www.saucedemo.com/inventory.html"
        
        if result:
            print("The routing process was successfully completed..\n5th test successful..")
        else :
            print("The redirection operation could not be performed..\n5th test failed..")
     

    def product_number_check(self):
        self.driver.get("https://www.saucedemo.com/")
        tester.login("standard_user", "secret_sauce")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(8)

        number_of_products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print("Successfully logged in..")
        print(f"The number of products seen : {len(number_of_products)}")

        result = len(number_of_products) == 6
        if result:
            print("6th test successful..")
        else :
            print("6th test failed..")


tester = SauceExample()
tester.username_and_password_are_blank()
tester.just_the_password_is_blank()
tester.lockedUsername_and_password_check()
tester.x_icon()
tester.standardUsername_and_password_check()
tester.product_number_check()
