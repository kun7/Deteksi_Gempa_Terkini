"""
Aplikasi pendeteksi gempa
modularisasi dengan function
modularisasi dengan package
"""
import gempa_terkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempa_terkini.extraction_data()
    gempa_terkini.show_result(result)