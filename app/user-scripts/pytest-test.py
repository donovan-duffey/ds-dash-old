from seleniumbase import BaseCase
# from selenium.webdriver.chrome.options import Options

# chrome_options = Options();
# chrome_options.add_experimental_option("detach", True)

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.google.co.za")