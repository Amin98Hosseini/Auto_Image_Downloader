from pygoogle_image import image as pi
import tkinter
import tkinter.messagebox
import customtkinter
import tkinter as tk
from tkinter import ttk
from customtkinter import filedialog as fd
from CTkMessagebox import CTkMessagebox
import os
import sys
import threading
import ctypes
import webbrowser


url = "https://github.com/Amin98Hosseini"

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


'''class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label_Toplevel = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label_Toplevel.pack(padx=20, pady=20)'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.directory = "Configuration"
        # Parent Directory path
        self.parent_dir = os.getcwd()
        # Path
        self.path = os.path.join(self.parent_dir, self.directory)
        # Create the directory
        # 'GeeksForGeeks' in
        # '/home / User / Documents'
        try: 
            os.mkdir(self.path) 
            print("Directory '% s' created" % self.directory)
        except OSError as error: 
            print("Directory is created")  
                
        

        # configure window
        self.title("Image Datasets Downloader V1.0.1")
        self.geometry(f"{720}x{480}")

        self.iconbitmap(r'download.ico')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3,4), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.resizable(False, False)
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Configuration", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
        

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Information", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=5, column=0, padx=20, pady=10)


        self.restart_label = customtkinter.CTkLabel(self.sidebar_frame, text="Restart App:", anchor="w")
        self.restart_label.grid(row=3, column=0, padx=20, pady=(10, 0))


        self.restart_button = customtkinter.CTkButton(self.sidebar_frame, text="Restart App", command=self.restart_app)
        self.restart_button.grid(row=4, column=0, padx=20, pady=(10, 20))



        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=60,height=200)
        self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(10, 5), sticky="nsew",columnspan=2)

        self.main_button_1_label = customtkinter.CTkLabel(self, text="         Make Config File ", anchor="w")
        self.main_button_1_label.grid(row=1, column=1, padx=5, pady=(5, 0))
        self.main_button_1_label.place(x=200 , y=300)

        self.main_button_1 = customtkinter.CTkButton(master=self, border_width=2, text="Make File" , command=self.Make_Text)
        self.main_button_1.grid(row=1, column=1)
        self.main_button_1.place(x=200 , y=325)

        self.main_button_2_label = customtkinter.CTkLabel(self, text="         Make Config File ", anchor="w")
        self.main_button_2_label.grid(row=1, column=1, padx=5, pady=(5, 0))
        self.main_button_2_label.place(x=200 , y=355)

        self.main_button_2 = customtkinter.CTkButton(master=self, border_width=2, text="Load File" , command=self.Load_Text)
        self.main_button_2.grid(row=2, column=1)
        self.main_button_2.place(x=200 , y=380)


        self.optionmenu_1_label = customtkinter.CTkLabel(self, text="    Set Number Of Data ", anchor="w")
        self.optionmenu_1_label.grid(row=1, column=2, padx=5, pady=(5, 0))
        self.optionmenu_1_label.place(x=565 , y=300)


        self.optionmenu_1 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["2000", "3000", "4000","5000", "6000", "7000","8000", "9000", "10000"])
        self.optionmenu_1.grid(row=1, column=2, padx=(5, 5), pady=(5, 5))
        self.optionmenu_1.place(x=565 , y=325)

        self.optionmenu_2_label = customtkinter.CTkLabel(self, text="    Select Search Engine", anchor="w")
        self.optionmenu_2_label.grid(row=1, column=2, padx=5, pady=(5, 0))
        self.optionmenu_2_label.place(x=565 , y=355)

        self.optionmenu_2 = customtkinter.CTkOptionMenu(self, dynamic_resizing=False,
                                                        values=["Google", "Bing", "Yahoo"])
        self.optionmenu_2.grid(row=2, column=2, padx=(5, 5), pady=(5, 5))
        self.optionmenu_2.place(x=565 , y=380)

        self.progressbar_1_label = customtkinter.CTkLabel(self, text="Downloading", anchor="w" ,  font=customtkinter.CTkFont(size=15))
        self.progressbar_1_label.grid(row=1, column=2, padx=5, pady=(5, 0))
        self.progressbar_1_label.place(x=410 , y=420)

        self.progressbar_1 = customtkinter.CTkProgressBar(self,width=500,height=25)
        #self.progressbar_1.configure(mode="indeterminate")
        self.progressbar_1.grid(row=3, column=3, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.place(x=200 , y=450)
        self.progressbar_1.set(0)


        self.main_button_3 = customtkinter.CTkButton(master=self, border_width=2, text="Start" , width=90,height=85 , command=self.Start)
        self.main_button_3.grid(row=2, column=1)
        self.main_button_3.place(x=350 , y=325)

        self.main_button_4 = customtkinter.CTkButton(master=self, border_width=2, text="Stop" , width=90,height=85 , command=self.Stop)
        self.main_button_4.grid(row=2, column=1)
        self.main_button_4.place(x=465 , y=325)


        self.toplevel_window = None

    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def sidebar_button_event(self):
        print("sidebar_button click")
        new = 1
        webbrowser.open(url,new=new)
        '''if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it'''

    def Make_Text(self):
        print("Make")
        self.value = self.textbox.get("0.0", "end")
        print(self.value)
        f = open("Configuration/Data.txt", "w")
        f.write(self.value)
        f.close()


    def Load_Text(self):
        print("load")
        self.textbox.delete(0.0, 'end')
        # Specify the file types
        filetypes = (('text files', '*.txt'),
                    ('All files', '*.*'))
    
        # Show the open file dialog by specifying path
        f = fd.askopenfile(filetypes=filetypes,
                        initialdir=self.path)
        self.text=f.readlines()
        print(self.text)
        self.value=str(self.text)
        parts = eval(self.value)
        for self.part in parts:
            print(self.part.strip())
            self.Parameter=self.part.strip()+"\n"
            self.textbox.insert("0.0",self.Parameter)
            

    def Start(self):
        print("Start")
        state = self.optionmenu_1.get()
        state = str(state)
        
        state2 = self.optionmenu_2.get()
        state2 = str(state2)
        if state2 != "Google" :
            msg = CTkMessagebox(title="Warning Message!", message="Please Select Google Search Engine ",
                  icon="warning", option_1="Cancel", option_2="Retry")
            self.flag=0
    
            if msg.get()=="Retry":
                self.Start()
                self.flag=0

        else :
            self.flag=1
        
        if self.flag ==1 :
            print("Number of download : "+state)
            print("Search Engine : "+state2)

            self.limit_number=int(state)
            

            Data_List = []
            Data_List = [word.strip() for word in self.text]

            self.data_len = len(Data_List)
            things = self.data_len * self.limit_number


            print(things)
            self.t0=threading.Thread(target=self.Image_Downloader,args=(Data_List,self.limit_number),daemon=True)
            self.t0.start()
        else :
            print("Search Engine Is Not Google!")
        

        

        

    def Image_Downloader(self,Data_Name , Data_Limit):
        divider = 1 / self.data_len
        cnt = 0
        for value in Data_Name:
            print("\n")
            print(value)
            self.downloaded = pi.download(keywords=value, limit=Data_Limit)
            cnt = cnt + divider
            self.progressbar_1.set(cnt)
        self.progressbar_1.set(1)
            
            
        


    def Stop(self):
        print("Stop")
        thread_id = self.t0.ident
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
        print(self.t0.ident)
        print(self.t0.is_alive())

    def restart_app(self):
        print("restart")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)




if __name__ == "__main__":
    os.system('cls')
    app = App()
    app.mainloop()
