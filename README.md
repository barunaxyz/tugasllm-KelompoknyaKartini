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

## Contoh Eksperimen (Tugas A)

### Input Teks
> Institut Teknologi Sumatera atau ITERA adalah perguruan tinggi negeri berbasis sains dan teknologi yang terletak di Kecamatan Jati Agung, Lampung Selatan. Kampus ini resmi berdiri pada tahun 2014 sebagai bagian dari upaya pemerintah untuk memperluas pendidikan teknologi berkualitas di luar Pulau Jawa, khususnya di wilayah Sumatera. ITERA dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi yang mendukung pembangunan Sumatera di berbagai sektor seperti energi, infrastruktur, lingkungan, transportasi, dan teknologi informasi. Dalam masa awal pengembangannya, ITERA dibina langsung oleh Institut Teknologi Bandung sehingga memiliki fondasi akademik yang kuat di bidang teknik dan sains. ITERA dikenal sebagai kampus yang memiliki area sangat luas dengan konsep “Smart, Friendly, and Forest Campus.” Lingkungan kampus dipenuhi ruang terbuka hijau, embung, kawasan konservasi, serta bangunan modern yang terus berkembang dari tahun ke tahun. Suasana akademiknya didominasi oleh bidang teknik, teknologi, dan sains, dengan berbagai program studi seperti Teknik Informatika, Teknik Sipil, Teknik Elektro, Teknik Geologi, Arsitektur, Farmasi, Matematika, hingga Sains Data. Mahasiswanya berasal dari berbagai daerah di Sumatera sehingga menciptakan lingkungan yang beragam dan dinamis. Sebagai kampus yang masih tergolong muda, ITERA berkembang sangat cepat baik dari segi jumlah mahasiswa, fasilitas, maupun kegiatan riset. Kampus ini memiliki visi untuk menjadi institut teknologi terbaik di Sumatera dan mampu bersaing secara nasional. Selain fokus pada pendidikan akademik, ITERA juga menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial. Dengan kombinasi antara lingkungan kampus yang luas, fokus pada teknologi modern, serta semangat pembangunan daerah, ITERA menjadi salah satu perguruan tinggi yang memiliki potensi besar dalam mencetak generasi muda unggul di bidang sains dan teknologi.

### Hasil Eksperimen Berdasarkan Temperature

#### Temperature = 0.1 (Faktual & Konsisten)
> Berikut adalah ringkasan konten tentang Institut Teknologi Sumatera (ITERA):
>
> ITERA adalah perguruan tinggi negeri di Lampung Selatan yang berdiri pada tahun 2014. Kampus ini dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi untuk mendukung pembangunan Sumatera. ITERA memiliki konsep "Smart, Friendly, and Forest Campus" dengan lingkungan kampus yang luas dan modern. Kampus ini menawarkan berbagai program studi di bidang teknik, teknologi, dan sains, serta memiliki visi untuk menjadi institut teknologi terbaik di Sumatera. ITERA juga menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial. Dengan kombinasi antara lingkungan kampus yang luas dan fokus pada teknologi modern, ITERA memiliki potensi besar dalam mencetak generasi muda unggul di bidang sains dan teknologi.

#### Temperature = 0.7 (Seimbang)
> Berikut adalah ringkasan dari konten tersebut:
>
> Institut Teknologi Sumatera (ITERA) adalah perguruan tinggi negeri di Lampung Selatan yang berfokus pada sains dan teknologi. ITERA didirikan pada tahun 2014 dan dirancang sebagai pusat pengembangan ilmu pengetahuan, teknologi, dan inovasi untuk mendukung pembangunan Sumatera. Kampus ini memiliki area yang luas dengan konsep "Smart, Friendly, and Forest Campus" dan menawarkan berbagai program studi di bidang teknik, teknologi, dan sains. ITERA memiliki visi untuk menjadi institut teknologi terbaik di Sumatera dan mampu bersaing secara nasional, serta menekankan pengembangan karakter mahasiswa melalui organisasi, penelitian, inovasi, dan kegiatan sosial.

#### Temperature = 1.2 (Kreatif & Lebih Variatif)
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