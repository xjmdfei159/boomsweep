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
		self._boomposlist = []
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

	def boom_pos(self):
		self._boomposlist = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
		return self._boomposlist

	def boom_posnum(self, row, col):
		count = 0
		basicpos = self.boom_pos()
		for i,boom in enumerate(basicpos):
			if row + boom[0] >= 0 and col + boom[1] >= 0 and row + boom[0] <= 9 and col + boom[1] <= 9:
				if self._board[row + boom[0]][col + boom[1]] == "X":
					count +=1
		return count

def main():
	kabi = BoomMap(10, 10)
	kabi.show_boom()
	kabi.show_board()
	guess_row = int(raw_input("guess row:"))
	guess_col = int(raw_input("guess col:"))
	b = kabi.boom_posnum(guess_row, guess_col)
	print(b)

if __name__ == "__main__":
	main()