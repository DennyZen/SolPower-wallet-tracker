import httpx

helius_api_key = "6cbf9a71-36c4-4d19-aad0-5e375448894a"
url = f"https://api.helius.xyz/v0/webhooks?api-key={helius_api_key}"
try:
    # Send a GET request to Helius API
    response = httpx.get(url)

    if response.status_code == 200:
        webhooks = response.json()
        print("Existing Webhooks:")
        print(webhooks)
    else:
        print(f"Failed to retrieve webhooks. Status code: {response.status_code}")
        print("Response:", response.text)

except Exception as e:
    print(f"An error occurred: {e}")
