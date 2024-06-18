import random
from rich import print as rp
import rich.prompt
from rich.table import Table
from rich.console import Console

def pop():
    output={}
    for j in range(3,13+1):
        for k in range(2):
            output[j+(13*k)] = [j+(13*2)-1, j+(13*3)-1]
            rp(f'output[{j+(13*k)}] == {j+(13*2)-1}, {j+(13*3)-1}',end=',        ')
            output[j+(13*(k+2))] = [j-1, j+12]
            print(f'output[{j+(13*(k+2))}] == {j-1}, {j+12}',end=',        ')
        print()        
    #print(sorted(output))
    for t,i in enumerate(sorted(output)):
            if t%8 == 0 and t != 0:
                 print()
            rp(f"{i}: {output[i]}",end=', ')
    
    
    q=(1,2,14,15,27,28,40,41);print()
    for z in range(1,53):
         if z not in q:
              print(f'{z}: {output[z]}',end=", ")
         if z%10 == 0 and z != 0:
              print()   
    
    suitlit = ['[blue]0[/]']
    heart= [hy for hy in range(1,14)];print()    #♥
    for hu,hv in enumerate(heart):
        if hv == 1:
            rp(f"[red]A♥[/]:0{hv}",end=', ');suitlit.append('[red]A♥[/]')
        elif hv == 10:
            rp(f"[red]T♥[/]:{hv}",end=', ');suitlit.append('[red]T♥[/]')
        elif hv == 11:
            rp(f"[red]J♥[/]:{hv}",end=', ');suitlit.append('[red]J♥[/]')
        elif hv == 12:
            rp(f"[red]Q♥[/]:{hv}",end=', ');suitlit.append('[red]Q♥[/]')
        elif hv == 13:
            rp(f"[red]K♥[/]:{hv}",end=', ');suitlit.append('[red]K♥[/]')
        else:
            rp(f"[red]{hu+1}♥[/]:0{hv}",end=', ');suitlit.append('[red]'+str(hu+1)+'♥[/]')
    #print(suitlit)
    diamond = [dy for dy in range(14,27)];print()
    for du,dv in enumerate(diamond):
        if dv == 14:
            rp(f"[red]A♦[/]:{dv}",end=', ');suitlit.append('[red]A♦[/]')
        elif dv == 23:
            rp(f"[red]T♦[/]:{dv}",end=', ');suitlit.append('[red]T♦[/]')
        elif dv == 24:
            rp(f"[red]J♦[/]:{dv}",end=', ');suitlit.append('[red]J♦[/]')
        elif dv == 25:
            rp(f"[red]Q♦[/]:{dv}",end=', ');suitlit.append('[red]Q♦[/]')
        elif dv == 26:
            rp(f"[red]K♦[/]:{dv}",end=', ');suitlit.append('[red]K♦[/]')
        else:
            rp(f"[red]{du+1}♦[/]:{dv}",end=', ');suitlit.append('[red]'+str(du+1)+'♦[/]')
    spade = [sy for sy in range(27,40)];print()
    for su,sv in enumerate(spade):
        if sv == 27:
            rp(f"[black]A♠[/]:{sv}",end=', ');suitlit.append('[black]A♠[/]')
        elif sv == 36:
            rp(f"[black]T♠[/]:{sv}",end=', ');suitlit.append('[black]T♠[/]')
        elif sv == 37:
            rp(f"[black]J♠[/]:{sv}",end=', ');suitlit.append('[black]J♠[/]')
        elif sv == 38:
            rp(f"[black]Q♠[/]:{sv}",end=', ');suitlit.append('[black]Q♠[/]')
        elif sv == 39:
            rp(f"[black]K♠[/]:{sv}",end=', ');suitlit.append('[black]K♠[/]')
        else:
            rp(f"[black]{su+1}♠[/]:{sv}",end=', ');suitlit.append('[black]'+str(su+1)+'♠[/]')
    club = [cy for cy in range(40,53)];print()    #♣
    for cu,cv in enumerate(club):
        if cv == 40:
            rp(f"[black]A♣[/]:{cv}",end=', ');suitlit.append('[black]A♣[/]')
        elif cv == 49:
            rp(f"[black]T♣[/]:{cv}",end=', ');suitlit.append('[black]T♣[/]')
        elif cv == 50:
            rp(f"[black]J♣[/]:{cv}",end=', ');suitlit.append('[black]J♣[/]')
        elif cv == 51:
            rp(f"[black]Q♣[/]:{cv}",end=', ');suitlit.append('[black]Q♣[/]')
        elif cv == 52:
            rp(f"[black]K♣[/]:{cv}",end=', ');suitlit.append('[black]K♣[/]')
        else:
            rp(f"[black]{cu+1}♣[/]:{cv}",end=', ');suitlit.append('[black]'+str(cu+1)+'♣[/]')
    #print('suitlit:')
    outa=[[0,0,0,0,0,0,0,0]]
    sdeck = [qw for qw in range(1,53)]
    print(f'{sdeck=}')
    random.shuffle(sdeck)
    print(f'{sdeck=}')
    running=True
   
    cdeck = []
    #   above is init    below is running
    
    for s in sdeck:
        cdeck.append(suitlit[s])
    print(cdeck)
    ic=-1
    
    for row in range(22):
        outo=[]
        for col in range(8):
            ic += 1
            if ic < 52:
                outo.append(sdeck[ic])
            else:
                outo.append(0)
        outa.append(outo)
    #Py2Dlist = [sdeck[(ic:=ic+1)] if ic < 51 else 0 for j in range(8) for i in range(22) ]
    #rp(f'{Py2Dlist=}')
    rp(outa)
    ksdj=0
    ksdj=31
    mr=7;mc=3;dr=7;dc=0
    
    for a,b in enumerate(cdeck):        #if a%7 == 0 and a == 7:        #    print()
        if a%8 == 0:                    # and a > 8:
            print() 
        rp(b if not (b=='0') else '',end=',')
    return running, output, suitlit, sdeck, outa, q
    #   above is init    below is running
