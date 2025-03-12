MOD = 998244353

def main1():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    p = list(map(int, input().split()))
    for i in range(2, n+1):
        adj[p[i - 2]].append(i)

    D=0
    a=[]
    q=[1]
    while q:
        a.append([])
        new_q=[]
        for u in q:
            a[D].append(u)
            new_q.extend(adj[u])
        q=new_q
        D+=1

    F = [0]*(D+2)
    f = [0]*(n+1)

    for d in range(D-1, 0, -1):
        for u in a[d]:
            f[u] =(1+ F[d+1]) %MOD
            for v in adj[u]:
                f[u]= (f[u]-f[v]) %MOD
            F[d]=(F[d]+ f[u])% MOD
    F[1] = (F[1]+1+MOD)%MOD
    print(F[1])

def main():
    TC = int(input())
    for _ in range(TC):
        main1()

main()
