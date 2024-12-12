from tkinter import *
from gtts import gTTS
from playsound import playsound

def play_text():
    global text_entry
    text = text_entry.get()
    if text:
        speech = gTTS(text=text, lang='en')
        speech.save("speech.mp3")
        playsound("speech.mp3")

def clear_text():
    global text_entry
    text_entry.delete(0, 'end')

root = Tk()
root.title("Text to Speech")
root.geometry("400x300")

Label(root, text="Text to Speech", font=("arial", 20)).pack(pady=10)
Label(root, text="Enter your text:", font=("arial", 12)).pack()

text_entry = Entry(root, width=40, font=("helvetica", 14))
text_entry.pack(pady=10) 

play_button = Button(root, text="Play", width=20, command=play_text)
play_button.pack(pady=5)


exit_button = Button(root, text="Exit", width=20, command=root.destroy, bg="red", fg="white")
exit_button.pack(pady=5)


set_button = Button(root, text="Clear", width=20, command=clear_text, bg="blue", fg="white")
set_button.pack(pady=5)


root.mainloop()