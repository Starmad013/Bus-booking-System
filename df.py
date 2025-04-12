from tkinter import *
import subprocess
root=Tk()
root.title("Submission Info")
root.state('zoomed')

root.configure(bg="Bisque")

def secpg(event):
    subprocess.run(["python","admin.py"])
'''
image=PhotoImage(file="starbus.png")
Label(root,image=image,bg="Bisque").place(relx=0.38,rely=0.08)
'''
Label(root,text="Online Bus Booking System",font="Arial 35",bg="Sandy brown",fg="brown4").place(relx=0.32,rely=0.5)
Label(root,text="Name: Pramiti Tewari",font="Arial 15",bg="Bisque").place(relx=0.44,rely=0.6)
Label(root,text="Enrollment No.: 221B162",font="Arial 15",bg="Bisque").place(relx=0.43,rely=0.65)
Label(root,text="Mobile: 7440266105",font="Arial 15",bg="Bisque").place(relx=0.44,rely=0.7)
Label(root,text="Submitted To: Dr Mahesh Kumar",font="Arial 25",bg="tomato2").place(relx=0.35,rely=0.8)
Label(root,text="Project Based Learning",font="Arial 17",bg="Bisque").place(relx=0.43,rely=0.87)

learn=Label(root,text="Press any Key to continue",font="Poppins 10 bold",bg="Bisque",fg="tomato2").place(relx=0.78,rely=0.89)
#learn.pack(pady=20)

root.bind("<Key>",secpg)
root.mainloop()
