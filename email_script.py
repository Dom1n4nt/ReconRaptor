mport requests


API_KEY = '355b659d6b4d5414737015ead4c923e3d0acd2ff'


def search_email_info(email):
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        # Debug: print the raw JSON response for troubleshooting
        print("Response from Hunter.io:", data)

        if data.get('data'):
            email_info = data['data']
            result = {
                'email': email_info.get('email'),
                'score': email_info.get('score'),
                'result': email_info.get('result'),
                'disposable': email_info.get('disposable'),
                'webmail': email_info.get('webmail')
            }
            return result
        else:
            return f"No data found for email: {email}"
    else:
        return f"Error: Unable to fetch data  (Status Code: {response.status_code})"


if __name__ == '__main__':
    
    email_to_search = input("Please enter the email address you want to search: ")

    email_info = search_email_info(email_to_search)
    
    if isinstance(email_info, dict):
        print("Email Information:")
        for key, value in email_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print(email_info)
