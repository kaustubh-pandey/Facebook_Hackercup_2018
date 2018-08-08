def mapping(n,m,r):
	if(m>=r):
		return m-r
	return n+m-r

with open('tourist.txt','r') as f:
	for line in f:
		t=int(line)
		#print(t)
		break
	for z in range(t):
		for line in f:
			n,k,v=list(map(int,line.strip().split()))
			#print(n,k,v)
			break
		a=[]
		for i in range(n):
			for line in f:
				s=line.strip()
				#print(s)
				break
			a.append([i,s])
		a=a[::-1]
		r=(k*(v-1))%n
		b=[]
		for m in range(n-1,n-k-1,-1):
			b.append(a[mapping(n,m,r)])
		b.sort()
		# print('Case #%d: '%(z+1),end="")
		# for i in range(len(b)):
		# 	print(b[i][1],end=" ")
		# print("")
		with open('tourist_output.txt','a') as fp:
			fp.write('Case #%d: '%(z+1))
			for i in range(len(b)):
				fp.write(b[i][1])
				fp.write(" ")
			fp.write("\n")


# t=int(input())
# for z in range(t):
# 	n,k,v=list(map(int,input().split()))
# 	a=[]
# 	for i in range(n):
# 		s=input()
# 		a.append([i,s])
# 	a=a[::-1]
# 	r=(k*(v-1))%n
# 	b=[]
# 	for m in range(n-1,n-k-1,-1):
# 		b.append(a[mapping(n,m,r)])
# 	b.sort()
# 	print('Case #%d: '%(z+1),end="")
# 	for i in range(len(b)):
# 		print(b[i][1],end=" ")
# 	print("")
