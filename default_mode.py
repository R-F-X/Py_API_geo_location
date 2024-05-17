from Geolocation import Geolocation
from colorama import Fore 

import time
import os 
# -------------------
            

def title() -> None:
	# from https://patorjk.com/software/taag/#p=display&f=Big%20Money-sw&t=APIs
    title = """
  ______                       __                                  __      __                     
 /      \                     /  |                                /  |    /  |                    
/$$$$$$  |  ______    ______  $$ |  ______    _______   ______   _$$ |_   $$/   ______   _______  
$$ | _$$/  /      \  /      \ $$ | /      \  /       | /      \ / $$   |  /  | /      \ /       \ 
$$ |/    |/$$$$$$  |/$$$$$$  |$$ |/$$$$$$  |/$$$$$$$/  $$$$$$  |$$$$$$/   $$ |/$$$$$$  |$$$$$$$  |
$$ |$$$$ |$$    $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |       /    $$ |  $$ | __ $$ |$$ |  $$ |$$ |  $$ |
$$ \__$$ |$$$$$$$$/ $$ \__$$ |$$ |$$ \__$$ |$$ \_____ /$$$$$$$ |  $$ |/  |$$ |$$ \__$$ |$$ |  $$ |
$$    $$/ $$       |$$    $$/ $$ |$$    $$/ $$       |$$    $$ |  $$  $$/ $$ |$$    $$/ $$ |  $$ |
 $$$$$$/   $$$$$$$/  $$$$$$/  $$/  $$$$$$/   $$$$$$$/  $$$$$$$/    $$$$/  $$/  $$$$$$/  $$/   $$/ 
                                                                                                  
    """

    print("\n" + title + "\n")
# ================================


def main():
    os.system("cls")
    test_obj = Geolocation()

    # checking if there is an internet connection
    if test_obj.internet_connection():
        title()
        time.sleep(1)

        # instructions
        print(Fore.YELLOW + "Type 'esc' to leave" + Fore.RESET)
        print("\nEnter an IPv4 address")
        print(Fore.YELLOW + "Example: 102.233.100.12" + Fore.RESET)

        # used to close the program; end the loop
        close_program = False

        # MAIN LOOP
        while not close_program:

            # user input; stripping blank spaces
            input_ip = input("\nIPv4 address: ").strip()

            # close program
            if input_ip == "esc":
                close_program = True 
                print(Fore.YELLOW + "leaving..." + Fore.RESET)
                time.sleep(1)

            # IP search 
            else: 
                # making a request to the API
                # getting the data
                # displaying the data
                try:
                    data_ip = test_obj.get_data(input_ip)
                    test_obj.display_data(data_ip)

                # error handling
                except TypeError:
                    # print("<Invalid IP address>")
                    print(Fore.RED + "*Invalid IPv4 address*" + Fore.RESET) 


                except:
                    # print("<unknown error>")
                    print(Fore.RED + "*unknown error*" + Fore.RESET) 

    else:
        print(Fore.RED + "\nERROR \n*Not connected to the Internet*" + Fore.RESET) 

# ================================
