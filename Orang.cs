namespace SistemRumahSakit;

public class Orang
{
    public string Nama { get; set; }
    public int Umur { get; set; }

    public Orang(string nama, int umur)
    {
        Nama = nama;
        Umur = umur;
    }

    public virtual void Aktivitas()
    {
        Console.WriteLine($"{Nama} ({Umur} tahun) sedang beraktivitas umum.");
    }

    public void InfoOrang()
    {
        Console.WriteLine($"Nama: {Nama} | Umur: {Umur}");
    }
}
