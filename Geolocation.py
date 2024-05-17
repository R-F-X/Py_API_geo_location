import requests
import time 
import colorama 
from colorama import Fore 
import sys 


class Geolocation():
    def __init__(self):
        colorama.init()
        self.important_info_keys = [
            # "ip", 
            "type", 
            "continent", 
            "continent_code", 
            "country", 
            "country_code", 
            "region", 
            "region_code", 
            "city", 
            "latitude", 
            "longitude", 
            "is_eu", 
            "calling_code", 
            "capital",
            "connection", 
            "timezone",  
        ]
        self.color1 = Fore.YELLOW

    """
    Number of methods: 3
    """
    # ======================================
    

    def internet_connection(self) -> bool:
        try:
            requests.get("https://www.google.com", timeout=5)
            response = requests.get("https://www.google.com", timeout=5)
            # print(response)
            return True
        except requests.ConnectionError:
            return False    
    # ======================================
    
    # retrives data from the API
    def get_data(self, ipv4:str) -> dict:
        # base_url = f"https://ipapi.co/{ipv4}/json/" # has a limit
        base_url = f"http://ipwho.is/{ipv4}"

        response = requests.get(base_url)
        data = response.json()
        
        if data["success"] is True:
            return data 
    # ======================================

    def display_data(self, data_ip:dict) -> None:
        print(f"\nIP Address: {Fore.YELLOW}{data_ip['ip']}{Fore.RESET}")

        # line
        print(len("IP Address: " + data_ip['ip']) * "=")
        print()

        data_ip_keys = list(data_ip.keys())

        # displaying all the details
        for key in sorted(data_ip_keys):
            if key in self.important_info_keys:

                # special key
                if key == "timezone":
                    print(f"{key}")
                    print(f"{self.color1}- Zone offset: {data_ip['timezone']['offset']}")
                    print(f"- UTC: {data_ip['timezone']['utc']}")
                    print(f"- Current_time: {data_ip['timezone']['current_time']} {Fore.RESET}")

                # special key
                elif key == "connection":
                    print(f"{key}")
                    print(f"{self.color1}- ASN (Autonomous System Number): {data_ip[key]['asn']}")
                    print(f"- Org: {data_ip['connection']['org']}")
                    print(f"- ISP: {data_ip['connection']['isp']}")
                    print(f"- Domain: {data_ip['connection']['domain']} {Fore.RESET}")

                # the rest of the keys
                else:
                    print(f"{key}: {self.color1}{data_ip[key]} {Fore.RESET}")

        # line
        print(len("IP Address: " + data_ip['ip']) * "=")
        
    # ======================================

# ------------------------------------------

def test_main(): pass 
   
# ------------------------------------------

# if __name__ == "__main__":
    # test_main()
    # print("\n<END OF TEST>")
# ------------------------------------------
