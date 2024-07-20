import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
# 설치 pip install selenium webdriver-manager
# pip install requests, pip install pandas selenium webdriver-manager requests

# 구동 python test.py


# CSV 파일 읽기
file_path = 'C:/Users/82107/Desktop/food_list.csv'  # CSV 파일 경로
df = pd.read_csv(file_path)

# WebDriver Manager를 사용하여 드라이버 설치
service = Service(ChromeDriverManager().install())

# Chrome WebDriver를 초기화
driver = webdriver.Chrome(service=service)

for index, row in df.iterrows():
    food_name = row['food_name'].strip()

    if not food_name:
        continue

    # YouTube 페이지를 open
    driver.get("https://www.youtube.com/")

    # 페이지가 로드될 때까지 잠시 대기
    time.sleep(3)

    # 검색창을 찾고 음식을 입력한 후, Enter 키 입력
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(food_name+" 레시피")
    search_box.send_keys(Keys.RETURN)

    # 검색 결과가 로드될 때까지 잠시 대기
    time.sleep(3)

    try:
        # 첫 번째 영상을 클릭
        first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()

        # 첫 번째 영상이 로드될 때까지 잠시 대기
        time.sleep(3)

        # 현재 URL을 가져오기
        current_url = driver.current_url
        print(f"Food: {food_name}, URL: {current_url}")

        # 결과 URL을 데이터프레임에 추가
        df.at[index, 'food_video'] = current_url

    except Exception as e:
        print(f"An error occurred for {food_name}: {e}")
        df.at[index, 'food_video'] = None

# 브라우저 닫기
driver.quit()

# 수정된 데이터프레임을 CSV 파일로 저장
df.to_csv('C:/Users/82107/Desktop/food_list_with_urls.csv', index=False)
