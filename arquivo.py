import os
import platform
import time
import pikepdf
from tqdm import tqdm
from termcolor import colored

def header():
    ascii_art1 = """
                       ______
                   .-"      "-.
                  /            \\
                 |              |
                 |,  .-.  .-.  ,|
                 | )(_o/  \\o_)( |
                 |/     /\\     \\|
       (@_       (_     ^^     _)
  _     ) \\_______\\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|___________________________>
        )_/        \\          /
       (@           `--------`
    """
    
    ascii_art2 = """
    ██████╗░██████╗░███████╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██████╔╝██║░░██║█████╗░░██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ██╔═══╝░██║░░██║██╔══╝░░██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ██║░░░░░██████╔╝██║░░░░░╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
    ╚═╝░░░░░╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """
    
    terminal_width = os.get_terminal_size().columns
    print(colored(ascii_art1.center(terminal_width), 'red'))
    print(colored(ascii_art2.center(terminal_width), 'red'))
    print(colored("https://github.com/Str44ng33 | Matheus 802 CMM".center(terminal_width), 'red'))

def install_requirements():
    if platform.system().startswith("Windows"):
        os.system("python -m pip install pikepdf tqdm termcolor pyfiglet -q -q -q")
    elif platform.system().startswith("Linux"):
        os.system("python3 -m pip install pikepdf tqdm termcolor pyfiglet -q -q -q")

def crack():
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    
    pdf_filename = input(colored("[•] Digita o caminho do seu arquivo PDF: ", 'red'))
    if not os.path.exists(pdf_filename):
        print(colored("\n[ ✘ ] Arquivo " + pdf_filename + " não encontrado, coloca um nome e caminho válidos!", 'red'))
        exit()
    
    print(colored("\n[*] Analisando o arquivo PDF: ", 'red'), pdf_filename)
    time.sleep(1)
    
    if pdf_filename[-3:].lower() == "pdf":
        print(colored("\n[ ✔ ] Arquivo PDF válido encontrado...", 'green'))
    else:
        print(colored("\n[ ✘ ] Isso não é um arquivo .pdf válido...\n", 'red'))
        exit()
    
    pwd_filename = input(colored("\nDigite o caminho da sua lista de senhas: ", 'red'))
    if not os.path.exists(pwd_filename):
        print(colored("\n[ ✘ ] Arquivo " + pwd_filename + " não encontrado, coloca um nome e caminho válidos!", 'red'))
        exit()
    
    passwords = [line.strip() for line in open(pwd_filename)]
    
    for password in tqdm(passwords, desc=f"Tentando quebrar o arquivo PDF -> {pdf_filename}: ", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"):
        try:
            with pikepdf.open(pdf_filename, password=password) as pdf:
                print(colored("\n[ ☢ ] Senha do PDF encontrada!!!: ", 'green'), password)
                break
        except pikepdf.PasswordError:
            continue

if __name__ == "__main__":
    install_requirements()
    crack()

