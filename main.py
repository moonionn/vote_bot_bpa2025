from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import time
import random

def human_like_typing(element, text):
    """模擬人類打字的速度和節奏"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))  # 隨機延遲模擬人類打字節奏

def random_scroll(driver, min_pixels=100, max_pixels=300):
    """隨機滾動頁面以模擬人類行為"""
    scroll_amount = random.randint(min_pixels, max_pixels)
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(random.uniform(0.5, 1.5))

def vote_bot(firstname, lastname, birth_year, gender, country, email, use_undetected=True):
    """
    Bangkok Pride 投票機器人
    
    參數:
    - firstname: 名字
    - lastname: 姓氏
    - birth_year: 出生年份
    - gender: 性別
    - country: 國家
    - email: 電子郵件
    - use_undetected: 是否使用 undetected_chromedriver (默認為是)
    """
    try:
        # 選擇瀏覽器驅動 - 可以嘗試兩種方法
        if use_undetected:
            # 使用 undetected_chromedriver (更難被檢測)
            options = uc.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = uc.Chrome(options=options)
        else:
            # 使用標準 Selenium (如果 undetected 不工作)
            options = Options()
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36')
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-extensions')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-infobars')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-gpu')
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
            # 隱藏 Selenium 的特徵
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # 設置等待
        wait = WebDriverWait(driver, 20)
        
        # 訪問投票網站
        driver.get("https://awards.bangkokpride.org/en/vote/")
        print("已進入網站")
        
        # 隨機等待，模擬人類加載頁面的等待時間
        time.sleep(random.uniform(2, 4))
        
        # 隨機滾動頁面
        random_scroll(driver)
        
        # 填寫表單
        print("開始填寫表單...")
        
        # 名字
        firstname_field = wait.until(EC.element_to_be_clickable((By.ID, "firstName")))
        human_like_typing(firstname_field, firstname)
        time.sleep(random.uniform(0.5, 1.2))
        
        # 姓氏
        lastname_field = driver.find_element(By.ID, "lastName")
        human_like_typing(lastname_field, lastname)
        time.sleep(random.uniform(0.5, 1.2))
        
        # 出生年份
        birthyear_field = driver.find_element(By.ID, "birthYear")
        human_like_typing(birthyear_field, str(birth_year))
        time.sleep(random.uniform(0.5, 1.2))
        
        # 性別
        gender_field = driver.find_element(By.ID, "gender")
        human_like_typing(gender_field, gender)
        time.sleep(random.uniform(0.5, 1.2))
        
        # 國家
        country_field = driver.find_element(By.ID, "country")
        human_like_typing(country_field, country)
        time.sleep(random.uniform(0.5, 1.2))
        
        # 電子郵件
        email_field = driver.find_element(By.ID, "email")
        human_like_typing(email_field, email)
        time.sleep(random.uniform(0.5, 1.2))
        
        # 隨機滾動頁面
        random_scroll(driver)
        
        print("表單已填寫完成")
        
        # 點擊第一個 Select 按鈕
        print("嘗試選擇第一個候選人...")

        try:
            # 獲取第一個 Select 按鈕
            select_button = driver.find_element(By.XPATH, "/html/body/div/astro-island/section[2]/section[3]/h2/a/button")
            select_button.click()

            time.sleep(1)  # 等待下拉菜單出現
                
            try:
                candidate1 = driver.find_element(By.XPATH, '//*[@id="3-5"]')
                candidate1.click()
            except:
                print("無法找到第一個候選人，嘗試繼續...")

            print("已選擇第一個候選人")
            time.sleep(1)
        except Exception as e:
            print(f"選擇第一個候選人時出錯: {e}")
        
        # 隨機滾動頁面
        random_scroll(driver)
        
        # 點擊第二個 Select 按鈕
        print("嘗試選擇第二個候選人...")
        try:
            # 獲取第二個 Select 按鈕
            select_button = driver.find_element(By.XPATH, "/html/body/div/astro-island/section[2]/section[6]/h2/a/button")
            select_button.click()
            time.sleep(1)

            try:
                candidate2 = driver.find_element(By.XPATH, '//*[@id="6-6"]')
                candidate2.click()
            except:
                print("無法找到第二個候選人，嘗試繼續...")
            
            print("已選擇第二個候選人")
            time.sleep(1)
        except Exception as e:
            print(f"選擇第二個候選人時出錯: {e}")
        
        
        # 點擊 Vote 按鈕提交
        print("嘗試提交投票...")
        try:
            # 嘗試多種方式找到 Vote 按鈕
            try:
                # 方法1: 使用文本
                vote_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Vote')]")
                vote_button.click()
            except:
                try:
                    # 方法2: 使用CSS選擇器
                    vote_button = driver.find_element(By.CSS_SELECTOR, "button.px-8.py-4.w-full")
                    vote_button.click()
                except:
                    # 方法3: 使用JavaScript直接點擊
                    driver.execute_script("""
                    const buttons = Array.from(document.querySelectorAll('button'));
                    const voteButton = buttons.find(b => b.innerText.includes('Vote'));
                    if (voteButton) voteButton.click();
                    """)
            
            print("已提交投票")
            time.sleep(3)

        except Exception as e:
            print(f"提交投票時出錯: {e}")
            
    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
        
    finally:
        # 關閉瀏覽器
        try:
            driver.quit()
            print("瀏覽器已關閉")
        except:
            print("關閉瀏覽器時出錯")

# 使用範例
if __name__ == "__main__":
    vote_bot("Yi", "Zheng", 2000, "female", "Taiwan", "g8pupuqqq@gmail.com")