

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

content = input("Masukkan Teks: ")
client = Groq()
completion1 = client.chat.completions.create(
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
    temperature=0.1
)

completion2 = client.chat.completions.create(
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
    temperature=0.7
)

completion3 = client.chat.completions.create(
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
    temperature=1.2
)

print("="*50)

print("temperature=0.1:")
print(completion1.choices[0].message.content)
print("--------------------------------\n")
print("temperature=0.7:")
print(completion2.choices[0].message.content)
print("--------------------------------\n")
print("temperature=1.2:")
print(completion3.choices[0].message.content)
print("--------------------------------\n")

print("tokens temperature=0.1")
print("Prompt tokens:", completion1.usage.prompt_tokens)
print("Completion tokens:", completion1.usage.completion_tokens)
print("Total tokens:", completion1.usage.total_tokens)
print("--------------------------------\n")

print("tokens temperature=0.7")
print("Prompt tokens:", completion2.usage.prompt_tokens)
print("Completion tokens:", completion2.usage.completion_tokens)
print("Total tokens:", completion2.usage.total_tokens)
print("--------------------------------\n")

print("tokens temperature=1.2")
print("Prompt tokens:", completion3.usage.prompt_tokens)
print("Completion tokens:", completion3.usage.completion_tokens)
print("Total tokens:", completion3.usage.total_tokens)
print("--------------------------------\n")
