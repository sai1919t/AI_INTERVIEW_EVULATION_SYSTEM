from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, output_audio_path):

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    with VideoFileClip(video_path) as clip:
        clip.audio.write_audiofile(output_audio_path)