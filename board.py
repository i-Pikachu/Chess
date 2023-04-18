from pieces import *

class Board:
	def __init__(self, pieces):
		self.pieces = pieces
		self.lastmove = []
		self.history = []
		self.board = [
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
			[[],[],[],[],[],[],[],[]],
		]

	def reset(self):
		pieces_in_play = []
		for piece in self.pieces.values():
			pieces_in_play.append(piece)
			r, c = piece.coordinates
			self.board[r][c] = piece

		return pieces_in_play

	def makeMove(self, piece, move):
		if move == "O-O":
			x,y = piece.coordinates
			self.board[x][y] = []
			self.board[x][y+2] = piece
			piece.coordinates = (x, y+2)
			piece.hasMoved = True

			rook = self.board[x][y+3]
			self.board[x][y+3] = []
			self.board[x][y+1] = rook
			rook.coordinates = (x, y+1)
			rook.hasMoved = True

			self.history.append(self.lastmove)
			self.lastmove = [[(x,y), (x,y+2), piece], [(x,y+3), (x,y+1), rook], []]

			return []

		elif move == "O-O-O":
			x,y = piece.coordinates
			self.board[x][y] = []
			self.board[x][y-2] = piece
			piece.coordinates = (x, y-2)
			piece.hasMoved = True

			rook = self.board[x][y-4]
			self.board[x][y-4] = []
			self.board[x][y-1] = rook
			rook.coordinates = (x, y-1)
			rook.hasMoved = True

			self.history.append(self.lastmove)
			self.lastmove = [[(x,y), (x,y-2), piece], [(x,y-4), (x,y-1), rook], []]

			return []

		x,y = piece.coordinates
		self.board[x][y] = []
		old_piece = self.board[move[0]][move[1]]
		self.board[move[0]][move[1]] = piece
		piece.coordinates = move
		piece.hasMoved = True

		if piece.pieceType == "king" or piece.pieceType == "rook":
			piece.movelist.append(move)

		if self.lastmove != []:
			self.history.append(self.lastmove)
		self.lastmove = [[(x,y), move, piece], old_piece]
		return old_piece

	def undoMove(self):
		if self.lastmove[0] == "promotion":
			to, from_, piece = self.lastmove[1]
			old_piece = self.lastmove[-1]
			self.board[from_[0]][from_[1]] = old_piece
			self.board[to[0]][to[1]] = piece
			piece.coordinates = to

			if self.history != []:
				self.lastmove = self.history.pop()
			else:
				self.lastmove.clear()

			return old_piece

		elif len(self.lastmove) == 3:
			self.lastmove[0][-1].hasMoved = False
			self.lastmove[1][-1].hasMoved = False

			for x in self.lastmove[:-1]:
				to, from_, piece = x
				old_piece = self.lastmove[-1]
				self.board[from_[0]][from_[1]] = old_piece
				self.board[to[0]][to[1]] = piece
				piece.coordinates = to

			self.lastmove = self.history.pop()
			return []

		else:
			to, from_, piece = self.lastmove[0]
			old_piece = self.lastmove[-1]
			self.board[from_[0]][from_[1]] = old_piece
			self.board[to[0]][to[1]] = piece
			piece.coordinates = to

			if piece.pieceType == "king" or piece.pieceType == "rook":
				piece.movelist.remove(from_)

			if piece.pieceType == "pawn":
				if piece.coordinates == piece.starting_coordinates:
					piece.hasMoved = False

			if self.history != []:
				self.lastmove = self.history.pop()
			else:
				self.lastmove.clear()

			return old_piece

	def get(self, coordinates):
		return self.board[coordinates[0]][coordinates[1]]

	def set(self, piece, coordinates):
		self.board[coordinates[0]][coordinates[1]] = piece

	def show(self):
		print("\n")
		print("|----"*8, end="")
		print("|")

		for i in self.board:
			k = 0
			for j in i:
				if j != []:
					print("| " + j.pieceType[0].upper() + "  " , end="")
				else:
					print("|    ", end="")
				k += 1
			print("|  ")
			print("|----"*8, end="")
			print("|")

		print("\n")