#system
import os

#install_Library
os.system('pip install rubika')
os.system('pip install time')
os.system('pip install random')
os.system('clear')

#import_Library
from rubika import Bot
from rubika.configs import reports
from time import sleep as sp
from random import choice

#baner
print(f'\033[31m')
from time import sleep
x = ("""

               .+=                                                                  ++=:  
       .   .:::#%%=--=--:::::::::::------.........................................:-====: 
     =--#**##%#######%###%%%########%%%%#***************************************++#######-
     -#%#***#%@@%**++++=======-----=-----***********==========----------------------=+#%#+
      *++%%%%@@@%%%%%%#%%###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###########*+=*##*-            Reporter GHOGHNOS
      :+@@@@@@@%@@@@@@%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%############*+=*#%+      CREATOR REPORTER : GHOGHNOS BLACK
     -+@@@@@@@@%@@@@@%%%%%%%%%%%%%%%%%%@%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%#############*+*##+             Reporter RUBIKA GOD
    .##%%%%%%%@@@@@@@%%%%%%%%%%@%@@@%%%%%%%@%%%%%@@@#%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%*###= 
  .-#@*%%%%%%%@@%%%%%%%%%%%%#*#@@@%########%%%%%%%@%*%%%%@@%#%##%%%%%%%%%%%%%%%%%%%#+*##= 
:+##%%*%%%%%@@@%%%%%%%%%%%%#+*%%%%%%%%%%%##%%%%%%%%@%%%%%%@######%%%%%%%%%%%##%%%%%%*:::. 
  ..:=**%%%@@%%%%%%%%%%%%%%*+#@@%%%%%%%%%##########%%%%%#*=-------::--:::-:. .::::-::     
      .-*#%%%%%%##%#%######*#%##+-:..+#%#-      .:=#%%%#:                                 
        =*%%%%%%%%%%%########**:      *#+           =###.                                 
        .###%%%%%%%%######*%**-       =#+            +##                                  
        :*##%%#%#%%%####**##**.        -#-           =#*                                  
       .**%#%%%%%######**%%%##=         :++:         *#+                                  
      :=*##%%%%%%%%##%**@%%**##+:         .-=:     :*#*-                                  
      -#*#%%%%%%%%####*+#%%###*++=-:::... ....:::--:.                                     
     :*+##%%%%%%%######*##*+=.        .:::::..                                            
    :=#####%%%%%%%#####*#*+=                                                              
    -#*######%#%######*#**+:                                                              
   :**################*#*++                                                               
  .=#################*#**+-                                                               
  -#*################***++                                                                
 :**##################*++-                                                                
 =*######%%#########*#+++:                                                                
.**#%%%%%%%##%######+#+++:                                                                
.**#%%%%%#########*++#+++-                                                                
 .+..*-*%%%%%%%%%%%####**+-                                                               
  .--:  ...::--==++*###*+==.                                                              


		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)


x = '\033[32m'

#Enter Values
auth = ""
key = ""

bot = Bot("APP",auth,key)

print("\033[31m")
guid = input("inter your target guid : ")
ran = int(input("inter your range : "))


#Select Report
print("\033[32m")
rep = input("""
            > Select Report >
            
            PORNOGRAPHY => 1
            FISHING     => 2
            SPAM        => 3
            COPYRIGHT   => 4
            VIOLENCE    => 5
            >>>>>>>>>>>>>>>>>>>>>>>>   """)

print("\033[33m")
if rep == '1':
    a = 0
    for i in range(ran):
        bot.reportChat(guid,reports.PORNOGRAPHY)
        print(f"report pornografy {a}")
        a+=1
        sp(.3)

elif rep == '2':
    b = 0
    for i in range(ran):
        bot.reportChat(guid,reports.FISHING)
        print(f"report fishing {b}")
        b+=1
        sp(.3)

elif rep == '2':
    c = 0
    for i in range(ran):
        bot.reportChat(guid,reports.SPAM)
        print(f"report spam {c}")
        c+=1
        sp(.3)

elif rep == '3':
    d = 0
    for i in range(ran):
        bot.reportChat(guid,reports.COPYRIGHT)
        print(f"report copyrite {d}")
        d+=1
        sp(.3)
    
elif rep == '4':
    e = 0
    for i in range(ran):
        bot.reportChat(guid,reports.VIOLENCE)
        print(f"report violence {e}")
        e+=1
        sp(.3)

elif rep == '5':
    f = 0
    r = input('Please type your report : ')
    list_f = [r]
    for i in range(ran):
        list_f = choice(list_f)
        bot.reportChat(guid,reports.OTHER,list_f)
        print(f,r)
        f+=1
        sp(.3)

else:
    print("You made a mistake.!!")

print("*" * 10)
print("  done !")
input("\n\nexit??\n\n")
