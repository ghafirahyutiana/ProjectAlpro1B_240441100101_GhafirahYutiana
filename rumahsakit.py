# DATABASE
pasien_list = []
kapasitas_kamar = {
    1: {"nama": "VIP"    , "kapasitas": 1, "terisi": 0, "harga": 300000},
    2: {"nama": "Kelas 1", "kapasitas": 2, "terisi": 0, "harga": 200000},
    3: {"nama": "Kelas 2", "kapasitas": 4, "terisi": 0, "harga": 150000},
    4: {"nama": "Kelas 3", "kapasitas": 6, "terisi": 0, "harga": 100000},
}

# FITUR DAFTAR PASIEN
def daftar_pasien():
    global pasien_list, kapasitas_kamar
    # LOKET PENDAFTARAN
    baris1 = "PENDAFTARAN PASIEN BARU"
    baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(baris1), len(baris2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = baris1.center(lebar_struk)
    header2_tengah = baris2.center(lebar_struk)
    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)

    while True:
        print("Pendaftaran Pasien:")
        print("1. Pasien Umum")
        print("2. Pasien BPJS")
        tipe_pasien = input("Pilih jenis pasien (1/2): ")
        if tipe_pasien == "1" or tipe_pasien == "2":
            break
        print("Pilihan tidak valid. Harap masukkan 1 atau 2.")
    
    biaya_daftar = 0
    kategori_pasien = ""
    if tipe_pasien == "1":
        biaya_daftar = 10000
        kategori_pasien = "UMUM"
    elif tipe_pasien == "2":
        while True:
            print("Pilih Jenis BPJS:")
            print("1. BPJS Mandiri")
            print("2. BPJS Pemerintah")
            tipe_bpjs = input("Pilih jenis BPJS (1/2): ")
            if tipe_bpjs == "1":
                kategori_pasien = "BPJS Mandiri"
                break
            elif tipe_bpjs == "2":
                kategori_pasien = "BPJS Pemerintah"
                break
            print("Pilihan tidak valid. Harap masukkan 1 atau 2.")
    
    while True:
        nama_pasien = input("Masukkan nama pasien: ").strip()
        if all(x.isalpha() or x.isspace() for x in nama_pasien) and len(nama_pasien) > 0:
            break
        print("Nama pasien harus berupa huruf dan boleh mengandung spasi.")

    while True:
        usia_pasien = input("Masukkan umur: ")
        if usia_pasien.isdigit():
            usia_pasien = int(usia_pasien)
            if 0 < usia_pasien <= 100:
                break
        print("Umur harus berupa angka positif dan maksimal 100.")

    while True:
        alamat_pasien = input("Masukkan alamat: ").strip()
        if alamat_pasien:  
            break
        print("Alamat tidak boleh kosong.")

    while True:
        keluhan_pasien = input("Masukkan keluhan: ").strip()
        if keluhan_pasien and all(x.isalpha() or x.isspace() for x in keluhan_pasien):
            break
        print("Input tidak valid! Keluhan hanya boleh mengandung huruf alfabet dan spasi.")

    while True:
        tanggal_kunjungan = input("Masukkan tanggal kunjungan (DD-MM-YYYY): ").strip()
        if len(tanggal_kunjungan) == 10 and tanggal_kunjungan[2] == '-' and tanggal_kunjungan[5] == '-':
            day, month, year = tanggal_kunjungan.split('-')
            if day.isdigit() and month.isdigit() and year.isdigit():
                day, month, year = int(day), int(month), int(year)
                if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                    break
        print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")

    print(f"\nData pasien {nama_pasien} berhasil didaftarkan.")
    if kategori_pasien == "UMUM":
        print("Pasien UMUM, Biaya Pendaftaran: Rp. 10.000")
    else:
        print("Pasien BPJS, Tidak ada Biaya Pendaftaran")
    print(f"Tanggal Kunjungan: {tanggal_kunjungan}")

    pasien_info = {
        "nama": nama_pasien,
        "umur": usia_pasien,
        "alamat": alamat_pasien,
        "keluhan": keluhan_pasien,
        "kategori_pasien": kategori_pasien,
        "biaya_daftar": biaya_daftar,
        "tanggal_kunjungan": tanggal_kunjungan
    }
    
    # PEMILIHAN POLI
    baris1 = "PEMILIHAN POLI LANJUTAN"
    baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(baris1), len(baris2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = baris1.center(lebar_struk)
    header2_tengah = baris2.center(lebar_struk)
    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)

    print("Pilih Poli Lanjutan:")
    print("1. Poli Umum")
    print("2. Poli Gigi")
    print("3. Poli Mata")
    print("4. Poli KIA")

    while True:
        poli_input = input("Pilih poli (1-4): ").strip()
        if poli_input.isdigit():
            poli = int(poli_input)
            if 1 <= poli <= 4:
                break
        print("Input tidak valid. Harap masukkan angka 1-4.")

    biaya_poli = 0
    if kategori_pasien == "UMUM":
        if poli == 1:
            biaya_poli = 20000
        elif poli in [2, 3]:
            biaya_poli = 30000
        elif poli == 4:
            biaya_poli = 20000
    
    poli_nama = {
        1: "Poli Umum",
        2: "Poli Gigi",
        3: "Poli Mata",
        4: "Poli KIA"
    }
    print(f"\nAnda memilih {poli_nama[poli]} dengan biaya: Rp. {biaya_poli if kategori_pasien == 'UMUM' else 0}.")


    # RAWAT INAP
    baris1 = "RESERVASI KAMAR RAWAT INAP"
    baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(baris1), len(baris2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = baris1.center(lebar_struk)
    header2_tengah = baris2.center(lebar_struk)
    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)

    rawat_inap_biaya = 0

    while True:
        print("\nPilih Jenis Kamar:")
        for k, v in kapasitas_kamar.items():
            print(f"{k}. {v['nama']} (Rp {v['harga']}/malam, kapasitas: {v['kapasitas']}, terisi: {v['terisi']})")

        kamar_input = input("Pilih tipe kamar (1-4): ").strip()
        if kamar_input.isdigit() and int(kamar_input) in kapasitas_kamar:
            kamar = int(kamar_input)
            kamar_data = kapasitas_kamar[kamar]

            if kamar_data["terisi"] < kamar_data["kapasitas"]:
                kamar_data["terisi"] += 1  
                pasien_info["kategori_kamar"] = kamar_data["nama"]  
                rawat_inap_biaya = kamar_data["harga"]  
                print(f"\nPasien {nama_pasien} berhasil memilih kamar {kamar_data['nama']}.")
                break
            else:
                print("Maaf kamar ini sudah penuh, silakan pilih kamar lain.")
        else:
            print("Pilihan kamar tidak valid, pilih antara 1-4.")

    while True:
        hari_input = input(f"Berapa hari pasien akan dirawat di kamar {kamar_data['nama']}? (Harap masukkan angka): ").strip()
        if hari_input.isdigit():
            hari_rawat = int(hari_input)
            if hari_rawat > 0:
                rawat_inap_biaya *= hari_rawat  
                print(f"Pasien akan dirawat inap selama {hari_rawat} hari dengan biaya: Rp {rawat_inap_biaya}.")
                break
            else:
                print("Jumlah hari harus lebih dari 0. Silakan coba lagi.")
        else:
            print("Input tidak valid. Harap masukkan angka untuk jumlah hari.")

    pasien_info["biaya_rawat_inap"] = rawat_inap_biaya

    # POLI FARMASI
    baris1 = "POLI FARMASI"
    baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(baris1), len(baris2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = baris1.center(lebar_struk)
    header2_tengah = baris2.center(lebar_struk)
    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)

    biaya_obat = 0
    while True:
        print("Menu pilihan Obat:")
        print("1. Tambah Obat")
        print("2. selesai")
        pilihan = (input("Pilih opsi (1/2): "))
        if pilihan == "1":
            nama_obat = input("Masukkan nama obat: ")
            jumlah_obat = input(f"Masukkan jumlah untuk {nama_obat}: ")
            aturan_minum = input(f"Masukkan Aturan untuk minum obat {nama_obat}: ")
            if tipe_pasien == 2 :
                biaya_obat += 0
            else :
                biaya_obat += 30000
        elif pilihan == "2":
            print(f"Anda Dikenai Biaya Farmasi Sebesar : Rp.{biaya_obat}")
            break
        else :
            print("Input Salah!!,Ulangi Kembali!!")

    # LOKET PEMBAYARAN
    # TOTAL BIAYA
    baris1 = "LOKET PEMBAYARAN"
    baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(baris1), len(baris2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = baris1.center(lebar_struk)
    header2_tengah = baris2.center(lebar_struk)
    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)
    print("Masuk ke Loket Pembayaran")
    total_biaya = biaya_daftar + biaya_poli + rawat_inap_biaya + biaya_obat
    print(f"Total Biaya: Rp {total_biaya}")
    while True:
        tanggal_transaksi = input("Masukkan tanggal transaksi (format: YYYY-MM-DD): ")
        if len(tanggal_transaksi) == 10 and tanggal_transaksi[4] == '-' and tanggal_transaksi[7] == '-':
            year, month, day = tanggal_transaksi.split('-')
            if year.isdigit() and month.isdigit() and day.isdigit():
                year, month, day = int(year), int(month), int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
                else:
                    print("Tanggal tidak valid. Pastikan bulan dan hari dalam rentang yang benar.")
            else:
                print("Tanggal tidak valid. Pastikan format tanggal benar (YYYY-MM-DD).")
        else:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
    uang_dibayar = int(input("Masukkan jumlah uang untuk pembayaran: "))
    kembalian = uang_dibayar - total_biaya

    pasien_info["biaya_poli"] = biaya_poli
    pasien_info["rawat_inap_biaya"] = rawat_inap_biaya
    pasien_info["biaya_obat"] = biaya_obat
    pasien_info["total_biaya"] = total_biaya
    pasien_info["tanggal_transaksi"] = tanggal_transaksi
    pasien_list.append(pasien_info)

    # STRUK PEMBAYARAN
    header1 = "STRUK PEMBAYARAN ADMINISTRASI"
    header2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
    lebar_struk = max(len(header1), len(header2)) + 4
    garis_pembatas = "=" * lebar_struk
    header1_tengah = header1.center(lebar_struk)
    header2_tengah = header2.center(lebar_struk)

    print(garis_pembatas)
    print(header1_tengah)
    print(header2_tengah)
    print(garis_pembatas)
    print(f"Nama Pasien   : {nama_pasien}")
    print(f"Jenis Pasien  : {kategori_pasien}")
    print(f"Tanggal Transaksi: {tanggal_transaksi}")
    print(f"Rincian Biaya :")
    print(f"- Biaya Pendaftaran: Rp {biaya_daftar}")
    print(f"- Biaya Poli       : Rp {biaya_poli}")
    print(f"- Biaya Rawat Inap : Rp {rawat_inap_biaya}")
    print(f"- Biaya Farmasi    : Rp {biaya_obat}")
    print(f"Total Tagihan  : Rp {total_biaya}")
    print(f"Uang Dibayar   : Rp {uang_dibayar}")
    print(f"Kembalian      : Rp {kembalian}")
    print(garis_pembatas)

