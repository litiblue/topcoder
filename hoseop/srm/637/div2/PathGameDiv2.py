#!/usr/bin/env python

class PathGameDiv2:
	def calc(self, board):
		plus_cnt = 0
		minus_cnt = 0
		sharp = -1
		for i in range(len(board[0])):
			if board[0][i]=='.' and board[1][i]=='.':	plus_cnt+=1
			if board[0][i]=='#':
				if sharp==1:	minus_cnt+=1
				sharp = 0
			elif board[1][i]=='#':
				if sharp==0:	minus_cnt+=1
				sharp = 1
		if plus_cnt==0: return 0
		return plus_cnt-minus_cnt
