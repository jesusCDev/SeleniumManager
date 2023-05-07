# Selenium Browser Manager

Selenium Browser Manager is a Python class designed to create and manage Selenium browser instances. It includes several methods to set up browser configurations, such as user agents, proxies, and caching. It also provides methods for managing browser instances, such as opening and closing browsers.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jesuscdev/selenium-browser-manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd selenium-browser-manager
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including Selenium.

## Usage

First, you need to import the `SeleniumBrowserManager` class:

```python
from selenium_browser_manager import SeleniumBrowserManager
```

Then, create an instance of the class by providing the paths to the Chrome WebDriver and Chrome binary executables:

```python
manager = SeleniumBrowserManager(chrome_drive_path='path/to/chromedriver', binary_chrome_path='path/to/chrome')
```

You can now create a Selenium browser instance with the desired configuration:

```python
browser = manager.create_selenium_browser(auto_timeout=5, headless=True, proxy='proxy_address', window_size='window-size=1400,2800', clear_cache=False)
```

## Features

### Pre-generated user agents

This class utilizes pre-generated user agent strings to randomize the user agent for each browser instance. The `header_values` are imported from the `pre_generated_headers.py` file.

```python
from pre_generated_headers import header_values
```

### Customizable options

The `create_selenium_browser` method accepts several optional parameters to customize the browser configuration:

- `auto_timeout` (int, default: 5): The browser timeout in minutes.
- `headless` (bool, default: True): Whether to run the browser in headless mode.
- `proxy` (str, default: None): The proxy address to use, if any. Must authenticate through ip.
- `window_size` (str, default: 'window-size=1400,2800'): The browser window size.
- `clear_cache` (bool, default: False): Whether to clear the cache before starting the browser.

### Additional methods

The class also provides several utility methods, such as:

- `get_random_user_agent`: Returns a random user agent string from the pre-generated list.
- `get_user_agent_values`: Returns a user agent string from the pre-generated list by index.
- `get_selected_header_value`: Returns the currently selected user agent string.
- `close_selenium_browser`: Closes the given Selenium browser instance.
- `print_current_ip_address`: Prints the current IP address of the given Selenium browser instance, useful for verifying proxy settings.

## Future TODO List

- **Firefox support**: Add support for Firefox browser by implementing the necessary configurations and options.
- **Proxy username and password verification**: Implement support for verifying the username and password for proxy authentication.
- **Auto ChromeDriver download**: Implement an automatic download mechanism for ChromeDriver, eliminating the need for manual download and installation.
- **System Specific Driver Selector**: Automatically select the appropriate chromedriver based on the operating system. It detects the system type (Linux or Windows) and sets the chromedriver path accordingly, allowing seamless integration on different systems.

## Dependencies

This program requires the following Python libraries:

- Selenium: `pip install selenium`
- Requests: `pip install requests`

The dependencies are listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

In addition, you'll need to download the appropriate [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for your system and install [Google Chrome](https://www.google.com/chrome/).

## References

- [Selenium WebDriver](https://www.selenium.dev/documentation/en/webdriver/)
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)

For more details and usage examples, please refer to the [Notion documentation](https://spectrum-denim-cba.notion.site/SeleniumManager-efdde885c24444b4b22eb7cd823cd927).
