# %%
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#print it thx
if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(F'a={a}')
    print(f'list(dedupe(a)={list(dedupe(a))}')


# %%
collection_list = []
print(collection_list)
list123 = [1,2,3,4,5]
print(list123)
listalpha = ['a','b','c','d','e']
print(listalpha)
collection_list = list()
print(collection_list)

collection_list = [1] * 10 # [1,1,1,1,1,1,1,1,1,1]
collection_list.extend(listalpha)
collection_list.extend(list123)
print(collection_list)
# %%
