# Speech Transcriber

A Python project to convert MP3 files to WAV and transcribe the audio using Google Web Speech API, with a progress bar for both conversion and transcription processes.

> **Note:** This project was created with the assistance of AI.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Description

Speech Transcriber is a tool designed to help users convert MP3 audio files to WAV format and transcribe the audio into text. It utilizes the Google Web Speech API to provide accurate transcriptions. The project includes a progress bar to indicate the status of conversion and transcription.

## Features

- Convert MP3 files to WAV format
- Transcribe audio to text using Google Web Speech API
- Progress bar for conversion and transcription processes
- Handles audio files longer than 60 seconds by splitting into chunks

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/SpeechTranscriber.git
    cd SpeechTranscriber
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Place your MP3 file in the project directory** and rename it to `input.mp3` or update the `audio_file_path` variable in `transcribe_audio.py` with your file's name.

2. **Run the script**:
    ```sh
    python transcribe_audio.py
    ```

3. **Check the `transcriptions` folder** for the output text file containing the transcription.

## Screenshots

![Progress Bar](screenshot1.png)
*Screenshot showing the progress bar during conversion.*

![Transcription Result](screenshot2.png)
*Screenshot showing the final transcription output.*

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project was created with the assistance of AI.
