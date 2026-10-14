namespace SistemRumahSakit;

public class Perawat : TenagaMedis
{
    public Perawat(string nama, int umur, string spesialisasi)
        : base(nama, umur, spesialisasi)
    {
    }

    public void CekPasien(string namaPasien)
    {
        Console.WriteLine($"Perawat {Nama} ({Spesialisasi}) sedang memeriksa keadaan pasien: {namaPasien}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"Perawat {Nama} sedang merawat dan memantau pasien.");
    }
}
