# Text to Speech Converter using gTTS

This script converts the content of a txt file into speech and saves it as an mp3 file.

## Prerequisites

- Python 3.x
- Pip (Python Package Installer)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory and install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage
Modify the input_file and output_file variables in the script to point to your input text file and desired output mp3 location respectively.

```python
input_file = 'path_to_your_text_file.txt'
output_file = 'path_for_output_mp3.mp3'
Run the script:
```

```bash
python text_to_speech.py
```

Once completed, you'll find the generated mp3 file in the specified output location.

## Libraries Used
gTTS (Google Text-to-Speech): A Python interface for Google's Text to Speech API.

License
This project is open-sourced under the MIT License.
