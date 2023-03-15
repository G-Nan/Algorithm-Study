import math
#gcd: 최대공약수
def solution(numer1, denom1, numer2, denom2):
    n, d=numer1 * denom2 + denom1 * numer2, denom1 * denom2 #분자, 분모
    gcd=math.gcd(n,d) #최대공약수 반환
    
    return (n//gcd,d//gcd)