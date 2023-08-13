from bark import generate_audio, preload_models, SAMPLE_RATE
from scipy.io.wavfile import write as write_wav
from langdetect import detect
from googletrans import Translator
import os

# Preload the Bark models once during the program start
preload_models()

# List of Bark-supported languages
LANGUAGES = {
    "English": "en",
    "German": "de",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Turkish": "tr",
    "Chinese, simplified": "zh"
}

def text_to_speech(input_text, language_code):
    # Generate audio from the given text
    audio_array = generate_audio(input_text)

    # Form the output wav file name
    output_file = "bark_output-" + language_code + ".wav"
    
    # Save audio to disk
    write_wav(output_file, SAMPLE_RATE, audio_array)

    return output_file

def detect_and_translate(input_text, target_language_code):
    source_language = detect(input_text)
    
    # If the detected language is different from the target, translate it
    if source_language != target_language_code:
        translator = Translator()
        translated = translator.translate(input_text, src=source_language, dest=target_language_code)
        return translated.text

    return input_text

def select_language():
    # Print available languages
    for idx, language in enumerate(LANGUAGES.keys(), 1):
        print(f"{idx}. {language}")
    
    # Prompt user to select a language
    choice = int(input("Enter the number of your desired language: "))
    language = list(LANGUAGES.keys())[choice - 1]
    return LANGUAGES[language]

if __name__ == "__main__":
    input_file = input("Please provide the path to your text file: ")

    if os.path.exists(input_file):
        with open(input_file, 'r') as file:
            content = file.read()
        print("File read successfully.")

        target_language_code = select_language()
        print(f"Detected language: {detect(content)}.")
        
        translated_text = detect_and_translate(content, target_language_code)
        print("Translation completed (if needed).")
        
        output_path = text_to_speech(translated_text, target_language_code)
        print(f"Text to Speech conversion completed! Audio saved at: {output_path}")
    else:
        print("Invalid path. Please ensure the file exists and try again.")
