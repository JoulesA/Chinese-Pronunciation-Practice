# 🀄 Chinese Pronunciation Practice (Whisper + Pinyin)

Herramienta en Python para practicar **chino mandarín** usando reconocimiento de voz.
Evalúa tu pronunciación comparando lo que dices con la palabra objetivo mediante **pinyin** y **distancia de Levenshtein**.

---

## 🚀 ¿Qué hace este proyecto?

* 🎤 Graba tu voz desde el micrófono
* 🧠 Usa **Whisper** para transcribir lo que dijiste
* 🔤 Convierte caracteres chinos a **pinyin**
* 📏 Calcula qué tan cerca estuviste usando distancia de Levenshtein
* 🔁 Te da feedback inmediato para mejorar

---

## 🧩 Tecnologías utilizadas

* `whisper` → Speech-to-Text
* `pypinyin` → Conversión a pinyin
* `python-Levenshtein` → Distancia entre cadenas
* `pandas` → Manejo de vocabulario
* `sounddevice` → Grabación de audio

---

## 📦 Instalación

### 1. Clonar repositorio

```bash
git clone <tu-repo>
cd <tu-repo>
```

---

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```


```bash
conda create --name mi_entorno python=3.12  # Conda
conda activate name
```


---

### 3. Instalar dependencias

Ya cuentas con un archivo `requirements.txt`, entonces:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Dependencia importante: FFmpeg

Whisper necesita **FFmpeg** para procesar audio.

### Verificar instalación:

```bash
ffmpeg -version
```

Si no está instalado:

* Windows: descargar desde https://ffmpeg.org/download.html
* Mac:

```bash
brew install ffmpeg
```

* Linux:

```bash
sudo apt install ffmpeg
```

⚠️ Asegúrate de que esté en el PATH.

---

## 📂 Formato del vocabulario

Archivo: `VocabularioChino.csv`

Debe tener columnas como:

```csv
ID,Word,Pronunciation,Meaning,Significado,Context
1,你好,ni hao,Hello,Hola,Formal
2,谢谢,xie xie,Thank you,Gracias,Casual
```

---
Word: Palabra en caracteres chinos
Pronunciation: Palabra en pinyin
Meaning: Traducción al ingles
Significado: Traducción al español
Context: Contexto en el que se le suele usar (Casual, Legal, Industria, Medicina, etc)

## ▶️ Uso

Ejecuta:

```bash
python ChineseePractice.py
```

---

### Flujo:

1. Elige número de palabras
2. Elige tipo de práctica:

   * 1 → Pronunciación
   * 2 → Traducción
   * 3 → Mixto

---

## 🧠 ¿Cómo funciona la evaluación?

1. Dices una palabra
2. Whisper la transcribe
3. Se convierte a pinyin
4. Se compara con la palabra objetivo usando distancia de Levenshtein

Ejemplo:

```
Objetivo: 工作 → gong1 zuo4  
Dicho:    恭祝 → gong1 zhu4  
```

👉 Se calcula la distancia:

```
Distancia de Levenshtein: 2
```

Si está por debajo de un umbral → ✅ correcto

---

## ⚙️ Parámetros ajustables

Dentro del código:

```python
distance <= 7
```

Puedes cambiar ese valor para hacer el sistema:

* más estricto 🔒
* más flexible 🎯

---

## 📌 Funciones principales

### `practice(word)`

Evalúa pronunciación:

* graba audio
* transcribe
* compara con pinyin

---

### `translate(word)`

Evalúa traducción:

* muestra palabra
* usuario escribe significado

---

### `to_pinyin(text)`

Convierte caracteres chinos a pinyin:

```python
工作 → gong1 zuo4
```

---

### `record_audio()`

Graba audio desde micrófono y guarda archivo temporal.

---

## ⚠️ Limitaciones actuales

* ❌ Whisper analiza semánticamente (no fonéticamente)
* ❌ No detecta errores de tono directamente
* ❌ No identifica qué sílaba fallaste

---

## 🚀 Mejoras futuras

* 🔍 Evaluación por sílaba (más precisa)
* 🎯 Detección de errores de tono
* 📊 Score continuo de pronunciación
* 🧠 Uso de embeddings de audio (wav2vec2)
* 🎮 Interfaz tipo app interactiva

---

## 🧪 Ejemplo de salida

```
Palabra: 工作
Pronunciación: gong zuo

Has dicho: gong1 zhu4
Distancia de Levenshtein: 2

Buen trabajo!
```

---

## 🧑‍💻 Autor

Proyecto desarrollado como herramienta para curso de chino:

* reconocimiento de voz
* procesamiento de lenguaje
* aprendizaje de idiomas asistido por IA

---

## 📄 Licencia

MIT (puedes cambiarla si lo necesitas)

---

## 💡 Nota final

Este proyecto no evalúa “pronunciación perfecta”, sino:

👉 qué tan cerca estás de decir correctamente la palabra

Y eso es suficiente para mejorar rápido 🚀
