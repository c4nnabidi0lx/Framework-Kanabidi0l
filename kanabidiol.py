import socket
import requests
import urllib.request
import urllib.error
import sys
import os

r = "\033[1;31m"  
g = "\033[1;32m"  
y = "\033[1;33m"  
b = "\033[1;34m"  
m = "\033[1;35m"  
c = "\033[1;36m"  
w = "\033[1;37m"  
d = "\033[0m"     

def banner():
    print(f"""{b}
      ▄████████ 
     ███    ███ 
     ███    █▀  
    ▄███▄▄▄     
   ▀▀███▀▀▀     
     ███    █▄  
     ███    ███ 
     ████████▀  {d}""")
    print(f"{g}                                      [ dev: cannabidi0lx ]{d}\n")

def menu():
    print(f"{b}===================={w} kanabidi0l mad3d by c4nabiz {b}===================={d}\n")
    print(f"                          {c}∆ menu for hackers ∆{d}\n")
    print(f"                    {b}[{y} 1 {b}]{w} web fuzzer with bruteforce{d}")
    print(f"                    {b}[{y} 2 {b}]{w} portscanner advanced(?){d}")
    print(f"                    {b}[{y} 3 {b}]{w} capture headers for host{d}")
    print(f"                    {b}[{y} 4 {b}]{w} exit framework{d}\n")
    print(f"{b}====================================================================={d}\n")

def webfuzzer():
    os.system('clear')
    print(f"{b}----{w} w3b fuzzer by c4nabiz {b}----{d}\n\n")
    target = input(f"{b}[{y} ? {b}]{w} target(example: http://google.com) : {m}")
    print(f"{d}")
    if not target.endswith("/"):
        target += "/"
    w_file = input(f"{b}[{y} ? {b}]{w} wordlist please! : {m}")
    print(f"{d}\n\n{b}=================================================={d}")
    print(f"{c}[*] inicializing attack brute...! :){d}")
    print(f"{b}=================================================={d}\n")
    try:
        with open(w_file, 'r', encoding='utf-8', errors='ignore') as arqv:
            for lines in arqv:
                delines = lines.strip()
                if not delines or delines.startswith('#'):
                    continue
                u_finally = target + delines
                try:
                    req = urllib.request.Request(u_finally, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=2.0) as resp:
                        if resp.status == 200:
                            print(f"{g}[+] expl0ited!! dict found: /{delines} (200) ok!{d}\n")
                except urllib.error.HTTPError as erro:
                    if erro.code == 404:
                        pass
                    elif erro.code == 403:
                        print(f"{y}[!] restrict but expl0ited! /{delines} (403) ok(?){d}\n")
                except Exception:
                    pass

    except FileNotFoundError:
        print(f"{r}[!] error: wordlist '{w_file}' not found...{d}\n")
    except Exception as e:
        print(f"{r}[!] crash error: {e}{d}\n")
    print(f"\n{b}=================================================={d}")
    print(f"{g}[+] attack finished successfully(?) :){d}")
    print(f"{b}=================================================={d}\n")
    input(f"{c}\n[ press enter to return menu ]...{d}")

def portscanner():
    os.system('clear')
    print(f"{b}----{w} p0rt-scanner by c4nabiz {b}----{d}\n\n")
    host = input(f"{b}[{y} ? {b}]{w} host for scanning : {m}")
    print(f"{d}\n{b}=================================================={d}")
    print(f"{c}[*] initializing mass port scanning...{d}")
    print(f"{b}=================================================={d}\n")
    for portas in range(1, 65536):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            r_code = s.connect_ex((host, portas))
            if r_code == 0:
                print(f"{g}--> open port : {portas}{d}\n")
                try:
                    s.send(b'\r\n')
                    banner_data = s.recv(1024)
                    print(f"    {c}[ banner ] --> {w}{banner_data.decode('utf-8', errors='ignore').strip()}{d}\n")
                except Exception:
                    print(f"    {y}[ banner ] --> no result or timeout in capture...{d}\n")
                print(f"{b}--------------------------------------------------{d}\n")
            s.close()
        except Exception as error:
            print(f"{r}[*] port {portas} catched error: {error}{d}\n")
    print(f"\n{b}=================================================={d}")
    print(f"{g}[+] port scanning completed!{d}")
    print(f"{b}=================================================={d}\n")
    input(f"{c}\n[ press enter to return menu ]...{d}")

def grabb():
    os.system('clear')
    print(f"\n{b}----{w} server fingerprinting by cannabidi0lx {b}----{d}\n\n")
    targeter = input(f"{b}[{y} ? {b}]{w} target url for grabb: {m}")
    print(f"{d}\n")
    if not targeter.startswith("http://") and not targeter.startswith("https://"):
        targeter = "https://" + targeter
    print(f"{c}[*] sending bytes head for: {w}{targeter}\n{d}")
    
    try:
        resp = requests.head(targeter, timeout=2.5, allow_redirects=True)
        cabe = resp.headers
        print(f"{b}================{w} headers f0und(?) {b}================{d}\n")
        server = cabe.get("Server", "oculted/not info")
        tech = cabe.get("X-Powered-By", "unknown")
        print(f"    {b}[{g}👉{b}]{w} server-web: {c}{server}{d}\n")
        print(f"    {b}[{g}👉{b}]{w} tech in use: {y}{tech}{d}\n")

        if "X-Frame-Options" not in cabe:
            print(f"    {b}[{r} critical {b}]{r} vuln f0und!! --> clickjacking haha(?){d}\n")
        else:
            print(f"    {b}[{g} * {b}]{w} iframe protect --> {c}{cabe.get('X-Frame-Options')}{d}\n")
        print(f"{b}=================================================={d}\n")
    except Exception as erro_web:
        print(f"    {r}[!] error read bytes http: {erro_web}{d}\n")
        print(f"{b}=================================================={d}\n")
    input(f"{c}\n[ press enter to return menu ]...{d}")

try:
    while True:
        os.system('clear')
        banner()
        menu()
        opcao_input = input(f"{b}[{y} > {b}]{w} select opc: {m}")
        print(f"{d}", end="")
        if not opcao_input.strip():
            continue
            
        opc = int(opcao_input)
        
        if opc == 1:
            webfuzzer()
        elif opc == 2:
            portscanner()
        elif opc == 3:
            grabb()
        elif opc == 4:
            os.system('clear')
            print(f"\n{r}[!] closing framework... finished!{d}\n")
            break
        else:
            print(f"\n{y}[ info ] decision incorrect! try again...{d}")
            sys.stdout.flush()
            os.system('sleep 2')
except KeyboardInterrupt:
    os.system('clear')
    print(f"\n{r}[!] framework destroyed by user terminal.{d}\n")
