n, m=map(int,input().split())

basket = [0]*n #바구니: 총 N개

for _ in range(m):
    i,j,k=map(int,input().split()) #i번 바구니부터 j번 바구니까지 k번 번호 공을 넣는다

    for b in range(i-1, j): #i번 바구니부터 j번 바구니까지
        basket[b]=k #k번 번호 공을 넣는다
        
print(*basket)