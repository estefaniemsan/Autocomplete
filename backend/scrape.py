import requests

def get_google_suggestions(query):
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "q": query
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()  
        result = res.json()
        return result[1]  
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}") 
    except Exception as e:
        print("Erro", e) 
    return []


