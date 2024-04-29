from seleniumbase import Driver

class Browser:
    chrome = Driver()
    chrome.maximize_window()
    chrome.get("https://www.saucedemo.com/")

    def close(self):
        self.chrome.quit()
