
#!/usr/bin/env python

import sys

class BracketExpressions:
	def ifPossible(self, exp):
		stack = []
		new_exp = []
		free = [0 for i in range(11)]
		free[1] = free[2] = free[5] = free[6] = free[9] = free[10] = 1
		cnt = [0 for i in range(14)]
		print 'exp: ', exp
		if len(exp)%2==1:	return 'impossible'
		for ch in exp:
			if ch=='(':
				cnt[1] += 1
				new_exp.append(1)
			elif ch==')':  
				cnt[2] += 1
				new_exp.append(2)
			elif ch=='[':
				cnt[5] += 1
				new_exp.append(5)
			elif ch==']':  
				cnt[6] += 1
				new_exp.append(6)
			elif ch=='{':  
				cnt[9] += 1
				new_exp.append(9)
			elif ch=='}':  
				cnt[10] += 1
				new_exp.append(10)
			elif ch=='X':  
				cnt[13] += 1
				new_exp.append(13)
		if cnt[13] > 5: return 'impossible'
		print 'cnt: ', cnt

		rm_cnt = 1
		while rm_cnt!=0:
			x = 0
			rm_cnt = 0
			print 'new_exp: ', new_exp
			while x < len(new_exp)-1:
				pop_flag = 0
				if new_exp[x+1]-new_exp[x]==1:	#remove str
					pop_flag = 1
				elif new_exp[x]==13 and new_exp[x+1]==13:	# both X
					for str in range(10):
						if free[str]==1 and free[str+1]==1:		# did not used
							if str%2==1 and cnt[str]-cnt[str+1]==0:		# can be used
								print 'remove: ', new_exp[x], new_exp[x+1], 'str: ', str, str+1
								free[str] = free[str+1] = 0
								pop_flag = 1
				elif new_exp[x]==13:	# left X
					for str in range(11):
						if free[str]==1 and new_exp[x+1]-str==1:	#not used, can be removed
							if (str%2==0 and cnt[str]-cnt[str-1]!=0) or (str%2==1 and cnt[str+1]-cnt[str]!=0):		#can be used
								print 'remove: ', new_exp[x], new_exp[x+1], 'str: ', str
								free[str] = 0
								pop_flag = 1
				elif new_exp[x+1]==13:	# rifht X
					for str in range(11):
						if free[str]==1 and str-new_exp[x]==1:	#not used, can be removed
							if (str%2==0 and cnt[str]-cnt[str-1]!=0) or (str%2==1 and cnt[str+1]-cnt[str]!=0):		#can be used
								print 'remove: ', new_exp[x], new_exp[x+1], 'str: ', str
								free[str] = 0
								pop_flag = 1
				if pop_flag==1:
					new_exp.pop(x)
					new_exp.pop(x)
					rm_cnt += 1	
				else:	x += 1
			print 'rm_cnt: ', rm_cnt
			
		print new_exp
		if len(new_exp)==0:	return 'possible'
		else:	return 'impossible'
