dokumen_itera = [
    """
    Institut Teknologi Sumatera (ITERA) adalah perguruan tinggi negeri yang berada di Provinsi Lampung. ITERA didirikan secara resmi pada tahun 2014 melalui Peraturan Presiden Republik Indonesia Nomor 124 Tahun 2014 pada masa pemerintahan Presiden Susilo Bambang Yudhoyono. Kampus ini dibangun sebagai bagian dari pemerataan pendidikan tinggi berbasis teknologi di Pulau Sumatera dan menjadi salah satu institut teknologi negeri terbesar di wilayah tersebut.
    """,

    """
    Kampus ITERA memiliki luas area sekitar 275 hektar yang berlokasi di Kecamatan Jati Agung, Kabupaten Lampung Selatan. Dengan area yang sangat luas, ITERA mengembangkan konsep smart campus dan eco campus yang mengintegrasikan pendidikan, penelitian, teknologi, serta pelestarian lingkungan dalam satu kawasan terpadu.
    """,

    """
    ITERA memiliki beberapa fakultas utama, di antaranya Fakultas Sains (FS), Fakultas Teknologi Infrastruktur dan Kewilayahan (FTIK), dan Fakultas Teknologi Industri (FTI). Fakultas-fakultas ini menaungi berbagai program studi yang berfokus pada pengembangan teknologi, sains, rekayasa, dan perencanaan wilayah untuk mendukung pembangunan Sumatera.
    """,

    """
    Fakultas Sains (FS) di ITERA memiliki berbagai program studi seperti Biologi, Fisika, Kimia, Matematika, Farmasi, Sains Data, dan Sains Atmosfer dan Keplanetan. Fakultas ini berfokus pada pengembangan ilmu pengetahuan dasar, analisis data, dan penelitian ilmiah berbasis laboratorium serta komputasi modern.
    """,

    """
    Fakultas Teknologi Industri (FTI) ITERA menaungi program studi seperti Teknik Elektro, Teknik Mesin, Teknik Kimia, Teknik Material, Teknik Fisika, Teknik Biomedis, Teknik Biosistem, Teknologi Pangan, dan Rekayasa Kosmetik. Fakultas ini berorientasi pada pengembangan industri, manufaktur, energi, dan teknologi terapan untuk kebutuhan industri nasional.
    """,

    """
    Fakultas Teknologi Infrastruktur dan Kewilayahan (FTIK) ITERA memiliki program studi seperti Teknik Sipil, Teknik Lingkungan, Arsitektur, dan Perencanaan Wilayah dan Kota (PWK). Fakultas ini berfokus pada pembangunan infrastruktur, tata ruang wilayah, pengelolaan lingkungan, serta pengembangan kawasan perkotaan dan regional.
    """,

    """
    ITERA juga memiliki program studi kebumian dan energi seperti Teknik Geologi dan Teknik Pertambangan yang mendukung eksplorasi sumber daya alam di Sumatera. Program studi ini mempelajari geologi, mineral, energi, mitigasi bencana, dan teknologi pertambangan modern berbasis keberlanjutan lingkungan.
    """,

    """
    Salah satu ikon penting kampus ITERA adalah Kebun Raya ITERA yang dikembangkan sebagai kawasan konservasi, penelitian, dan edukasi lingkungan. Kebun raya ini menjadi pusat pelestarian flora khas Sumatera serta dimanfaatkan untuk penelitian biodiversitas, ekologi, dan pengembangan tanaman tropis oleh mahasiswa dan dosen.
    """,

    """
    Kebun Raya ITERA memiliki fungsi tidak hanya sebagai ruang hijau kampus, tetapi juga sebagai laboratorium alam terbuka. Kawasan ini mendukung penelitian mengenai tumbuhan endemik, konservasi air, ekosistem rawa, dan pengembangan energi berkelanjutan yang selaras dengan konsep eco campus ITERA.
    """,

    """
    Sejak berdiri, ITERA terus berkembang dengan penambahan fasilitas seperti laboratorium modern, pusat riset, asrama mahasiswa, observatorium, dan kawasan teknologi terpadu. Kampus ini memiliki visi menjadi institut teknologi unggul di Sumatera yang mampu menghasilkan lulusan inovatif, adaptif, dan berdaya saing global dalam bidang sains dan teknologi.
    """
]

from groq import Groq
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

client = Groq(api_key="API_KEY")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embed = model.encode(
    dokumen_itera,
    convert_to_numpy = True,
    show_progress_bar=True
)

embeddings = embed.astype("float32")
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(
    index,
    "itera_faiss.index"
)

# Retrieval and Generated

query = "ada berapa banyak fakultas di ITERA"
top_k = 3
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
).astype("float32")
distances, indices = index.search(
    query_embedding,
    top_k
)
rank_1_idx = indices[0][0]
rank_1_context = dokumen_itera[rank_1_idx]

prompt = f"""
Kamu adalah asisten RAG yang mempunyai ilmu tentang ITERA.
Jawab pertanyaan user hanya berdasarkan context berikut.

Context:
{rank_1_context}

Pertanyaan:
{query}

Jawaban:
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "Jawab dengan singkat, jelas, dan hanya berdasarkan context."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2
)

answer = response.choices[0].message.content

print("Jawaban RAG")
print(answer)