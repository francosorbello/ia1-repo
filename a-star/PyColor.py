from colorama import init 
init(autoreset=True)
#init()

def prRed(skk): print("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk),end="|") 
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk),end="|") 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk), end="|") 
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk), end="|") 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk))