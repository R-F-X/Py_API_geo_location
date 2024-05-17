from Geolocation import Geolocation
import default_mode
from colorama import Fore 
import sys 
# -------------------
            

def main_app(input_ip:str) -> None:
    test_obj = Geolocation()

    # checking if there is an internet connection
    if test_obj.internet_connection():

        # stripping blank spaces
        input_ip = input_ip.strip()

        # making a request to the API
        # getting the data
        # displaying the data
        try:
            data_ip = test_obj.get_data(input_ip)
            test_obj.display_data(data_ip)

        # error handling
        except TypeError:
            print(Fore.RED + "*Invalid IPv4 address*" + Fore.RESET) 

        except:
            print(Fore.RED + "*unknown error*" + Fore.RESET) 


    else:
        print(Fore.RED + "\nERROR \n*Not connected to the Internet*" + Fore.RESET) 

# ================================


if __name__ == "__main__": 
    if len(sys.argv) > 1:
        main_app(sys.argv[1])

    else:
        default_mode.main()
# ================================
