namespace SistemRumahSakit;

/// <summary>
/// Kelas RumahSakit yang menyimpan koleksi (list) objek Orang.
/// </summary>
public class RumahSakit
{
    private readonly List<Orang> daftarOrang = new();

    /// <summary>
    /// Menambahkan sebuah objek Orang ke dalam rumah sakit.
    /// </summary>
    public void TambahOrang(Orang orang)
    {
        daftarOrang.Add(orang);
        Console.WriteLine($"{orang.Nama} telah ditambahkan ke data rumah sakit.");
    }

    /// <summary>
    /// Menampilkan seluruh data orang yang terdaftar di rumah sakit.
    /// </summary>
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

    /// <summary>
    /// Mengakses koleksi orang (untuk demonstrasi polymorphism).
    /// </summary>
    public List<Orang> GetSemuaOrang() => daftarOrang;
}
