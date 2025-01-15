
#Positional Argument
"""
def perc(hin, eng, math, odi, phy, che, his, geo):
    sub_perc = []
    sub_perc.append(hin / 100 * 100)
    sub_perc.append(eng / 100 * 100)
    sub_perc.append(odi / 100 * 100)
    sub_perc.append(math / 100 * 100)
    sub_perc.append(phy / 75 * 100)
    sub_perc.append(che / 75 * 100)
    sub_perc.append(his / 50 * 100)
    sub_perc.append(geo / 50 * 100)

    total = 650
    obt_mark = hin + eng + odi + phy + che + his + geo
    total_p = obt_mark / total * 100
    return sub_perc, total_p

hin = 60
eng = 80
math = 65
odi = 76
phy = 58
che = 53
his = 43
geo = 39

sub_perce = []
sub_perce, total_perc = perc(hin, math, eng, odi, phy, che, his, geo )

print(f"Subject Wise Percentage: {sub_perce}")
print(f"Total Percentage: {total_perc}")
"""
# KEYWORD ARGUMENATS

def perc(hin, eng, math, odi, phy, che, his, geo):
    sub_perc = []
    sub_perc.append(hin / 100 * 100)
    sub_perc.append(eng / 100 * 100)
    sub_perc.append(math / 100 * 100)
    sub_perc.append(odi / 100 * 100)    
    sub_perc.append(phy / 75 * 100)
    sub_perc.append(che / 75 * 100)
    sub_perc.append(his / 50 * 100)
    sub_perc.append(geo / 50 * 100)

    total = 650
    obt_mark = hin + eng + odi + phy + che + his + geo
    total_p = obt_mark / total * 100
    return sub_perc, total_p



sub_perce = []
sub_perce, total_perc = perc(hin=60, math=90, eng=87, odi=76, phy=53, che=52, his=30, geo=43 )

print(f"Subject Wise Percentage: {sub_perce}")
print(f"Total Percentage: {total_perc}")
