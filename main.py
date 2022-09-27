# Before running this on a new computer/laptop,
# open Command Prompt and write the following:
# pip install pyautogui
# pip install pyperclip
# pip install os-sys
# pip install python-time
# pip install pillow
# pip install opencv-python


class TSS_Maintenance:
    import pyautogui
    import time
    import os
    import sys
    import pyperclip

    def __init__(self):
        self.os.chdir(r'C:\Users\Aimee\Pictures\TSS Maintainence')

    def Open_TSS(self, username, password):
        while True:
            location = self.pyautogui.locateOnScreen('CBH.png', confidence=0.75)
            location = self.pyautogui.center(location)
            x, y = location
            self.pyautogui.click(x, y)
            print('Remote Desktop is now in focus')
            location = self.pyautogui.locateOnScreen('Settings.png', confidence=0.9)
            if location != None:
                print('TSS is already open and in focus.')
                TSS_Maintenance().isbackup_window_ok()
                TSS_Maintenance().isrestore_window_ok()
            elif location == None:
                print('TSS is not open.')
                print('I will now check if it may be minimised.')
                location = self.pyautogui.locateOnScreen('TSS_Minimised_Taskbar_Icon.png', confidence=0.9)
                location2 = self.pyautogui.locateOnScreen('TSS_Just_Minimised_Taskbar_Icon.png', confidence=0.9)
                if location != None:
                    print('TSS is open but minimised.')
                    location = self.pyautogui.center(location)
                    x, y = location
                    self.pyautogui.click(x, y)
                    TSS_Maintenance().isbackup_window_ok()
                    TSS_Maintenance().isrestore_window_ok()
                elif location2 != None:
                    print('TSS is open but minimised.')
                    location = self.pyautogui.center(location)
                    x, y = location
                    self.pyautogui.click(x, y)
                    TSS_Maintenance().isbackup_window_ok()
                    TSS_Maintenance().isrestore_window_ok()
                else:
                    print('Cannot locate TSS on the taskbar at all')
                    while True:
                        location = self.pyautogui.locateOnScreen('Show_Remote_Desktop.png', confidence=0.9)
                        if location != None:
                            location = self.pyautogui.center(location)
                            x, y = location
                            self.pyautogui.click(x, y)
                            print('Desktop is now showing')
                            break
                    while True:
                        location = self.pyautogui.locateOnScreen('TSS_Desktop_Icon.png', confidence=0.9)
                        if location != None:
                            location = self.pyautogui.center(location)
                            x, y = location
                            self.pyautogui.moveTo(x, y)
                            self.pyautogui.click(clicks=2)
                            print('I have found TSS icon on desktop and have double-clicked it!')
                            break
                        else:
                            print('Computer is slow. Please wait.')
                    while True:
                        location = self.pyautogui.locateOnScreen('Settings.png', confidence=0.9)
                        if location != None:
                            print('TSS is now open')
                            TSS_Maintenance().isbackup_window_ok()
                            TSS_Maintenance().isrestore_window_ok()
                        else:
                            print('TSS has not opened yet. Please wait.')
                            location = self.pyautogui.locateOnScreen('TSS_Login.png', confidence=0.9)
                            if location != None:
                                print('Entering TSS Login details')
                                location = self.pyautogui.locateOnScreen('Username.png', confidence=0.9)
                                location = self.pyautogui.center(location)
                                x, y = location
                                self.pyautogui.click(x, y)
                                self.pyautogui.typewrite(username)
                                location = self.pyautogui.locateOnScreen('Password.png', confidence=0.9)
                                location = self.pyautogui.center(location)
                                x, y = location
                                self.pyautogui.click(x, y)
                                self.pyautogui.typewrite(password)
                                self.pyautogui.hotkey('enter')
                                TSS_Maintenance().isbackup_window_ok()
                                TSS_Maintenance().isrestore_window_ok()

    def isbackup_window_ok(self):
        while True:
            location = self.pyautogui.locateOnScreen('Settings.png', confidence=0.9)
            if location != None:
                print('TSS is now open')
                print('I will now check all users are out of TSS')
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                break
        while True:
            location = self.pyautogui.locateOnScreen('Backup.png', confidence=0.9)
            if location != None:
                print('Setting dropdown list is now open')
                print('I will now open the Backup window')
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                while True:
                    location = self.pyautogui.locateOnScreen('Backup_Window_Tab.png', confidence=0.9)
                    if location != None:
                        print('Backup window is now open')
                        break
                break
        counter = 0
        while counter < 5:
            if counter == 5:
                print('ERROR - Someone has TSS open!!! Cannot continue.')
                # take screenshot! Send myself email.
                exit(0)
            else:
                location = self.pyautogui.locateOnScreen('Backup_Window.png', confidence=0.9)
                if location != None:
                    print('Backup window is okay.')
                    break
                else:
                    print ('Backup window is NOT okay')
                    counter = counter + 1

    def isrestore_window_ok(self):
        while True:
            location = self.pyautogui.locateOnScreen('Backup_Window_Tab.png', confidence=0.9)
            if location != None:
                print('I will now close the Backup window')
                x = location.left + location.width - 10
                y = location.top + 10
                self.pyautogui.click(x, y)
                break
        while True:
            location = self.pyautogui.locateOnScreen('Settings.png', confidence=0.9)
            if location != None:
                print('Setting dropdown list is now open')
                print('I will now open the Restore window')
                location = self.pyautogui.center(location)
                x, y = location
                self.pyautogui.click(x, y)
                while True:
                    location = self.pyautogui.locateOnScreen('Restore.png', confidence=0.9)
                    if location != None:
                        location = self.pyautogui.center(location)
                        x, y = location
                        self.pyautogui.click(x, y)
                        while True:
                            location = self.pyautogui.locateOnScreen('Restore_Window_Tab.png', confidence=0.9)
                            if location != None:
                                print('Restore window is now open')
                                break
                        break
                break
        counter = 0
        while counter < 5:
            if counter == 5:
                print('ERROR - Someone has TSS open!!! Cannot continue.')
                # take screenshot! Send myself email.
                exit(0)
            else:
                location = self.pyautogui.locateOnScreen('Restore_Window.png', confidence=0.9)
                if location != None:
                    print('Restore window is okay.')
                    exit(0)
                else:
                    print('Restore window is NOT okay.')
                    counter = counter + 1



        # while True:
        #     location = self.pyautogui.locateOnScreen('Backup_Window.png', confidence=0.9)
        #     if location != None:
        #         print('TSS is now open')
        #         print('I will now check all users are out of TSS')
        #         location = self.pyautogui.center(location)
        #         x, y = location
        #         self.pyautogui.click(x, y)
        #         break
        #
        # while True:
        #     location = self.pyautogui.locateOnScreen('Restore.png', confidence=0.9)
        #     if location != None:
        #         print('TSS is now open')
        #         print('I will now check all users are out of TSS')
        #         location = self.pyautogui.center(location)
        #         x, y = location
        #         self.pyautogui.click(x, y)
        #         break
        #
        # while True:
        #     location = self.pyautogui.locateOnScreen('Restore_Window.png', confidence=0.9)
        #     if location != None:
        #         print('TSS is now open')
        #         print('I will now check all users are out of TSS')
        #         location = self.pyautogui.center(location)
        #         x, y = location
        #         self.pyautogui.click(x, y)
        #         break



                #Remove_Job_Correspondence_Item_History
                #     print('I will now open it.')
                #     op = self.pyautogui.center(op)
                #     x, y = op
                #     self.pyautogui.moveTo(x, y)
                #     self.pyautogui.click(clicks=2)
                # else:
                #     print('I cannot see the remote server window on my desktop.')
                #     print('I will now check if it is already open but out of focus')
                #     op = self.pyautogui.locateOnScreen('OpenTSS_From_Taskbar2.png', confidence=0.9)
                #     if op != None:
                #         print('The remote server is open but out of focus')
                #
                #         def focusit():
                #             op = self.pyautogui.center(op)
                #             x, y = op
                #             self.pyautogui.click(x, y)
                #             print('The remote server should now be in focus.')
                #
                #         op = self.pyautogui.locateOnScreen('OpenTSS_From_Desktop.png', confidence=0.9)
                #     else:
                #         print('The remote server is not open at all.')
                #
                # TSS_Maintenance.showmydesktop()
                #         print('My desktop is now showing.')

TSS_Maintenance().Open_TSS('AIMEE', 'Casa7700')