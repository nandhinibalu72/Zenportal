"""
Stored all web locators in this locators.py
"""

class ZenLocators:
    username_locator = ':r0:' # ID
    password_locator = ':r1:' # ID
    login_button_locator = '//button[@type="submit"]' # XPATH
    logout_button_locator="//div[normalize-space()='Log out']" #xpath
    profile_id_click='//div[@class="avatar-main-div d-flex cursor mock-interview"]' #xpath