# FITUR TAMPILKAN DATA PASIEN
def tampilkan_pasien():
    if len(pasien_list) == 0:
        print("Tidak ada data pasien.")
        return

    while True:
        print("\nMenu Tampilkan Data Pasien:")
        print("1. History Pembayaran")
        print("2. History Data Pendaftaran Pasien")
        print("3. Data Pasien Berdasarkan Pengelompokan Kamar")
        print("4. Cari Pasien Berdasarkan Kata Kunci")
        print("5. Kembali ke Menu Utama dan Edit Data Pasien")
        try:
            pilihan = int(input("Pilih opsi (1/2/3/4/5): "))
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka dari 1 sampai 5.")
            continue
        
        if pilihan == 1:
            # History Pembayaran
            print("\nHistory Pembayaran:")
            for index, pasien in enumerate(pasien_list, 1):
                print(f"{index}. Nama: {pasien['nama']}, Tanggal Transaksi: {pasien['tanggal_transaksi']}, Total Biaya: Rp {pasien['total_biaya']}, Kategori: {pasien['kategori_pasien']}")
        
        elif pilihan == 2:
            # History Data Pendaftaran Pasien
            print("\nHistory Data Pendaftaran Pasien:")
            for index, pasien in enumerate(pasien_list, 1):
                print(f"{index}. Nama: {pasien['nama']}, Tanggal Kunjungan: {pasien['tanggal_kunjungan']}, Umur: {pasien['umur']}, Alamat: {pasien['alamat']}, Keluhan: {pasien['keluhan']}, Kategori: {pasien['kategori_pasien']}")
        
        elif pilihan == 3:
            # Data Pasien Berdasarkan Pengelompokan Kamar
            print("\nData Pasien Berdasarkan Pengelompokan Kamar:")
            kamar_data = {
                "VIP"    : {"kapasitas": 1, "pasien": []},
                "Kelas 1": {"kapasitas": 2, "pasien": []},
                "Kelas 2": {"kapasitas": 4, "pasien": []},
                "Kelas 3": {"kapasitas": 6, "pasien": []}
            }

            for pasien in pasien_list:
                if "biaya_rawat_inap" in pasien and pasien['biaya_rawat_inap'] > 0:
                    if "VIP" in pasien.get("kategori_kamar", ""):
                        kamar_data["VIP"]["pasien"].append(pasien["nama"])
                    elif "Kelas 1" in pasien.get("kategori_kamar", ""):
                        kamar_data["Kelas 1"]["pasien"].append(pasien["nama"])
                    elif "Kelas 2" in pasien.get("kategori_kamar", ""):
                        kamar_data["Kelas 2"]["pasien"].append(pasien["nama"])
                    elif "Kelas 3" in pasien.get("kategori_kamar", ""):
                        kamar_data["Kelas 3"]["pasien"].append(pasien["nama"])
            
            for kamar, info in kamar_data.items():
                print(f"Kamar {kamar} (Kapasitas Maksimal: {info['kapasitas']}):")
                if info["pasien"]:
                    print(", ".join(info["pasien"]))
                else:
                    print("Tidak ada pasien.")
        
        elif pilihan == 4:
            while True:
                print("\nPilih kategori pencarian:")
                print("1. Nama")
                print("2. Alamat")
                print("3. Keluhan")
                print("4. Kembali")
                keyword_choice = input("Pilih kata kunci pencarian (1/2/3/4): ")

                if keyword_choice == "1":
                    keyword = input("\nMasukkan nama pasien yang ingin dicari: ").lower()
                    print("\nHasil Pencarian berdasarkan Nama:")
                    found = False
                    for index, pasien in enumerate(pasien_list, 1):
                        if keyword in pasien['nama'].lower():
                            print(f"{index}. Nama: {pasien['nama']}, Umur: {pasien['umur']}, Alamat: {pasien['alamat']}, Keluhan: {pasien['keluhan']}, Kategori: {pasien['kategori_pasien']}")
                            found = True
                    if not found:
                        print("Tidak ada pasien yang sesuai dengan kata kunci.")

                elif keyword_choice == "2":
                    keyword = input("\nMasukkan alamat pasien yang ingin dicari: ").lower()
                    print("\nHasil Pencarian berdasarkan Alamat:")
                    found = False
                    for index, pasien in enumerate(pasien_list, 1):
                        if keyword in pasien['alamat'].lower():
                            print(f"{index}. Nama: {pasien['nama']}, Umur: {pasien['umur']}, Alamat: {pasien['alamat']}, Keluhan: {pasien['keluhan']}, Kategori: {pasien['kategori_pasien']}")
                            found = True
                    if not found:
                        print("Tidak ada pasien yang sesuai dengan kata kunci.")

                elif keyword_choice == "3":
                    keyword = input("\nMasukkan keluhan pasien yang ingin dicari: ").lower()
                    print("\nHasil Pencarian berdasarkan Keluhan:")
                    found = False
                    for index, pasien in enumerate(pasien_list, 1):
                        if keyword in pasien['keluhan'].lower():
                            print(f"{index}. Nama: {pasien['nama']}, Umur: {pasien['umur']}, Alamat: {pasien['alamat']}, Keluhan: {pasien['keluhan']}, Kategori: {pasien['kategori_pasien']}")
                            found = True
                    if not found:
                        print("Tidak ada pasien yang sesuai dengan kata kunci.")
                
                elif keyword_choice == "4":
                    break  # Kembali ke menu utama
                else:
                    print("Pilihan tidak valid, coba lagi.")

        elif pilihan == 5:
            # Kembali ke Menu Utama dan langsung menuju fungsi edit_pasien()
            print("\nKembali ke Menu Utama dan langsung mengedit data pasien...")
            menu()  # Panggil fungsi edit_pasien()
            break  # Keluar dari menu tampilkan_pasien
        else:
            print("Pilihan tidak valid.")

    
