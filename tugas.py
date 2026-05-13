

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

content = input("Masukkan Teks: ")
client = Groq()
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "Anda adalah asisten AI yang ahli dalam meringkas teks. Tugas Anda adalah memberikan ringkasan yang padat, jelas, dan akurat dari teks yang diberikan oleh pengguna. Jangan keluar dari konteks tetap pada pembahasa tugas anda hanya meringkas kontem"
        },
        {
            "role": "user",
            "content": f"Tolong ringkas konten berikut ini:\n\n{content}"
        }
    ],
    temperature=2
)


print(completion.choices[0].message.content)