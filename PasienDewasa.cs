namespace SistemRumahSakit;

public class PasienDewasa : Pasien
{
    public PasienDewasa(string nama, int umur, string keluhan)
        : base(nama, umur, keluhan)
    {
    }

    public void Konsultasi(string namaDokter)
    {
        Console.WriteLine($"{Nama} (pasien dewasa) sedang berkonsultasi dengan {namaDokter}.");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"{Nama} (pasien dewasa) sedang menunggu di ruang tunggu rumah sakit.");
    }
}
