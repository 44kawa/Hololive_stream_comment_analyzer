from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# def get_steam_url_list():


def get_page_source(channel_stream_url):
    options = Options()
    options.add_argument('--lang=ja')  # 日本語対応
    # サブピクセルレンダリングを無効化
    options.add_argument('--disable-font-subpixel-positioning')
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])  # ログ無効化
    options.add_argument('--disable-cache')  # キャッシュを無効化
    options.add_argument('--headless')  # ヘッドレスモードを有効化

    # WebDriverをコンテキストマネージャーで管理
    with webdriver.Chrome(options=options) as driver:
        try:
            driver.get(channel_stream_url)

            # 暗黙的な待機時間の設定（例：最大10秒待つ）
            driver.implicitly_wait(10)

            # ページ全体が読み込まれるのを待つ
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # ページの文字コードをUTF-8に設定
            driver.execute_script("document.charset = 'UTF-8';")

            # ページソースを取得
            page_source = driver.page_source

            # 動的コンテンツが問題の場合は、こちらでテキストを取得する
            # page_source = driver.find_element(By.TAG_NAME, 'body').text

            return page_source

        except TimeoutException:
            print("Error: ページの読み込みがタイムアウトしました")
            return None

        except Exception as e:
            print(f"Error: {e}")
            return None


if __name__ == "__main__":
    print(get_page_source("https://www.youtube.com/@ui_shig/streams"))
