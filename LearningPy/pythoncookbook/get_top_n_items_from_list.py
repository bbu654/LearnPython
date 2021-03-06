from collections import Counter
#from bbutilities import atimer
# Determine the most common words in a list
shorty=[]
#@atimer
def exampleBBU():
   words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
]
   
   word_counts = Counter(words)
   top_three = word_counts.most_common(3)
   #lookinggood= list(word_counts.items.__str__)
   shorty.append(f'{top_three}        ')        # print(top_three,end="        ")
   # outputs [('eyes', 8), ('the', 5), ('look', 4)]
   
   # Example of merging in more words
   
   morewords = ['why','are','you','not','looking','in','my','eyes']
   word_counts.update(morewords)
   shorty.append(f'{word_counts.most_common(3)}')
   return shorty


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x,end='  ')