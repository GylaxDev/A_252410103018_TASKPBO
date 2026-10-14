# -*- coding: utf-8 -*-
"""Generate HTML report, then print to PDF with Edge headless."""
import html
import os
import re
import subprocess

BASE = r"C:\Users\Vincent\Downloads\SistemRumahSakit"
REPORT = os.path.join(BASE, "Report")
OUT_HTML = os.path.join(REPORT, "report.html")
OUT_PDF = os.path.join(REPORT, "Laporan_Tugas_PBO_SistemRumahSakit.pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ---------------------------------------------------------------- reading inputs
def read(path, enc="utf-8"):
    with open(path, "r", encoding=enc) as f:
        return f.read()

source_files = ["Orang.cs", "Pasien.cs", "TenagaMedis.cs", "Dokter.cs",
                "Perawat.cs", "PasienAnak.cs", "PasienDewasa.cs",
                "RumahSakit.cs", "Program.cs"]
sources = {name: read(os.path.join(BASE, name)) for name in source_files}
hierarchy = read(os.path.join(REPORT, "_hierarchy.txt"))
program_output = read(os.path.join(REPORT, "output.txt"), enc="utf-8-sig").rstrip("\n")

# ---------------------------------------------------------------- C# highlighter
KEYWORDS = {
    "public", "private", "protected", "internal", "class", "static", "void",
    "string", "int", "bool", "double", "new", "override", "virtual", "using",
    "namespace", "readonly", "const", "if", "else", "foreach", "for", "while",
    "return", "base", "this", "true", "false", "var", "get", "set", "partial",
}
KNOWN_TYPES = {
    "Orang", "Pasien", "TenagaMedis", "Dokter", "Perawat", "PasienAnak",
    "PasienDewasa", "RumahSakit", "List", "Console", "Encoding", "StringComparison",
}
CONTROL_KEYWORDS = {"if", "else", "foreach", "for", "while", "return", "new"}

TOKEN_RE = re.compile(r"""
    (?P<comment>//[^\n]*|/\*.*?\*/|///[^\n]*)
  | (?P<string>"(?:[^"\\\n]|\\.)*")
  | (?P<number>\b\d+(\.\d+)?\b)
  | (?P<ident>[A-Za-z_][A-Za-z0-9_]*)
  | (?P<punct>[{}()\[\];,.<>=+\-*/%!&|^~?:])
""", re.VERBOSE | re.DOTALL)


def tokenize_csharp(code):
    out = []
    pos = 0
    for m in TOKEN_RE.finditer(code):
        if m.start() > pos:
            out.append(("text", code[pos:m.start()]))
        kind = m.lastgroup
        val = m.group()
        if kind == "comment":
            out.append(("cmt", val))
        elif kind == "string":
            out.append(("str", val))
        elif kind == "number":
            out.append(("num", val))
        elif kind == "ident":
            if val in CONTROL_KEYWORDS:
                out.append(("kw", val))
            elif val in KEYWORDS:
                out.append(("kw", val))
            elif val in KNOWN_TYPES:
                out.append(("typ", val))
            else:
                out.append(("txt", val))
        else:
            out.append(("txt", val))
        pos = m.end()
    if pos < len(code):
        out.append(("text", code[pos:]))
    return out


def highlight_csharp(code):
    """Return HTML with syntax colors. Newlines preserved as \n."""
    tokens = tokenize_csharp(code)
    cls = {"cmt": "c", "str": "s", "num": "n", "kw": "k", "typ": "t"}
    parts = []
    for kind, val in tokens:
        esc = html.escape(val)
        if kind in cls:
            parts.append(f'<span class="{cls[kind]}">{esc}</span>')
        else:
            parts.append(esc)
    return "".join(parts)


def code_block_html(code, line_numbers=True):
    code = code.rstrip("\n")
    lines = code.split("\n")
    wrapped = []
    for ln in lines:
        while len(ln) > 100:
            wrapped.append(ln[:100])
            ln = "        " + ln[100:]
        wrapped.append(ln)
    rows = []
    for i, ln in enumerate(wrapped, 1):
        rows.append(
            f'<div class="cl"><span class="ln">{i if line_numbers else ""}</span>'
            f'<span class="cc">{highlight_csharp(ln)}</span></div>'
        )
    return '<div class="codeblock">' + "".join(rows) + "</div>"


def plain_block(text, numbers=True):
    lines = text.rstrip("\n").split("\n")
    rows = []
    for i, ln in enumerate(lines, 1):
        esc = html.escape(ln.replace("\t", "    ")).replace(" ", "&nbsp;")
        rows.append(f'<div class="cl"><span class="ln">{i if numbers else ""}</span>'
                    f'<span class="cc">{esc}</span></div>')
    return '<div class="codeblock out">' + "".join(rows) + "</div>"


# ---------------------------------------------------------------- CSS
CSS = """
@page { size: A4; margin: 16mm 14mm 14mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", Arial, sans-serif; color: #222; font-size: 11pt;
       line-height: 1.55; margin: 0; }
h1.cover-title { font-size: 25pt; color: #1F3864; text-align: center; margin: 0; line-height: 1.4; }
h2.bab { background: #1F3864; color: #fff; padding: 8px 12px; border-radius: 3px;
         font-size: 14pt; margin: 0 0 12px 0; page-break-after: avoid; }
h3.sec { background: #2E5AA8; color: #fff; padding: 5px 10px; border-radius: 3px;
         font-size: 11.5pt; margin: 14px 0 8px 0; page-break-after: avoid; }
p { margin: 6px 0; text-align: justify; }
.cover { text-align: center; padding-top: 150px; page-break-after: always; }
.cover h1.big { font-size: 30pt; color: #1F3864; margin: 6px 0 0 0; }
.cover .subtitle { color: #666; font-size: 13pt; margin-top: 16px; }
.cover .rule { width: 220px; height: 3px; background: #2E5AA8; margin: 26px auto; }
table.ident { margin: 40px auto 0 auto; border-collapse: collapse; font-size: 12pt; }
table.ident td { padding: 6px 10px; text-align: left; }
table.ident td.lab { color: #1F3864; font-weight: 600; }
table.ident td.dots { color: #1F3864; letter-spacing: 2px; }
.cover .foot { margin-top: 120px; color: #777; font-size: 9.5pt; }
.codeblock { font-family: Consolas, "Courier New", monospace; font-size: 8.9pt;
             background: #F5F6F8; border: 1px solid #DFE2E8; border-radius: 4px;
             padding: 6px 0; margin: 4px 0 10px 0; page-break-inside: auto; }
.codeblock.out { background: #FAFAFA; }
.cl { display: flex; padding: 0 10px; page-break-inside: avoid; }
.ln { width: 34px; min-width: 34px; text-align: right; color: #B0B6BF;
      user-select: none; padding-right: 12px; }
.cc { white-space: pre; }
.c { color: #57A64A; font-style: italic; }
.s { color: #A31515; }
.k { color: #0000FF; }
.t { color: #267F99; }
.n { color: #098658; }
table.summary { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.5pt; }
table.summary th { background: #1F3864; color: #fff; padding: 5px 8px; border: 1px solid #1F3864; text-align: center; }
table.summary td { border: 1px solid #C3CBD9; padding: 4px 8px; }
table.summary tr:nth-child(even) td { background: #EDF2FA; }
table.summary td.mono { font-family: Consolas, monospace; }
table.qa { border-collapse: collapse; width: 100%; margin: 10px 0 14px 0; font-size: 10pt; }
table.qa td, table.qa th { border: 1px solid #9AA6C0; vertical-align: top; padding: 7px 9px; }
table.qa th.qhead { background: #1F3864; color: #fff; text-align: left; font-size: 10.5pt; }
table.qa td.q { width: 57mm; background: #E9F0FA; color: #1F3864; font-weight: 600; }
table.qa td.a { background: #fff; text-align: justify; }
table.qa ol, table.qa ul { margin: 4px 0 4px 18px; padding: 0; }
.note { background: #FFF8E1; border-left: 4px solid #F2B705; padding: 8px 12px; margin: 10px 0; font-size: 10pt; }
.newpage { page-break-before: always; }
"""

# ---------------------------------------------------------------- answers content
ANSWERS = [
    {
        "q": "Jalankan method Aktivitas() pada objek Dokter dan Pasien. "
             "Apa yang terjadi? Mengapa demikian?",
        "a": """<p><b>Yang terjadi:</b> method Aktivitas() yang dijalankan adalah versi
        <i>override</i> milik kelas <b>Dokter</b> (menampilkan
        &ldquo;Dokter ... sedang memeriksa pasien di ruang praktik&rdquo;) dan versi
        <i>override</i> milik kelas <b>Pasien</b> (&ldquo;... sedang beristirahat di kamar
        rumah sakit&rdquo;), <b>bukan</b> versi dari kelas Orang.</p>
        <p><b>Mengapa demikian:</b> karena method Aktivitas() pada kelas Orang dideklarasikan
        dengan keyword <b>virtual</b>, lalu di-<i>override</i> di setiap subclass. Saat
        program dijalankan, C# melakukan <i>dynamic dispatch</i> (late binding):
        pemilihan method dilakukan berdasarkan <b>tipe objek sebenarnya saat runtime</b>,
        bukan tipe variabelnya. Inilah konsep <b>polymorphism</b> (banyak rupa) dalam PBO.</p>""",
    },
    {
        "q": "Jalankan method Diagnosa() pada objek Dokter. Apa yang terjadi? Mengapa demikian?",
        "a": """<p><b>Yang terjadi:</b> method Diagnosa() berjalan normal dan menampilkan
        informasi bahwa dokter sedang mendiagnosa pasien.</p>
        <p><b>Mengapa demikian:</b> karena method Diagnosa() didefinisikan langsung di dalam
        kelas <b>Dokter</b>, dan objek yang digunakan (dokter1) bertipe Dokter. Karena tipe
        variabel sama dengan kelas tempat method didefinisikan, method tersebut dapat
        dipanggil langsung.</p>
        <p>Sebaliknya, jika objek tersebut disimpan dalam variabel bertipe Orang atau
        TenagaMedis, maka Diagnosa() <b>tidak bisa</b> dipanggil tanpa <i>downcast</i>,
        misalnya: <code>((Dokter)variabel).Diagnosa(...)</code>.</p>""",
    },
    {
        "q": "Dapatkah Anda menampilkan informasi lengkap (nama, umur, spesialisasi) dari objek "
             "Dokter? Bagaimana caranya?",
        "a": """<p><b>Ya, bisa.</b> Caranya sebagai berikut:</p>
        <ol>
        <li>Memanggil method <code>InfoOrang()</code> (warisan dari kelas Orang) untuk
        menampilkan nama dan umur, lalu memanggil <code>CekSpesialis()</code> (warisan dari
        kelas TenagaMedis) untuk menampilkan spesialisasi.</li>
        <li>Mengakses properti secara langsung: <code>dokter.Nama</code>,
        <code>dokter.Umur</code>, dan <code>dokter.Spesialisasi</code>.</li>
        <li>Jika objek disimpan dalam variabel bertipe Orang, gunakan <i>downcast</i>,
        misalnya <code>((TenagaMedis)orang).CekSpesialis()</code>.</li>
        <li>Alternatif lain: membuat method baru, misalnya <code>InfoLengkap()</code>, di
        kelas Dokter yang menggabungkan seluruh informasi tersebut dalam satu method.</li>
        </ol>""",
    },
    {
        "q": "Jalankan method Menangis() pada objek PasienAnak. Apa yang terjadi? Mengapa demikian?",
        "a": """<p><b>Yang terjadi:</b> method Menangis() berjalan normal dan menampilkan
        aktivitas menangis dari pasien anak.</p>
        <p><b>Mengapa demikian:</b> karena method Menangis() didefinisikan di kelas
        <b>PasienAnak</b>, dan objek yang digunakan bertipe PasienAnak, sehingga objek
        langsung memiliki akses ke method tersebut. Jika objek disimpan dalam variabel
        bertipe Pasien atau Orang, method Menangis() tidak bisa dipanggil tanpa
        <i>downcast</i> ke PasienAnak.</p>""",
    },
    {
        "q": "Buatlah variabel bertipe Orang, lalu isi dengan objek Perawat. Jalankan method "
             "Aktivitas(). Apa yang terjadi? Mengapa demikian?",
        "a": """<p><b>Yang terjadi:</b> yang dijalankan adalah Aktivitas() versi
        <b>Perawat</b> (&ldquo;Perawat ... sedang merawat dan memantau pasien&rdquo;),
        <b>BUKAN</b> versi kelas Orang.</p>
        <p><b>Mengapa demikian:</b> variabel bertipe Orang diperbolehkan menyimpan objek
        subclass apa pun (<i>upcasting</i>). Karena Aktivitas() bersifat <b>virtual</b> dan
        telah di-<i>override</i> oleh kelas Perawat, C# melakukan <i>dynamic dispatch</i>:
        method yang dipilih ditentukan oleh <b>tipe objek sebenarnya saat runtime</b>
        (Perawat), bukan tipe variabel saat compile time (Orang).</p>
        <p><b>Catatan:</b> method khusus Perawat seperti <code>CekPasien()</code> tidak dapat
        dipanggil langsung dari variabel bertipe Orang; harus menggunakan <i>downcast</i>:
        <code>((Perawat)orang).CekPasien(...)</code>.</p>""",
    },
    {
        "q": "Kesimpulan apa yang dapat Anda ambil?",
        "a": """<ol>
        <li><b>Inheritance (pewarisan)</b> memungkinkan subclass menggunakan kembali properti
        dan method dari superclass, sehingga program lebih ringkas, terstruktur, dan mudah
        dikembangkan.</li>
        <li><b>Polymorphism (virtual + override)</b> membuat method yang sama dapat berperilaku
        berbeda sesuai objek sebenarnya, meskipun dipanggil melalui variabel bertipe induk.
        Contohnya <code>List&lt;Orang&gt;</code> dapat menampung objek Dokter, Perawat, dan
        Pasien sekaligus.</li>
        <li>Method khusus subclass hanya dapat diakses bila tipe variabel sesuai dengan kelas
        tempat method itu didefinisikan, atau dengan menggunakan <i>downcast</i>.</li>
        <li>Pewarisan bertingkat (multilevel inheritance) memperjelas hierarki sistem:
        Orang &rarr; TenagaMedis &rarr; Dokter/Perawat, dan
        Orang &rarr; Pasien &rarr; PasienAnak/PasienDewasa.</li>
        </ol>""",
    },
]

# ---------------------------------------------------------------- build html
H = []
H.append("""<!DOCTYPE html>
<html lang="id"><head><meta charset="utf-8">
<title>Laporan Tugas PBO - Sistem Rumah Sakit</title>
<style>""" + CSS + """</style></head><body>""")

# ---- cover
H.append("""
<div class="cover">
  <div style="font-size:26pt;color:#1F3864;font-weight:700;">LAPORAN TUGAS<br>
  PEMROGRAMAN BERBASIS OBJEK</div>
  <div class="rule"></div>
  <h1 class="big">SISTEM RUMAH SAKIT</h1>
  <div class="subtitle">Implementasi Inheritance dan Polymorphism dengan C# (.NET)</div>
  <table class="ident">
    <tr><td class="lab">Nama</td><td>:</td><td class="dots">..............................</td></tr>
    <tr><td class="lab">NIM</td><td>:</td><td class="dots">..............................</td></tr>
    <tr><td class="lab">Kelas</td><td>:</td><td>A</td></tr>
    <tr><td class="lab">Link Repository GitHub</td><td>:</td><td class="dots">..............................</td></tr>
  </table>
  <div class="foot">Dibuat dengan Visual Studio / .NET SDK 10 &nbsp;&bull;&nbsp;
  Bahasa pemrograman C#<br>
  Nama Repository: KELAS_NIM_TASKPBO (public) &nbsp;&bull;&nbsp;
  Link Pengumpulan: https://forms.gle/5KVcRH9JYByq7soc8</div>
</div>
""")

# ---- BAB I
H.append('<div class="newpage"></div><h2 class="bab">BAB I &nbsp; PENDAHULUAN</h2>')
H.append("""<p>Laporan ini menyajikan implementasi program <b>Sistem Rumah Sakit</b> menggunakan
bahasa pemrograman <b>C#</b> pada platform .NET. Program dibuat untuk memenuhi instruksi tugas
Pemrograman Berbasis Objek (PBO), yaitu mengimplementasikan hierarki kelas, pewarisan
(<i>inheritance</i>), <i>override</i> method, <i>polymorphism</i>, serta koleksi objek.</p>
<p>Struktur program terdiri dari kelas dasar <b>Orang</b>, kelas turunan <b>Pasien</b> dan
<b>TenagaMedis</b>, kelas turunan lanjutan (<b>Dokter</b>, <b>Perawat</b>, <b>PasienAnak</b>,
<b>PasienDewasa</b>), serta kelas <b>RumahSakit</b> yang menyimpan koleksi Orang. Method
<b>Main()</b> mendemonstrasikan pembuatan objek, penambahan objek ke rumah sakit, penampilan
data, polymorphism, dan pemanggilan method khusus setiap kelas.</p>""")

H.append('<h3 class="sec">A. Hierarki Kelas (Class Hierarchy)</h3>')
H.append('<div class="codeblock out"><div class="cl"><span class="ln"></span><span class="cc">'
         + html.escape(hierarchy.rstrip("\n")) +
         '</span></div></div>')

H.append('<h3 class="sec">B. Daftar Kelas, Properti, dan Method</h3>')
summary_rows = [
    ("Orang", "-", "Nama, Umur", "Aktivitas() (virtual), InfoOrang()"),
    ("Pasien", "Orang", "Keluhan", "CekKeluhan(), Aktivitas() override"),
    ("TenagaMedis", "Orang", "Spesialisasi", "CekSpesialis(), Aktivitas() override"),
    ("Dokter", "TenagaMedis", "-", "Diagnosa(string), Aktivitas() override"),
    ("Perawat", "TenagaMedis", "-", "CekPasien(string), Aktivitas() override"),
    ("PasienAnak", "Pasien", "-", "Menangis(), Aktivitas() override"),
    ("PasienDewasa", "Pasien", "-", "Konsultasi(string), Aktivitas() override"),
    ("RumahSakit", "-", "List&lt;Orang&gt;", "TambahOrang(Orang), DaftarOrang()"),
]
H.append('<table class="summary"><tr><th>Kelas</th><th>Induk</th>'
         '<th>Properti Tambahan</th><th>Method Khusus (selain warisan)</th></tr>')
for k, parent, props, methods in summary_rows:
    H.append(f'<tr><td class="mono">{k}</td><td class="mono">{parent}</td>'
             f'<td class="mono">{props}</td><td class="mono">{methods}</td></tr>')
H.append("</table>")
H.append("""<div class="note"><b>Catatan:</b> Semua subclass mewarisi properti
<b>Nama</b> dan <b>Umur</b> dari kelas <b>Orang</b>. Method <b>Aktivitas()</b> di-override di
setiap subclass sehingga menghasilkan output berbeda sesuai objek sebenarnya
(<i>polymorphism</i>). Kelas <b>RumahSakit</b> menyimpan koleksi <code>List&lt;Orang&gt;</code>
sehingga dapat menampung objek Dokter, Perawat, PasienAnak, dan PasienDewasa secara
bersama-sama.</div>""")

# ---- BAB II: source code
H.append('<div class="newpage"></div><h2 class="bab">BAB II &nbsp; KODE PROGRAM</h2>')
sections = [
    ("1. Kelas Orang (Induk / Superclass)", "Orang.cs"),
    ("2. Kelas Pasien (Mewarisi Orang)", "Pasien.cs"),
    ("3. Kelas TenagaMedis (Mewarisi Orang)", "TenagaMedis.cs"),
    ("4. Kelas Dokter (Mewarisi TenagaMedis)", "Dokter.cs"),
    ("5. Kelas Perawat (Mewarisi TenagaMedis)", "Perawat.cs"),
    ("6. Kelas PasienAnak (Mewarisi Pasien)", "PasienAnak.cs"),
    ("7. Kelas PasienDewasa (Mewarisi Pasien)", "PasienDewasa.cs"),
    ("8. Kelas RumahSakit (Koleksi Orang)", "RumahSakit.cs"),
    ("9. Program.cs — Method Main() dan Demonstrasi Soal", "Program.cs"),
]
for title, fname in sections:
    H.append(f'<h3 class="sec">{title}</h3>')
    H.append(code_block_html(sources[fname]))

# ---- BAB III: output
H.append('<div class="newpage"></div><h2 class="bab">BAB III &nbsp; OUTPUT PROGRAM</h2>')
H.append("""<p>Berikut adalah hasil keluaran program ketika dijalankan
(<code>dotnet run</code>). Output ini memperlihatkan seluruh langkah yang diminta: pembuatan
objek rumah sakit, pembuatan objek, penambahan objek, penampilan data, demonstrasi
polymorphism, pemanggilan method khusus, serta demonstrasi untuk menjawab Soal 1 sampai
Soal 6.</p>""")
H.append(plain_block(program_output))

# ---- BAB IV: answers
H.append('<div class="newpage"></div><h2 class="bab">BAB IV &nbsp; JAWABAN SOAL-SOAL</h2>')
for i, item in enumerate(ANSWERS, start=1):
    H.append(f"""<table class="qa">
    <tr><th class="qhead" colspan="2">Pertanyaan {i}</th></tr>
    <tr><td class="q">{item["q"]}</td><td class="a">{item["a"]}</td></tr>
    </table>""")

# ---- BAB V: penutup
H.append("""<div class="newpage"></div><h2 class="bab">BAB V &nbsp; PENUTUP</h2>
<p>Seluruh instruksi tugas telah diimplementasikan pada program Sistem Rumah Sakit:
kelas-kelas beserta properti dan method-nya, <i>override</i> method Aktivitas() di setiap
subclass, koleksi Orang pada kelas RumahSakit, serta method Main() yang mendemonstrasikan
pembuatan objek, penambahan objek, penampilan data, polymorphism, dan pemanggilan method
khusus. Demonstrasi untuk menjawab seluruh pertanyaan (Soal 1&ndash;6) juga disertakan di
dalam program dan ditampilkan pada output BAB III laporan ini.</p>
<p>Project diunggah ke repository GitHub dengan nama <b>KELAS_NIM_TASKPBO</b> dengan akses
<b>public</b> sesuai instruksi pengumpulan, dan modul disimpan dalam format PDF agar siap
dikumpulkan melalui tautan: https://forms.gle/5KVcRH9JYByq7soc8</p>""")

H.append("</body></html>")

html_doc = "".join(H)
with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_doc)
print("HTML written:", OUT_HTML, f"({len(html_doc)} bytes)")

# ---------------------------------------------------------------- print to pdf
cmd = [
    EDGE,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--print-to-pdf=" + OUT_PDF,
    "--no-pdf-header-footer",
    "file:///" + OUT_HTML.replace("\\", "/"),
]
if os.path.exists(OUT_PDF):
    os.remove(OUT_PDF)
res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
if os.path.exists(OUT_PDF):
    print("PDF created:", OUT_PDF, f"({os.path.getsize(OUT_PDF)} bytes)")
else:
    print("FAILED")
    print(res.stdout)
    print(res.stderr)
