# Tugas A

Proyek ini adalah script Python sederhana untuk merangkum teks menggunakan model **LLaMA 3.3 (70B Versatile)** melalui Groq API. Program ini dibuat secara interaktif sehingga pengguna dapat memasukkan teks panjang (multiline) yang ingin diringkas, lalu membandingkan hasil ringkasan berdasarkan tingkat kreativitas model (*Temperature*).

## Fitur
- **Input Interaktif**: Mendukung input teks panjang (multiline) langsung dari terminal.
- **Eksperimen Temperature**: Menguji 3 tingkat `temperature` (0.1, 0.7, dan 1.2) secara bersamaan untuk melihat pengaruhnya terhadap gaya bahasa dan panjang ringkasan teks.
- **Tracking Token**: Menampilkan jumlah penggunaan token (prompt & completion) untuk tiap pengujian.

## Persiapan

1. **Buat Virtual Environment (Sangat Disarankan)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

3. **Atur API Key**
   Buat file bernama `.env` di dalam folder proyek, lalu isi dengan API Key Groq Anda:
   ```env
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxx
   ```

## Contoh Eksperimen

### Input Teks
> Institut Teknologi Sumatera atau ITERA adalah perguruan tinggi negeri berbasis sains dan teknologi yang terletak di Kecamatan Jati Agung, Lampung Selatan. Kampus ini resmi berdiri pada tahun 2014 sebagai bagian dari upaya pemerintah untuk memperluas pendidikan teknologi berkualitas di luar Pulau Jawa, khususnya di wilayah Sumatera. ITERA dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi yang mendukung pembangunan Sumatera di berbagai sektor seperti energi, infrastruktur, lingkungan, transportasi, dan teknologi informasi. Dalam masa awal pengembangannya, ITERA dibina langsung oleh Institut Teknologi Bandung sehingga memiliki fondasi akademik yang kuat di bidang teknik dan sains. ITERA dikenal sebagai kampus yang memiliki area sangat luas dengan konsep “Smart, Friendly, and Forest Campus.” Lingkungan kampus dipenuhi ruang terbuka hijau, embung, kawasan konservasi, serta bangunan modern yang terus berkembang dari tahun ke tahun. Suasana akademiknya didominasi oleh bidang teknik, teknologi, dan sains, dengan berbagai program studi seperti Teknik Informatika, Teknik Sipil, Teknik Elektro, Teknik Geologi, Arsitektur, Farmasi, Matematika, hingga Sains Data. Mahasiswanya berasal dari berbagai daerah di Sumatera sehingga menciptakan lingkungan yang beragam dan dinamis. Sebagai kampus yang masih tergolong muda, ITERA berkembang sangat cepat baik dari segi jumlah mahasiswa, fasilitas, maupun kegiatan riset. Kampus ini memiliki visi untuk menjadi institut teknologi terbaik di Sumatera dan mampu bersaing secara nasional. Selain fokus pada pendidikan akademik, ITERA juga menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial. Dengan kombinasi antara lingkungan kampus yang luas, fokus pada teknologi modern, serta semangat pembangunan daerah, ITERA menjadi salah satu perguruan tinggi yang memiliki potensi besar dalam mencetak generasi muda unggul di bidang sains dan teknologi.

### Hasil Eksperimen Berdasarkan Temperature

#### Temperature = 0.1 
> Berikut adalah ringkasan konten tentang Institut Teknologi Sumatera (ITERA):
>
> ITERA adalah perguruan tinggi negeri di Lampung Selatan yang berdiri pada tahun 2014. Kampus ini dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi untuk mendukung pembangunan Sumatera. ITERA memiliki konsep "Smart, Friendly, and Forest Campus" dengan lingkungan kampus yang luas dan modern. Kampus ini menawarkan berbagai program studi di bidang teknik, teknologi, dan sains, serta memiliki visi untuk menjadi institut teknologi terbaik di Sumatera. ITERA juga menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial. Dengan kombinasi antara lingkungan kampus yang luas dan fokus pada teknologi modern, ITERA memiliki potensi besar dalam mencetak generasi muda unggul di bidang sains dan teknologi.

#### Temperature = 0.7 
> Berikut adalah ringkasan dari konten tersebut:
>
> Institut Teknologi Sumatera (ITERA) adalah perguruan tinggi negeri di Lampung Selatan yang berfokus pada sains dan teknologi. ITERA didirikan pada tahun 2014 dan dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi untuk mendukung pembangunan Sumatera. Kampus ini memiliki area yang luas dengan konsep "Smart, Friendly, and Forest Campus" dan menawarkan berbagai program studi di bidang teknik, teknologi, dan sains. ITERA memiliki visi untuk menjadi institut teknologi terbaik di Sumatera dan mampu bersaing secara nasional, serta menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial.

