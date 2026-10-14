using System.Text;
using SistemRumahSakit;

Console.OutputEncoding = Encoding.UTF8;

Console.WriteLine("=======================================================");
Console.WriteLine("        SISTEM RUMAH SAKIT - TUGAS PBO");
Console.WriteLine("=======================================================");
Console.WriteLine();

// ---------------------------------------------------------------
// 6a. Buat objek rumah sakit
// ---------------------------------------------------------------
var rumahSakit = new RumahSakit();

// ---------------------------------------------------------------
// 6b. Buat beberapa objek orang
// ---------------------------------------------------------------
var dokter1 = new Dokter("Dr. Andi Prasetyo", 45, "Jantung");
var dokter2 = new Dokter("Dr. Siti Rahayu", 38, "Anak");
var perawat1 = new Perawat("Budi Santoso", 30, "Perawatan Umum");
var pasienAnak1 = new PasienAnak("Timmy", 7, "Demam");
var pasienDewasa1 = new PasienDewasa("Rina Wijaya", 40, "Hipertensi");
var pasienUmum1 = new Pasien("Joko Susilo", 55, "Sakit Gigi");

Console.WriteLine(">>> Objek-objek telah dibuat.\n");

// ---------------------------------------------------------------
// 6c. Tambahkan ke rumah sakit
// ---------------------------------------------------------------
Console.WriteLine(">>> Menambahkan objek ke rumah sakit:");
rumahSakit.TambahOrang(dokter1);
rumahSakit.TambahOrang(dokter2);
rumahSakit.TambahOrang(perawat1);
rumahSakit.TambahOrang(pasienAnak1);
rumahSakit.TambahOrang(pasienDewasa1);
rumahSakit.TambahOrang(pasienUmum1);

// ---------------------------------------------------------------
// 6d. Tampilkan semua data
// ---------------------------------------------------------------
rumahSakit.DaftarOrang();

// ---------------------------------------------------------------
// 6e. Demonstrasikan polymorphism
//     Memanggil Aktivitas() yang sama pada variabel bertipe Orang,
//     namun hasilnya berbeda-beda sesuai tipe objek sebenarnya.
// ---------------------------------------------------------------
Console.WriteLine("\n>>> Demonstrasi Polymorphism:");
Console.WriteLine("Memanggil Aktivitas() melalui variabel bertipe Orang:");
foreach (var orang in rumahSakit.GetSemuaOrang())
{
    Console.Write($"[{orang.GetType().Name}] ".PadRight(20));
    orang.Aktivitas();
}

Console.WriteLine("\n>>> Demonstrasi Polymorphism dengan ARRAY bertipe Orang:");
Orang[] kumpulanOrang = { dokter1, perawat1, pasienAnak1, pasienDewasa1 };
foreach (var orang in kumpulanOrang)
{
    orang.Aktivitas();
}

// ---------------------------------------------------------------
// 6f. Panggil method khusus
// ---------------------------------------------------------------
Console.WriteLine("\n>>> Memanggil method khusus setiap kelas:");
dokter1.CekSpesialis();
dokter2.CekSpesialis();
perawat1.CekSpesialis();
pasienAnak1.CekKeluhan();
pasienDewasa1.CekKeluhan();
pasienUmum1.CekKeluhan();

Console.WriteLine("\n>>> Method khusus Dokter & Perawat:");
dokter1.Diagnosa(pasienUmum1.Nama);
perawat1.CekPasien(pasienAnak1.Nama);

Console.WriteLine("\n>>> Method khusus PasienAnak & PasienDewasa:");
pasienAnak1.Menangis();
pasienDewasa1.Konsultasi(dokter2.Nama);

// ===============================================================
// JAWABAN SOAL-SOAL (dengan demonstrasi pada method Main)
// ===============================================================

// ---------------------------------------------------------------
// SOAL 1: Jalankan method Aktivitas() pada objek Dokter dan Pasien.
//          Apa yang terjadi? Mengapa demikian?
// ---------------------------------------------------------------
Console.WriteLine("\n\n================ SOAL 1 ================");
Console.WriteLine("Menjalankan Aktivitas() pada objek Dokter dan Pasien:");
dokter1.Aktivitas();
pasienUmum1.Aktivitas();
Console.WriteLine(">> Yang terjadi: masing-masing objek menjalankan versi Aktivitas()");
Console.WriteLine("   milik kelasnya sendiri (override), bukan versi kelas Orang.");
Console.WriteLine(">> Mengapa: Aktivitas() di kelas Orang bersifat 'virtual' dan");
Console.WriteLine("   di-override di setiap subclass, sehingga C# memilih versi");
Console.WriteLine("   method sesuai tipe objek sebenarnya (runtime polymorphism).");

// ---------------------------------------------------------------
// SOAL 2: Jalankan method Diagnosa() pada objek Dokter.
//          Apa yang terjadi? Mengapa demikian?
// ---------------------------------------------------------------
Console.WriteLine("\n================ SOAL 2 ================");
Console.WriteLine("Menjalankan Diagnosa() pada objek Dokter:");
dokter1.Diagnosa(pasienUmum1.Nama);
Console.WriteLine(">> Yang terjadi: method Diagnosa() berjalan normal dan menampilkan");
Console.WriteLine("   informasi diagnosis.");
Console.WriteLine(">> Mengapa: Diagnosa() adalah method yang didefinisikan di kelas");
Console.WriteLine("   Dokter, dan variabel dokter1 bertipe Dokter, sehingga method");
Console.WriteLine("   tersebut bisa langsung diakses.");

