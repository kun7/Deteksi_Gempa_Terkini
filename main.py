"""
Aplikasi pendeteksi gempa
modularisasi dengan function
"""
from gempa_terkini import extraction_data, show_result

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = extraction_data()
    show_result(result)