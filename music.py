import customtkinter
import subprocess

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.path = "C:\\Users\\User\\Music"

        self.geometry("600x400")
        self.title("Download Music")
        self.minsize(300, 200)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 0))

        self.button_search = customtkinter.CTkButton(master=self, text="Seach", command=self.search)
        self.button_search.grid(row=2, column=2, padx=20, pady=20)

        self.button_download = customtkinter.CTkButton(master=self, text="Download", command=self.download)
        self.button_download.grid(row=1, column=2, padx=20, pady=20)

        self.button_change_path = customtkinter.CTkButton(master=self, text="Change path", command=self.create_toplevel)
        self.button_change_path.grid(row=1, column=0, padx=20, pady=20)

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="Search Artist")
        self.entry.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        
    def download(self):
        self.textbox.insert("insert", self.entry.get() + "\n")
        self.entry.delete(0, "end")

    def search(self):
        self.textbox.insert("insert", self.entry.get() + "\n")
        self.entry.delete(0, "end")

    def create_toplevel(self):
        self.toplevel = customtkinter.CTkToplevel(self)
        self.toplevel.title("Download Path")
        self.toplevel.geometry("380x80")

        entry = customtkinter.CTkEntry(master=self.toplevel, placeholder_text=self.path)
        entry.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        button = customtkinter.CTkButton(master=self.toplevel, text="Apply", command=lambda: self.change_path(entry))
        button.grid(row=0, column=2, padx=20, pady=20)


    def change_path(self, entry):
        self.path = entry.get()
        self.toplevel.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
