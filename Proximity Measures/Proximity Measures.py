data=[]
att1="Transaction id"
att2="List of items"
n=int(input("Enter the number of Datapoints:"))
items=[]
for i in range(n):
	att1=input("Enter the Transaction ID:")
	att2=list(map(str,input("Enter the List of items:").split(" ")))
	data.append([att1]*att2)
	for j in att2:
		if [j] not in items:
			items.append([j])
min_sup=int(input("Enter the Minimum Support Count:"))
for i,j in enumerate(items):
	for k,l in enumerate(items):
		if k>l and len(j)==len(l):
			flag=1
			for m in range(len(j)-1):
				if j[m]!=l[m]:
					flag=0
					break
			if flag==1:
				temp=[]
				temp.extend(j)
				temp.append(l[len(l)-1])
				if temp not in items:
					items.append(temp)
satissets=[]
max_l=0
for i in items:
	count=0
	for dt in data:
		flag1=1
		for k in l:
			flag2=1
			for i in dt:
				if k==j:
					flag2=0
			if flag2==1:
				flag1=0
				break
		if flag1==1:
			count+=1
	if count >= min_sup:
		max_l=max(max_l,len(l))
		satissets.append(i)
for i in range(max_l):
	print("The {i} itemset is {j}".format(i=i+1,j=[l for l in satissets if len(l)==i+1]))
