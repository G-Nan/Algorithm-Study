n=int(input())
pattern = input().split("*")
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
	file = input()
	if length > len(file):
		print("NE")
		
	else:
		if pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
			print("DA")
		else:
			print("NE")
			
# n=int(input())
# pattern = input()

# for _ in range(n):
# 	file=input()
# 	if pattern[0]==file[0] and pattern[-1]==file[-1]:
# 		print("DA")
# 	else:
# 		print("NE")

#abc*def