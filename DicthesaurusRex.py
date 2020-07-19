import PyDictionary as dc
import tkinter as tk

def search_word(event=None):
    try:    
        for label in label_list:
            label.destroy()
        word = word_entry.get()
        meanings = dictionary.meaning(word)
        for meaning in meanings:
            part_label = tk.Label(window, text=meaning, wraplength=600, width=600, anchor='w', justify='left', font='Calibri 16 bold', bg='#121212', fg='#BEBEBE')
            part_label.pack()
            label_list.append(part_label)
            for i in range(len(meanings[meaning])):
                num = '{}. '.format(i+1)
                meaning_label = tk.Label(window, text=num + meanings[meaning][i], wraplength=600, width=600, anchor='w', justify='left', font='Calibri 16', bg='#121212', fg='#BEBEBE')
                meaning_label.pack()
                label_list.append(meaning_label)

        try:
            only_syn(True)
        except:
            pass
    except:
        for label in label_list:
            label.destroy()
        tmp = tk.Label(window,text='That is not a word IDIOT', bg='#121212', fg='#BEBEBE')
        tmp.pack()
        label_list.append(tmp)

def only_syn(meaning_called=False, event=None):
    if not meaning_called:
        for label in label_list:
            label.destroy()
    word = word_entry.get()
    synonyms = dictionary.synonym(word)
    synonyms_title = tk.Label(window, text='Synonyms', wraplength=600, width=600, anchor='w', justify='left', font='Calibri 16 bold', bg='#121212', fg='#BEBEBE')
    synonyms_title.pack()
    label_list.append(synonyms_title)

    syn_list=''
    for synonym in synonyms:
        temp_syn = synonym + ', '
        syn_list += temp_syn
    syn_label = tk.Label(window, text=syn_list, font='Calibri 12', wraplength=600, width=600, anchor='w', justify='left', bg='#121212', fg='#BEBEBE')
    syn_label.pack()
    label_list.append(syn_label)

window = tk.Tk()
window.title('Dicthesaurus Rex')
window.geometry('700x600')
window.configure(bg='#121212')
label_list = []

dictionary = dc.PyDictionary()
word_entry = tk.StringVar()
entry_box = tk.Entry(window, textvariable=word_entry, width=30, bg='#333333', fg='#BEBEBE').pack(pady=(15,15))
search_btn = tk.Button(window, text='Search', command=search_word, bg='#121212', fg='#BEBEBE').pack()
only_syn_btn = tk.Button(window, text='Search Only Synonyms', command=only_syn, bg='#121212', fg='#BEBEBE').pack()

window.bind('<Return>', search_word)

window.mainloop()