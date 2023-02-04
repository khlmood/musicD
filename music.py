import customtkinter
import json
import requests

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.path = "C:\\Users\\User\\Music"

        self.geometry("730x380")
        self.title("Download Music")
        self.minsize(300, 200)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.pack(side='top', padx=20, pady=(20, 0))

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
        self.textbox.insert("insert", self.entry.get() + "\n")
        self.entry.delete(0, "end")

    def search(self):
        if self.entry.get() != "":
            self.textbox.delete("0.0", "end")
            response = requests.get("https://itunes.apple.com/search?entity=song&limit=15&term=" + self.entry.get())
            o = response.json()
            songs = []
            self.entry.delete(0, "end")
            for result in o["results"]:
                self.textbox.insert("insert", result["trackName"] + "\n")

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

if __name__ == "__main__":
    app = App()
    app.mainloop()