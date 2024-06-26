# ui libs
import customtkinter  # tkinterV2 (with better ui)
import os
import tkinter
import tkinter.messagebox
from PIL import Image
# math libs
import time
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # plotting a graph into a frame


# usb / bluetooth controller libs

# global variables
global start
start = time.time()
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # images (loads images with light and dark mode image)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "test_logo.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "test_image.jpg")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "test_large_logo.jpg")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame (sidebar)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  FosterLab  ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Data",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Config. Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame (Set Up - check for components)
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        # Button 1 (Usage Undefined)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Button 1", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_1.place(relx=0.3, rely=0.4, anchor=tkinter.E)
        # Button 2 (Usage Undefined)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Button 2", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_2.place(relx=0.3, rely=0.465, anchor=tkinter.E)
        # Button 3 (Usage Undefined)
        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Button 3", image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_3.place(relx=0.3, rely=0.555, anchor=tkinter.E)
        # button  4 (Usage Undefined)
        self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="Button 4", image=self.image_icon_image, compound="bottom")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_button_4.place(relx=0.3, rely=0.67, anchor=tkinter.E)

        # create second frame (DATA TAB)
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        # self.textbox = customtkinter.CTkTextbox(self.second_frame, width=250)
        self.textbox = customtkinter.CTkTextbox(self.second_frame, width=250)
        self.label_tab_2 = customtkinter.CTkLabel(self.second_frame, text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
            # graphing
        # Graph Button (opens Matlab.ply and plots current data)
        self.second_frame_graph_button = customtkinter.CTkButton(self.second_frame, text="Graph Current Data",
                                                                 command=self.graph, image=self.image_icon_image,
                                                                 compound="top")
        self.second_frame_graph_button.place(relx=0.3, rely=0.1, anchor=tkinter.E)
        self.second_frame_display_text_button = customtkinter.CTkButton(self.second_frame, text="Post Rate",
                                                                 command=self.updateBox, image=self.image_icon_image,
                                                                 compound="top")
        self.second_frame_display_text_button.place(relx=0.3, rely=0.225, anchor=tkinter.E)

        # create third frame (Configs)
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame_update_config_button = customtkinter.CTkButton(self.third_frame, text="Apply Current Settings",
                                                                 command=self.configUpdate, image=self.image_icon_image,
                                                                 compound="top")
        self.third_frame_update_config_button.place(relx=0.3, rely=0.1, anchor=tkinter.E)
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def graph(self):
        data = None  # set up from config
        if not data:
            data = np.arange(0, 3, .01)  # x-values for sine curve between 0 and 3w
            plt.plot(data, 2 * np.sin(2 * np.pi * data))
            plt.show()
        else:
            for point in data: # assuming data is a pair of points in a csv
                plt.plot(point[0], point[1])
            plt.show()
        print("Updates Box")
    # calibration curves that takes the current across the 2 pairs of the voltmeters.  Read the application of the Howling Current. I = V/R
    def updateBox(self):
        self.textbox.insert("0.0", text=str(time.time()-start) + " ")
        print("Updates Box")

    def meanAvgVoltage(self):
        # taking from the 4 voltage readings measure the voltage across the pair.
        return 0
    def setVoltage(self, appliedEqualsExperimental): # mode is an true or false, true represents that the voltage applied to the circuits will match
        # the value that is supposed to be applied and reduce the small errors that occur (slower than keeping it false)
        if appliedEqualsExperimental == False:
            return
        else:
            return
        return 0
    def voltageCorrection(self): # helper function for voltage. returns the voiltage after a correction
        return 0
    def configUpdate(self): # checks all the accessable variables on the current screen and updates them if the tab is then changed
        if (name == "home"): # on home it is used to check warning settings and if the device is plugged in
            return 0
        if (name == "frame_2"):
            return 0
        if (name == "frame_3"):
            return 0

if __name__ == "__main__":
    app = App()
    app.mainloop()
