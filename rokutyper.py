#!/usr/bin/evn python

# By: Clempton
# 9/17/21

import os
import subprocess

# Moves the cursor back to the a position
def gethome(up,left,count_r, count_c):

    for n in range(0,count_r):
        os.system(left)
    for n in range(0,count_c):
        os.system(up)
    return

# Moves the cursor to correct row
def leftright(row_mov,left,right):
    
    # Finds correct number of shifts left or right
    t = abs(row_mov)
    count = 0
    while t != 0:
        if row_mov < 0:
            os.system(left)
            count = count - 1
        else:
            os.system(right)
            count = count + 1
        t = t - 1

    return(count)
# Moves the cursor to the correct column
def updown(col_mov,up,down):

    # Finds correct number of shifts up or down
    t = abs(col_mov)
    count = 0
    while t !=0:
        if col_mov < 0:
            os.system(up)
            count = count - 1
        else:
            os.system(down)
            count = count + 1
        t = t - 1

    return(count)

def printer(message,up,down,right,left,select):

    cur_pos = 0
    # Counts positions of rows and columns at end of letter
    count_r = 0
    count_c = 0

    # Representation of the Roku keyboard
    board = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
    'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,
    'm':12,'n':13,'o':14,'p':15,'q':16,'r':17,
    's':18,'t':19,'u':20,'v':21,'w':22,'x':23,
    'y':24,'z':25,'1':26,'2':27,'3':28,'4':29,
    '5':30,'6':31,'7':32,'8':33,'9':34,'0':35,
    '~':36,'!':37,' ':38,'@':39,'bck':40,'$':41
    }
    
    # Finds letter in message and matches it to value in keyboard
    for letter in message:
        active = board.get(letter)
        
        # Prints working letter in message 
        print("   >>> Typing: " + letter)

        # Check to make sure letter isnt the same as pervious letter    
        if(active != cur_pos):
            
            # Calculates number of moves
            col_mov = (active//6)-(cur_pos//6)
            row_mov = (active%6)-(cur_pos%6)

            # Fixes problem with bottom row only having 3 buttons
            if(letter==' ' or letter=='~'):
                count_r = count_r + leftright(row_mov,left,right)
                count_c = count_c + updown(col_mov,up,down)
            else:
                count_c = count_c + updown(col_mov,up,down)
                count_r = count_r + leftright(row_mov,left,right)
        os.system(select)
        
        # Updates position of cursor to be correct for the next letter
        cur_pos = active
    gethome(up,left,count_r, count_c)
        
    return()

# Main Function
def main():
    print("""
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @,,,,,,,,,,,,,,,                                                                
    @,,,,,,    ,,,,,,,        ,,,,,                                               , 
    @,,,,,,     .,,,,,,  ,,,,,,,,,,,,,,    ,,,,,,     ,,,,,,,  ,,,,,,     ,,,,,,.   
    @,,,,,,     ,,,,,,  ,,,,,,,   ,,,,,,,  ,,,,,,  ,,,,,,,,    ,,,,,,     ,,,,,,.   
    @,,,,,,,,,,,,,,,,  ,,,,,,      ,,,,,,, ,,,,,,,,,,,,,       ,,,,,,     ,,,,,,.   
    @,,,,,,,,,,,,,,    ,,,,,,      ,,,,,,, ,,,,,,,,,,,,,       ,,,,,,     ,,,,,,.   
    @,,,,,,   ,,,,,,,  ,,,,,,,    ,,,,,,,  ,,,,,,  ,,,,,,,,    ,,,,,,     ,,,,,,.   
    @,,,,,,     ,,,,,,,  ,,,,,,,,,,,,,,,   ,,,,,,    ,,,,,,,,  ,,,,,,,,,,,,,,,,,.   
    @,,,,,,       ,,,,,,,   ,,,,,,,,,      ,,,,,,       ,,,,,,,,  ,,,,,,,,    ,,.  
    @ Typer
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    By: Clempton
    
    """)
    # Get IP address input
    try:
        IP = str(input("\nEnter Roku IP Address. If unknown, press enter for nmap scan automation: "))
    except KeyError:
        pass
    # Automates nmap search for Roku IP address onnetwork
    if IP == '':
        # Finds the gateway IP address
        proc = subprocess.Popen("ip route | grep -E -o \"default.+([0-9]{1,3}[\.]){3}[0-9]{1,3}\" | sed 's/^default via //'",shell=True, stdout=subprocess.PIPE)
        gateway = str(proc.communicate()[0].strip())[2:-1]
        print("Gateway found at: "+gateway)

        # Finds the Roku IP address on network from quick nmap scan 
        proc = subprocess.Popen("nmap -sP -n "+gateway+"/24 | grep -B 2 \"Roku\" | grep -E -o \"([0-9]{1,3}[\.]){3}[0-9]{1,3}\"",shell=True, stdout=subprocess.PIPE)
        IP = str(proc.communicate()[0].strip())[2:-1]
        print("Roku IP address found at: "+IP)

    # Curl request strings with IP address added
    # These are remote control button requests
    up ="curl -d '' \"http://"+IP+":8060/keypress/up\""
    down ="curl -d '' \"http://"+IP+":8060/keypress/down\""
    right = "curl -d '' \"http://"+IP+":8060/keypress/right\""
    left = "curl -d '' \"http://"+IP+":8060/keypress/left\""
    home ="curl -d '' \"http://"+IP+":8060/keypress/home\""
    select = "curl -d '' \"http://"+IP+":8060/keypress/select\""
    search = "curl -d '' \"http://"+IP+":8060/search/a\""

    # Operations to get to the search menu / keyboard
    os.system(home)
    os.system("sleep 2")
    os.system(search)
    os.system("sleep 2")

    while(1):
        # Get message text to be output
        message = str(input("\nEnter a message: ").lower())
        
        # Run printer methods
        printer(message,up,down,right,left,select)
    
    return()

# Calls the main() function
if __name__ == '__main__':
    main()