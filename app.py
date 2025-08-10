import requests
import pandas as pd

# API endpoint
url = "https://api.coingecko.com/api/v3/simple/price" # api sees this 
params = {
    "ids": "bitcoin,ethereum,dogecoin",        # which coin do we want
    "vs_currencies": "usd,inr,eur"  # which currencies do we need
}

response = requests.get(url , params=params)
if response.status_code == 200:
    data = response.json()

    print(data)

    df = pd.DataFrame(data)
    flipped_df = df.T # interchanges cols and rows
    
    print(flipped_df)
    # print("Bitcoin rate: ")
    # for coin,prices in data.items():
    #     print(f"{coin.capitalize()}: USD {prices['usd']}, INR {prices['inr']}, EUR {prices['eur']}")
else:
    print("Error",response.status_code)








