import requests
import json

BASE_URL = "http://localhost:4000"

def testar_scraping(base):
    res = requests.post(f"{BASE_URL}/autocomplete/scrape", json={"base": base})

    if res.status_code == 200:
        data = res.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))

    print(f"\n🔎 Verificando busca local com q={base[:3]}...")
    res2 = requests.get(f"{BASE_URL}/autocomplete", params={"q": base[:3]})
    print(json.dumps(res2.json(), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    testar_scraping("python desenvolvedor")
