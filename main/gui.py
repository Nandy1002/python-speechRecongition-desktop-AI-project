import customtkinter as ctk
from PIL import Image
root = ctk.CTk()
root.title("IRIS")
root.geometry("1080x720")
root._set_appearance_mode("dark")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20)

logo = ctk.CTkImage(Image.open(
    "/home/nabendu/Documents/MCA/projects/python-speechRecongition-desktop-AI-project/main/img/walle.png"), size=(200, 180))
label = ctk.CTkLabel(frame, image=logo, text="")
label.grid(row=0, column=0, pady=0, padx=0)

aiTextBox = ctk.CTkTextbox(master=frame, height=100, width=500)
aiTextBox.grid(row=0, column=1, pady=10, padx=50)

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=10)

userTextBox = ctk.CTkTextbox(master=frame2, height=50, width=500)
userTextBox.grid(row=0, column=0, padx=30, pady=10)

command = ctk.CTkButton(master=frame2, text="Enter Command",
                        height=50)
command.grid(row=0, column=1, padx=50, pady=10)


root.mainloop()
