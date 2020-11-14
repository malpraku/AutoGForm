#Mengimport Module Ke Script Python
#Fungsi dari 'from' itu gunanya untuk mengambil hanya salah satu fungsi
#dari module. Sehingga dapat meringankan efek CPU dan Kinerja Komputer.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import gmtime, strftime
from random import randint
import pathlib
import ctypes
import time
import os

#Mengganti Judul Command Prompt

ctypes.windll.kernel32.SetConsoleTitleW("AutoKAIS BETA [Coded by Fallen#0021!]")

#Menyatakan String Menjadi Beberapa Variable

gform= "https://docs.google.com/forms/d/e/1FAIpQLSfZSF4aBhTtwMzqcdK15qO95pWXDK0PBi0bYFF0pnpuhVlRSw/viewform?usp=sf_link"
forminfo = "yea"
check = ["true", "false"]
haveseggs= "no"

#Menggunakan module bawaan "os" untuk mengontrol aktifitas terminal.
#Jika Sistem Berkode NT atau Windows, maka akan menjalankan command 'cls' untuk membersihkan Command Prompt.
#Bila sistem tidak berkode NT, maka akan menjalankan command 'clear' untuk membersihkan Terminal.

os.system('cls' if os.name == 'nt' else 'clear')

# Print berfungsi untuk menunjukkan teks ke Terminal.
# ASCII tersebut di Generate melalui http://patorjk.com/software/taag/

print("  ___        _        _   __  ___  _____ _____  ")
print(" / _ \      | |      | | / / / _ \|_   _/  ___| ")
print("/ /_\ \_   _| |_ ___ | |/ / / /_\ \ | | \ `--.  ")
print("|  _  | | | | __/ _ \|    \ |  _  | | |  `--. \ ")
print("| | | | |_| | || (_) | |\  \| | | |_| |_/\__/ / ")
print("\_| |_/\__,_|\__\___/\_| \_/\_| |_/\___/\____/  ")
print("");
print("");
print("AutoKAIS [fill out your form task automatically]")
print("Sepertinya, ini adalah pertama kalinya anda menjalankan program kami.")
print("Mohon isi data konfigurasi program.")
print("");

# Menanyakan pengguna untuk memasuki Email dan Nama di Command Prompt.
# dan Input tersebut dimasukkan dalam variable masing masing.

email= input("Masukkan Email: ")
name= input("Masukkan Nama Lengkap: ")

# time.sleep(value) digunakan untuk mendelay script.
# Disini, script akan mendelay selama tiga detik sebelum aktifitas
# selanjutnya dimulai.

print("Please wait...");
time.sleep(3)

#Menggunakan module bawaan "os" untuk mengontrol aktifitas terminal.
#Jika Sistem Berkode NT atau Windows, maka akan menjalankan command 'cls' untuk membersihkan Command Prompt.
#Bila sistem tidak berkode NT, maka akan menjalankan command 'clear' untuk membersihkan Terminal.

os.system('cls' if os.name == 'nt' else 'clear')

# Print berfungsi untuk menunjukkan teks ke Terminal.
# ASCII tersebut di Generate melalui http://patorjk.com/software/taag/

print("  ___        _        _   __  ___  _____ _____  ")
print(" / _ \      | |      | | / / / _ \|_   _/  ___| ")
print("/ /_\ \_   _| |_ ___ | |/ / / /_\ \ | | \ `--.  ")
print("|  _  | | | | __/ _ \|    \ |  _  | | |  `--. \ ")
print("| | | | |_| | || (_) | |\  \| | | |_| |_/\__/ / ")
print("\_| |_/\__,_|\__\___/\_| \_/\_| |_/\___/\____/  ")

print("");
print("");
print("AutoKAIS [fill out your form task automatically]");
print("")
print("The date and time now is",strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("It seems like you haven't submit your task form today.")
print("")
print("Awaiting for the time to manual prevent bot detection...");

# Pengaturan Browser Chrome yang akan digunakan oleh
# Selenium untuk mengotomatiskan pengisian form.

# Meringkas sebuah script supaya tidak terlihat berantakan
# Maka, baris kode awal yang berupa <webdriver.ChromeOptions()>
# dimasukkan kedalam variable bernama option supaya lebih mudah
# dibaca dan terlihat ringkas.

option = webdriver.ChromeOptions()

# Membuat sebuah opsi argumen berupa incognito supaya nanti
# Google Chrome akan membuka dengan mode Incognito. Sehingga, Google Form
# tidak dapat melihat cookie yang tersimpan di Tab biasa.

option.add_argument("-incognito")

# Membuat sebuah opsi experimental kepada Browser Chrome
# Supaya di Chrome bisa menjalankan otomasi dengan script dengan enable-automation
# dan meng-exclude Switches.

option.add_experimental_option("excludeSwitches", ['enable-automation']);

# Mendefine atau Meringkas Script Awal yang panjang.
# Baris kode dibawah digunakan untuk mengload driver Google Chrome
# dengan mengset executable path ke folder script melainkan ke PATH
# dan mengset option dengan variable option yang sudah di define diatas.

browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)

# Membuka browser dengan link yang sudah didefine diatas
# dengan nama variable gform (bisa dilihat di awal script)

browser.get(gform)

# time.sleep(value) digunakan untuk mendelay script.
# Disini, script akan mendelay selama tiga detik sebelum aktifitas
# selanjutnya dimulai.

time.sleep(2)
print("We're starting process.")

