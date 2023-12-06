import tkinter as tk
from gtts import gTTS


def teks_ke_suara():
    # Ambil teks dari entry
    teks = text_entry.get()
    # Ambil bahasa dari entry
    bahasa = language_entry.get()
    # Buat objek TTS
    tts = gTTS(teks, lang='id')  # Changed 'lang=bahasa' to 'lang='id'
    # Simpan file audio
    tts.save('output.mp3')
    # Buat jendela pemutar audio
    player = tk.Tk()
    player.title('Teks ke Suara')
    # Tampilkan label pemutaran
    player_label = tk.Label(player, text='Memutar audio...')
    player_label.pack()
    # Jalankan jendela pemutar
    player.mainloop()


root = tk.Tk()
root.title('Teks ke Suara')

# Label teks
text_label = tk.Label(root, text='Masukkan teks:')
text_label.pack()

# Entry teks
text_entry = tk.Entry(root)
text_entry.pack()

# Label bahasa
language_label = tk.Label(root, text='Masukkan bahasa:')
language_label.pack()

# Entry bahasa
language_entry = tk.Entry(root)
language_entry.pack()

# Tombol putar
speak_button = tk.Button(root, text='Bicara', command=teks_ke_suara)
speak_button.pack()

root.mainloop()