# FITUR UPDATE DATA
def edit_pasien():
    if len(pasien_list) == 0:
        print("Tidak ada data pasien untuk diedit.")
        return

    # Menampilkan semua data pasien yang telah dimasukkan
    print("\nDaftar Semua Pasien:")
    for index, pasien in enumerate(pasien_list, 1):
        print(f"{index}. Nama: {pasien['nama']}, Umur: {pasien['umur']}, Alamat: {pasien['alamat']}, Keluhan: {pasien['keluhan']}, Kategori: {pasien['kategori_pasien']}")

    while True:
        pilihan = input("\nMasukkan nomor pasien yang ingin diedit: ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(pasien_list):
                pasien = pasien_list[pilihan - 1]
                print(f"\nData Pasien yang dipilih: {pasien['nama']} - {pasien['kategori_pasien']}")
                
                # Mengedit nama pasien
                pasien['nama'] = input("Masukkan nama pasien baru: ").strip()

                # Mengedit usia pasien
                while True:
                    usia_pasien = input("Masukkan umur pasien baru: ")
                    if 0 < usia_pasien <= 100:
                        pasien['umur'] = usia_pasien
                        break
                    else :
                        print("Umur harus berupa angka positif dan maksimal 100.")


                # Mengedit alamat pasien
                pasien['alamat'] = input("Masukkan alamat pasien baru: ").strip()

                # Mengedit keluhan pasien
                pasien['keluhan'] = input("Masukkan keluhan pasien baru: ").strip()

                # Mengedit tanggal kunjungan
                while True:
                    tanggal_kunjungan = input("Masukkan tanggal kunjungan baru (DD-MM-YYYY): ").strip()
                    if len(tanggal_kunjungan) == 10 and tanggal_kunjungan[2] == '-' and tanggal_kunjungan[5] == '-': 
                        day, month, year = tanggal_kunjungan.split('-')
                        if day.isdigit() and month.isdigit() and year.isdigit():
                            day, month, year = int(day), int(month), int(year)
                            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                                break
                    else :
                        print("Format tanggal tidak valid. Gunakan format DD-MM-YYYY.")
                        pasien['tanggal_kunjungan'] = tanggal_kunjungan
                        break

                print(f"\nData pasien {pasien['nama']} berhasil diubah.")
                break
            else:
                print("Nomor pasien tidak valid.")
        else:
            print("Input tidak valid, harap masukkan angka.")

# FITUR MENGHAPUS DATA
def hapus_pasien():
    tampilkan_pasien()
    global pasien_list, kapasitas_kamar
    tampilkan_pasien()
    if len(pasien_list) == 0:
        return

    while True:
        pilihan = input("\nMasukkan nomor pasien yang ingin dihapus: ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(pasien_list):
                pasien = pasien_list.pop(pilihan - 1)

                # Mengembalikan kapasitas kamar jika pasien dihapus
                for kamar in kapasitas_kamar.values():
                    if pasien['kategori_kamar'] == kamar['nama']:
                        kamar['terisi'] -= 1
                        break

                print(f"Data pasien {pasien['nama']} berhasil dihapus.")
                break
            else:
                print("Nomor pasien tidak valid.")
        else:
            print("Input tidak valid, harap masukkan angka.")

# Fungsi untuk menu utama
def menu():
    while True:
        # Header Program 
        baris1 = "SELAMAT DATANG DI SISTEM LAYANAN ADMINISTRASI"
        baris2 = "RUMAH SAKIT UNIVERSITAS TRUNOJOYO MADURA"
        baris3 = "Jl. Raya Telang Kec. Kamal Kab. Bangkalan Jawa Timur"
        lebar_tampilan = max(len(baris1), len(baris2), len(baris3)) + 4
        pembatas = "=" * lebar_tampilan
        baris1_tengah = baris1.center(lebar_tampilan)
        baris2_tengah = baris2.center(lebar_tampilan)
        baris3_tengah = baris3.center(lebar_tampilan)
        # Menampilkan hasil
        print(pembatas)
        print(baris1_tengah)
        print(baris2_tengah)
        print(baris3_tengah)
        print(pembatas)
        print("Menu Pelayanan Administrasi :")
        print("1. Daftar Pasien Baru")
        print("2. Tampilkan Daftar Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            daftar_pasien()
        elif pilihan == "2":
            tampilkan_pasien()
        elif pilihan == "3":
            edit_pasien()
        elif pilihan == "4":
            hapus_pasien()
        elif pilihan == "5":
            print("Terima kasih Semoga Lekas Sembuh, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1-5.")

# Panggil menu utama
menu()