#created by xiaolong
# 2016-08-17

#上楼梯问题


def UpStairs(n):
	if(n<=0): 
		return 1;
	elif(n>1): 
		return UpStairs(n-1)+UpStairs(n-2);
	elif (n==1):
		return 1;

def Main(): 
	k = int(input("输入楼梯层数:"));
	if(k==0): 
		print(0);
	else:
		print(UpStairs(k));
		
Main();