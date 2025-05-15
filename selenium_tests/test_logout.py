import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver
driver = uc.Chrome()
driver.get("https://sac.ukdw.ac.id")

# Login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "uname"))).send_keys("ISI NIM")  # Ganti dengan NIM
driver.find_element(By.NAME, "pword").send_keys("ISI PASSWORD")  # Ganti dengan password 
driver.find_element(By.TAG_NAME, "form").submit()

# Tunggu sampai dropdown user muncul (berdasarkan icon user atau nama)
try:
    user_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.dropdown-toggle"))
    )
    user_menu.click()
    time.sleep(1)  # Beri waktu dropdown muncul

    # Klik tombol logout
    logout_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "LOGOUT"))
    )
    logout_button.click()

    time.sleep(2)

    # Verifikasi sudah logout
    if "login" in driver.page_source.lower():
        print("✅ Logout test passed!")
    else:
        print("❌ Logout test failed!")

except Exception as e:
    print(f"❌ Terjadi error saat logout: {e}")

# Tutup browser
driver.quit()
