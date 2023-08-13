from gtts import gTTS
import os

def text_to_speech(input_file):
    # Extract the base filename without extension from the input path
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Form the output mp3 file path
    output_file = os.path.join(os.path.dirname(input_file), base_filename + ".mp3")

    # Read the text from the file
    with open(input_file, 'r') as file:
        text = file.read()
        
    # Convert the text to speech
    tts = gTTS(text, lang='en')
    
    # Save the converted audio to an mp3 file
    tts.save(output_file)

    return output_file

if __name__ == "__main__":
    # Ask user for the input txt file path
    input_file = input("Please provide the path to your text file: ")

    if os.path.exists(input_file):
        output_path = text_to_speech(input_file)
        print(f"Text to Speech conversion completed! Audio saved at: {output_path}")
    else:
        print("Invalid path. Please ensure the file exists and try again.")

