# Tugas C

Proyek ini adalah script Python sederhana untuk membandingkan dengan menggunakan uji chain-of-thought dan tanpa uji chain-of-thoght dan melihat streotip yang muncul ketika dijalankan di llm dengan menggunakan model **LLaMA 3.3 (70B Versatile)** melalui Groq API. 

## hasil Eksperimen
Berdasarkan hasil pengujian, model LLM menghasilkan beberapa stereotip profesi berupa generalisasi tugas dan karakteristik umum dari suatu pekerjaan. Namun, model tidak menunjukkan bias gender secara eksplisit karena tidak mengasosiasikan profesi tertentu dengan laki-laki maupun perempuan. Bias yang muncul lebih berupa occupational streotip dibanding gender streotip.

## hasil menggunakan cot
============================================================
Baik, mari kita pecah langkah demi langkah:

1. Budi awalnya memiliki 20 permen.
2. Ia memberikan setengahnya (20 / 2 = 10 permen) kepada Ani, sehingga Budi memiliki 20 - 10 = 10 permen.
3. Kemudian, Budi membeli lagi 8 permen, sehingga total permen yang dimilikinya sekarang adalah 10 + 8 = 18 permen.

Jadi, Budi sekarang memiliki 18 permen.
============================================================
Untuk mengetahui lama perjalanan, kita perlu menghitung selisih antara waktu tiba dan waktu berangkat.

Waktu berangkat: 08.00
Waktu tiba: 11.30

Selisih waktu = Waktu tiba - Waktu berangkat
= 11.30 - 08.00
= 3 jam 30 menit

Jadi, lama perjalanan kereta adalah 3 jam 30 menit.
============================================================
    Mari berpikir langkah demi langkah untuk menjawab pertanyaan ini.

    1. Semua kucing adalah hewan.
    2. Milo adalah kucing.
    3. Karena Milo adalah kucing dan semua kucing adalah hewan, maka Milo juga adalah hewan.

    Jadi, jawaban pertanyaan tersebut adalah: Milo adalah hewan.

## hasil tanpa cot

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
