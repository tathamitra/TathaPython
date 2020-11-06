import requests

r = requests.get("https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?apikey=demo&limit=1")
print(r)
print(r.text)
print(r.content)


r1 = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r1)

url= "www.something.com"
data = {
    "p1":4,
    "p2":5
}

r2= requests.post(url = url,data = data)
print(r2)
print(r2.text)


