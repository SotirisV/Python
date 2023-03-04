from tkinter import*

def cancel():
    entry_Username.delete(0,'end')
    entry_Password.delete(0,'end')
    
root=Tk()

window_width=240
window_height=100
scr_width=root.winfo_screenwidth()
scr_height=root.winfo_screenheight()
center_x=int(scr_width/2-window_width/2)
center_y=int(scr_height/2-window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.title('SignUp Required')
root.resizable(0,0)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)


label_Username=Label(root,text='Username:',font='Times 12 bold')
label_Username.grid(row=0,column=0,sticky=W,padx=5,pady=5)
entry_Username=Entry(root)
entry_Username.focus()
entry_Username.grid(row=0,column=1,sticky=E,padx=5,pady=5)

label_Password=Label(root,text='Password:',font='Times 12 bold')
label_Password.grid(row=1,column=0,sticky=W,padx=5,pady=5)
entry_Password=Entry(root,show='*')
entry_Password.grid(row=1,column=1,sticky=E,padx=5,pady=5)

button_OK=Button(root,text='OK',)
#button_OK=Button(root,text='OK',command=accept())
button_OK.grid(row=2,column=0)
#button_Cancel=Button(root,text='Cancel')
button_Cancel=Button(root,text='Cancel',command=cancel)
button_Cancel.grid(row=2,column=1)