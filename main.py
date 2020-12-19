from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Something went wrong!!",fg="red")


    #download function
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Youtube Video Downloader (Webdyno-Bhutan)")
root.geometry("500x600") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#icon
root.iconbitmap("icon.ico")
file = PhotoImage(file='youtubeIcon.png')
headingIcon =Label(root, image=file)
headingIcon.grid(ipady=15)

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=60,textvariable=ytdEntryVar)
ytdEntry.grid(ipady=10)

#Error Msg
ytdError = Label(root,text="paste a link to download",fg="black",font=("jost",10))
ytdError.grid(ipady=10)

#btn of save file
saveEntry = Button(root,width=10,bg="pink",fg="black",text="Save Video to",command=openLocation)
saveEntry.grid(ipady=5)

#Error Msg location
locationError = Label(root,text="",fg="red",font=("jost",10))
locationError.grid(ipady=10)

#Download Quality
ytdQuality = Label(root,text="Choose Quality",font=("jost",10))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()
ytdQuality = Label(root,text="")
ytdQuality.grid(ipady=5)
#donwload btn
downloadbtn = Button(root,text="Donwload",width=10,bg="teal",fg="white",command=DownloadVideo)
downloadbtn.grid(ipady=10)

#developer Label
developerlabel = Label(root,text="@webdyno-Bhutan | Tandin Wangchuk",font=("jost",10))
developerlabel.grid(ipady=10)
root.mainloop()