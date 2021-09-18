from selenium import webdriver
import webbrowser


class firefoxAutomating:
    def __init__(self):
        pass

    def open_url(self, url):
        # driver = webdriver.Firefox(executable_path="C:/Users/leogu/PycharmProjects/voice-assistant/Driver/geckodriver.exe")
        # driver.get(url)
        webbrowser.open_new(url)
