#%%
plutarch=[]
Magic4 = ((00,00,"00"),
          (00,00,"Ah"), (00,00,"2h"), (29,42,"3h"), (30,43,"4h"), (31,44,"5h"), (32,45,"6h"), (33,46,"7h"), (34,47,"8h"), (35,48,"9h"), (36,49,"Th"), (37,50,"Jh"), (38,51,"Qh"), (39,52,"Kh"),
          (00,00,"Ad"), (00,00,"2d"), (29,42,"3d"), (30,43,"4d"), (31,44,"5d"), (32,45,"6d"), (33,46,"7d"), (34,47,"8d"), (35,48,"9d"), (36,49,"Td"), (37,50,"Jd"), (38,51,"Qd"), (39,52,"Kd"),
          (00,00,"As"), (00,00,"2s"), ( 3,16,"3s"), ( 4,17,"4s"), ( 5,18,"5s"), ( 6,19,"6s"), ( 7,20,"7s"), ( 8,21,"8s"), ( 9,22,"9s"), (10,23,"Ts"), (11,24,"Js"), (12,25,"Qs"), (13,26,"Ks"),
          (00,00,"Ac"), (00,00,"2c"), ( 3,16,"3c"), ( 4,17,"4c"), ( 5,18,"5c"), ( 6,19,"6c"), ( 7,20,"7c"), ( 8,21,"8c"), ( 9,22,"9c"), (10,23,"Tc"), (11,24,"Jc"), (12,25,"Qc"), (13,26,"Kc"))
aces = [1,14,27,40]
king = [13,26,39,52]

print("Hello world")
for ihop in range(1,14):
    print(f"M4{Magic4[ihop]}, {Magic4[ihop+13]}, {Magic4[ihop+26]}, {Magic4[ihop+39]}")

