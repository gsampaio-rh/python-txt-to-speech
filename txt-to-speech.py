from gtts import gTTS, lang
from langdetect import detect
from googletrans import Translator
import os

def text_to_speech(input_text, language):
     # Extract the base filename without extension from the input path
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Form the output mp3 file path
    output_file = os.path.join(os.path.dirname(input_file), base_filename + "-" + language + ".mp3")

    # Convert the text to speech with the selected language
    tts = gTTS(input_text, lang=language)
    tts.save(output_file)

    return output_file

def detect_and_translate(input_text, target_language):
    source_language = detect(input_text)
    
    # If the detected language is different from the target, translate it
    if source_language != target_language:
        translator = Translator()
        translated = translator.translate(input_text, src=source_language, dest=target_language)
        return translated.text

    return input_text

def select_language():
    # Print available languages
    languages = lang.tts_langs()
    sorted_langs = sorted(languages.items())
    for idx, (code, name) in enumerate(sorted_langs, 1):
        print(f"{idx}. {name} ({code})")
    
    # Prompt user to select a language
    choice = int(input("Enter the number of your desired language: "))
    return sorted_langs[choice - 1][0]

if __name__ == "__main__":
    input_file = input("Please provide the path to your text file: ")

    if os.path.exists(input_file):
        with open(input_file, 'r') as file:
            content = file.read()

        target_language = select_language()  # Using the function provided in the previous code
        translated_text = detect_and_translate(content, target_language)
        output_path = text_to_speech(translated_text, target_language)

        print(f"Text to Speech conversion completed! Audio saved at: {output_path}")
    else:
        print("Invalid path. Please ensure the file exists and try again.")
