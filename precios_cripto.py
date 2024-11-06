import requests
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os


def download_prices():
    # Diccionario de criptomonedas con sus identificadores en CoinGecko
    cryptocurrencies = {
        "usdt": "tether",
        "dai": "dai",
        "btc": "bitcoin",
        "eth": "ethereum",
        "dot": "polkadot",
        "bnb": "binancecoin",
        "astr": "astar",
        "ksm": "kusama",
        "cro": "crypto-com-chain",
        "bit": "bitdao",
        "aave": "aave",
        "ewt": "energy-web-token",
        "ftm": "fantom",
        "volta": "volta-club",
        "flow": "flow",
        "hbar": "hedera-hashgraph",
        "avax": "avalanche-2",
        "matic": "matic-network",
        "woop": "woonkly-power",
        "glmr": "moonbeam",
        "gohm": "governance-ohm",
        "sol": "solana",
        "link": "chainlink",
        "movr": "moonriver",
        "sand": "the-sandbox",
        "ada": "cardano",
        "theta": "theta-token",
        "phala": "pha",
        "mvi": "metaverse-index",
        "cfg": "centrifuge",
        "sys": "syscoin",
        "qi": "benqi",
        "rose": "oasis-network",
        "zlk": "zenlink-network-token",
        "nu": "nucypher",
        "near": "near",
        "uni": "uniswap",
        "rmrk": "rmrk",
        "chz": "chiliz",
        "algo": "algorand",
        "celo": "celo",
        "pnk": "kleros",
        "para": "parallel-finance",
        "aca": "acala",
        "mina": "mina-protocol",
        "sdn": "shiden",
        "neer": "metaverse-network-pioneer",
        "mana": "decentraland",
        "kilt": "kilt-protocol",
        "rare": "superrare",
        "kma": "calamari-network",
        "air": "altair",
        "vlx": "velas",
        "senso": "senso",
        "scrt": "secret",
        "xvc": "xave-coin",
        "celr": "celer-network",
        "rly": "rally-2",
        "cws": "crowns",
        "umi": "umi-digital",
        "kar": "karura",
        "sushi": "sushi",
        "ztg": "zeitgeist",
        "val": "sora-validator-token",
        "efx": "effect-network",
        "ube": "ubex",
        "png": "pangolin",
        "pswap": "polkaswap",
        "bnc": "bifrost-native-coin",
        "bondly": "bondly",
        "sos": "opendao",
        "thg": "thetan-arena",
        "rain": "rainmaker-games",
        "xor": "sora",
        "wexpoly": "waultswap",
        "luna": "terra-luna",
        "slr": "solar",
        "kubic": "kubic",
        "pica": "picasso",
        "gens": "genshiro",
        "enj": "enjincoin",
        "sats": "sats-ordinals",
        "doge": "dogecoin",
        "shib": "shiba-inu",
        "wif": "dogwifcoin",
        "orca": "orca",
        "rbt": "robonomics-network",
        "popcat": "popcat",
        "saga": "saga",
        "hydra": "hydradx",
        "arsw": "arthswap",
        "atom": "cosmos",
        "osmo": "osmosis",
        "chonky": "chonky",
        "acs": "access-protocol",
        "analos": "analos",
        "inj": "injective-protocol",
        "evm": "evmos",
        "tia": "celestia",
        "eq": "equilibrium",
        "dev": "dev-protocol",
        "arb": "arbitrum",
        "xai": "xai-blockchain",
        "jup": "jupiter-exchange-solana",
        "jlp": "jupiter-perpetuals-liquidity-provider-token",
        "ondo": "ondo-finance",
        "ton": "the-open-network",
        "cake": "pancakeswap-token",
        "saga": "saga-2",
        "sui": "sui",
        "normilio": "normilio",
        "purr": "purr",
        "not": "notcoin",
        "mode": "mode",
        "param": "param",
        "nyan": "nyan",
        "wrsETH": "wrapped-rseth",
        "weETH": "bridged-weeth-linea",
        "ezETH": "renzo-restaked-eth",
        "ovn": "overnight-finance",
        "pendle": "pendle",
        "mpendle": "mpendle",
        "aero": "aerodrome-finance",
        "pendle": "pendle",
        "mpendle": "mpendle",
        "mother": "mother-iggy",
        "billy": "billy",
        "kmno": "kamino",
        "bonk": "bonk",
        "MEW": "cat-in-a-dogs-world",
        "WEN": "wen-4",
        "michi": "michicoin",
        "WDOG": "wrapped-dog",
        "scf": "smoking-chicken-fish",
        "MOODENG": "moo-deng",
        "OP": "optimism",
        "DBR": "debridge",
        "GIGA": "gigachad-2",
        "FWOG": "fwog",
        "gnon": "numogram",

    }

    # URL base de CoinGecko API
    base_url = "https://api.coingecko.com/api/v3/simple/price"

    # Parámetros de la solicitud
    params = {
        'ids': ','.join(cryptocurrencies.values()),
        'vs_currencies': 'usd'
    }

    # Realizar la solicitud GET
    response = requests.get(base_url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        prices = response.json()

        # Crear una lista de diccionarios con los datos
        data = []
        for key, value in cryptocurrencies.items():
            price = prices.get(value, {}).get('usd', None)
            data.append({'Criptomoneda': key.upper(), 'Precio (USD)': price})

        # Crear el DataFrame
        df = pd.DataFrame(data)
        print(df)
    else:
        print(f"Error {response.status_code}: No se pudieron obtener los datos.")

    df.to_excel('C:/Users/marmo/OneDrive/Documentos/MEGA/MARMOL-MEGA/3_Financiero/Gestion del patrimonio/precios.xlsx')

    messagebox.showinfo("Éxito", "¡Descarga exitosa!")


# os.chdir("C:/Users/marmo/OneDrive/Documentos/MEGA/MARMOL-MEGA/3_Financiero/Gestion del patrimonio")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Descarga de precios de criptomonedas")
ventana.geometry("300x200")  # Ancho x Alto

# Crear un botón que ejecuta la función mi_funcion al hacer clic
boton = tk.Button(ventana, text="Download", command=download_prices)
boton.pack(pady=20)  # Empaquetar el botón en la ventana y añadir un poco de espacio alrededor

# Iniciar el bucle principal de la interfaz
ventana.mainloop()


'''

# LISTA DE NOMBRES DE CRIPTOMONEDAS LISTADAS EN COINGEKO

# URL of the CoinGecko API endpoint
url = "https://api.coingecko.com/api/v3/coins/list"

# Perform a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Display the first few rows of the DataFrame
    print(df.head())
else:
    print(f"Error {response.status_code}: Unable to fetch data")


# Optionally, save the DataFrame to a CSV file
df.to_excel('coingecko_coins_list.xlsx', index=False)

'''