# example.py
#
# Example of calculating with dictionaries

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}
zipofdicts = zip(prices.values(), prices.keys()) # Tuples];; This didnt work minprice = min(zipofdicts) maxprice = max(zipofdicts)

minprice = (0,"")
maxprice = (0,"")

for x in zipofdicts:
   if x[0] < minprice[0] or minprice[0]==0:
      minprice = x
   if x[0] > maxprice[0]:
      maxprice = x
   print(f'{x}', end='    ')
else:
   print()
# Find min and max price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('min price: ', min_price, '    max price: ', max_price, '    minzip: ', minprice, '    maxzip: ', maxprice)

print('sorted prices:',end='    ')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price, end='    ')
else:
    print()


