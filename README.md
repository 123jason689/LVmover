# LVmover

This is a mini app for making the life of moving html,css,js,assets file into other folders EASIER

This app finds every html file, creates the directory mimic-ing the original directory paths (folder and subfolders) and move it to the destination file. This app also capable of automatically changing the html routing (href's or src's relative paths) inside the html file to route from the new html destination folder to the resource folder (contains css,js,assets folder) eventhough they are separated. If the destination resource path does not contain any folder named css, js, or assets, it will automatically creates it.

Usefull for:
1. Moving front end files (pure html, css, js projects) to other projects folder
2. Automatically creates a separate folders for css, js, and asset files
3. Automatically change the routing/relative paths of css, js, or asset files inside the html files
4. DFS(Depth First Search) searching from the source path/folder(source front end project or other project containing html files) and moving it to other folders(destination path)
5. Automatically mimic the origin(source) path/folder's directories structure and moving the html,css,js,assets file to the simmilar directory inside the destination path

There is a short cut file in the repo that runs the app, you can either run the app from that shortcut or make another shortcut to the shortcut or find the original .exe file

App is still under development and uncertained.
