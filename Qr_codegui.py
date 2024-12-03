import qrcode
from PIL import Image 
from tkinter import filedialog
import customtkinter as ctk
import io

ctk.set_appearance_mode='system'
root=ctk.CTk()
icon_path = 'E:/githubprojects/QR code gui/icon.ico' 
root.iconbitmap(icon_path)
root.title('Qr Code Generator')
root.resizable(False,False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 630
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

#_______________________________________________________________________________________________________________
import webbrowser

def open_github():
    webbrowser.open("https://github.com/RemovedTax")

def show_about():
    about_window = ctk.CTkToplevel(root)
    icon_path = 'E:/githubprojects/QR code gui/icon.ico' 
    about_window.iconbitmap(icon_path)   
    about_window.title("About")
    about_window.geometry("300x200")
    about_window.resizable(False, False)

    label = ctk.CTkLabel(
        about_window,
        text="QR Code Generator\nVersion: 1.0\nDeveloper: RemovedTax",
        font=("", 12),
        justify="center",
    )
    label.pack(pady=10)

    link_button = ctk.CTkButton(
        about_window,
        text="Visit GitHub",
        command=open_github,
        fg_color="blue",
        hover_color="darkblue",
        width=120,
    )
    link_button.pack(pady=5)

    close_btn = ctk.CTkButton(about_window, text="Close", command=about_window.destroy)
    close_btn.pack(pady=10)


about_btn = ctk.CTkButton(root, text="i", command=show_about,width=20,height=10,fg_color='grey')
about_btn.place(x=10,y=10)
#_________________________________________Above code is not required____________________________________________
#_______________________________________________________________________________________________________________

#                                                 Window Components

frame2=ctk.CTkFrame(root,fg_color=root.cget('bg'))
frame2.place(x=75,y=90)
frame3=ctk.CTkFrame(root,fg_color=root.cget('bg'))
frame3.pack(side='bottom',pady=15)
label1=ctk.CTkLabel(frame2,text='Enter your text below',font=('',15))
label1.pack()
entry=ctk.CTkEntry(frame2,width=250,border_color=root.cget('bg'))
entry.pack()
frame1=ctk.CTkFrame(root,fg_color='black',width=300,height=300)
frame1.place(x=50,y=230)
label2 =ctk.CTkLabel(frame1,text="",bg_color=root.cget('bg'))
label2.pack(expand=True)
label_title = ctk.CTkLabel(root, text="QR Code Generator", font=('', 20))
label_title.place(x=110, y=25)

# Save button function to save the qr code

def save_button_func():
    data = entry.get()
    img  = qrcode.make(data)
    name = data + '.png'
    file_path=filedialog.asksaveasfilename(initialfile=name,defaultextension='.png',filetypes=[('PNG files','*.png')],)
    def change_button_color():
        savebtn.configure(text='Save',fg_color="blue")

    if file_path:
        with open(file_path, 'wb') as file:
            img.save(file,"PNG")
        savebtn.configure(text="Saved ✓ ",fg_color="green",border_color="black")
        savebtn.after(ms=3000,func=change_button_color)
savebtn=ctk.CTkButton(frame3,text='Save',width=100,height=10,command=save_button_func)

#Delete button function to delet the generated Qr code 

def delet_button_func():
    global qr_image
    qr_image = None
    label2.configure(image=None)
    label2.configure(text="Preview")
    deletebtn.grid_remove()
    savebtn.grid_remove()

deletebtn=ctk.CTkButton(frame3,text ='Delete',width=100,height=10,command=delet_button_func,fg_color='red',border_color='red',border_width=2)


def change_button_name():
    button1.configure(text='Generate',fg_color="blue")

qrimg = None

def generate_qr(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer,'PNG')
    buffer.seek(0)
    pil_image = Image.open(buffer)
    return ctk.CTkImage(pil_image, size=(300, 300))

def returnkeyfunc(event = None):
    data = entry.get()
    if not data.strip():
        button1.configure(text="Enter valid text!", fg_color="red")
        button1.after(ms=2000, func=change_button_name,)
        return
    ctk_image = generate_qr(data)  
    label2.configure(image=ctk_image, text="")
    label2._image = ctk_image  

    button1.configure(text="QR Code Generated!", fg_color="green")
    button1.after(2000,change_button_name)
    deletebtn.grid(row=0, column=2, padx=5)
    savebtn.grid(row=0, column=1, padx=5)
    entry.delete(0,ctk.END)
   
root.bind('<Return>',returnkeyfunc)
button1=ctk.CTkButton(frame2,text='Generate',command=returnkeyfunc,hover_color='black',border_color='blue',border_width=1)
button1.pack(pady=20)
close_button = ctk.CTkButton(frame3, text="Exit",text_color='black',font=('bolt',14),command=root.quit,fg_color='grey',hover_color='red',border_color='black',border_width=1,width=100,height=10,corner_radius=5)
close_button.grid(row=0,column=0,padx=5) 

root.mainloop()