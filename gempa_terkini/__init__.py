def extraction_data():
    hasil = dict()
    hasil['tanggal'] = '1 september 2021'
    hasil['waktu'] = '08:56:28 WIB'
    hasil['magnitudo'] = 3.3
    hasil['lokasi'] = {'ls' : 1.48, 'bt' : 134.01}
    hasil['pusat'] = 'Pusat gempa berada di darat 18KM Barat Laut Ransiki'
    hasil['dirasakan'] = '(Skala NNI): II-III Ransiki'
    return hasil

def show_result(hasil):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal, {hasil['tanggal']}")
    print(f"Waktu, {hasil['waktu']}")
    print(f"lokasi: LS={hasil['lokasi']['ls']}, BT={hasil['lokasi']['bt']}")
    print(f"Pusat, {hasil['pusat']}")
    print(f"Dirasakan, {hasil['dirasakan']}")