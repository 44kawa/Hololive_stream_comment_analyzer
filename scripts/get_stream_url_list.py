"""
This module provides a function to retrieve the page source of a specified
URL using Selenium WebDriver with Chrome in headless mode. It handles
timeouts and other possible exceptions during the page loading process.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException


def get_page_source(channel_stream_url: str) -> str:
    """
    Retrieves the page source of the specified YouTube channel stream URL.

    Parameters
    ----------
    channel_stream_url : str
        The URL of the YouTube channel's stream page.

    Returns
    -------
    str
        The page source of the channel's stream page, or None if an error occurs.
    """
    options = Options()
    options.add_argument('--lang=ja')
    options.add_argument('--disable-font-subpixel-positioning')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--disable-cache')
    options.add_argument('--headless')

    with webdriver.Chrome(options=options) as driver:
        try:
            driver.get(channel_stream_url)

            driver.implicitly_wait(10)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            driver.execute_script("document.charset = 'UTF-8';")

            return driver.page_source

        except TimeoutException:
            print("Error: Page loading timed out.")
            return None

        except WebDriverException as e:
            print(f"WebDriver Error: {e}")
            return None

        except Exception as e:
            print(f"Unexpected Error: {e}")
            return None


if __name__ == "__main__":
    print(get_page_source("https://www.youtube.com/@ui_shig/streams"))
