namespace SistemRumahSakit;

/// <summary>
/// Kelas Dokter mewarisi kelas TenagaMedis.
/// </summary>
public class Dokter : TenagaMedis
{
    public Dokter(string nama, int umur, string spesialisasi)
        : base(nama, umur, spesialisasi)
    {
    }

    /// <summary>
    /// Method khusus kelas Dokter untuk mendiagnosa pasien.
    /// </summary>
    public void Diagnosa(string namaPasien)
    {
        Console.WriteLine($"Dokter {Nama} ({Spesialisasi}) sedang mendiagnosa pasien: {namaPasien}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"Dokter {Nama} sedang memeriksa pasien di ruang praktik.");
    }
}
