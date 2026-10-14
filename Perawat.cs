namespace SistemRumahSakit;

/// <summary>
/// Kelas Perawat mewarisi kelas TenagaMedis.
/// </summary>
public class Perawat : TenagaMedis
{
    public Perawat(string nama, int umur, string spesialisasi)
        : base(nama, umur, spesialisasi)
    {
    }

    /// <summary>
    /// Method khusus kelas Perawat untuk memeriksa keadaan pasien.
    /// </summary>
    public void CekPasien(string namaPasien)
    {
        Console.WriteLine($"Perawat {Nama} ({Spesialisasi}) sedang memeriksa keadaan pasien: {namaPasien}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"Perawat {Nama} sedang merawat dan memantau pasien.");
    }
}
