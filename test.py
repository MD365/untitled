from appium import webdriver

desired_caps = {
        ''
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '7.0',
        'appPackage': 'com.android.calculator2',
        'appActivity': 'com.android.calculator2.Calculator'
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_id('7').click()