from tkinter import Tk, Label, Frame, Button, StringVar, PhotoImage, ttk
from PIL import Image
import pytube.contrib.search
from pytube import YouTube
import os, stat, requests, tkinter as tk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

name_image = "video_image.png"

class search:
    def __init__(self, words):
        self.search_words = str(pytube.contrib.search.Search(words).results)
        self.search_words_url = words
        self.result = ""
        self.result1 = ""
        self.num = 0
        self.search1 = ""
    @property
    def search_for(self):
        try:
            if "https://" in self.search_words_url:
                self.search1 = self.search_words_url
            else:
                for _ in self.search_words:
                    self.num += 1
                    if '=' in self.search_words[self.num]:
                        self.num += 1
                        self.result = self.num
                        break
                self.num = 0
                for _ in self.search_words:
                    self.num += 1
                    if '>' in self.search_words[self.num]:
                        self.result1 = self.num
                        break
                self.search1 = "https://www.youtube.com/watch?v=" + self.search_words[self.result:self.result1]
            try:
                os.chmod(name_image, stat.S_IWRITE)
                os.remove(name_image)
            except FileNotFoundError:
                pass
            video_Image = requests.get(YouTube(self.search1).thumbnail_url).content
            with open(name_image, "wb") as imagen:
                imagen.write(video_Image)
            Image.open(name_image).resize((200,100)).save(name_image,'png')
            return self.search1
        except IndexError:
            pass

class youtube:
    def __init__(self, windows):
        windows.title("Youtube downloader")
        windows.geometry("500x500")
        windows.minsize(width=530, height=500)
        windows.resizable(0,0)
        windows.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.close = windows
        self.frame_video_Audio = Frame(windows, bg="white", width="400", height="400")
        self.T_V = StringVar()
        self.L_E = Label(windows, text="Enter a URL or a word")
        self.L_E.place(x=159, y=30)
        self.E_W = ttk.Entry(windows, width="30", textvariable=self.T_V, validate='key', validatecommand=(windows.register(self.D_E_W), '%P'))
        self.E_W.place(x=107, y=100)
        self.alert = Label(windows, text="Search not found", fg="red")
        self.B_A = Button(windows, text="Audio", width=30, state="disable", command=self.Audio)
        self.B_A.place(x=110, y=170)
        self.B_V = Button(windows, text="video", command=self.video, width=30, state="disable")
        self.B_V.place(x=110, y=220)
        self.title = 0
        self.image = 0
        self.B_B = 0
        self.wait = 0
        windows.mainloop()

    def video(self):
        try:
            self.search = YouTube(search(self.T_V.get()).search_for)
            self.img = PhotoImage(file=name_image)
            self.image = Label(self.frame_video_Audio, image=self.img)
            self.image.place(x=100)
            self.title = Label(self.frame_video_Audio, text=self.search.title, bg="white")
            self.title.place(x=90, y=120)
            self.B_D = Button(self.frame_video_Audio, text="Download", width=30, command=lambda: self.search.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=self.search.title + ".mp4"))
            self.B_D.place(x=90, y=190)
            self.B_B = Button(self.frame_video_Audio, text="Back", width=10, command=self.Back)
            self.B_B.place(x=10, y=360)
            self.E_W.place_forget()
            self.L_E.place_forget()
            self.B_A.place_forget()
            self.B_V.place_forget()
            self.frame_video_Audio.place(x=0, y=0)
            self.alert.place_forget()
        except TypeError:
            self.alert.place(x=154, y=80)

    def Audio(self):
        try:
            self.search = YouTube(search(self.T_V.get()).search_for)
            self.img = PhotoImage(file=name_image)
            self.image = Label(self.frame_video_Audio, image=self.img)
            self.image.place(x=100)
            self.title = Label(self.frame_video_Audio, text=self.search.title, bg="white")
            self.title.place(x=90, y=120)
            self.B_D = Button(self.frame_video_Audio, text="Download", width=30, command=lambda: self.search.streams.get_audio_only().download(filename=self.search.title + ".mp3"))
            self.B_D.place(x=90, y=190)
            self.B_B = Button(self.frame_video_Audio, text="Back", width=10, command=self.Back)
            self.B_B.place(x=10, y=360)
            self.E_W.place_forget()
            self.L_E.place_forget()
            self.B_A.place_forget()
            self.B_V.place_forget()
            self.frame_video_Audio.place(x=0, y=0)
            self.alert.place_forget()
        except TypeError:
            self.alert.place(x=154, y=80)

    def D_E_W(self, digit):
        if len(digit) > 1:
            self.B_A["state"] = tk.NORMAL
            self.B_V["state"] = tk.NORMAL
        else:
            self.B_A["state"] = tk.DISABLED
            self.B_V["state"] = tk.DISABLED
        return True
    def Back(self):
        self.L_E.place(x=139, y=30)
        self.B_D.place_forget()
        self.E_W.place(x=107, y=50)
        self.B_A.place(x=90, y=140)
        self.B_V.place(x=90, y=190)
        self.title.place_forget()
        self.image.place_forget()
        self.frame_video_Audio.place_forget()
        self.B_B.place_forget()
        
    def on_closing(self):
        try:
            os.chmod(name_image, stat.S_IWRITE)
            os.remove(name_image)
            self.close.destroy()
        except FileNotFoundError:
            self.close.destroy()
        
youtube(windows=Tk())