import os
import sys
from PIL import Image
def convert_image(input_path, himage_path, format):
    try:
        image = Image.open(input_path)
        if format == "PNG":
            image.save(himage_path, "PNG")
            print("Gambar berhasil dikonversi ke PNG dan Tersimpan Di Path " + himage_path)
        elif format == "JPEG":
            image.save(himage_path, "JPEG")
            print("Gambar berhasil dikonversi ke JPEG dan Tersimpan Di Path " + himage_path)
        elif format == "GIF":
            image.save(himage_path, "GIF")
            print("Gambar berhasil dikonversi ke GIF dan Tersimpan Di Path " + himage_path)
        else:
            print("Format gambar tidak didukung harap gunakan format gambar(PNG, JPEG, GIF)")
    except FileNotFoundError:
        print("File tidak ditemukan")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))
def banner():
    print("""
        ╻┏┳┓┏━╸
        ┃┃┃┃┃  
        ╹╹ ╹┗━╸
    (IMAGE CONVERTER)
    Creator: FerzChills/Ferdinand
    Country: Indonesia
    Github: https://github.com/FerzChills
    WhatsApp: https://chat.whatsapp.com/FWfWHpWOXq1Hlqz8nVPHfm
""")
os.system("clear")
banner()
input_path = input("Masukkan path gambar yang akan di konversi: ")
print("wait for search path")
os.system("sleep 3")
himage_path = input("Masukkan path gambar untuk hasil konversi: ")
print("wait for search path")
os.system("sleep 3")
format = input("Masukkan hasil format gambar (PNG, JPEG, GIF): ")
print("wait for results")
os.system("sleep 5")
convert_image(input_path, himage_path, format)
