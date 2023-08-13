from gtts import gTTS, lang
import os

def text_to_speech(input_file, language):
    # Extract the base filename without extension from the input path
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Form the output mp3 file path
    output_file = os.path.join(os.path.dirname(input_file), base_filename + "-" + language + ".mp3")

    # Read the text from the file
    with open(input_file, 'r') as file:
        text = file.read()
        
    # Convert the text to speech with the selected language
    tts = gTTS(text, lang=language)
    
    # Save the converted audio to an mp3 file
    tts.save(output_file)

    return output_file

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
    # Ask user for the input txt file path
    input_file = input("Please provide the path to your text file: ")

    if os.path.exists(input_file):
        language = select_language()
        output_path = text_to_speech(input_file, language)
        print(f"Text to Speech conversion completed! Audio saved at: {output_path}")
    else:
        print("Invalid path. Please ensure the file exists and try again.")
