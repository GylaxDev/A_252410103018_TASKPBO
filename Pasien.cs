namespace SistemRumahSakit;

public class Pasien : Orang
{
    public string Keluhan { get; set; }

    public Pasien(string nama, int umur, string keluhan)
        : base(nama, umur)
    {
        Keluhan = keluhan;
    }

    public void CekKeluhan()
    {
        Console.WriteLine($"{Nama} memiliki keluhan: {Keluhan}");
    }

    public override void Aktivitas()
    {
        Console.WriteLine($"{Nama} (pasien) sedang beristirahat di kamar rumah sakit.");
    }
}
