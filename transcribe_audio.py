import os
from pydub import AudioSegment
import speech_recognition as sr
from tqdm import tqdm
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to convert MP3 to WAV with progress
def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    duration_ms = len(audio)  # Duration in milliseconds

    chunk_size = 1000  # Process in 1-second chunks
    progress_bar = tqdm(total=duration_ms, unit='ms', desc=Fore.GREEN + 'Converting MP3 to WAV' + Style.RESET_ALL, bar_format='{l_bar}{bar}{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]')

    # Initialize an empty AudioSegment for concatenation
    combined_audio = AudioSegment.empty()

    for start in range(0, duration_ms, chunk_size):
        end = min(start + chunk_size, duration_ms)
        chunk = audio[start:end]
        combined_audio += chunk
        progress_bar.update(chunk_size)

    # Export the combined audio to WAV
    combined_audio.export(wav_path, format="wav")
    progress_bar.update(duration_ms - progress_bar.n)  # Ensure progress bar ends at 100%
    progress_bar.close()

# Function to split audio into smaller chunks
def split_audio(audio, chunk_length_ms):
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunks.append(chunk)
    return chunks

# Function to transcribe audio with progress
def transcribe_audio(wav_path, output_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)  # Read the entire audio file
        duration_s = source.DURATION  # Duration in seconds

    progress_bar = tqdm(total=duration_s, unit='s', desc=Fore.GREEN + 'Transcribing Audio' + Style.RESET_ALL, bar_format='{l_bar}{bar}{n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]')

    try:
        # Check if audio is too long and split if necessary
        if duration_s > 60:
            combined_transcript = ""
            audio_data = AudioSegment.from_wav(wav_path)
            chunks = split_audio(audio_data, 60000)  # Split into 60-second chunks

            for chunk in chunks:
                with sr.AudioFile(chunk.export(format="wav")) as source_chunk:
                    audio_chunk = recognizer.record(source_chunk)
                    transcript = recognizer.recognize_google(audio_chunk)
                    combined_transcript += transcript + " "
                    progress_bar.update(len(chunk) / 1000)

            progress_bar.update(duration_s - progress_bar.n)  # Finish the progress bar
            progress_bar.close()
            with open(output_file_path, 'w') as f:
                f.write(combined_transcript.strip())
            print(f"Transcription saved to {output_file_path}")
        else:
            # Simulate progress for transcription (since recognizer is not chunked)
            for i in range(int(duration_s)):
                time.sleep(0.1)  # Simulate time taken for transcription
                progress_bar.update(1)

            transcript = recognizer.recognize_google(audio)
            progress_bar.update(duration_s - progress_bar.n)  # Finish the progress bar
            progress_bar.close()
            with open(output_file_path, 'w') as f:
                f.write(transcript)
            print(f"Transcription saved to {output_file_path}")
    except sr.UnknownValueError:
        progress_bar.close()
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        progress_bar.close()
        print(f"Could not request results from Google Web Speech API; {e}")
    except Exception as e:
        progress_bar.close()
        print(f"An error occurred during transcription: {e}")

# Paths to the audio files
audio_file_path = 'input.mp3'  # Replace with your input MP3 file path
wav_file_path = 'output.wav'
output_folder = 'transcriptions'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, 'transcription.txt')

# Convert MP3 to WAV
convert_mp3_to_wav(audio_file_path, wav_file_path)

# Transcribe Audio and save to file
transcribe_audio(wav_file_path, output_file_path)
