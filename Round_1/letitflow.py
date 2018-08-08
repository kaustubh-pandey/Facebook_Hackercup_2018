def impossible(a,n):
	if(a[0][0]=='#' or a[2][n-1]=='#'):
		return True
	for i in range(n):
		if(a[1][i]=='#'):
			return True
	return False
with open('let_it_flow.txt','r') as f:
	for line in f:
		t=int(line)
		break
	#t=int(input())
	for z in range(t):
		for line in f:
			n=int(line)
			break
		#n=int(input())
		a=[]
		for i in range(3):
			for line in f:
				a.append(list(line.strip()))
				break
		#print(a)
		with open('output.txt','a') as fp:
			fp.write('Case #%d: '%(z+1))
			if(n%2):
				fp.write("0\n")
			elif(impossible(a,n)):
				fp.write("0\n")
			else:
				arr=[2]*((n-2)//2)
				pos=0
				for i in range(1,n-2,2):
					if(a[0][i]=='#' or a[0][i+1]=='#'):
						arr[pos]-=1
					if(a[2][i]=='#' or a[2][i+1]=='#'):
						arr[pos]-=1
					pos+=1
				pro=1
				for i in range(len(arr)):
					pro=(pro*arr[i])%(10**9+7)
				fp.write(str(pro%(10**9+7)))
				fp.write("\n")