def rpit(  running, output, suitlit, sdeck, outa, q):
 
    #above is init     below is rpit
    gameview = Table(title='Freecell')
    #for qe in range(8):
    #   gameview.add_column('')
    for idy,row1 in enumerate(outa):
        #str4=zip(row1)        #str5=str4
        str0='';str1='';str2='';str3='';str4=''
        str5='';str6='';str7=''
        for idx,col1 in enumerate(row1):
            if idy==0:#strx=str(col1)
                gameview.add_column(suitlit[col1])
            else:
                if idx == 0:
                    str0=f'{suitlit[col1]}'
                elif idx == 1:
                    str1+=f'{suitlit[col1]}'
                elif idx == 2:
                    str2+=f'{suitlit[col1]}'
                elif idx == 3:
                    str3+=f'{suitlit[col1]}'
                elif idx == 4:
                    str4+=f'{suitlit[col1]}'
                elif idx == 5:
                    str5+=f'{suitlit[col1]}'
                elif idx == 6:
                    str6+=f'{suitlit[col1]}'
                elif idx == 7:
                    str7+=f'{suitlit[col1]}'
        if sum(row1) > 0:
            gameview.add_row(str0,str1,str2,str3,str4,str5,str6,str7)
    consol=Console()    
    consol.print(gameview)

    return  running, output, suitlit, sdeck, outa, q

def movit( running, output, suitlit, sdeck, outa, q, minp, dinp):
    if sum(outa[0]) > 0:
        pass
    m0=minp[0];    m1=minp[1];    d0=dinp[0];    d1=dinp[1]
    if m1=='F' or m1=='G' or d1=='F' or d1=='G':
        if (d1=='F' and outa[0][d0]==0) or (d1=='G' and outa[0][d0]==0 and m0=='A'):
            piuy=[i for i, x in enumerate(outa) if x == minp]
            poi=piuy[0];roi=piuy[1]
            outa[0][d0] = outa[poi][roi]
            outa[poi][roi]=0
        #if (d1=='G' and outa[0][d0]==0 and m0=='A'):
        #    cuiy=[i for i, x in enumerate(outa) if x == minp]
        #    coi=cuiy[0];ooi=cuiy[1]
        #    outa[0][d0] = outa[coi][ooi]
        else:
            piuy=[i for i, x in enumerate(outa) if x == minp]
            poi=piuy[0];roi=piuy[1]
            outa[0][d1+1] = outa[poi][roi]
            outa[poi][roi]=0
    else:
        if outa[d0+1][d1] == 0:
            outa[d0+1][d1] = outa[m0][m1]
            outa[m0][m1]   = 0
    return  running, output, suitlit, sdeck, outa, q
