#This project is studied from youtube tutorial by: Dev Ed "Build A Python GUI App Tutorial"
#This Project is about building a GUI App for Windows

#importing Tkinker api
import tkinter as tk
#importing filedialog and text
from tkinter import filedialog, Text
#to run the apps
import os

#calling tk as the name of the windows form
root = tk.Tk()
#For addApp function
apps = []

#loading the txt file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#adding a function
def addApp():
    #to delete the last list
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/",title="Select File", filetypes=(("executables",".exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    #for every app in text in the apps append
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
#running the app
def runApps():
    for app in apps:
        os.startfile(app)
#arguments {root to attach to the windows form, for bg the color}
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
#to attach the canvas
canvas.pack()
#putting a frame in the app

frame = tk.Frame(root, bg="white")
#placing the frame to the app
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#putting a button in the app
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

#running app button
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

#running the app
root.mainloop()

#saving to the txt
with open('save.txt', 'w')as f:
    for app in apps:
        f.write(app + ',')