import requests

hunter_api_key = "355b659d6b4d5414737015ead4c923e3d0acd2ff"
rapidapi_key = "62933b8b36amshfa4d4a44f1db14dp15bd03jsnae23beec02d6"

def check_breachdirectory(email):
    print("[+] Checking BreachDirectory...")
    url = f"https://breachdirectory.p.rapidapi.com/?func=auto&term={email}"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            print("[+] Breaches found:")
            for entry in data["result"]:
                print(f"  - {entry}")
        else:
            print("[-] No breaches found.")
    else:
        print(f"[-] BreachDirectory API error: {response.status_code} - {response.text}")

def hunter_lookup(email):
    print("[+] Running Hunter.io lookup...")
    domain = email.split("@")[-1]
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={hunter_api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            org = data["data"].get("organization", "Unknown")
            emails = data["data"].get("emails", [])

            print(f"[+] Lookup for domain: {domain}")
            print(f"  Organization: {org}")
            print("  Emails found:")
            for e in emails[:5]:
                print(f"   - {e.get('value')}")
        else:
            print("[-] No data returned from Hunter.io")
    else:
        print(f"[-] Hunter.io API error: {response.status_code} - {response.text}")

def main():
    email = input("?] Enter the target email: ").strip()
    print(f"[~] Starting OSINT scan for: {email}")
    check_breachdirectory(email)
    hunter_lookup(email)

if __name__ == "__main__":
    main()
