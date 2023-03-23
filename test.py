import ctypes
from time import sleep
from win10toast_click import ToastNotifier

notification = ToastNotifier()


def showNotification():
    notification.show_toast("Locking", "You choosed lock your PC", duration=3)


def lock_screen():
    '''locking screen function'''
    ctypes.windll.user32.LockWorkStation()


inputShut = input("Do you wanna lock your pc ? (yes/no): ")

if inputShut == 'yes':
    showNotification()
    lock_screen()
else:
    print("Leaving the program!")
    exit()
