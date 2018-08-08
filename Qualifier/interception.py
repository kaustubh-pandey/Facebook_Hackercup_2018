# def power(after_sum):
# 	for x in range():
# 		after_mul=[i*x for i in after_sum]
# 		po=0
# 		for r in range(len(after_mul)-1,-1,-1):
# 			po=after_mul[r]**po

# def poly(a,n):
# 	terms=[]
# 	for i in range(n,-1,-1):
# 		terms.append([a[n],n])
# 	after_sum=[]
# 	after_sum.append(terms[0][0])
# 	for i in range(1,len(terms)):
# 		y=terms[i][0]+terms[i-1][2]
# 		after_sum.append(y)
with open('interception.txt','r') as f:
	for line in f:
		t=int(line)
		break
	for z in range(t):
		for line in f:
			n=int(line)
			break
		#print(n)
		for i in range(n+1):
			for line in f:
				s=int(line)
				#print(s)
				break
		with open('interception_output.txt','a') as fp:
			if(n%2):
				fp.write('Case #%d: 1\n'%(z+1))
				#print('Case #%d: 1'%(z+1))
				fp.write("0.0\n")
				#print('0.0')
			else:
				fp.write('Case #%d: 0\n'%(z+1))
				#print('Case #%d: 0\n'%(z+1))
	
