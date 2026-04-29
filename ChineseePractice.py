import Levenshtein
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os
import pandas as pd
import random
import Levenshtein 
from pypinyin import pinyin, Style

# Path Vocabulary
path = "VocabularioChino.csv"

# Load vocabulary as dictionary
# First row: is header, so keep it in mind when accessing data
vocab_df = pd.read_csv(path)

# print(vocab_df.columns)  # Check column names
# print(vocab_df.head())  # Check the first few rows to understand the structure

# Cargar modelo
model = whisper.load_model("small")

# Function to convert Chinese characters to Pinyin
def to_pinyin(chinese):
    pinyin_list = pinyin(chinese, style=Style.TONE3)
    return ' '.join([item[0] for item in pinyin_list]) 


# Speaking practice function
def practice(word):
    incorrect_pronunciation = True
    while incorrect_pronunciation:

        print(f"\nPalabra: {word.Word}")
        print(f"Pronunciación : {word.Pronunciation}")
        input('Presiona Enter para grabar')
        audio_path = record_audio()

        result = model.transcribe(audio_path, language="zh")
        pronunciation = result["text"].strip()

        target = to_pinyin(word.Word)
        pred = to_pinyin(pronunciation)

        print(f"Has dicho: {pred}")

        # Levenshtein distance
        distance = Levenshtein.distance(pred, target)
        print(f"Distancia de Levenshtein: {distance}")


        # Comparación simple
        if distance <= 7:  # Puedes ajustar este umbral según tus necesidades
            print("Buen trabajo!")
            os.remove(audio_path)
            incorrect_pronunciation = False

        else:
            print("Intenta de nuevo...\n")
            os.remove(audio_path)

# Translate function (optional)
def translate(word):
    incorrect_translation = True
    while incorrect_translation:
        print(f"¿Cuál es la traducción de '{word.Word}'?")
        print(f"Pista: {word.Pronunciation}")
        user_translation = input('Tu respuesta: ')

        if user_translation.strip().lower() == word.Meaning.strip().lower():
            print("Correcto!")
            incorrect_translation = False
        else:
            print("Intenta de nuevo...\n")

# Record audio
def record_audio(duration=3, fs=16000):
    print("Grabando...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Grabación lista")

    # Guardar temporalmente
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_file.name, fs, audio)
    return temp_file.name

# ===== MAIN =====
if __name__ == "__main__":
    # Words [write, pronunciation, meaning]
    # [不客气, bu ke qi, You're welcome], [再见, zai jian, Goodbye], [请, qing, Please]]
    # words = [["你好", "ni hao", "Hello"], ["谢谢", "xie xie", "Thank you"], ["中国", "zhong guo", "China"]]

    print("Bienvenido a la práctica de chino mandarín!")
    words2practice = int(input("¿Cuántas palabras quieres practicar? "))

    print('Tipo de practica: 1. Pronunciación, 2. Traducción, 3. Ambas ')
    practice_type = int(input("Selecciona el tipo de práctica (1, 2 o 3): "))

    random_words = vocab_df.sample(n=words2practice)


    for word in random_words.itertuples(index=False):
        print(type(word))
        print(word)
        if practice_type == 1:
            practice(word)
        elif practice_type == 2:
            translate(word)
        else:
            type_of_practice = random.choice([practice, translate])
            type_of_practice(word)

    print("\n Sesión terminada")