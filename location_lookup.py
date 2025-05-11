import requests

def ip_lookup(ip):
    token = "6dbdca42768a1d"
    url = f"https://ipinfo.io/{ip}?token={token}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("\n[+] IP Information:")
            print(f"  IP: {data.get('ip', 'N/A')}")
            print(f"  Hostname: {data.get('hostname', 'N/A')}")
            print(f"  City: {data.get('city', 'N/A')}")
            print(f"  Region: {data.get('region', 'N/A')}")
            print(f"  Country: {data.get('country', 'N/A')}")
            print(f"  Location (lat,long): {data.get('loc', 'N/A')}")
            print(f"  Organization: {data.get('org', 'N/A')}")
            print(f"  Timezone: {data.get('timezone', 'N/A')}")
        else:
            print(f"[!] Lookup failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error during lookup: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address to lookup: ").strip()
    ip_lookup(ip)