#### Temperature = 1.2 
> Berikut adalah ringkasan dari konten tersebut:
>
> Institut Teknologi Sumatera (ITERA) adalah perguruan tinggi negeri yang terletak di Lampung Selatan, didirikan pada tahun 2014. ITERA difokuskan pada pendidikan teknologi berkualitas dan memiliki visi untuk menjadi institut teknologi terbaik di Sumatera. Kampus ini dikenal dengan lingkungan yang luas dan modern, serta memiliki berbagai program studi di bidang teknik, teknologi, dan sains. ITERA memiliki potensi besar dalam mencetak generasi muda unggul di bidang sains dan teknologi melalui kombinasi antara pendidikan akademik, organisasi, penelitian, inovasi, dan kegiatan sosial.

### Penggunaan Token

| Temperature | Prompt Tokens | Completion Tokens | Total Tokens |
|:---:|:---:|:---:|:---:|
| **0.1** | 660 | 228 | 888 |
| **0.7** | 660 | 193 | 853 |
| **1.2** | 660 | 172 | 832 |

Terlihat bahwa meskipun prompt tokens selalu sama, completion tokens dapat berbeda-beda. Pada kasus teks ITERA ini, temperature yang lebih tinggi (1.2) menghasilkan teks yang sedikit lebih ringkas (172 tokens), sedangkan temperature rendah (0.1) lebih cenderung mengambil banyak kalimat secara utuh (228 tokens).

# Tugas B

RAG (Retrieval Augmented Generation) digunakan untuk menghasilkan jawaban terkait deskripsi ITERA dengan memanfaatkan model `llama-3.1-8b-instant`. Cara kerja RAG pada sistem ini adalah sebagai berikut.

1. Pengguna terlebih dahulu membuat dokumen corpus yang berisi konten terkait ITERA. Seluruh corpus tersebut kemudian diubah menjadi representasi vektor (embedding) menggunakan model `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` dengan bantuan library `SentenceTransformer`.

2. Vektor embedding yang telah dihasilkan kemudian disimpan ke dalam database vektor FAISS agar proses pencarian semantic similarity dapat dilakukan dengan cepat dan efisien.

3. Ketika pengguna memberikan query atau pertanyaan, sistem akan melakukan pencarian kemiripan terhadap embedding yang ada di database vektor. Dari hasil pencarian tersebut, sistem mengambil Top-3 dokumen yang paling relevan dengan query pengguna.

4. Semakin tinggi urutan hasil retrieval, maka semakin relevan dokumen tersebut terhadap pertanyaan yang diberikan. Dokumen dengan peringkat tertinggi kemudian diambil sebagai context dan dikirim kembali ke LLM bersama query pengguna.

5. LLM selanjutnya menghasilkan jawaban yang lebih natural, kontekstual, dan mudah dipahami dibandingkan jika hasil retrieval hanya ditampilkan secara mentah tanpa proses generasi bahasa alami.

# Tugas C

Proyek ini adalah script Python sederhana untuk membandingkan dengan menggunakan uji chain-of-thought dan tanpa uji chain-of-thoght dan melihat streotip yang muncul ketika dijalankan di llm dengan menggunakan model **LLaMA 3.3 (70B Versatile)** melalui Groq API. 

## hasil Eksperimen
Berdasarkan hasil pengujian, model LLM menghasilkan beberapa stereotip profesi berupa generalisasi tugas dan karakteristik umum dari suatu pekerjaan. Namun, model tidak menunjukkan bias gender secara eksplisit karena tidak mengasosiasikan profesi tertentu dengan laki-laki maupun perempuan. Bias yang muncul lebih berupa occupational streotip dibanding gender streotip.

## hasil menggunakan cot

Baik, mari kita pecah langkah demi langkah:

1. Budi awalnya memiliki 20 permen.
2. Ia memberikan setengahnya (20 / 2 = 10 permen) kepada Ani, sehingga Budi memiliki 20 - 10 = 10 permen.
3. Kemudian, Budi membeli lagi 8 permen, sehingga total permen yang dimilikinya sekarang adalah 10 + 8 = 18 permen.

Jadi, Budi sekarang memiliki 18 permen.

Untuk mengetahui lama perjalanan, kita perlu menghitung selisih antara waktu tiba dan waktu berangkat.

Waktu berangkat: 08.00
Waktu tiba: 11.30

Selisih waktu = Waktu tiba - Waktu berangkat
= 11.30 - 08.00
= 3 jam 30 menit

Jadi, lama perjalanan kereta adalah 3 jam 30 menit.

    Mari berpikir langkah demi langkah untuk menjawab pertanyaan ini.

    1. Semua kucing adalah hewan.
    2. Milo adalah kucing.
    3. Karena Milo adalah kucing dan semua kucing adalah hewan, maka Milo juga adalah hewan.

    Jadi, jawaban pertanyaan tersebut adalah: Milo adalah hewan.

## hasil tanpa cot
```text
14 permen.

3,5 jam

hewan.

## Perhitungan Akurasi

### Tanpa CoT

Jumlah jawaban benar = 2  
Total soal = 3  

Rumus akurasi:
```text
Akurasi = (Jumlah Benar / Total Soal) × 100%
```

Perhitungan:
```text
Akurasi = (2 / 3) × 100%
         = 66.7%
```

### Dengan CoT

Jumlah jawaban benar = 3  
Total soal = 3  
```text
Akurasi = (3 / 3) × 100%
         = 100%
```
