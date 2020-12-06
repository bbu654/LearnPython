   # example.py
   #
   # Example of using heapq to find the N smallest or largest items
   
import heapq

def printhq(li):
   shorty=[]
   for i in li:
      if isinstance(i,int):
         shorty.append(f'{i},    ')
      else:
         for j, k in i.items():
            shorty.append(f'{j} : {k},  ')
         else:
            shorty.append('\n')
   #else:
   #   shorty.append('|')
   return shorty
      
portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(f"cheap={printhq(cheap)}")
#for x in cheap:
#   print(f'{x}',end=',    ')
#else:
#   print()
print(f"expensive={printhq(expensive)}")
#for y in expensive:
#   print(f'{y}', end=',    ')
#else:
#   print()
# Python code to demonstrate working of 
# heapify(), heappush() and heappop() 

# importing "heapq" to implement heap queue 


# initializing list 
hope = [5, 7, 9, 1, 3] 

# using heapify to convert list into heap 
heapq.heapify(hope) 

# printing created heap #prq=Util.printheapq()

print (f"The created heap is : {printhq(hope)}")    #print (list(li)) 

# using heappush() to push elements into heap 
# pushes 4 #heapq.heappush(li,4) 

# printing modified heap 
print (f"The modified heap after push{heapq.heappush(hope,4) } is : {printhq(hope)}") 

# using heappop() to pop smallest element 
print ("The popped and smallest element is : ",end="") 
print(f'{heapq.heappop(hope)} n {printhq(hope)}')
