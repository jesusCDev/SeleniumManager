from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service

import random
import traceback
import platform

import yaml
import os

from .pre_generated_headers import header_values

# The SeleniumBrowserManager class is designed to create and manage Selenium browser instances.
# It includes several methods to set up browser configuration, such as user agents, proxies, and caching.
# It also provides methods for managing browser instances, such as opening and closing browsers.
class SeleniumBrowserManager:
    
    chrome_driver_path: str
    chrome_binary_path: str
    selected_header_value: str
    
    # @chrome_drive_path: The path to the Chrome WebDriver executable.
    # @chrome_binary_path: The path to the Chrome binary executable.
    def __init__(self, chrome_drive_path: str, chrome_binary_path: str = ""):
        self.chrome_driver_path = chrome_drive_path
        self.chrome_binary_path = chrome_binary_path
        
    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "SeleniumManager", "config.yaml")
        config = self.load_config(config_path)

        self.chrome_driver_path = str(config["chrome_driver_path"])
        self.chrome_binary_path = str(config["chrome_binary_path"])

    @staticmethod
    def load_config(file_path):
        with open(file_path, 'r') as config_file:
            try:
                config = yaml.safe_load(config_file)
            except yaml.YAMLError as exc:
                print(f"Error in reading the configuration file: {exc}")
                config = None

        return config
         
    def create_browser(self, timeout: int = 5, headless: bool = True, proxy: str = None, window_size: str = 'window-size=1400,2800', clear_cache: bool = False):
        # Main function to create and configure a browser instance  
        chrome_options = webdriver.ChromeOptions()

        chrome_options = self._configure_chrome_options(chrome_options, window_size, headless)
        capabilities = self._configure_proxy(webdriver, chrome_options, proxy)

        self._configure_user_agents(chrome_options)
        self._configure_cache(clear_cache)

        chrome_service = Service(self.chrome_driver_path)

        browser = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=capabilities)

        self._configure_default_timeout(browser, timeout)
        self._clear_browser_cache(clear_cache, browser)

        return browser

    def _configure_chrome_options(self, chrome_options, window_size, headless):
        # Configures Chrome options for the browser instance
        # Bypass OS security model, necessary for running a headless environment
        chrome_options.add_argument('--no-sandbox')
        
        # Overcome limited resource problems, mainly related to shared memory when running in Docker
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Disables various extensions that a user can enable to customize their browser
        chrome_options.add_argument('--disable-extensions')
        
        # Disables GPU hardware acceleration, can sometimes cause issues
        chrome_options.add_argument('--disable-gpu')
        
        # Disables the info bars that sometimes appear at the top of the browser
        chrome_options.add_argument('--disable-infobars')
        
        # Disables Chrome automation, prevents websites from detecting that we're using Selenium
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Enables Chrome automation, required for some functionality
        chrome_options.add_argument('enable-automation')
        
        # Disables browser-side navigation, which can cause issues with page loading
        chrome_options.add_argument('--disable-browser-side-navigation')
        
        # Sets the location of the Chrome binary executable
        if self.chrome_binary_path:
            chrome_options.binary_location = self.chrome_binary_path
        
        # Enables headless mode if the 'headless' parameter is set to True
        if headless:
            chrome_options.add_argument('--headless')
        
        # Sets the window size for the browser, defaults to 1400x2800 if not specified
        chrome_options.add_argument(window_size)

        return chrome_options

    @staticmethod
    def _configure_proxy(webdriver, chrome_options, proxy):
        # Configures the proxy settings for the browser instance
        capabilities = webdriver.DesiredCapabilities.CHROME

        # Check if the 'proxy' parameter is not empty
        if proxy:
    
            try:
                # Set up the proxy configuration for Selenium
                proxy = Proxy({
                    'proxyType': ProxyType.MANUAL,
                    'httpProxy': proxy,
                    'httpsProxy': proxy,
                    'noProxy': ''
                })

                # Set the Chrome WebDriver proxy settings
                webdriver.DesiredCapabilities.CHROME['proxy'] = {
                    'proxyType': ProxyType.MANUAL,
                    'httpProxy': proxy,
                    'ftpProxy': proxy,
                    'sslProxy': proxy,
                    'proxyType': 'MANUAL',
                }
                
                # Create a new Proxy object and configure it with the proxy settings
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = proxy
                prox.socks_proxy = proxy
                prox.ssl_proxy = proxy

                prox.add_to_capabilities(capabilities)

                chrome_options.add_argument('--proxy-server=%s' % proxy)

            except Exception as e:
                traceback.print_exc()

        return capabilities

    def _configure_user_agents(self, chrome_options):
        # Configures the user agent settings for the browser instance
        user_agent = self._get_random_user_agent()
        self.selected_header_value = user_agent
        chrome_options.add_argument(f'user-agent={user_agent}')
    
    @staticmethod
    def _configure_default_timeout(browser: webdriver.Chrome, timeout: int):
        # Configures the default timeouts for the browser instance
        SECONDS = 60
        timeout = timeout * SECONDS
            
        browser.set_page_load_timeout(timeout)
        browser.implicitly_wait(timeout)
        
    @staticmethod
    def _configure_cache(clear_cache: bool):
        # Configures the cache settings for the browser instance
        if clear_cache:
            # Disables the application cache to prevent storing web application data.
            chrome_options.add_argument('--disable-application-cache')

            # Sets the disk cache size to 0 bytes, effectively disabling the disk cache.
            chrome_options.add_argument('--disk-cache-size=0')

            # Creates a dictionary with 'disk-cache-size' set to 0.
            prefs = {'disk-cache-size': 0}

            # This also sets the disk cache size to 0, disabling the disk cache.
            chrome_options.add_experimental_option('prefs', prefs)

    @staticmethod
    def _clear_browser_cache(clear_cache: bool, browser: webdriver.Chrome):
        # Clears the browser cache if clear_cache is set to True
        if clear_cache:
            # Executes a Chrome DevTools Protocol command to disable the cache.
            # This command disables caching of all resources for the lifetime of the browser.
            browser.execute_cdp_cmd('Network.setCacheDisabled', {'cacheDisabled': True})

            # Deletes all cookies stored by the browser.
            browser.delete_all_cookies()
        
    @staticmethod
    def _get_random_user_agent():
        # Returns a random user agent string from pre_generated_headers
        return random.choice(header_values)['User-Agent']
        
    @staticmethod
    def get_user_agent_values(index: int):
        # Returns a specific user agent string from pre_generated_headers by index
        return header_values[index]['User-Agent'];
    
    def get_selected_header_value(self):
        # Returns the selected user agent string for the browser instance
        return self.selected_header_value
    
    @staticmethod
    def close_selenium_browser(browser: webdriver.Chrome):
        # Closes the browser instance and handles any exceptions
        try:
            browser.quit()
        except Exception as e:
            traceback.print_exc()
    
    @staticmethod
    def print_current_ip_address(browser: webdriver.Chrome):
        # Prints the current IP address of the browser instance, mainly for verifying proxy settings
        ip_check_site = 'http://getip.c14.workers.dev/'
        
        try:
            browser.get(ip_check_site)
        except Exception as e:
            print("Error loading the IP check site:")
            traceback.print_exc()
            return

        try:
            page_source = browser.page_source

            ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
            match = re.search(ip_pattern, page_source)

            if match:
                # * Should print only the IP value
                print(f"\n-----\n{match.group(0)}\n-----\n")
            else:
                print("IP address not found in the page page_source.")

        except Exception as e:
            print("Error extracting IP address:")
            traceback.print_exc()

