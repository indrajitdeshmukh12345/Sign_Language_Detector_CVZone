import customtkinter
import pyttsx3


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("600x300")

audio = pyttsx3.init()




class SimpleGUI:
    def __init__(self, master=root):
        self.master = master or customtkinter.CTk()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.master.title("Hand sign")
        label = customtkinter.CTkLabel(master=frame, text="Sign Language Detector", fg_color="transparent")
        label.pack()
        self.text_box = customtkinter.CTkTextbox(master=frame, text_color="white", width=600)
        self.text_box.insert(text="", index=0.0)

        self.text_box.pack(pady=5, padx=10)
        button = customtkinter.CTkButton(master=frame, text="Refresh", command=self.clear_text())
        button.pack()



    def run(self):
        self.master.mainloop()



    def update_text(self, message):
        self.text_box.insert(text=message + "\n", index="end")


    def clear_text(self):
        self.text_box.delete("0.0", "end")



if __name__ == "__main__":
    gui = SimpleGUI()
    gui.run()
