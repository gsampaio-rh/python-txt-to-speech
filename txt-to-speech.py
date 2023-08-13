from gtts import gTTS

def text_to_speech(input_file, output_file):
    # Read the text from the file
    with open(input_file, 'r') as file:
        text = file.read()
        
    # Convert the text to speech
    tts = gTTS(text, lang='en')
    
    # Save the converted audio to an mp3 file
    tts.save(output_file)

if __name__ == "__main__":
    # Specify your input txt file and desired output mp3 file
    input_file = 'example.txt'
    output_file = 'example.mp3'
    
    text_to_speech(input_file, output_file)
    print("Text to Speech conversion completed!")

