import requests 

def main():
    response = requests.get("https://www.google.com")
    print(response.text)

if __name__=="__main__":
    main()