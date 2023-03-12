import unittest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestFindElement(unittest.TestCase):
    
    def test_findElement1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
        input1.send_keys("Kot")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
        input2.send_keys("Kot")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
        input3.send_keys("Kot")
        
        
        
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        
        time.sleep(1)
        
        congratulate_text_elt = browser.find_element(By.XPATH, "//h1")
        congratulate_text = congratulate_text_elt.text
        
        self.assertEqual(congratulate_text, "Congratulations! You have successfully registered!")
    

    def test_findElement2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    
        input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
        input1.send_keys("Kot")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
        input2.send_keys("Kot")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
        input3.send_keys("Kot")
        
        
        
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        
        time.sleep(1)
        
        congratulate_text_elt = browser.find_element(By.XPATH, "//h1")
        congratulate_text = congratulate_text_elt.text
        
        self.assertEqual(congratulate_text, "Congratulations! You have successfully registered!")
        
if __name__ == "__main__":
    unittest.main()