// ---------------------------------------------------------------
// SOAL 3: Dapatkah Anda menampilkan informasi lengkap
//          (nama, umur, spesialisasi) dari objek Dokter?
//          Bagaimana caranya?
// ---------------------------------------------------------------
Console.WriteLine("\n================ SOAL 3 ================");
Console.WriteLine("Ya, bisa. Informasi lengkap objek Dokter dapat ditampilkan dengan");
Console.WriteLine("menggabungkan InfoOrang() (warisan Orang) dan CekSpesialis()");
Console.WriteLine("(warisan TenagaMedis). Contoh:");

// Cara 1: memakai method yang sudah ada
dokter1.InfoOrang();
dokter1.CekSpesialis();

// Cara 2: memakai variabel bertipe Orang (melalui downcast)
Console.WriteLine("\nCara lain dengan variabel bertipe Orang (via downcast):");
Orang orangDokter = dokter1;
orangDokter.InfoOrang();
((TenagaMedis)orangDokter).CekSpesialis();

// Cara 3: mengakses properti secara langsung
Console.WriteLine("\nCara lain dengan mengakses properti secara langsung:");
Console.WriteLine($"Nama: {dokter1.Nama} | Umur: {dokter1.Umur} | Spesialisasi: {dokter1.Spesialisasi}");

// ---------------------------------------------------------------
// SOAL 4: Jalankan method Menangis() pada objek PasienAnak.
//          Apa yang terjadi? Mengapa demikian?
// ---------------------------------------------------------------
Console.WriteLine("\n================ SOAL 4 ================");
Console.WriteLine("Menjalankan Menangis() pada objek PasienAnak:");
pasienAnak1.Menangis();
Console.WriteLine(">> Yang terjadi: method Menangis() berjalan normal dan menampilkan");
Console.WriteLine("   aktivitas menangis dari pasien anak.");
Console.WriteLine(">> Mengapa: Menangis() didefinisikan di kelas PasienAnak, dan objek");
Console.WriteLine("   pasienAnak1 memang bertipe PasienAnak, sehingga method tersebut");
Console.WriteLine("   bisa diakses langsung.");

// ---------------------------------------------------------------
// SOAL 5: Buatlah variabel bertipe Orang, lalu isi dengan objek
//          Perawat. Jalankan method Aktivitas(). Apa yang terjadi?
//          Mengapa demikian?
// ---------------------------------------------------------------
Console.WriteLine("\n================ SOAL 5 ================");
Orang orangPerawat = new Perawat("Dewi Lestari", 35, "Kebidanan");
Console.WriteLine("Variabel bertipe Orang diisi dengan objek Perawat.");
Console.WriteLine("Menjalankan Aktivitas():");
orangPerawat.Aktivitas();
Console.WriteLine(">> Yang terjadi: yang dijalankan adalah Aktivitas() versi Perawat,");
Console.WriteLine("   BUKAN versi kelas Orang.");
Console.WriteLine(">> Mengapa: karena Aktivitas() bersifat 'virtual' dan telah");
Console.WriteLine("   di-override oleh kelas Perawat, C# melakukan dynamic dispatch");
Console.WriteLine("   (pemanggilan method ditentukan oleh tipe objek saat runtime,");
Console.WriteLine("   bukan tipe variabel saat compile time).");
Console.WriteLine(">> Catatan: method khusus Perawat (misal CekPasien) TIDAK bisa");
Console.WriteLine("   dipanggil langsung dari variabel bertipe Orang; perlu downcast:");

// Menunjukkan bahwa method khusus butuh downcast
// orangPerawat.CekPasien("X");  // <- ini akan ERROR compile
((Perawat)orangPerawat).CekPasien("Timmy");
Console.WriteLine("   (baris orangPerawat.CekPasien(...) akan menghasilkan error");
Console.WriteLine("    compiler karena tipe variabel hanya Orang)");

// ---------------------------------------------------------------
// SOAL 6: Kesimpulan apa yang dapat Anda ambil?
// ---------------------------------------------------------------
Console.WriteLine("\n================ SOAL 6 ================");
Console.WriteLine("KESIMPULAN:");
Console.WriteLine("1. Inheritance (pewarisan) memungkinkan subclass (Dokter, Perawat,");
Console.WriteLine("   Pasien, dll.) menggunakan kembali properti dan method dari");
Console.WriteLine("   kelas induk Orang, sehingga lebih sederhana dan terstruktur.");
Console.WriteLine("2. Polymorphism (virtual + override) membuat method yang sama,");
Console.WriteLine("   misalnya Aktivitas(), dapat berperilaku berbeda sesuai objek");
Console.WriteLine("   sebenarnya meskipun dipanggil lewat variabel bertipe induk.");
Console.WriteLine("3. Variabel bertipe induk (Orang) bisa menyimpan objek subclass");
Console.WriteLine("   apa pun, sehingga memudahkan pengelolaan koleksi orang di");
Console.WriteLine("   rumah sakit (misalnya List<Orang>).");
Console.WriteLine("4. Method khusus tiap subclass hanya bisa diakses bila tipe variabel");
Console.WriteLine("   sesuai dengan kelas tempat method itu didefinisikan, atau");
Console.WriteLine("   menggunakan downcast ((Subkelas)variabel).");

Console.WriteLine("\n================ SELESAI ================");