def runit( running, output, suitlit, sdeck, outa, q):
    '''from rich.prompt import Prompt as rin
    minp=rin.ask('move from')
    dinp=rin.ask('goto dest')'''
    running, output, suitlit, sdeck, outa, q = rpit(running, output, suitlit, sdeck, outa, q)
    suits = ['H','D','S','C','F','G','z','Z']
    questions = 'Quit, Move From: (comma), GoTo Dest: '
    minp = '9C';dinp = '0F'
    colh = list(zip(*outa))
    minp, dinp = input(questions).split(',')
    if minp == 'q':
        return False, output, suitlit, sdeck,outa,q
    elif minp[1] not in suits:
        return True, output, suitlit, sdeck,outa,q
    if minp[1]=='H':
        mino =   f'[red]{minp[0]}♥[/]'
    if minp[1]=='D':
        mino =   f'[red]{minp[0]}♦[/]'
    if minp[1]=='S':
        mino = f'[black]{minp[0]}♠[/]'
    if minp[1]=='C':
        mino = f'[black]{minp[0]}♣[/]'
    if minp[1]=='F' or minp[1] == 'G':
        mino = f'[blue]{minp}[/]'
    if dinp[1]=='H':
        dino =   f'[red]{dinp[0]}♥[/]'
    if dinp[1]=='D':
        dino =   f'[red]{dinp[0]}♦[/]'
    if dinp[1]=='S':
        dino = f'[black]{dinp[0]}♠[/]'
    if dinp[1]=='C':
        dino = f'[black]{dinp[0]}♣[/]'
    if dinp[1]=='F' or dinp[1] == 'G' or dinp[1]=='Z':
        dino = f'[blue]{dinp}[/]'
        mii=0;dii=int(dinp[0])
    
    #SKIP m if m == "F" or "G"
    if mino in suitlit:
        mii = suitlit.index(mino)
    if not mii:
        mii=0
    #SKIP d if d == "F" or "G"
    if dino in suitlit:
        dii = suitlit.index(dino)
    if not dii:
        dii=0
    moapt=[0,0]; doapt=[0,0]
    dou = 0; mou= 0; validMove=False
    #if out1/2.index(dii/mii)=0 this doesnt work 
    #doi=[out2.index(dii) if dii in out2 else 0 for out2 in outa]
    if dinp[1]=='F' or dinp[1]=='G':
        dou=0;doo=int(dinp[0]);doapt=[dou,doo]
    elif dinp[1]=='Z':
        dou=1;doo=int(dinp[0]);doapt=[dou,doo]
    else:
        for tout,sout in enumerate(outa):
            if dii in sout and dinp[1]!= 'F' and dinp[1]!='G':
                dou = tout
                doo = sout.index(dii)
                doapt=[dou,doo]
                break
    #doo = sum(doi);

    #moi=[out1.index(mii) if mii in out1 else 0 for out1 in outa]
    if minp[1]=='F' or minp[1]=='G':
        mou=0;moo=int(dinp[0]);moapt=[mou,moo]
    else:
        for uout,vout in enumerate(outa):
            if mii in vout:
                mou = uout
                moo = vout.index(mii)
                moapt = [mou,moo]
                break
    #moo = sum(moi);
    
    #for iu,qe in enumerate(moi):
    #    if qe > 0:
    #        mou=iu
    #        break
    rp(f'row{mou=},col{moo=}',end=',    ')
    #for ov,wf in enumerate(doi):
    #    if wf > 0:
    #        dou=ov
    #        break
    rp(f'row{dou=},col{doo=}')
    if dinp[1]=='Z':
        qqq=colh[int(dinp[0])]
    if dinp[1] == 'G':    #Foundation A-K
        dl=int(dinp[0])
        if dl in range(4,8):
            if outa[0][dl] == 0 \
            or outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
                outa[0][dl]=outa[mou][moo]
                outa[mou][moo]=0
                validMove=False #pass# valid move
            else:
                validMove=False
            #elif outa[mou][moo]==outa[0][dl] + 1:   #TODO samesuit and +1
            #    outa[0][dl]=outa[mou][moo]
            #    outa[mou][moo]=0
            #    validMove=False    
    elif dinp[1]=='Z' and sum(qqq[1:])==0:
        outa[1][int(dinp[0])]= outa[mou][moo]
        outa[mou][moo]=0
        validMove=False
    elif dinp[1] == 'F':    #Free Cell
        dk=int(dinp[0])
        if dk in range(4):
            if outa[0][dk] == 0:
                outa[0][dk]=outa[mou][moo]#pass# valid move
                outa[mou][moo]=0
                validMove=False #Done already    if not validMove:
    elif dii in q or dii==0:
        rp(f'invalid dest{dii=}')
    elif outa[mou][moo] in output[dii]:
        #moapt=[mou,moo];doapt=[dou,doo]
        validMove=True
        rp(f'Valid Move: {outa[mou][moo]=} in {output[dii]=}{dii=}')
    else:
        rp(f'{outa[mou][moo]=} notin{output[dii]=}{dii=}')
    #TODO:#add showing cards validation of a col of cards
          #move card(s) ADD CLASS and __init__      #1F0A1    #1F0A1
    #rp(f'[red,align(center,width({6})]🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂼🂽[/]')
    cardc = {0:'🂠',
             1:'[red]🂱[/]',   2:'[red]🂲[/]',   3:'[red]🂳[/]',   4:'[red]🂴[/]',   5:'[red]🂵[/]',   6:'[red]🂶[/]',   7:'[red]🂷[/]',   8:'[red]🂸[/]',   9:'[red]🂹[/]',  10:'[red]🂺[/]',  11:'[red]🂻[/]',  12:'[red]🂼[/]',  13:'[red]🂽[/]',
            14:'[red]🃁[/]',  15:'[red]🃂[/]',  16:'[red]🃃[/]',  17:'[red]🃄[/]',  18:'[red]🃅[/]',  19:'[red]🃆[/]',  20:'[red]🃇[/]',  21:'[red]🃈[/]',  22:'[red]🃉[/]',  23:'[red]🃊[/]',  24:'[red]🃋[/]',  25:'[red]🃌[/]',  26:'[red]🃍[/]',
            27:'[black]🂡[/]',28:'[black]🂢[/]',29:'[black]🂣[/]',30:'[black]🂤[/]',31:'[black]🂥[/]',32:'[black]🂦[/]',33:'[black]🂧[/]',34:'[black]🂨[/]',35:'[black]🂩[/]',36:'[black]🂪[/]',37:'[black]🂫[/]',38:'[black]🂬[/]',39:'[black]🂭[/]',
            40:'[black]🃑[/]',41:'[black]🃒[/]',42:'[black]🃓[/]',43:'[black]🃔[/]',44:'[black]🃕[/]',45:'[black]🃖[/]',46:'[black]🃗[/]',47:'[black]🃘[/]',48:'[black]🃙[/]',49:'[black]🃚[/]',50:'[black]🃛[/]',51:'[black]🃜[/]',52:'[black]🃝[/]'}
    rp(f'[red]{[cardc[x] for x in range(1,27)]}[/]')
    rp(f'[black]{[cardc[x] for x in range(27,53)]}[/]')
    coly=[[outa[xu][xt] for xu in range(22)] for xt in range(8)]
    
    #col0=[outa[xs][0] for xs in range(22)]
    #col7=[outa[xs][7] for xs in range(22)]    #     colx=[]
    #colx.append(col0);colx.append(col7)    rp(colx);
    rp(f'{coly},{colh[2][2]=}');ct=0
    for ex in range(22):
        for fx in range(8):
            if ct%8 == 0:                    # and a > 8:
                print() 
            rp(f'{cardc[outa[ex][fx]]}',end=', ')  #rp(b if not (b=='0') else '',end=',')
            ct+=1
    if validMove:
        movit(  running, output, suitlit, sdeck, outa, q, moapt, doapt)
    table1 = Table(title="Star Wars Movies")
    
    table1.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table1.add_column("Title", style="magenta")
    table1.add_column("Box Office", justify="right", style="green")
    
    table1.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
    table1.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
    table1.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
    table1.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")
    rp(f'{outa=}    colh:')#\n{colh[rw] for rw in colh}')#rp(table1)
    for rw in colh:    
        rp(rw)
    return running, output, suitlit, sdeck, outa, q
running, output, suitlit, sdeck, outa, q = pop()

while running:
    running, output, suitlit, sdeck, outa, q = runit(running, output, suitlit, sdeck, outa, q)