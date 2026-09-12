BATAS_KAFEIN_HARIAN = 400

daftar_kopi = [
    ("Cappucino" , 75 , 25000 , "09:00 WIB"),
    ("Iced Americano" , 120 , 22000 , "14:00 WIB"),
    ("Espresso (Double Shot)" , 126 , 25000 , "19:00 WIB"),
    ("Kopi Tubruk", 100 , 8000 , "07:00 WIB")
]

while True:
    print("\n" + "="*60)
    print(" KALKULATOR EFISIENSI COFFEE SHOP & KONSUMSI KAFEIN ")
    print("="*60)
    print(f"Batas Aman Kafein Harian: {BATAS_KAFEIN_HARIAN} mg")
    print("-" * 60)
    print("1. Tambah Data Pesanan (Create)")
    print("2. Tampilkan Semua Data & Analisis (Read)")
    print("3. Ubah Data Pesanan (Update)")
    print("4. Hapus Data Pesanan (Delete)")
    print("5. Keluar")
    print("="*60)

    pilihan = input ("pilih menu (1-5): ").strip()

    if pilihan == "1":
        print("\n--- Tambah Data Pesanan ---")
        nama = input("Masukkan Nama Minuman : ").strip()
        kafein_input = input("Masukkan Kandungan Kafein (mg)  : ").strip()
        harga_input = input("Harga (Rp)  : ").strip()
        waktu = input("Waktu Minum (10.00 WIB)  : ").strip()

        if nama and kafein_input.isdigit() and harga_input.isdigit() and waktu:
            kafein = int(kafein_input)
            harga = int(harga_input)
            daftar_kopi.append((nama, kafein, harga, waktu))
            print("Data minuman berhasil ditambahkan!")
        else:
            print("Gagal: input tidak lengkap atau angka tidak valid.")
        
    elif pilihan == "2":
        print("\n--- Daftar Pesanan & Analisis ---")
        if not daftar_kopi:
            print("Belum ada pesanan hari ini.")
        else:
            total_kafein = 0
            total_pengeluaran = 0

            for idx, item in enumerate(daftar_kopi, 1):
                nama, kafein, harga, waktu = item
                total_kafein += harga 
                total_pengeluaran += harga
                print(f"{idx}, [{waktu}] {nama} - {kafein} mg Kafein | Rp {harga:,.0f}")

            sisa_kuota_kafein = BATAS_KAFEIN_HARIAN - total_kafein

            print("-" * 60)
            print(f"Total Asupan Kafein : {total_kafein} mg / {BATAS_KAFEIN_HARIAN} mg")
            print(f"Total Pengeluaran : Rp {total_pengeluaran:,.0f}")

            if total_kafein > BATAS_KAFEIN_HARIAN:
                print(f"\n[PERINGATAN] Anda melebihi batas aman kafein sebesar {total_kafein - BATAS_KAFEIN_HARIAN} mg!")
                print("Efek: Bisa memicu jantung berdebar, tremor, gelisah, hingga aslam naik.")
            elif total_kafein >= BATAS_KAFEIN_HARIAN:
                print(f"\n[PERINGATAN] Asupan kafein anda mendekati batas maksimum harian.")
            else:
                print(f"\n[INFO] Asupan kafein aman, Sisa kuota aman: {sisa_kuota_kafein} mg.")

    elif pilihan == "3":
        print("\n--- Ubah Data Pesanan  ---")
        if not daftar_kopi:
            print("Belum ada data yang di ubah.")
        else:
            for idx, item in enumerate(daftar_kopi, 1):
                print(f"{idx}, {item[0]} ({item[1]} mg) - Rp {item[2]:,.0f}")

            pilihan_idx = input("Pilih data yang ingin di ubah: ")
            if pilihan_idx.isdigit():
                idx_ubah = int(pilihan_idx) - 1
                if 0 <= idx_ubah < len(daftar_kopi):
                    print("\nMasukkan Data Baru:")
                    nama_baru = input("Nama Pesanan Baru  : ").strip()
                    kafein_baru = input("Kafein Baru (mg)  : ").strip()
                    harga_baru = input("Harga Baru (Rp)  : ").strip()
                    waktu_baru = input("Waktu Minum Baru  : ").strip()

                    if nama_baru and kafein_baru.isdigit() and harga_baru.isdigit() and waktu_baru:
                        daftar_kopi[idx_ubah] = (nama_baru, int(kafein_baru), int(harga_baru), waktu_baru)
                        print(">> Data berhasil di perbarui!")
                    else:
                        print(">> Gagal: input tidak valid.")
                else:
                    print(">> Data tidak di temukan.")
            else:
                print(">> Input harus berupa angka.")

    elif pilihan == "4":
        print("\n--- Hapus Data Pesanan ---")
        if not daftar_kopi:
            print("Belum ada data untuk di hapus.")
        else:
            for idx, item in enumerate(daftar_kopi, 1):
                print(f"{idx}, {item[0]} ({item[1]} mg) - Rp {item[2]:,.0f}")

            pilihan_idx = input("Pilih data yang ingin di hapus: ")
            if pilihan_idx.isdigit():
                idx_hapus = int(pilihan_idx) - 1
                if 0 <= idx_ubah < len(daftar_kopi):
                    terhapus = daftar_kopi.pop(idx_hapus)
                    print(f">> Data '{terhapus[0]}' berhasil di hapus!")
                else:
                    print(">> Data tidak di temukan.")
            else:
                print(">> input harus berupa angka.")

    elif pilihan == "5":
        print("\nTerima kasih! Selalu jaga batas konsumsi kafein harianmu!")
        break

    else:
        print("\n[!] Pilihan menu tidak valid! Silahkan masukkan angka 1-5.")

        














