def fillseats(lines):
    mline=[]
    tlines=[]
    for line in lines:
        for i in range(len(line)):
            if line[i]=='L':
                mline.append('M')
            else:
                mline.append(line[i])
        else:
            tlines.append(mline)
    return tlines
def day11seatchart():
    path = f'day11seatchart.txt'
    day11seats=[]
    tlines=[]
    with open(path, 'r') as file11:
        for line in file11.readlines():
            day11seats.append(line.rsplit())
    tlines=fillseats(day11seats)
    for lidx, line in enumerate(day11seats):
        if lidx % 5 == 0: 
            print(f'{str(line)[2:10]}', end='  ')
    
    return 6969
