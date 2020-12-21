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
