import sys
input = sys.stdin.readline

cash = int(input())
MachineDuck = list(map(int,input().split()))

def JH(cash):

    stock = 0
    asset = cash

    for price in MachineDuck:
        if price <= cash:
            stock += cash//price
            asset -= stock*price
            break

    return stock, asset

def SM(cash):
    stock = 0
    asset = cash

    for i in range(len(MachineDuck)-3):

        if MachineDuck[i] < MachineDuck[i+1] < MachineDuck[i+2] < MachineDuck[i+3] and stock > 0:
            sellidx = i+3
            asset += MachineDuck[sellidx] * stock
            # print(f"sellidx = {sellidx}, asset = {asset}, stock = {stock}")
            stock = 0

        if MachineDuck[i] > MachineDuck[i+1] > MachineDuck[i+2] > MachineDuck[i+3] and asset >= MachineDuck[i+3]:
            buyidx = i+3
            # print(f"buyidx = {buyidx}")
            stock += asset // MachineDuck[buyidx]
            asset -= MachineDuck[buyidx]*stock

    if stock != 0:
        asset += stock * MachineDuck[len(MachineDuck)-1]
    return asset


jh_stock, jh_asset = JH(cash)
jh_tot = jh_stock*MachineDuck[-1] + jh_asset
sm = SM(cash)

if jh_tot > sm:
    print("BNP")
elif sm > jh_tot:
    print("TIMING")
else:
    print("SAMESAME")