import os
import curses
import requests
import shutil
eula_txt = "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#and also agreeing that tacos are tasty and you used mcserversetup.\n#timaaos is sus!\neula=true"
command_to_start = "java -jar server.jar"
conf_softtype = "none"
conf_ver = "none"
def startSetup():
    if os.path.exists(os.path.abspath(os.getcwd()) + '\\SERVER\\'):
        shutil.rmtree(os.path.abspath(os.getcwd()) + '\\SERVER\\')
    os.mkdir(os.path.abspath(os.getcwd()) + '\\SERVER\\')
    global conf_softtype
    global conf_ver
    if conf_softtype == 'vanilla':
        url = 'https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar'
        r = requests.get(url, allow_redirects=True)
        open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
        open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt,'utf8'))
        open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start,'utf8'))
        open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start,'utf8'))
    if conf_softtype == 'paper':
        if conf_ver == '1.8.9':
            url = 'https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
        if conf_ver == '1.12.2':
            url = 'https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
        if conf_ver == '1.16.5':
            url = 'https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/762/downloads/paper-1.16.5-762.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
    if conf_softtype == 'spigot':
        if conf_ver == '1.8.9':
            url = 'https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
        if conf_ver == '1.12.2':
            url = 'https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
        if conf_ver == '1.16.5':
            url = 'https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar'
            r = requests.get(url, allow_redirects=True)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\server.jar', 'wb').write(r.content)
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\eula.txt', 'wb').write(bytes(eula_txt, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.sh', 'wb').write(bytes(command_to_start, 'utf8'))
            open(os.path.abspath(os.getcwd()) + '\\SERVER\\start.bat', 'wb').write(bytes(command_to_start, 'utf8'))
    for i in range(25):
        print("GO TO: " + os.path.abspath(os.getcwd()) + '\\SERVER\\' + ' AND COLLECT FILES')
    exit(0)
def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()
    height, width = stdscr.getmaxyx()
    title = "MC Server Setup"[:width - 1]
    subtitle = "Setup minecraft server with easy"[:width - 1]
    statusbarstr = "Press q to exit. Press w to start.".format(cursor_x, cursor_y)
    stage = 'menu'
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # Loop where k is the last character pressed
    while (k != ord('q')):
        global conf_softtype
        global conf_ver
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == ord('w') and stage == 'menu':
            title = "Select server software!"
            subtitle = "1) Spigot 2) Paper 3) Vanilla"
            stage = 'softsel'
        if k == ord('1'):
            if stage == 'softsel':
                conf_softtype = 'spigot'
                title = "Select minecraft version!"
                subtitle = "1) 1.8.9  2) 1.12.2  3) 1.16.5"
                stage = 'versel'
            elif stage == 'versel':
                conf_ver = '1.8.9'
                title = "Is it right and are you accepting Mojang's EULA?"
                subtitle = "Software: " + conf_softtype + " MC Version: " + conf_ver
                statusbarstr = "Press q to exit. Press Yes or No (y or n)"
                stage = 'donesel'
        if k == ord('2'):
            if stage == 'softsel':
                conf_softtype = 'paper'
                title = "Select minecraft version!"
                subtitle = "1) 1.8.9  2) 1.12.2  3) 1.16.5"
                stage = 'versel'
            elif stage == 'versel':
                conf_ver = '1.12.2'
                title = "Is it right and are you accepting Mojang's EULA?"
                subtitle = "Software: " + conf_softtype + " MC Version: " + conf_ver
                statusbarstr = "Press q to exit. Press Yes or No (y or n)"
                stage = 'donesel'
        if k == ord('3'):
            if stage == 'softsel':
                conf_softtype = 'vanilla'
                conf_ver = 'latest'
                title = "Is it right?"
                subtitle = "Software: " + conf_softtype + " MC Version: " + conf_ver
                statusbarstr = "Press q to exit. Press Yes or No (y or n)"
                stage = 'donesel'
            elif stage == 'versel':
                conf_ver = '1.16.5'
                title = "Is it right and are you accepting Mojang's EULA?"
                subtitle = "Software: " + conf_softtype + " MC Version: " + conf_ver
                statusbarstr = "Press q to exit. Press Yes or No (y or n)"
                stage = 'donesel'
        if k == ord('y') and stage == 'donesel':
            title = "Downloading and installing mc server!"
            subtitle = "When done this program will close, copy content of folder SERVER to your folder"
        if k == ord('n') and stage == 'donesel':
            break
        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings


        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, start_x_subtitle, subtitle)
        stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()
        if k == ord('y') and stage == 'donesel':
            startSetup()
        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()