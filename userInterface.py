#!/usr/bin/python3
import customtkinter
from attendance import main
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
from List import run


root = customtkinter.CTk()
root.geometry("500 * 350") 
root.title("Attendance System")



def generateList():
    root.destroy()
    run()
    



frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=150, padx=200, fill = "both", expand= True)

label = customtkinter.CTkLabel(master = frame, text="Attendance System", font=("century gothic", 24))
label.pack(pady=100, padx= 150)


button = customtkinter.CTkButton(master=frame , text ="Take Attendance", font= ("century gothic", 15), command= main)
button.pack(pady=12, padx=10)

listing_button = customtkinter.CTkButton(master=frame , text ="Generate List", font= ("century gothic", 15), command= generateList)
listing_button.pack(pady=12, padx=10)

root.mainloop()

