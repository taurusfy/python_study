#coding=utf-8

#S-spade 黑桃
#H-heart 红桃
#D-diamond 方片
#C-club 梅花
#H2 表示红桃2 ，以此类推，red_Jocker-大王，black_Jocker-小王

import random
pocker_list=["H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA",\
             "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",\
             "D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",\
             "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",\
             "red_Jocker","black_Jocker"]
#洗牌
random.shuffle(pocker_list)
print "完成洗牌。。。"
#print pocker_list

player1=[]
player2=[]
player3=[]

i=0
while i < len(pocker_list)-3:
    player1.append(pocker_list[i])
    player2.append(pocker_list[i+1])
    player3.append(pocker_list[i+2])
    i=i+3
    
print "玩家1有 %d张牌: " % len(player1)
for i in player1:
    print i,
print "\n玩家2有 %d张牌: " % len(player2)
for j in player2:
    print j,
print "\n玩家3有 %d张牌: " % len(player3)
for k in player3:
    print k,
print "\n底牌:"
print pocker_list[-3],pocker_list[-2],pocker_list[-1]
