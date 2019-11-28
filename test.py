#!/usr/bin/env python3
import speech_recognition as sr
import subprocess
import os

# obtain path to "t1.wav", "t2.wav"
from os import path

def translate_to_thai(AUDIO_FILE):
    '''
    Input: File name (Audio)
    Output: Text recognizer from audio file (Thai language) 
    '''
    # Name new file
    AUDIO_FILE_CONV = AUDIO_FILE[:AUDIO_FILE.rfind('.')] + "-conv.wav"
    # Receive output from subprocedd
    FNULL = open(os.devnull, 'w')
    # Execute command convert file
    subprocess.run(["ffmpeg", "-y", "-i", AUDIO_FILE, "-acodec", "pcm_s16le", AUDIO_FILE_CONV], stdout=FNULL, stderr=subprocess.STDOUT)

    # Call API recognizer
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE_CONV) as source:
        audio = r.record(source)  # read the entire audio file
    return "You said: " + r.recognize_google(audio, None, 'th-TH')

def main():
    # AUDIO_FILE1 = path.join(path.dirname(path.realpath(__file__)), "../t1.wav")
    AUDIO_FILE1 = path.join(path.dirname(path.realpath(__file__)), "data/sound/ake.aac")
    # AUDIO_FILE2 = path.join(path.dirname(path.realpath(__file__)), "../t2.wav")
    print(translate_to_thai(AUDIO_FILE1))
    # print(translate_to_thai(AUDIO_FILE2))

if __name__ == "__main__":
    # Execute only if run as a script
    main()