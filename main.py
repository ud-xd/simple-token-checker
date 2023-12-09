import requests
import colorama
import os

    


def main():

    with open("input.txt", "r") as inputfile:
        tokens = inputfile.read().splitlines()
    

    validcounter = 0
    invalidcounter = 0
    billingcounter = 0

    for token in tokens:
        try:
            global l
            l = requests.get(url="https://discordapp.com/api/v6/users/@me", headers={"Authorization": token})

            if l.status_code == 200:
                validcounter += 1
                
                email = l.json()["email"]
                if email == None:
                    with open("UV.txt", "a") as uvfile:
                        uvfile.write(token + "\n")
                        print(f"[{colorama.Fore.YELLOW}UV{colorama.Fore.RESET}] - {colorama.Fore.YELLOW}{token}{colorama.Fore.RESET}")
                        # Token is not email verified!                        
                else:
                    with open("EV.txt", "a") as evfile:
                        evfile.write(token + "\n")
                        print(f"[{colorama.Fore.LIGHTGREEN_EX}EV{colorama.Fore.RESET}] - {colorama.Fore.LIGHTGREEN_EX}{token}{colorama.Fore.RESET}")
                        # Token is email verified!

                phone = l.json()["phone"]
                if phone == None:
                    pass 
                    # Token is not Fully Verified!
                else:
                    print("Token is FV!")
                    with open("FV.txt", "a") as fvfile:
                        fvfile.write(token + "\n")
                        print(f"[{colorama.Fore.GREEN}FV{colorama.Fore.RESET}] - {colorama.Fore.GREEN}{token}{colorama.Fore.RESET}")
                        # Token is fully verified!

                nitro_type = l.json()["premium_type"]
                if nitro_type == 0:
                    pass 
                    # No nitro (imagine lol, kinda cringe)
                else:
                    print(f"[{colorama.Fore.MAGENTA}BILLING HIT{colorama.Fore.RESET}] - {colorama.Fore.MAGENTA}{token}{colorama.Fore.RESET}")
                    billingcounter += 1
                    # Token has either nitro boost or basic
                

            
            else:
                print(f"[{colorama.Fore.RED}DEAD{colorama.Fore.RESET}] - {colorama.Fore.RED}{token}{colorama.Fore.RESET}")
                invalidcounter += 1

        except Exception as e:
            print("Failed to connect! ")
            print(e)

    
    print(f"{colorama.Fore.BLUE}Checking process done. Valid:", validcounter, ", Invalid:", invalidcounter, ", Tokens with billing:", billingcounter, f"{colorama.Fore.RESET}")


os.system("cls")
main()
