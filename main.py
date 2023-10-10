from googletrans import Translator
from tkinter import * 
import httpcore

def translate():
    translator = Translator()
    try:
        translated_text["text"] = translator.translate(sentences.get(),dest=lang.get()).text
    except ValueError:
        translated_text["text"] = "Eror with lang"
    except httpcore._exceptions.ConnectError:
        translated_text["text"] = "Eror with internet"
root = Tk()
root.title("translator by _sineD_0")

sentences = StringVar()
sentences.set("Input words to translate")
lang = StringVar()
lang.set("uk")

input_SENTENCES = Entry(textvariable=sentences,width=25,font="Arial 12 bold")
chose_lang = OptionMenu(root,lang, "uk","ru","en","de","pl","en")
chose_lang.config(width=20,font="Arial 12 bold")
input_lang = Entry(textvariable=lang,width=25,font="Arial 12 bold")
btn = Button(text="translate",command=translate,width=25,height=2,font="Arial 12 bold")
translated_text = Label(text=None,font="Arial 12 bold")

input_SENTENCES.pack()
chose_lang.pack()
input_lang.pack()
btn.pack()
translated_text.pack()

root.mainloop()