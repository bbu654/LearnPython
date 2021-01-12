def Floor(lines,irow,icol):
    FoC=False
    if lines[irow][icol]=='.': return True
    return FoC
def fillseats(lines):
    mline=[]
    tlines=[]
    zero0=0
    intline=[]
    
    rows, cols = (99, 97) 
    intlines = [[0 for i in range(cols)] for j in range(rows)] 
    #print(arr) 
    #for init1 in range(99):
    #    for init2 in range(97):
    #        intlines[init1,init2]=0
    count=0
    for irow,line in enumerate(lines):
        kline=str(line)
        for icol in range(cols):
            if lines[irow][icol] == '.':
                continue
            if icol>0 and irow>0 and icol<cols-1 and irow <rows-1:
                for x in range(-1,2):
                    for y in range(-1,2):
                        if lines[irow+x][icol+x] == '#':
                            bagtotal+=1
                        if lines[irow+x][icol+y] == '#':
                            bagtotal+=1
                        if lines[irow+y][icol+x] == '#':
                            bagtotal+=1
                        if lines[irow+y][icol+y] == '#':
                            bagtotal+=1
            #for j in range(len(i)):
            #need to copy like we are doingrules
            if lidx == 0:#row=0
                #don't check -1
                lkd=0
                if icol ==0:
                    kld=0
                    
                    if kline[i+1] == 'L':
                        if lines[lidx][i] == 'L':
                            if lines[lidx+1][i+1]=='L':
                    #don't check -1
            if kline[i]=='L':
                mline.append('M')
            
            else:
                #if count == 0:
                #    print(f'kline[i]={kline[i]}')
                if kline[i] == "[" or kline[i] == "'" or kline[i] == "]":
                    kld=0
                else:
                    mline.append(kline[i])
                    count+=1
        else:
            sline=str('')
            for x in mline: 
                sline += x 
            tlines.append(sline)
            count=0
    return tlines
def day11seatchart():
    path = f'day11seatchart.txt'
    day11seats=[]          
    tlines=[]
    rules = """All decisions are based on the number of occupied seats 
        adjacent to a given seat (one of the eight positions 
        immediately up, down, left, right, or diagonal from the seat). 
        The following rules are applied to every seat simultaneously:
        If a seat is empty (L) and there are no occupied seats adjacent 
        to it, the seat becomes occupied.  If a seat is occupied (#) 
        and four or more seats adjacent to it are also occupied, 
        the seat becomes empty.  Otherwise, the seat's state does not 
        change.  Floor (.) never changes; seats don't move, and nobody sits on the floor. """

    with open(path, 'r') as file11:
        for line in file11.readlines():
            day11seats.append(line.rsplit())
    tlines=initseats(day11seats)            
    tlines=fillseats(day11seats)
    for lidx, line in enumerate(tlines):
        if lidx % 5 == 0: 
            print(f'{str(line)[2:10]}', end='  ')
    print(rules)
    return 6969

if __name__ == '__main__':
    #for case in TEST_CASES:
    #    result = solve(case.case)
    #    case.check(result)

    t0 = time.time()
    popit=day11seatchart(()
    print(f'day11seatchart={popit}')
    t1 = time.time()
    
    #for i in range(40,42):
        #if 2**i >
    #    print(2**i, popit-(2**i),sep=',')
    print(f"{(t1 - t0) * 1000:0.1f} ms")