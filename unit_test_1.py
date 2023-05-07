import unittest
import os
from selenium_browser_manager import SeleniumBrowserManager

class TestSeleniumBrowserManager(unittest.TestCase):
    
    def test_create_and_close_browser(self):
        # Ensure that a browser instance can be created and closed without errors
        browser_manager = SeleniumBrowserManager()
        browser = browser_manager.create_browser()

        # Perform any additional checks or assertions here, such as verifying the user agent
        user_agent = browser_manager.get_selected_header_value()
        self.assertIsNotNone(user_agent, "User agent should not be None")

        # Close the browser instance
        SeleniumBrowserManager.close_selenium_browser(browser)

    def test_load_config(self):
        # Ensure that the configuration file can be loaded without errors
        browser_manager = SeleniumBrowserManager()

        # Dynamically find the path to the config.yaml file
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SeleniumManager", "config.yaml")

        config = SeleniumBrowserManager.load_config(config_path)

        # Check if the config is not empty and contains the required keys
        self.assertIsNotNone(config, "Config should not be None")
        self.assertIn("chrome_driver_path", config, "Config should contain 'chrome_driver_path'")
        self.assertIn("chrome_binary_path", config, "Config should contain 'chrome_binary_path'")

if __name__ == "__main__":
    unittest.main()
