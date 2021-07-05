from os import path
from pydub import AudioSegment

# files
src = "../audio/YTCartoonMetalThunk.mp3"
dst = "YTCartoonMetalThunk.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

# sound = AudioSegment.from_mp3("")
#
# sound.export(dst, format="wav")