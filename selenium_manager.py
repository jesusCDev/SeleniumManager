from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service

import random
import traceback
import platform

from pre_generated_headers import header_values

# The SeleniumBrowserManager class is designed to create and manage Selenium browser instances.
# It includes several methods to set up browser configuration, such as user agents, proxies, and caching.
# It also provides methods for managing browser instances, such as opening and closing browsers.
class SeleniumBrowserManager:
    
    chrome_driver_path: str
    binary_chrome_path: str
    selected_header_value: str
    
    # @chrome_drive_path: The path to the Chrome WebDriver executable.
    # @binary_chrome_path: The path to the Chrome binary executable.
    def __init__(self, chrome_drive_path: str, binary_chrome_path: str):
        self.chrome_driver_path = chrome_drive_path
        self.binary_chrome_path = binary_chrome_path
         
    def create_selenium_browser(self, auto_timeout: int = 5, headless: bool = True, proxy: str = None, window_size: str = 'window-size=1400,2800', clear_cache: bool = False):
            
        chrome_options = webdriver.ChromeOptions()

        chrome_options = self.setup_chrome_options_arguments(chrome_options, window_size, headless)
        capabilities = self.setup_proxy(webdriver, chrome_options, proxy)

        self.setup_user_agents(chrome_options)
        self.setup_clear_cache(clear_cache)

        chrome_service = Service(self.chrome_driver_path)

        browser = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=capabilities)

        self.setup_default_timeout(browser, auto_timeout)
        self.clear_cache_browser(clear_cache, browser)

        return browser

    def setup_chrome_options_arguments(self, chrome_options, window_size, headless):
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
        chrome_options.binary_location = self.binary_chrome_path
        
        # Enables headless mode if the 'headless' parameter is set to True
        if headless:
            chrome_options.add_argument('--headless')
        
        # Sets the window size for the browser, defaults to 1400x2800 if not specified
        chrome_options.add_argument(window_size)

        return chrome_options

    def setup_proxy(self, webdriver, chrome_options, proxy):
        # Set up desired capabilities for Chrome WebDriver
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

    def setup_user_agents(self, chrome_options):
        user_agent = self.get_random_user_agent()
        self.selected_header_value = user_agent
        chrome_options.add_argument(f'user-agent={user_agent}')
    
    @staticmethod
    def setup_default_timeout(browser: webdriver.Chrome, auto_timeout: int):
        SECONDS = 60
        auto_timeout = auto_timeout * SECONDS
            
        browser.set_page_load_timeout(auto_timeout)
        browser.implicitly_wait(auto_timeout)
        
    @staticmethod
    def setup_clear_cache(clear_cache: bool):
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
    def clear_cache_browser(clear_cache: bool, browser: webdriver.Chrome):
        if clear_cache:
            # Executes a Chrome DevTools Protocol command to disable the cache.
            # This command disables caching of all resources for the lifetime of the browser.
            browser.execute_cdp_cmd('Network.setCacheDisabled', {'cacheDisabled': True})

            # Deletes all cookies stored by the browser.
            browser.delete_all_cookies()
        
    @staticmethod
    def get_random_user_agent():
        return random.choice(header_values)['User-Agent']
        
    @staticmethod
    def get_user_agent_values(index: int):
        return header_values[index]['User-Agent'];
    
    def get_selected_header_value(self):
        return self.selected_header_value
    
    @staticmethod
    def close_selenium_browser(browser: webdriver.Chrome):
        try:
            browser.quit()
        except Exception as e:
            traceback.print_exc()
    
    @staticmethod
    def print_current_ip_address(browser: webdriver.Chrome):
        # * Generally used for verifying proxy
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

