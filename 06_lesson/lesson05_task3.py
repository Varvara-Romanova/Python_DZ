from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html "
    driver.get(url)

    # Ждём загрузки всех картинок
    WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Получаем список изображений
    images = driver.find_elements(By.TAG_NAME, "img")

    # Выводим src третьей картинки (индекс 2)
    if len(images) >= 3:
        third_image_src = images[2].get_attribute("src")
        print("src третьей картинки:")
        print(third_image_src)
    else:
        print("На странице меньше трёх изображений.")

finally:
    driver.quit()
