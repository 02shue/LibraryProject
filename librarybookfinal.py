"""
Library Reservation Bot Project - Minsuk "Sean" Hue and Sangsoo "Andy" Lim
Completed December 27, 2022

"""

#This code automatically books a reservation for the CalPoly SLO Fishbowl Library. 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
#Importing necessary modules for finding WebElements to select and fill out a registration form

def main():
    """
    This code is personalized for a specific user, in this case, my partner Sangsoo "Andy" Lim since he goes to CalPoly SLO.
    If wanted, this code can interact with the user to have a first name, last name, email, and group input.
    The body of this code will execute opening up the window and choosing the first avaliable slot open for reservation on the day specificed (line 51) on the site.
    It will then choose the first 3 avaliable slots (maximum is 3 slots = 3 hours) and automatically fill out the form using the information provided on line 24 - 27.
    The "Submit" button is then clicked to finalize the registration of the library room.
    
    """
    user_first_name = input("What is your first name? ") #Andy
    user_last_name = input("What is you last name? ") #Lim
    user_email = input("What is your CalPoly email? ") #alim30@calpoly.edu
    user_group = input("What is your group name? ") #Korean American Student Association
    user_url = "https://schedule.lib.calpoly.edu/rooms.php?i=2015"

    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(user_url)
    browser.implicitly_wait(10)

    #This code goes to the next month with an open avaliable slot
    nxt = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-cal']/div/div/a[2]")
    nxt.click()
    time.sleep(4)

    
    #Uncomment to select correct month in 2023
    #This code (preference) can also choose the correct month by using the drop-down menu instead of the next arrows
    #selected_month = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-cal']/div/div/div/select")
    #month_drop_down = Select(selected_month)
    #month_drop_down.select_by_visible_text("Feb")
    #time.sleep(4)
    

    #This chooses the specific date of the month to book a reservation. Ex: '4' is listed as the 4th date of the month, can change this number to any date in the month
    date = browser.find_element(By.XPATH, "//a[text()='4']")
    date.click()
    time.sleep(2)

    #This code selects the first three available slots on that month/day
    avail_times = browser.find_elements(By.XPATH, "//table[@id='s-lc-rm-scrolltb']//a")
    slots = 0
    while slots < 3:
        avail_times[slots].click()
        slots += 1
        time.sleep(1)

    #This code fills out the first name
    browser_first_name = browser.find_element(By.XPATH, "//*[@id='fname']")
    browser_first_name.send_keys(user_first_name)
    time.sleep(1)

    #This code fills out the last name
    browser_last_name =browser.find_element(By.XPATH, "//*[@id='lname']")
    browser_last_name.send_keys(user_last_name)
    time.sleep(1)

    #This code fills out the email
    browser_email = browser.find_element(By.XPATH, "//*[@id='email']")
    browser_email.send_keys(user_email)
    time.sleep(1)

    #This code fills out the group name
    browser_group = browser.find_element(By.XPATH, "//*[@id='nick']")
    browser_group.send_keys(user_group)
    time.sleep(1)

    #This code clicks on the submit button after filling out the form
    browser_submit = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-sub']")
    browser_submit.click()
    time.sleep(3)

    browser.quit()

if '__main__':
    main()