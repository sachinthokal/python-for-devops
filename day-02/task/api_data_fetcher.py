import requests
import json

# stock_url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo"

baseUrl = "https://www.alphavantage.co/"
symbol = "IBM"
apikey = "demo"
query = f"query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={apikey}"

response = requests.get(url=baseUrl+query)
data = response.json()

final_data = data['Meta Data'],data['Monthly Time Series']['2025-12-23']
print(final_data)

def save_to_file():
    with open("output.json", "w") as f:
        json.dump(final_data, f, indent=4)  # indent=4 makes it pretty

# new type with - with keyword
with open("response.json", "w") as f:
    json.dump(final_data, f, indent=4)  # indent=4 makes it pretty format /

# simple txt file output
with open("Demo.txt","w") as file:
    file.write(str(final_data))

# Old type without - with keyword
file = open("Demo2.txt","w")
file.write(str(final_data))
file.close()
# Save File Call
save_to_file()