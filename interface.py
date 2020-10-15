try:
    # for Python2
    from Tkinter import *  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import * ## notice lowercase 't' in tkinter here

from PIL import Image
from socket import *
import threading

class GUI:
    def __init__(self):
        self.Window = Tk()
        #self.Window.withdraw()
        ## Login will be implemented HERE!      
        # chat window which is currently hidden 
        self.Window = Tk() 
        # self.Window.withdraw() 
          
        # # login window 
        # self.login = Toplevel() 
        # # set the title 
        # self.login.title("Login") 
        # self.login.resizable(width = False,  
        #                      height = False) 
        # self.login.configure(width = 400, 
        #                      height = 300) 
        # # create a Label 
        # self.pls = Label(self.login,  
        #                text = "Please login to continue", 
        #                justify = CENTER,  
        #                font = "Times 14 bold") 
          
        # self.pls.place(relheight = 0.15, 
        #                relx = 0.2,  
        #                rely = 0.07) 
        # # create a Label 
        # self.labelName = Label(self.login, 
        #                        text = "Name: ", 
        #                        font = "Times 12") 
          
        # self.labelName.place(relheight = 0.2, 
        #                      relx = 0.1,  
        #                      rely = 0.2) 
          
        # # create a entry box for  
        # # tyoing the message 
        # self.entryName = Entry(self.login,  
        #                      font = "Times 14") 
          
        # self.entryName.place(relwidth = 0.4,  
        #                      relheight = 0.12, 
        #                      relx = 0.35, 
        #                      rely = 0.2) 
          
        # # set the focus of the curser 
        # self.entryName.focus() 
          
        # # create a Continue Button  
        # # along with action 
        # self.go = Button(self.login, 
        #                  text = "CONTINUE",  
        #                  font = "Times 14 bold",  
        #                  command = lambda: self.chat_Layout(self.entryName.get())
        # ) 
          
        # self.go.place(relx = 0.4, 
        #               rely = 0.55)
        self.chat_Layout("Murat") 
        self.Window.mainloop() 


    def goAhead(self, name): 
        self.login.destroy() 
        self.layout(name) 
          
        # the thread to receive messages 
        rcv = threading.Thread(target=self.receive) 
        rcv.start() 
    
    def chat_Layout(self,name):
        # get name of the chatter
        self.name = name
        # Chat Window
        self.Window.deiconify()
        self.Window.title("CHAT")

        self.Window.resizable(width=False,height=False)

        self.Window.configure(
            width=470,
            height=550,
            bg="white"
        )

        self.labelhead = Label(
            self.Window,
            bg="green",
            fg="white",
            text=self.name,
            font="Times 14 bold", 
            pady=5
        ).place(relwidth=1)

        self.line = Label(
            self.Window,
            width = 450,
            bg = "#ABB2B9"
        ).place(
            relwidth = 1,
            rely = 0.07,
            relheight = 0.012
        )

        self.textChat = Text(
            self.Window,
            width = 20,
            height = 2,
            bg = "#17202A", 
            fg = "#EAECEE", 
            font = "Times 14",  
            padx = 5, 
            pady = 5
        ).place(
            relheight = 0.745,
            relwidth = 1,
            rely = 0.08
        )

        self.labelBottom = Label(
            self.Window,
            bg = "#ABB2B9",
            height = 80
        ).place(
            relwidth = 1,
            rely = 0.825
        )

        self.msgBox = Entry(
            self.labelBottom,
            bg = "white",
            fg = "black",
            font = "Times 13"
        ).place(
            relwidth = 0.74,
            relheight = 0.06,
            rely = 0.008,
            relx = 0.011
        )

        self.msgBox.focus()
                # create a Send Button 
        self.buttonMsg = Button(self.labelBottom, 
                                text = "Send", 
                                font = "Times 10 bold",  
                                width = 20, 
                                bg = "#ABB2B9", 
                                command = lambda : self.sendButton(self.entryMsg.get())) 
          
        self.buttonMsg.place(relx = 0.77, 
                             rely = 0.008, 
                             relheight = 0.06,  
                             relwidth = 0.22) 
          
        self.textCons.config(cursor = "arrow") 
          
        # create a scroll bar 
        scrollbar = Scrollbar(self.textCons) 
          
        # place the scroll bar  
        # into the gui window 
        scrollbar.place(relheight = 1, 
                        relx = 0.974) 
          
        scrollbar.config(command = self.textCons.yview) 
          
        self.textCons.config(state = DISABLED) 


g = GUI()




# def send_msg():
#     myLabel = Label(window, text=msg.get())
#     myLabel.pack()


# # Canvas, actual window size and config!
# canvas = Canvas(window,width=550,height=800,bg="white")
# canvas.pack()


# Main = Label(text="Welcome to Message App!",bg="white",width=100,height=50)

# #Image related stuff!
# image = Image.open('MUBE.png')
# new_image = image.resize((100,100))
# new_image.save('resized_MUBE.png')
# img = PhotoImage(file="resized_MUBE.png")
# canvas.create_image(225,25,anchor=NW,image=img)

# # Send Button!
# button = Button(
#     text="Send Message",
#     width=10,
#     height=5,
#     bg="green",
#     fg="white",
#     command=send_msg
# ).place(x=238,y=700)

# #Text Field
# tekst = Text(
#     width=70,
#     height=30
# ).place(x=30,y=190)


# my_menu = Menu(window)
# window.config(menu=my_menu)


# def connect_as_client():
#     # s = socket(AF_INET, SOCK_STREAM)
#     # s.connect(('192.168.1.51', 5000))
#     # print("client is connected")
#     # print("what do you want to send!")
#     # inp = input()
#     # mesg = inp.encode('utf-8')
#     # s.sendto(mesg,('192.168.1.51',5000))

#     # data = s.recv(1024)
#     # print('Received', data)
#     # s.close()
#     # s = socket(AF_INET, SOCK_STREAM)
#     # s.connect(('localhost', 5000))
#     # tekst.insert(END,"Client is connected")
#     # #print("Client is connected")

#     # s.send(b'Hello, world')

#     # data = s.recv(1024)
#     # #print('Received', data)
#     # self.tekst.insert(END, 'Received'+ data)
#     # s.close()
#     pass

# #Create a menu item
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="Connect to Chat", menu=file_menu)
# file_menu.add_command(label="Connect . . .",command=connect_as_client)


# msg = Entry(window,width=50, bg="blue")
# msg.pack()


# window.mainloop()
