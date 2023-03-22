import ctypes


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


inputShut = input("Do you wanna lock your pc ? (yes/no): ")

if inputShut == 'yes':
    print("Locking your PC!")
    lock_screen()
else:
    print("Leaving the program!")
    exit()
