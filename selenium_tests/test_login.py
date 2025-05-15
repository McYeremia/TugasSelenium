import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()  # otomatis handle ChromeDriver
try:
    driver.get("https://sac.ukdw.ac.id")
    time.sleep(2)  # beri waktu agar halaman termuat

    driver.find_element(By.NAME, "uname").send_keys("ISI NIM YG BENER")  # ganti dengan NIM sebenarnya
    driver.find_element(By.NAME, "pword").send_keys("ISI PW YG BENER")  # ganti dengan password sebenarnya
    driver.find_element(By.TAG_NAME, "form").submit()

    time.sleep(3)
    print("driver titlenya:", driver.title)
    assert "SAC" in driver.title
    print("✅ Login test passed!")

finally:
    driver.quit()