import time
from colorama import Fore, Style

mmdrza = '''
███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
 --------- x4@mmdrza.com ----------- Mmdrza.Com ------------- Dev.to/mmdrza ------------                                                                                    
'''
print(Fore.YELLOW, mmdrza)
stx = "Insert Word For first character hasher create Next Section Entered ...\n\n\n\n\n\n\n"
stt = Fore.GREEN + stx
for sta in stt:
    print(sta, end='', flush=True)
    time.sleep(.11)

chrc = input("Insert First Character Value = >>>  ")
how = input("How Many Needed (JUST ENTER NUMBER) = >>> ")
print(Fore.YELLOW, "\n========================[ M M D R Z A . C o M ]========================\n")
z = 1
while z <= int(how):
    print(Fore.YELLOW + str(chrc) + str(z) + " = str(random.choice('123456789abcdefABCDEF'))")
    z += 1
    f = open("print.txt", "a")
    f.write(str(chrc) + str(z) + " = str(random.choice('123456789abcdefABCDEF'))\n")
    f.close()
    fg = open("printstr.txt", "a")
    fg.write('str(' + str(chrc) + str(z) + ') + ')
    fg.close()
chap1 = "\n\n\n Your Data Code Created On This File -> print.txt \n For Donate Programmer = Bitcoin Address : " \
       "16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8 \n Website : Mmdrza.Com \n Email : X4@Mmdrza.Com\n " \
       "------------------------------------------\n\n\n\n\n\n"
chap = Fore.WHITE, str(chap1)
for stq in chap:
    print(stq, end='', flush=True)
    time.sleep(.01)
