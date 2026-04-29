import os, time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress

# Board:
num = ['|  ','|','0','|','1','|','2','|','3','|','4','|','5','|','6','|','7','|','8','|','9','|']
line0 = ['| A','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line1 = ['| B','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line2 = ['| C','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line3 = ['| D','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line4 = ['| E','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line5 = ['| F','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line6 = ['| G','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line7 = ['| H','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line8 = ['| I','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']
line9 = ['| J','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']

lineMap = {
    'A': line0, 'B': line1, 'C': line2, 'D': line3, 'E': line4,
    'F': line5, 'G': line6, 'H': line7, 'I': line8, 'J': line9
} 
        
"""
Demonstration of Console.screen() 
"""

# Variables:
c = Console()

Destroyer = 2
Submarine = 3
Cruiser = 3
Battleship = 4
Carrier = 5 


# Functions + Procdef welcomeMessage():
def welcomeMessage():
    print('''
█▄▄ ▄▀█ ▀█▀ ▀█▀ █░░ █▀▀ █▀ █░█ █ █▀█ █▀
█▄█ █▀█ ░█░ ░█░ █▄▄ ██▄ ▄█ █▀█ █ █▀▀ ▄█

''')

def cls():
    os.system("clear")

def loadingScreen():
    fft_size=1000
    end_str = '\r'
    for i in range(0,10):
        fft_size = 2**(i%10)
        if(i%10 == 9):
            end_str = '\n'
        else:
            end_str = '\r'
        print(f"\r{i: >9} | {fft_size: >9} | LOADING",end=end_str,flush=True)
        time.sleep(0.1)

        cls()
    
    with Progress() as progress:

        task1 = progress.add_task("[red]Building Ships...", total=100)
        time.sleep(1)
        task2 = progress.add_task("[green]Creating Waters...", total=120)
        time.sleep(1)
        task3 = progress.add_task("[cyan]Preparing Shells...", total=75)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.4)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)

    time.sleep(1)
    cls()
    time.sleep(1)

def boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9):
    for line in [num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9]:
        time.sleep(0.1)
        joined = ''.join(item.center(3) if item == '|' else item for item in line)
        c.print(joined)

def submarinePlacing():

    print('''
    A Submarine takes up 3 places:

        |   |   |   |
        | * - * - * |
        |   |   |   |

    ''')
    submarinePlacementLetValid = False
    while submarinePlacementLetValid == False:
        submarinePlacementLet = input("Where do you want to place your submarine [letter]?")
        if submarinePlacementLet in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'):
            submarinePlacementLetValid = True
        else:
            pass
    
    cls()
    selectedLine = lineMap[submarinePlacementLet.upper()]
    for i in range(2, 21, 2):
        selectedLine[i] = f'[green]-[/green]'
    welcomeMessage()
    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)


    submarinePlacementNumValid = False
    while submarinePlacementNumValid == False:
        try:
            submarinePlacementNum = int(input("Where do you want to place your submarine [number]?"))
            submarinePlacementNumValid = True
            if (submarinePlacementNum > 9) or (submarinePlacementNum < 0):
                submarinePlacementNum = False
            else:
                pass
        except:
            pass

    cls()
    for i in range(2, 21, 2):
        selectedLine[i] = ' '
    selectedLine[submarinePlacementNum * 2 + 2] = f'[green]+[/green]'
    welcomeMessage()
    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
    

    if submarinePlacementLet.upper() == 'A':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line0[submarinePlacementNum * 2 + 2] = '*'
                    line0[submarinePlacementNum * 2 + 3] = '-'
                    line0[submarinePlacementNum * 2 + 4] = '*'
                    line0[submarinePlacementNum * 2 + 5] = '-'
                    line0[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line0[submarinePlacementNum * 2 + 2] = '*'
                    line0[submarinePlacementNum * 2 + 1] = ' '
                    line0[submarinePlacementNum * 2 + 0] = '*'
                    line0[submarinePlacementNum * 2 - 1] = ' '
                    line0[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':
                    print('ERROR NOT POSSIBLE')
                    welcomeMessage()
                    submarinePlacing()
                elif subDirection.lower() == 'down':
                    line0[submarinePlacementNum * 2 + 2] = '*'
                    line1[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'B':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line1[submarinePlacementNum * 2 + 2] += '*'
                    line1[submarinePlacementNum * 2 + 3] += '-'
                    line1[submarinePlacementNum * 2 + 4] += '*'
                    line1[submarinePlacementNum * 2 + 5] += '-'
                    line1[submarinePlacementNum * 2 + 6] += '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line1[submarinePlacementNum * 2 + 2] = '*'
                    line1[submarinePlacementNum * 2 + 1] = '-'
                    line1[submarinePlacementNum * 2 + 0] = '*'
                    line1[submarinePlacementNum * 2 - 1] = '-'
                    line1[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line1[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':                        
                    print('ERROR NOT POSSIBLE')
                    welcomeMessage()
                    submarinePlacing()  
                else:
                    welcomeMessage()
                    submarinePlacing()
                    
    if submarinePlacementLet.upper() == 'C':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 3] = '-'
                    line2[submarinePlacementNum * 2 + 4] = '*'
                    line2[submarinePlacementNum * 2 + 5] = '-'
                    line2[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 1] = '-'
                    line2[submarinePlacementNum * 2 + 0] = '*'
                    line2[submarinePlacementNum * 2 - 1] = '-'
                    line2[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':                        
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line1[submarinePlacementNum * 2 + 2] = '*'
                    line0[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'D':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 3] = '-'
                    line3[submarinePlacementNum * 2 + 4] = '*'
                    line3[submarinePlacementNum * 2 + 5] = '-'
                    line3[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 1] = '-'
                    line3[submarinePlacementNum * 2 + 0] = '*'
                    line3[submarinePlacementNum * 2 - 1] = '-'
                    line3[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':                        
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    line1[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'E':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 3] = '-'
                    line4[submarinePlacementNum * 2 + 4] = '*'
                    line4[submarinePlacementNum * 2 + 5] = '-'
                    line4[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 1] = '-'
                    line4[submarinePlacementNum * 2 + 0] = '*'
                    line4[submarinePlacementNum * 2 - 1] = '-'
                    line4[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':                        
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    line2[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'F':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 3] = '-'
                    line5[submarinePlacementNum * 2 + 4] = '*'
                    line5[submarinePlacementNum * 2 + 5] = '-'
                    line5[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 1] = '-'
                    line5[submarinePlacementNum * 2 + 0] = '*'
                    line5[submarinePlacementNum * 2 - 1] = '-'
                    line5[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    line3[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'G':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 3] = '-'
                    line6[submarinePlacementNum * 2 + 4] = '*'
                    line6[submarinePlacementNum * 2 + 5] = '-'
                    line6[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 1] = '-'
                    line6[submarinePlacementNum * 2 + 0] = '*'
                    line6[submarinePlacementNum * 2 - 1] = '-'
                    line6[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    line4[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'H':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 3] = '-'
                    line7[submarinePlacementNum * 2 + 4] = '*'
                    line7[submarinePlacementNum * 2 + 5] = '-'
                    line7[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 1] = '-'
                    line7[submarinePlacementNum * 2 + 0] = '*'
                    line7[submarinePlacementNum * 2 - 1] = '-'
                    line7[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    line9[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':                        
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    line5[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)

                else:
                    welcomeMessage()
                    submarinePlacing()

    if submarinePlacementLet.upper() == 'I':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    line8[submarinePlacementNum * 2 + 3] = '-'
                    line8[submarinePlacementNum * 2 + 4] = '*'
                    line8[submarinePlacementNum * 2 + 5] = '-'
                    line8[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    line8[submarinePlacementNum * 2 + 1] = '-'
                    line8[submarinePlacementNum * 2 + 0] = '*'
                    line8[submarinePlacementNum * 2 - 1] = '-'
                    line8[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':
                    print('ERROR NOT POSSIBLE')
                    welcomeMessage()
                    submarinePlacing()
                elif subDirection.lower() == 'up':                        
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    line6[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                else:
                    welcomeMessage()
                    submarinePlacing()
                                            
    if submarinePlacementLet.upper() == 'J':

 

        for i in range(10):
            if submarinePlacementNum == i:
                subDirection = input('What direction? [Up,Down,Left,Right?]')
                if subDirection.lower() == 'right':
                    line9[submarinePlacementNum * 2 + 2] = '*'
                    line9[submarinePlacementNum * 2 + 3] = '-'
                    line9[submarinePlacementNum * 2 + 4] = '*'
                    line9[submarinePlacementNum * 2 + 5] = '-'
                    line9[submarinePlacementNum * 2 + 6] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'left':
                    line9[submarinePlacementNum * 2 + 2] = '*'
                    line9[submarinePlacementNum * 2 + 1] = '-'
                    line9[submarinePlacementNum * 2 + 0] = '*'
                    line9[submarinePlacementNum * 2 - 1] = '-'
                    line9[submarinePlacementNum * 2 - 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'up':
                    line9[submarinePlacementNum * 2 + 2] = '*'
                    line8[submarinePlacementNum * 2 + 2] = '*'
                    line7[submarinePlacementNum * 2 + 2] = '*'
                    cls()
                    welcomeMessage()
                    boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
                elif subDirection.lower() == 'down':    
                    print('ERROR NOT POSSIBLE')
                    welcomeMessage()
                    submarinePlacing()                    
                else:
                    welcomeMessage()
                    submarinePlacing()                       


loadingScreen()
welcomeMessage()
boardLog(num, line0, line1, line2, line3, line4, line5, line6, line7, line8, line9)
submarinePlacing()
