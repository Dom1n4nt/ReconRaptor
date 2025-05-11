import requests
import time

def generate_usernames(first_name, last_name):
    return list(set([
        f"{first_name}{last_name}",
        f"{first_name}.{last_name}",
        f"{first_name}_{last_name}",
        f"{last_name}{first_name}",
        f"{first_name}{last_name}123",
        f"{first_name[0]}{last_name}",
        f"{last_name}.{first_name}",
        f"{first_name}{last_name[0]}",
    ]))

def check_platform(username, platform):
    urls = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "GitHub": f"https://github.com/{username}",
    }

    try:
        response = requests.get(urls[platform], timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    print("=== Social Media OSINT Tool ===")
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    email = input("Enter email (optional): ").strip().lower()
    phone = input("Enter phone number (optional): ").strip()

    usernames = generate_usernames(first_name, last_name)
    platforms = ["Instagram", "Twitter", "TikTok", "Facebook", "Pinterest", "GitHub"]

    print("\n[~] Checking usernames across social media platforms...\n")
    for username in usernames:
        print(f"Checking username: {username}")
        for platform in platforms:
            time.sleep(1)  # avoid rate limiting
            exists = check_platform(username, platform)
            status = "[+] Found" if exists else "[-] Not Found"
            print(f"   {status} on {platform}")
        print()

    print("Scan complete.")

if __name__ == "__main__":
    main()
