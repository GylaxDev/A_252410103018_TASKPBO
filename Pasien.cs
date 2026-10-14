namespace SistemRumahSakit;

/// <summary>
/// Kelas Pasien mewarisi kelas Orang.
/// </summary>
public class Pasien : Orang
{
    public string Keluhan { get; set; }

    public Pasien(string nama, int umur, string keluhan)
        : base(nama, umur)
    {
        Keluhan = keluhan;
    }

    /// <summary>
    /// Method khusus kelas Pasien untuk menampilkan keluhan.
    /// </summary>
    public void CekKeluhan()
    {
        Console.WriteLine($"{Nama} memiliki keluhan: {Keluhan}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"{Nama} (pasien) sedang beristirahat di kamar rumah sakit.");
    }
}
