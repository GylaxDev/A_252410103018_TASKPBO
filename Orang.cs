namespace SistemRumahSakit;

/// <summary>
/// Kelas dasar Orang (Induk dari semua kelas dalam sistem rumah sakit).
/// </summary>
public class Orang
{
    public string Nama { get; set; }
    public int Umur { get; set; }

    public Orang(string nama, int umur)
    {
        Nama = nama;
        Umur = umur;
    }

    /// <summary>
    /// Method aktivitas umum. Bersifat virtual agar bisa di-override oleh subclass.
    /// </summary>
    public virtual void Aktivitas()
    {
        Console.WriteLine($"{Nama} ({Umur} tahun) sedang beraktivitas umum.");
    }

    /// <summary>
    /// Menampilkan informasi dasar orang.
    /// </summary>
    public void InfoOrang()
    {
        Console.WriteLine($"Nama: {Nama} | Umur: {Umur}");
    }
}
