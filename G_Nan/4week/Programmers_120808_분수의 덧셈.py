def divisor(num):
    elem = []
    for i in range(1, int(num**(1/2)) + 1):
        if num%i == 0:
            elem.append(i)
            elem.append(int(num/i))
            
    elem.sort()
    return elem
            
def max_divisor(num1, num2):
    gcd = 0
    
    divisor_num1 = divisor(num1)
    divisor_num2 = divisor(num2)
    print(divisor_num1, divisor_num2)
    for i in divisor_num1:
        if i in divisor_num2:
            gcd = i
            
    return gcd

def solution(numer1, denom1, numer2, denom2):
    
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    gcd = max_divisor(denom, numer)
    
    denom = int(denom / gcd)
    numer = int(numer / gcd)
    
    return [int(numer), int(denom)]