import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()  # otomatis handle ChromeDriver
# Setelah login berhasil:
dashboard_html = driver.page_source
assert "Nama Mahasiswa" in dashboard_html or "logout" in dashboard_html
print("✅ Dashboard tampil dengan benar")

driver.quit()