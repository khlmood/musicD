import customtkinter
import json
import requests
from socket import gethostbyname
from socket import create_connection
from winsound import Beep

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.path = "C:\\Users\\User\\Music"

        self.geometry("730x380")
        self.title("Download Music")
        self.minsize(300, 200)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(side='bottom')

        self.button_change_path = customtkinter.CTkButton(master=self.frame, text="Change path", command=self.create_toplevel)
        self.button_change_path.pack(side='left', padx=20, pady=20)

        self.button_download = customtkinter.CTkButton(master=self.frame, text="Download", command=self.download)
        self.button_download.pack(side='right', padx=20, pady=20)

        self.button_search = customtkinter.CTkButton(master=self.frame, text="Seach", command=self.search)
        self.button_search.pack(side='right', padx=20, pady=20)

        self.entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Search Artist")
        self.entry.pack(side='left', padx=20, pady=20)
        
    def download(self):
        if is_connected():
            print("ok")
        else:
            print("ok")

    def search(self):
        if is_connected():
            if self.entry.get() != "":
                response = requests.get("https://itunes.apple.com/search?entity=song&limit=15&term=" + self.entry.get())
                o = response.json()
                songs = []
                self.entry.delete(0, "end")
                for result in o["results"]:
                    songs.append(result["trackName"])
                self.create_widgets(songs)
        else:
            self.connection_error()

    def create_toplevel(self):
        self.toplevel = customtkinter.CTkToplevel(self)
        self.toplevel.title("Download Path")
        self.toplevel.geometry("380x80")

        entry = customtkinter.CTkEntry(master=self.toplevel, placeholder_text=self.path)
        entry.pack(side='left', padx=20, pady=20)

        button = customtkinter.CTkButton(master=self.toplevel, text="Apply", command=lambda: self.change_path(entry))
        button.pack(side='right', padx=20, pady=20)


    def change_path(self, entry):
        if entry.get() != "":
            self.path = entry.get()
        self.toplevel.destroy()

    def create_widgets(self, songs):
        for i, song in enumerate(songs):
            var = customtkinter.IntVar()
            cb = customtkinter.CTkCheckBox(self, text=song, variable=var)
            cb.pack()
            #label = customtkinter.CTkLabel(self, text=f"Selection {i+1}: {var.get()}")
            #label.pack()
    
    def connection_error(self):
        self.toplevel = customtkinter.CTkToplevel(self)
        self.toplevel.title("Connection Error")
        self.toplevel.geometry("280x100+400+300")

        warning_sign = "⚠️"
        label = customtkinter.CTkLabel(master=self.toplevel, text=f"{warning_sign} Please check your internet connection.")
        label.pack(side='left', padx=20, pady=20)
        Beep(frequency=1000, duration=500)


def is_connected():
    try:
        host = gethostbyname("www.google.com")
        create_connection((host, 80), 2)
        return True
    except:
        return False
