import requests
#topics covered : requests,api (application programming interface)
#taking json value from website api.fixer.ip(used to get currency exchenge rates)

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    #taking inputs for the currencies

    res = requests.get("https://api.fixer.io/latest",params={"base": base, "symbols": other})
    #need api key for this, now paid :(
    #var = take url as input, get request, var= http response 
    #params are for parameters, called base and symbols because its in the format of website


    #status code 200 is returned by default if everything fine
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
        
    data = res.json()  #extract the jason data
    rate = data["rates"][other]  #in json data, nested, 'rates':{'EUR': 0.836}, hence extracting the rate 
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
