a = "AWUBBWUBC"
b = "AWUBWUBWUBBWUBWUBWUBC"
c = "WUBAWUBBWUBCWUB"

def song_decoder(s):
    s = s.replace('WUB', "*")
    s = list(s)

    new_song = ""
    return s

print(song_decoder(a))
print(song_decoder(b))
print(song_decoder(c))