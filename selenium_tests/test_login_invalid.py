import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
import time

# Setup
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

# Buka halaman
driver.get("https://sac.ukdw.ac.id")

# Tunggu halaman login tampil
time.sleep(3)

# Cari input dengan name="uname" dan "pword"
username_input = driver.find_element(By.NAME, "uname")
password_input = driver.find_element(By.NAME, "pword")

# Isi form
username_input.send_keys("71220953")  # Ganti dengan NIM kamu
password_input.send_keys("PASSWORD_KAMU")  # Ganti dengan password kamu

# Submit form
password_input.send_keys(Keys.RETURN)

# Tunggu redirect atau alert
time.sleep(3)

try:
    # Coba cek apakah ada alert yang muncul
    alert = driver.switch_to.alert
    print("ALERT DITEMUKAN:", alert.text)
    alert.accept()  # Tutup alert
    print("Login Gagal!")
except NoAlertPresentException:
    # Jika tidak ada alert, cek judul halaman
    if "SAC" in driver.title:
        print("Login Berhasil!")
    else:
        print("Login tidak berhasil, tapi tidak ada alert.")

# Jangan lupa tutup driver
driver.quit()
