# Import library
import urllib.request

# URL file yang ingin diunduh
url = input("Masukkan link URL file yang ingin diunduh: ")

# Nama file yang akan disimpan
filename = input("Masukkan nama file yang ingin disimpan: ")

# Unduh file dari internet
urllib.request.urlretrieve(url, filename)
