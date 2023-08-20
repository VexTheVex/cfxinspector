import requests
from colorama import init, Fore
import fivempy
import pyperclip
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("CFXInspector By: VexTheVex")

init(autoreset=True)

cfxinspector = "╭━━━┳━━━┳━╮╭━╮\n"\
"┃╭━╮┃╭━━┻╮╰╯╭╯\n"\
"┃┃╱╰┫╰━━╮╰╮╭╯\n"\
"┃┃╱╭┫╭━━╯╭╯╰╮\n"\
"┃╰━╯┃┃╱╱╭╯╭╮╰╮\n"\
"╰━━━┻╯╱╱╰━╯╰━╯\n"\
"╭━━┳━╮╱╭┳━━━┳━━━┳━━━┳━━━┳━━━━┳━━━┳━━━╮\n"\
"╰┫┣┫┃╰╮┃┃╭━╮┃╭━╮┃╭━━┫╭━╮┃╭╮╭╮┃╭━╮┃╭━╮┃\n"\
"╱┃┃┃╭╮╰╯┃╰━━┫╰━╯┃╰━━┫┃╱╰┻╯┃┃╰┫┃╱┃┃╰━╯┃\n"\
"╱┃┃┃┃╰╮┃┣━━╮┃╭━━┫╭━━┫┃╱╭╮╱┃┃╱┃┃╱┃┃╭╮╭╯\n"\
"╭┫┣┫┃╱┃┃┃╰━╯┃┃╱╱┃╰━━┫╰━╯┃╱┃┃╱┃╰━╯┃┃┃╰╮\n"\
"╰━━┻╯╱╰━┻━━━┻╯╱╱╰━━━┻━━━╯╱╰╯╱╰━━━┻╯╰━╯"

print(Fore.RED + "VexTheVex")
print(Fore.CYAN + cfxinspector + "\n\n")

def main():
    url = input("Enter the CFX connect code or Join Url: ")
    
    if url.startswith("cfx.re/join/"):
        request = "https://" + url
    elif url.startswith("https://cfx.re/join/"):
        request = url
        url = url.replace("https://", "")
    else:
        request = "https://cfx.re/join/" + url
        url = "cfx.re/join/" + url
    try:
      response = requests.get(request).headers["x-citizenfx-url"].replace("http://", "").replace("/", "")
      found = True
    except:
      response = "Server does not exist or is offline."
    
    print(f"\nCFX.re Address: \x1b[38;5;40m{url}")
    print(f"\x1b[0mIP address: \x1b[38;5;40m{response}\x1b[0m\n\n")
    print("Type 'copy' to copy IP to clipboard, press RETURN to search again...")
    ui = input()
    if ui.lower() == 'copy':
        pyperclip.copy(response)
        print("Copied IP to clipboard.\n")
    main()

main()