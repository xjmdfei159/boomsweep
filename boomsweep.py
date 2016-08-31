#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: kabi
@license: Apache Licence 
@file: boomsweep.py
@time: 2016/8/31 0031 下午 11:05
"""


from random import randint
import random

class BoomMap(object):

	def __init__(self, row, col):
		self._board = []
		self._boommap = []
		self._boomnum = 50

		for i in range(col):
			self._board.append(["0"] * row)

		while len(self._boommap) < self._boomnum:
			new_boom = [random.randint(0, len(self._board[1]) - 1),random.randint(0, len(self._board) - 1)]
			for i in self._boommap:
				if i == new_boom:
					break
			else:
				self._boommap.append(new_boom)

	def show_board(self):
		for i in self._board:
			print(" ".join(i))

	def show_boom(self):
		for i in range(len(self._boommap)):
			boom = self._boommap[i]
			self._board[boom[0]][boom[1]] = "X"

	def boom_pos(self, row, col):
		count = 0
		if row - 1 >= 0 and col - 1 >= 0:
			if self._board[row-1][col-1] == "X":
				count +=1
		if row >= 0 and col - 1 >= 0:
			if self._board[row][col-1] == "X":
				count +=1
		if row + 1 >= 0 and col - 1 >= 0:
			if self._board[row+1][col-1] == "X":
				count +=1
		if row - 1 >= 0 and col >= 0:
			if self._board[row-1][col] == "X":
				count +=1
		if row + 1 >= 0 and col >= 0:
			if self._board[row+1][col] == "X":
				count +=1
		if row - 1 >= 0 and col + 1 >= 0:
			if self._board[row-1][col+1] == "X":
				count +=1
		if row >= 0 and col + 1 >= 0:
			if self._board[row][col+1] == "X":
				count +=1
		if row + 1 >= 0 and col + 1 >= 0:
			if self._board[row-1][col+1] == "X":
				count +=1
		return count

def main():
	kabi = BoomMap(10, 10)
	kabi.show_boom()
	kabi.show_board()
	guess_row = int(raw_input("guess row"))
	guess_col = int(raw_input("guess col"))
	a = kabi.boom_pos(guess_row - 1,guess_col)
	print(a)

if __name__ == "main":
	main()