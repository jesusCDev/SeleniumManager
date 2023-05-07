# This file defines the public interface for the selenium_browser package.
# It exports the `header_values` list and the `SeleniumBrowserManager` class.

# Import the `header_values` list from the `pre_generated_headers` module.
# The `header_values` list contains pre-generated header values that can be used to avoid being blocked by websites.
from .pre_generated_headers import header_values

# Import the `SeleniumBrowserManager` class from the `selenium_browser_manager` module.
# The `SeleniumBrowserManager` class is designed to create and manage Selenium browser instances.
# It includes several methods to set up browser configuration, such as user agents, proxies, and caching.
# It also provides methods for managing browser instances, such as opening and closing browsers.
from .selenium_browser_manager import SeleniumBrowserManager
