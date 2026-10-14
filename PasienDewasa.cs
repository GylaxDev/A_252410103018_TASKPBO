namespace SistemRumahSakit;

/// <summary>
/// Kelas PasienDewasa mewarisi kelas Pasien.
/// </summary>
public class PasienDewasa : Pasien
{
    public PasienDewasa(string nama, int umur, string keluhan)
        : base(nama, umur, keluhan)
    {
    }

    /// <summary>
    /// Method khusus kelas PasienDewasa.
    /// </summary>
    public void Konsultasi(string namaDokter)
    {
        Console.WriteLine($"{Nama} (pasien dewasa) sedang berkonsultasi dengan {namaDokter}.");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"{Nama} (pasien dewasa) sedang menunggu di ruang tunggu rumah sakit.");
    }
}
