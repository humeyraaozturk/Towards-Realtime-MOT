"""
python reencode_video.py --input ./input/human.mp4 --output ./input/human_reencoded.mp4 --width 1088 --height 608
"""

import subprocess
import argparse
import os

def reencode_video(input_path, output_path, width, height):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input video not found: {input_path}")

    # ffmpeg komutunu oluştur
    command = [
        "ffmpeg",
        "-i", input_path,
        "-vf", f"scale={width}:{height}",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "22",
        "-c:a", "aac",
        output_path
    ]

    print("Running ffmpeg command:")
    print(" ".join(command))

    # Komutu çalıştır
    subprocess.run(command, check=True)
    print(f"Video successfully re-encoded and saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video re-encoding script using ffmpeg")
    parser.add_argument("--input", required=True, help="Path to the input video")
    parser.add_argument("--output", required=True, help="Path to save the re-encoded video")
    parser.add_argument("--width", type=int, required=True, help="Target width of the output video")
    parser.add_argument("--height", type=int, required=True, help="Target height of the output video")

    args = parser.parse_args()
    
    reencode_video(args.input, args.output, args.width, args.height)
