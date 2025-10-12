import os
import whisper
os.environ['PATH']+=os.pathsep+r"C:\Users\aadil\Downloads\ffmpeg-2025-10-09-git-469aad3897-full_build.7z\ffmpeg-2025-10-09-git-469aad3897-full_build\bin"
model=whisper.load_model("base")
def transcribe_audio(file_path):
    result=model.transcribe(file_path)
    return result["text"]
