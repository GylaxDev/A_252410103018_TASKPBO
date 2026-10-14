namespace SistemRumahSakit;

public class RumahSakit
{
    private readonly List<Orang> daftarOrang = new();

    public void TambahOrang(Orang orang)
    {
        daftarOrang.Add(orang);
        Console.WriteLine($"{orang.Nama} telah ditambahkan ke data rumah sakit.");
    }

    public void DaftarOrang()
    {
        Console.WriteLine();
        Console.WriteLine("=== DAFTAR SELURUH ORANG DI RUMAH SAKIT ===");
        foreach (var orang in daftarOrang)
        {
            orang.InfoOrang();
        }
        Console.WriteLine("===========================================");
    }

    public List<Orang> GetSemuaOrang() => daftarOrang;
}
