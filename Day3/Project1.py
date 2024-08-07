import requests
import pandas as pd
import json

# URL of the API endpoint
state = "karnataka"  
url = f"https://vegetablemarketprice.com/api/dataapi/market/{state}/daywisedata?date=2024-08-06"


headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

try:
    # Fetch  data from the API
    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    # Parse the JSON response
    js_data = response.json()
    print(json.dumps(js_data, indent=2)) 

    # Extract & structure the data
    arr_data = []
    for api in js_data.get("data", []):
        veg_id = str(api.get("id", ""))
        veg_name = str(api.get("vegetablename", ""))
        whole_price = str(api.get("price", ""))
        retail_price = str(api.get("retailprice", ""))
        shoping_mall_price = str(api.get("shopingmallprice", ""))
        unit_val = str(api.get("units", ""))
        veg_image = str(api.get("vegetableimage", ""))  

        new_js = {
            "Date": "2024-08-06",  
            "State Name": state,
            "Vegetable Name": veg_name,
            "Wholesale Price": whole_price,
            "Retail Price": retail_price,
            "Shopping Mall Price": shoping_mall_price,
            "Units": unit_val,
            "Vegetable Image": veg_image
        }
        arr_data.append(new_js)

    # Create a DF
    df = pd.DataFrame(arr_data)

    # Save DF to a CSV 
    output_file = "vegetable_prices_karnataka.csv"
    df.to_csv(output_file, index=False)

    print(f"Data successfully saved to {output_file}")

except requests.RequestException as e:
    print(f"Request failed: {e}")
    if response is not None:
        print("Response content:", response.text)
except Exception as e:
    print(f"An error occurred: {e}")
