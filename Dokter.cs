namespace SistemRumahSakit;

public class Dokter : TenagaMedis
{
    public Dokter(string nama, int umur, string spesialisasi)
        : base(nama, umur, spesialisasi)
    {
    }

    public void Diagnosa(string namaPasien)
    {
        Console.WriteLine($"Dokter {Nama} ({Spesialisasi}) sedang mendiagnosa pasien: {namaPasien}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"Dokter {Nama} sedang memeriksa pasien di ruang praktik.");
    }
}
