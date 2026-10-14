# Sistem Rumah Sakit — Tugas PBO

Program Sistem Rumah Sakit sederhana menggunakan **C# / .NET 10** sebagai pemenuhan tugas
Pemrograman Berbasis Objek (PBO). Program mendemonstrasikan konsep **inheritance (pewarisan)**,
**override**, **polymorphism**, **upcasting/downcasting**, serta koleksi objek.

## Struktur Kelas

```
Orang                 (nama, umur)                     : Aktivitas() [virtual], InfoOrang()
├── Pasien             (keluhan)                        : CekKeluhan()
│   ├── PasienAnak                                     : Menangis()
│   └── PasienDewasa                                   : Konsultasi(dokter)
└── TenagaMedis        (spesialisasi)                  : CekSpesialis()
    ├── Dokter                                          : Diagnosa(pasien)
    └── Perawat                                          : CekPasien(pasien)

RumahSakit                                              : TambahOrang(Orang), DaftarOrang()
```

## Cara Menjalankan

```bash
dotnet run
```

## Isi Program (Program.cs)

1. Membuat objek rumah sakit
2. Membuat beberapa objek orang (Dokter, Perawat, PasienAnak, PasienDewasa, Pasien)
3. Menambahkan objek ke rumah sakit
4. Menampilkan semua data (`DaftarOrang()`)
5. Demonstrasi polymorphism (`Aktivitas()` melalui variabel bertipe `Orang`)
6. Memanggil method khusus tiap kelas
7. Demonstrasi untuk menjawab Soal 1–6 (aktivitas override, pent-cast method khusus, dll.)

## Laporan

Laporan lengkap (kode, output, jawaban soal) tersedia di:
`Report/Laporan_Tugas_PBO_SistemRumahSakit.pdf`

## Repository

https://github.com/GylaxDev/A_252410103018_TASKPBO (public)

Nama repository: `A_252410103018_TASKPBO` (format: KELAS_NIM_TASKPBO)

