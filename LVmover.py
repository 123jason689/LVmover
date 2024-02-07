import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
import shutil
import re

class App():
    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry('600x400')
        self.root.iconbitmap('L.ico')
        self.root.title('LVmover')
        self.mainframe = tk.Frame(self.root, background='SlateBlue')
        self.mainframe.pack(fill='both', expand=True)

        self.default_none = 'Unknown'
        self.from_info = self.default_none
        self.to_info = self.default_none
        # self.tto_info = {
        #     ".html": self.default_none,
        #     ".css": self.default_none,
        #     ".js": self.default_none,
        #     "img": self.default_none,
        #     "video": self.default_none,
        #     "audio": self.default_none,
        # }
        self.to_info_resource = self.default_none
        self.path_sep = os.path.sep
        self.file_ext = ('.html', '.css', '.js', '.blade.php', '.php', '.py')
        self.audio = ('.mp3', '.wav', '.aif', '.mid', '.midi', '.mpa', '.ogg', '.wma', '.flac', '.m4a', '.ape')
        self.video = ('.webm','.mpg', '.mp2', '.mpeg', '.mpe', '.mpv','.ogg','.mp4', '.m4p', '.m4v','.avi','.wmv','.mov', '.qt','.flv', '.swf','.mkv','.vob','.rmvb')
        self.img = ('.jpeg', '.jpg', '.jpe', '.jif', '.jfif', '.jfi','.png','.gif','.tiff', '.tif','.psd','.pdf','.eps','.ai','.indd','.heif', '.heic','.svg','.bmp','.webp','.raw')

        self.style = ttk.Style()
        self.style.configure("frameColor.TFrame", background='SlateBlue')
        self.style.configure("reset.TButton", background='Magenta', foreground='Red')

        self.h1title = ttk.Label(self.mainframe, text='LVmover', background='SlateBlue', font=("Poppins", 40), anchor='w')
        self.h1title.grid(row=0,column=0)

        # shows info for path
        self.infframe = ttk.Frame(self.mainframe, style='frameColor.TFrame')
        self.infframe.grid(row=1, column=0, pady=5)

        self.info = ttk.Label(self.infframe, text= "Move from", background='SlateBlue', font=('Poppins', 10))
        self.info.grid(row=0,column=0,pady=10)
        self.info1 = ttk.Label(self.infframe, text= self.from_info, background='Plum', font=('Poppins',7))
        self.info1.grid(row=0,column=1,pady=10, padx=5)
        self.info2 = ttk.Label(self.infframe, text= "to", background='SlateBlue', font=('Poppins', 10))
        self.info2.grid(row=0,column=2,pady=10)
        self.info3 = ttk.Label(self.infframe, text= self.to_info, background='Plum', font=('Poppins', 7))
        self.info3.grid(row=0,column=3,pady=10, padx=5)
        self.info4 = ttk.Button(self.infframe, text='Reset', command=self.resetpath,style='reset.TButton', width=0)
        self.info4.grid(row=0, column=4, pady=5, padx=10, sticky='W')
        # end

        # input field
        self.inputframe = ttk.Frame(self.mainframe, style='frameColor.TFrame')
        self.inputframe.grid(row=2, column=0, pady=5)

        # source
        self.src_field= ttk.Label(self.inputframe, text='Source path:', background='SlateBlue', font=('Poppins', 15))
        self.src_field.grid(row=0, column=0, pady=5, padx=10)

        self.src_field= ttk.Label(self.inputframe, text='Choose source Path', background='PaleTurquoise', font=('Calibri', 10))
        self.src_field.grid(row=0, column=1, pady=5,sticky='NWES')

        self.set_path = ttk.Button(self.inputframe, text='Select', command=lambda:self.setpath('src'))
        self.set_path.grid(row=0, column=2, pady=5, padx=10)
        
        # destination
        self.dst_f= ttk.Label(self.inputframe, text='Destination Path:', background='SlateBlue', font=('Poppins', 15))
        self.dst_f.grid(row=1, column=0, pady=5, padx=10)

        self.dst_f= ttk.Label(self.inputframe, text='Choose Dest Path', background='PaleTurquoise', font=('Calibri', 10))
        self.dst_f.grid(row=1, column=1, pady=5,sticky='NWES')

        self.set_dest = ttk.Button(self.inputframe, text='Select', command=lambda:self.setpath('dst'))
        self.set_dest.grid(row=1, column=2, pady=5, padx=10)

        # resource destination
        self.dst_rsc= ttk.Label(self.inputframe, text='Dest Resource Folder:', background='SlateBlue', font=('Poppins', 15))
        self.dst_rsc.grid(row=2, column=0, pady=5, padx=10)

        self.dst_rsc= ttk.Label(self.inputframe, text='Choose Dest Resource Path', background='PaleTurquoise', font=('Calibri', 10))
        self.dst_rsc.grid(row=2, column=1, pady=5,sticky='NWES')

        self.set_rsc = ttk.Button(self.inputframe, text='Select', command=lambda:self.setpath('rsc'))
        self.set_rsc.grid(row=2, column=2, pady=5, padx=10)

        # end

        # Start process
        self.set_dest = ttk.Button(self.mainframe, text='Start', command=self.movnconv)
        self.set_dest.grid(row=4, column=0, pady=20, padx=10)

        self.path_warn= ttk.Label(self.mainframe, text='Path not complete!', background='Tomato', font=('Calibri', 15))
        self.path_warn.grid(row=5, column=0, pady=25, sticky='N')

        self.root.mainloop()
        return
    
    def select_directory(self):
        self.root.withdraw()  # Hide the main window.
        directory = filedialog.askdirectory()  # Show the dialog and get the chosen directory.
        self.root.deiconify()  # Make the main window reappear.
        return os.path.normpath(directory)
    
    def setpath(self, typ):
        direc = self.select_directory()
        if direc != None:
            if typ == 'src':
                self.from_info = direc
            elif typ == 'dst':
                self.to_info = direc
            elif typ == 'rsc':
                self.to_info_resource = direc
        self.updateInf()

    def updateInf(self):
        self.info1.config(text= self.truncatePath(self.from_info))
        self.info3.config(text=self.truncatePath(self.to_info))
        self.src_field.config(text= self.truncatePath(self.from_info))
        self.dst_f.config(text= self.truncatePath(self.to_info))
        self.dst_rsc.config(text= self.truncatePath(self.to_info_resource))

    def truncatePath(self, string):
        if len(string)>30:
            ar = string.split(self.path_sep)
            for i in range(1,4):
                if len(ar[-i])>10:
                    ar[-i]=ar[-i][:3]+'...'+ar[-i][-3:]
                else:
                    continue
            ar = [ar[0],'...']+ar[-3:]
            return self.path_sep.join(ar)
        else:
            return string

    def resetpath(self):
        self.from_info = self.default_none
        self.to_info = self.default_none
        self.to_info_resource = self.default_none
        self.updateInf()

    def movnconv(self):
        if not self.to_info==self.default_none and not self.from_info==self.default_none and not self.to_info_resource==self.default_none:
            self.path_warn.grid_remove()
            self.rSearchFile(self.from_info)
        else:
            self.path_warn.grid()

    def rSearchFile(self,curpath):
        for file in os.listdir(curpath):
            full_path = os.path.join(curpath, file)
            # full_path = os.path.normpath(full_path)

            if full_path.endswith('.git'):
                continue
            elif os.path.isdir(full_path):
                self.rSearchFile(full_path)
            else:
                file_type = '.'.join(file.split('.')[1:]) if len(file.split('.')) >= 1 else '.'+file.split('.')[:-1]
                # file_type = '"'+file_type+'"'
                if '.'+file_type == '.html': #changing html to blade
                    destdir =self.path_sep.join(full_path.replace(self.from_info, self.to_info).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                        # #print(destdir)
                    shutil.copy2(full_path, destdir)
                    new_full_html = os.path.normpath(os.path.join(destdir, file))
                    with open(new_full_html, "r", encoding='utf-8') as html:
                        html_content = html.read()

                    # Define a regular expression pattern to match tags with href or src attributes
                    pattern = re.compile(r'<\s*\w+\s+[^>]*(?:href|src)=["\']((?!http[s]?://|#\s*(?:[^/\s]|$))[^"\']*)["\'][^>]*>')
                    # Replace each match with the modified path
                    modified_content = re.sub(pattern, lambda match: self.replace_section(full_path, match=match), html_content)

                    # modified content write to file
                    with open(new_full_html, "w", encoding="utf-8") as htmls:
                        htmls.write(modified_content)

                elif '.'+file_type == '.css':
                    destdir =self.path_sep.join(full_path.replace(self.from_info, os.path.join(self.to_info_resource, file_type)).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                    #print(destdir)
                    shutil.copy2(full_path, destdir)
                elif '.'+file_type == '.js':
                    destdir =self.path_sep.join(full_path.replace(self.from_info, os.path.join(self.to_info_resource, file_type)).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                    #print(destdir)
                    shutil.copy2(full_path, destdir)
                elif '.'+file_type in self.img:
                    destdir =self.path_sep.join(full_path.replace(self.from_info, os.path.join(self.to_info_resource, 'asset')).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                    #print(destdir)
                    shutil.copy2(full_path, destdir)
                elif '.'+file_type in self.video:
                    destdir =self.path_sep.join(full_path.replace(self.from_info, os.path.join(self.to_info_resource, 'asset')).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                    #print(destdir)
                    shutil.copy2(full_path, destdir)
                elif '.'+file_type in self.audio:
                    destdir =self.path_sep.join(full_path.replace(self.from_info, os.path.join(self.to_info_resource, 'asset')).split(self.path_sep)[:-1])
                    if not os.path.exists(destdir):
                        os.makedirs(os.path.normpath(destdir))
                    #print(destdir)
                    shutil.copy2(full_path, destdir)
                # print(file_type)
            # print(full_path)
        # print("\n")
    
    def modifpath(self,old_path, html_path, file_ext):
        # Your custom logic to modify the old path
        # Replace this with your actual modification logic
        old_path = os.path.normpath(old_path)
        html_dir = os.path.normpath(os.path.dirname(html_path))
        if os.path.isabs(old_path):
        # Remove the first path separator to make it relative
            old_path = old_path.lstrip(os.path.sep)
            
        file_path = os.path.normpath(os.path.join(html_dir, old_path))
        new_path_html = os.path.normpath(html_path.replace(self.from_info, self.to_info))
        new_path_file = os.path.normpath(file_path.replace(self.from_info, os.path.join(self.to_info_resource,file_ext)))
        relpath = os.path.relpath(new_path_file, start=os.path.dirname(new_path_html))
        # print('html='+new_path_html)
        # print('file='+new_path_file)
        # print('file_path='+file_path)
        # print('rel='+relpath)
        # print(os.path.join(html_dir, old_path) + "<--->" + html_dir+ "<--->" + old_path)
        # print(os.path.join(self.to_info_resource,file_ext) + "<--->" + self.to_info_resource + "<--->" + file_ext)
        # print(old_path)
        # print("\n\n")
        
        return relpath 

    def replace_section(self,html_path,match):
        full_match = match.group(0)
        old_path = match.group(1)
        typ = '.' + '.'.join(old_path.split(self.path_sep)[-1].split('.')[1:])
        file_ext = '~UNKNOWN~'
        if typ == '.css':
            file_ext = 'css'
        elif typ == '.js':
            file_ext = 'js'
        elif typ == '.html':
            return full_match
        elif typ in self.img or typ in self.video or typ in self.audio:
            file_ext = 'asset'
        else:
            return old_path
        new_path = self.modifpath(old_path, html_path, file_ext)
        return full_match.replace(old_path, new_path)
    


if __name__ == '__main__':
    App()