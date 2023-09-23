
input = {
  "data": [
    {
      "quantity": 4,
      "price": 5.0,
      "currency": "HKD",
      "sector": "ECommerce",
      "assetClass": "Equity",
      "region": "APAC"
    },
    {
      "quantity": 5,
      "price": 4.0,
      "currency": "JPY",
      "sector": "Finance",
      "assetClass": "FixedIncome",
      "region": "APAC"
    },
    {
      "quantity": 10,
      "price": 6.0,
      "currency": "EUR",
      "sector": "Education",
      "assetClass": "Derivatives",
      "region": "EMEA"
    }
  ],
  "part": "FIRST"
}
input2 = {
  "data": [
    {
      "quantity": 110,
      "price": 10.0,
      "currency": "SGD",
      "sector": "ECommerce",
      "assetClass": "Equity",
      "region": "APAC"
    },
    {
      "quantity": 5,
      "price": 1.0,
      "currency": "USD",
      "sector": "Technology",
      "assetClass": "Equity",
      "region": "NORTH_AMERICA"
    },
    {
      "quantity": 39,
      "price": 5.0,
      "currency": "GBP",
      "sector": "Education",
      "assetClass": "Equity",
      "region": "EMEA"
    },
    {
      "quantity": 32,
      "price": 100.0,
      "currency": "Other",
      "sector": "Pharmaceutical",
      "assetClass": "Equity",
      "region": "APAC"
    },
    {
      "quantity": 200,
      "price": 30.0,
      "currency": "HKD",
      "sector": "Technology",
      "assetClass": "FixedIncome",
      "region": "APAC"
    }
  ],
  "part": "FIRST" 
}
import math
def pieChart(data):
    if data['part'] == "FIRST":
        piePart1(data)
    else:
        piePart2(data)

def piePart1(data):
    dataforcalculate = data['data']
    amount = []
    for i in dataforcalculate:
        quantity = i['quantity']
        price = i['price']
        amountForEach = quantity * price
        amount.append(amountForEach)
    totalInvested = sum(amount)
    # fractionalAmount = sorted(amount/totalInvested)
    result = []
    for i in amount:
        returnAngle = 2*math.pi*i/totalInvested
        result.append(returnAngle)
    result = sorted(result, reverse=True)
    for i in range(len(result)):
        if i != 0:
            result[i] = round(float(result[i]) + float(result[i-1]), 8)
        else:
            result[i] = round(float(result[i]), 8)
    result.insert(0, 0.0)
    return result

def piePart2(data):
    return 0

print(piePart1(input2))