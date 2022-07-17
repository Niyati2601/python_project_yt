from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry('800x700')
root.resizable(0,0)
root.title("YouTube video downloader by Niyati")
logo = PhotoImage(file='youtube1.png')
imgLbl = Label(root, image=logo)
imgLbl.place(x=50,y=0)

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15').place(x= 60 , y = 440)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 240, y = 450)



def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.filter(file_extension='mp4', progressive='True').get_by_itag(22)
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 320 , y = 550)



Button(root,text = 'DOWNLOAD', font = 'arial 15' ,fg='white',bg = 'red', padx = 2, command = Downloader).place(x=320 ,y = 520)


root.mainloop()