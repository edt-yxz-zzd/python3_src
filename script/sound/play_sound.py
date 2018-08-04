
def linux_play_wav():
    import ossaudiodev
    # ???
    return play_wav

def windows_play_wav():
    import winsound

    def play_wav(fname):
        return winsound.PlaySound(fname, winsound.SND_FILENAME)
    return play_wav


try:
    play_wav = linux_play_wav()
except:
    play_wav = windows_play_wav()

