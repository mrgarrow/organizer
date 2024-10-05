# Simple notepad with UI and automatic tabulating records :)
# v1.1 - first version with manual data entry
# v1.2 - added dark mode for eyes care
# v1.3 - will include drop-down menu of sites and Excel extension (.xlsx)

import tkinter as tk
from tkinter import messagebox
import os

def index_update():
    if not os.path.exists('Courses.txt'):
        return 1
    with open('Courses.txt','r') as file:
        rows = file.readlines()
        if len(rows) == 0:
            return 1
        return len(rows)+1

def save_to_file(site,organizator,course,link):
    index = index_update()
    if site and organizator and course and link:
        with open('Courses.txt','a') as file:
            file.write(f'{index}\t{organizator}\t{site}\t{course}\t{link}\n')
        messagebox.showinfo('Success','Successfully noted into Courses.txt!')
    else:
        messagebox.showwarning('Error','Something went wrong. Try again!')
    
def add_to_array():
    site = entry_site.get()
    organizator = entry_organizator.get()
    course = entry_course.get()
    link = entry_link.get()
    save_to_file(site,organizator,course,link)

    entry_site.delete(0,tk.END)
    entry_organizator.delete(0,tk.END)
    entry_course.delete(0,tk.END)
    entry_link.delete(0,tk.END)

window = tk.Tk()
window.title('Notepad for courses by Artur Lelito! :)')
window.configure(bg='#2C333A')

w = 250 
h = 250

sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w,h,x,y))

label_site = tk.Label(window,text='Site:',bg='#2C333A', fg='white')
label_site.pack()

entry_site = tk.Entry(window,bg='#454F59', fg='white')
entry_site.pack()

label_organizator = tk.Label(window,text='Organizator:',bg='#2C333A', fg='white')
label_organizator.pack()

entry_organizator = tk.Entry(window,bg='#454F59', fg='white')
entry_organizator.pack()

label_course = tk.Label(window,text='Course title:',bg='#2C333A', fg='white')
label_course.pack()

entry_course = tk.Entry(window,bg='#454F59', fg='white')
entry_course.pack()

label_link = tk.Label(window,text='Link to site:',bg='#2C333A', fg='white')
label_link.pack()

entry_link = tk.Entry(window,bg='#454F59', fg='white')
entry_link.pack()

button = tk.Button(window, text='Add to list!', command=add_to_array,bg='#454F59', fg='white')
button.pack(padx=10,pady=10)

window.mainloop()