# Mendefine beberapa script panjang supaya lebih ringkas dan mudah dibaca.
# Fungsi baris barisan kode dibawah ini digunakan untuk browser mencari element
# element apa yang harus diotomasikan. Berikut adalah elements elements Google Form
# yang sudah di define oleh saya pribadi.

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
dropdown = browser.find_elements_by_xpath("//div[@role='option']")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# Bagaimana cara saya menemukan element element tersebut?
# Caranya cukup mudah, anda juga bisa tahu dengan membaca barisan diatas.
# Ada beberapa yang harus saya cari melalui metode class name, ada juga yang
# melalui XPATH karena susah dicari. Anda hanya tinggal ke Inspect Elements atau
# Developer Tools dari Google Form anda, dan menselect elements yang ingin dicari XPATH atau
# class-namenya. Setelah ditemukan, saatnya mencari class name atau XPATH.
#
# Jika ingin mencari melalui class_name, maka anda hanya perlu mencari barisan kode
# < class name = "(class namenya ini)" > di kode HTML yang telah di Inspect melalui
# Edit As HTML. Begitu cara mencarian dengan class_name.
#
# Jika ingin mencari dengan XPATH, bisa dengan klik kanan pada kode HTML
# element yang dicari, arahkan ke copy dan klik Copy Full XPATH atau XPATH.
# Akan tetapi, yang saya gunakan di Script ini karena memang ada banyak yang harus
# dicari, maka saya menggunakan < //div[@role='option'] >. Ini akan mencari element
# yang ada di bagian Divider situs dengan role atas nama "option".
#
# Untuk mengecek apabila Elements anda sudah bisa dicari oleh Selenium atau tidak
# cukup mudah, hanya perlu menekan CTRL + F di Inspect Element halaman situs tersebut
# dan copy XPATH atau class_name yang ingin anda cek, jika ketemu elementnya. Maka dari
# Selenium sudah bisa dicari, jika belum maka, tidak bisa.

# Ngisi Textbox dengan fungsi send_keys dari Selenium.
# Dibarisan kode berikut, Selenium akan mulai mengisi element textbox pertama dengan variable email
# yang telah di input oleh user, dan menekan tombol TAB untuk ke elements dibawah.
# textbox tersebut

textboxes[0].send_keys(email)
textboxes[0].send_keys(Keys.TAB)

# Ngisi Dropdown dengan metode (Click-Delay-Find
#
# Dikarenakan Dropdown ini unik dan berbeda dari elements yang lain, maka saya
# pake metode tersendiri. Caranya, dengan mengklik element dropdown, lalu tunggu
# 0.5 detik, dan mendefine XPATH dari Tombol Seleksi di Dropdown Tersebut, lalu
# Jika sudah ketemu, maka akan segera mengklik opsinya.

# Ngisi Jurusan

dropdown[0].click()
time.sleep(0.5)

select_smpit = browser.find_elements_by_xpath("//div//span[contains(., 'SMP-IT')]")
for smpit in select_smpit:
    try:
        smpit.click()
    except Exception as e:
        print(e)


#Ngisi Tingkat

dropdown[4].click()
time.sleep(0.5)

select_tingkat8 = browser.find_elements_by_xpath("//div//span[contains(., '8')]")
for select8 in select_tingkat8:
    try:
        select8.click()
    except Exception as e:
        print(e)

#Ngisi Kelas

dropdown[11].click()
time.sleep(0.5)

select_kelasa = browser.find_elements_by_xpath("//div//span[@class='quantumWizMenuPaperselectContent exportContent' and contains(., 'A')]")
for selecta in select_kelasa:
    try:
        selecta.click()
        time.sleep(0.5)
    except Exception as e:
        print(e)

# 

#Ngisi Nama dengan Textbox
textboxes[1].send_keys(name)


#Ngisi Amalan Ibadah Harian

# Jika ada yang nanya, apa nomor yang ada disetelah
# name variable, itu adalah urutan element dari object.
# Jadi, jika ada baris kode seperti :
# checkboxes[0].click(), maka itu berarti akan mengklik pada
# object checkbox yang pertama. // Karena di Python, satu dimulai dari enol ;)

checkboxes[0].click()
checkboxes[2].click()
checkboxes[3].click()
checkboxes[4].click()
checkboxes[6].click()
checkboxes[7].click()
checkboxes[9].click()
checkboxes[10].click()
checkboxes[11].click()
checkboxes[12].click()
checkboxes[13].click()
checkboxes[14].click()
checkboxes[16].click()
checkboxes[17].click()

#Ngisi Amalan Ibadah Mingguan
checkboxes[21].click()
checkboxes[22].click()
checkboxes[25].click()
checkboxes[26].click()
checkboxes[27].click()

#Ngisi Amalan Ibadah Situasional
checkboxes[29].click()
checkboxes[30].click()
checkboxes[31].click()
checkboxes[32].click()
checkboxes[34].click()
checkboxes[36].click()
checkboxes[37].click()
checkboxes[38].click()
checkboxes[39].click()

#Mengklik tombol Submit
submitbutton[0].click()

os.system('cls' if os.name == 'nt' else 'clear')

print("  ___        _        _   __  ___  _____ _____  ")
print(" / _ \      | |      | | / / / _ \|_   _/  ___| ")
print("/ /_\ \_   _| |_ ___ | |/ / / /_\ \ | | \ `--.  ")
print("|  _  | | | | __/ _ \|    \ |  _  | | |  `--. \ ")
print("| | | | |_| | || (_) | |\  \| | | |_| |_/\__/ / ")
print("\_| |_/\__,_|\__\___/\_| \_/\_| |_/\___/\____/  ")
print("");
print("");
print("AutoKAIS v.0.21 [fill out your form task automatically]");
print("You have filled the form at",strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("We will close our script at 10 seconds.")
time.sleep(2)
browser.close()
time.sleep(8)
exit();

# Semoga bermanfaat!.