# Speech Transcriber

A Python project to convert MP3 files to WAV and transcribe the audio using Google Web Speech API, with a progress bar for both conversion and transcription processes.

> **Note:** This project was created with the assistance of AI.

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

## Notes

- Ensure you have a stable internet connection for the Google Web Speech API to work.
- The script handles audio files longer than 60 seconds by splitting them into smaller chunks before transcription.

## Acknowledgments

This project was created with the assistance of AI.
