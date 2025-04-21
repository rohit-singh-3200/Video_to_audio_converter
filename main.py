from moviepy import VideoFileClip #Import moviepy to work with video clips

video_path=input("Enter the video path: ") # Enter the video name with extension or the whole path

try:
    video=VideoFileClip(video_path) #Variable that holds the video

    output_name=input("Enter the name of the converted Audio file: ") #Output name of the audiofile { without extension}

    audio_path=f"{output_name}.mp3" # extension {can be changed if needed}

    video.audio.write_audiofile(audio_path, bitrate="320k") #bitrate

    print(f"✅ Audio saved successfully as {audio_path}")
except Exception as e:
    print(f"❌ Error: {e}")


