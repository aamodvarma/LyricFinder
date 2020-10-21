import requests
from bs4 import BeautifulSoup
from tkinter import *
import time

def main(artist, song):
    artists = artist.split(' ')
    for a in range(len(artists)):
        artists[a] = artists[a] + '-'
    main_artist = ''.join(artists)
    songs = song.split(' ')
    for a in range(len(songs)):
        songs[a] = songs[a] + '-'
    main_song = ''.join(songs)
    baseurl = 'https://genius.com/'
    page = requests.get(baseurl + main_artist + main_song + 'lyrics')
    time.sleep(0.2)

    html = BeautifulSoup(page.text, "html.parser")
    try:
        lyrics = html.find("div", class_="lyrics").get_text()
        return(lyrics)

    except:
        main(artist, song)



def send():

    artist = login.get()
    song = password.get()
    lyrics = main(artist,song)
    ly.config(text = lyrics)
    ly.pack()

    print(lyrics)

tk = Tk()
tk.geometry('1000x900')
# create 2 text boxes

loginame = Label(tk, text='Artist name')
loginame.pack()

login = Entry(tk)
login.pack()

passwordname = Label(tk, text='Enter Song name')
passwordname.pack()

password = Entry(tk)
password.pack()

ly = Label(tk)

enter = Button(tk, text='Submit', command=send)
enter.pack()




tk.mainloop()
