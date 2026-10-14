namespace SistemRumahSakit;

/// <summary>
/// Kelas PasienAnak mewarisi kelas Pasien.
/// </summary>
public class PasienAnak : Pasien
{
    public PasienAnak(string nama, int umur, string keluhan)
        : base(nama, umur, keluhan)
    {
    }

    /// <summary>
    /// Method khusus kelas PasienAnak.
    /// </summary>
    public void Menangis()
    {
        Console.WriteLine($"{Nama} (pasien anak) sedang menangis: \"Waaa... waaa...\"");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"{Nama} (pasien anak) sedang bermain di ruang bermain rumah sakit.");
    }
}
