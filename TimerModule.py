import time
from threading import Thread
from pygame import mixer
import os


def play_music(wav_file, volume, loops):
    # Starting the mixer
    mixer.init()

    # Loading the morse code
    mixer.music.load(wav_file)

    # Setting the volume
    mixer.music.set_volume(volume)

    # Start playing the morse code
    mixer.music.play(loops=loops)


def stop_music(music_thread, duration):
    time.sleep(duration)
    mixer.music.stop()
    mixer.quit()
    print('music stopped')
    music_thread.join()

def start_music(wav_file, duration, volume, loops):
    # Play Music on Separate Thread (in background)
    music_thread = Thread(target=play_music, args=(wav_file, volume, loops))

    stop_music_thread = Thread(target=stop_music, args=(music_thread, duration,))

    music_thread.start()

    stop_music_thread.start()
    stop_music_thread.join()

#example function call
# start_music(os.path.abspath("audio/YTCartoonMetalThunk.mp3"), 15, 1, 1)

