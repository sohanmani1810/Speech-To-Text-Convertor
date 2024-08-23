import tkinter as tk
from PIL import ImageTk, Image
import speech_recognition as sr

def convert_speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything to convert into text:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        result_label.config(text="Spoken Text is: " + text)
    except sr.UnknownValueError:
        result_label.config(text="Sorry, could not recognize the voice.")
    except sr.RequestError:
        result_label.config(text="Sorry, speech recognition service is unavailable.")

#Create the main window
window = tk.Tk()
window.title("ASR")
window.geometry("800x500")
window.config()

#Set background image
image = Image.open("C:\\Users\\Gaurav Tripathi\\Desktop\\ADproject\\img1.jpg")  # Replace "background_image.png" with your image file
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Create the GUI components
label = tk.Label(window, text="AUTOMATIC SPEECH RECOGNIZER", font=("Arial", 18, "bold"), fg="#d1d1d1", bg="#33313b")
label.pack(pady=0)

result_label = tk.Label(window, text="", font=("Arial", 14), fg="#3a4750", bg="#b7b7b7")
result_label.pack(pady=70)

button = tk.Button(window, text="Click To Record", command=convert_speech_to_text, width=20, bg="#dfcdc3", font=("Arial", 12))
button.pack(side=tk.BOTTOM, pady=20)

#Start the main event loop
window.mainloop()

