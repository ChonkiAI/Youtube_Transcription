# YouTube Transcription Pipeline with Self-Hosted Whisper

This project provides a complete pipeline to download audio from a YouTube video, transcribe it using a locally-run instance of OpenAI's Whisper model, and save the resulting transcription as a PDF document. This approach allows for accurate, free transcriptions without relying on paid APIs.

## Features

- **YouTube Audio Downloader**: Downloads the best quality audio from any YouTube video URL.
- **Local Transcription**: Uses OpenAI's Whisper for high-accuracy, on-device speech-to-text.
- **Multi-Language Support**: Automatically detects the audio language and can translate it to a specified target language.
- **Multiple Model Sizes**: Supports various Whisper models ("tiny", "base", "small", "medium", "large") to balance speed and accuracy.
- **Text Cleaning**: Includes functionality to remove repetitive phrases and consecutive duplicate lines from the transcript for better readability.
- **PDF Generation**: Saves the final, cleaned transcript as a well-formatted PDF file.
- **Hardware Acceleration**: Recommends and supports GPU (CUDA) for faster processing, but also runs on CPU.
- **Batch Processing**: Contains a boilerplate for processing multiple videos at once.

## Technologies Used

- **Python 3.8+**
- **Core Libraries**:
    - `yt-dlp`: For downloading YouTube video audio.
    - `openai-whisper`: For local audio transcription.
    - `torch`: As the backend for the Whisper model.
    - `fpdf`: For generating PDF files from the transcript.
- **System Dependency**:
    - `FFmpeg`: Required by `yt-dlp` for audio processing and format conversion.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ChonkiAI/Youtube_Transcription.git
    cd Youtube_Transcription
    ```

2.  **Install FFmpeg:**
    You must have FFmpeg installed on your system.
    - **On macOS (using Homebrew):**
      ```bash
      brew install ffmpeg
      ```
    - **On Ubuntu/Debian:**
      ```bash
      sudo apt update && sudo apt install ffmpeg
      ```
    - **On Windows:**
      Download the executable from the [official FFmpeg website](https://ffmpeg.org/download.html) and add it to your system's PATH.

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: For GPU support, you may need a specific build of PyTorch. Please refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/) for instructions tailored to your CUDA version.*

## Example Usage

The primary logic is contained within the `transcription_pipeline.ipynb` Jupyter Notebook.

1.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

2.  **Open the notebook:**
    Open the `transcription_pipeline.ipynb` file in your browser.

3.  **Configure the pipeline:**
    - In the **Select Whisper Model Size** section, you can change the model. The `tiny` model is used by default for speed, but `base` or `small` offer better accuracy.
      ```python
      WHISPER_MODEL_SIZE = "base"  # Change this to "tiny", "small", "medium", or "large"
      ```

4.  **Run the pipeline:**
    - Navigate to the **Run the Pipeline** section near the end of the notebook.
    - Replace the placeholder URL with the YouTube video you want to transcribe.
    - Set your desired output language (e.g., 'en' for English, 'es' for Spanish).
      ```python
      # Set the YouTube URL and target language
      youtube_url = "[https://www.youtube.com/watch?v=your_video_id_here](https://www.youtube.com/watch?v=your_video_id_here)"
      target_language = "en"
      ```
    - Run the cells to start the process. The script will download, transcribe, and create a PDF.

5.  **Find the output:**
    The generated PDF will be saved in the `transcripts/` directory. A link to the file will also be displayed in the notebook output.

## Folder Structure
├── downloads/              # Stores downloaded .mp3 audio files
├── example_input/
│   └── urls.txt            # Contains example YouTube URLs
├── transcripts/            # Stores the final .pdf transcripts
├── README.md
├── requirements.txt
├── setup.py
└── transcription_pipeline.ipynb # Main project notebook
