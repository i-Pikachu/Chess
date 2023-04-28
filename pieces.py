import pygame

class Rook:
	def __init__(self, color, coordinates, hasMoved = False):
		self.color = color
		self.pieceType = "rook"
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.movelist = []
		self.hasMoved = hasMoved
		self.directions = ["N", "E", "S", "W"]
		self.image = pygame.image.load(f"images\\{self.color}_rook.png")

	def get_possible_moves(self, board):
		self.moves.clear()
		for direction in self.directions:
			self.get_next_square(direction, self.coordinates, board)

		return self.moves

	def get_next_square(self, direction, coordinates, board):
		if direction == "N" and coordinates[0] != 0:
			x, y = coordinates[0] - 1, coordinates[1]
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		if direction == "S" and coordinates[0] != 7:
			x, y = coordinates[0] + 1, coordinates[1]
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		if direction == "E" and coordinates[1] != 7:
			x, y = coordinates[0], coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		if direction == "W" and coordinates[1] != 0:
			x, y = coordinates[0], coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

class Knight:
	def __init__(self, color, coordinates):
		self.color = color
		self.pieceType = "knight"
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.directions = ["N", "E", "S", "W"]
		self.image = pygame.image.load(f"images\\{self.color}_knight.png")

	def get_possible_moves(self, board):
		self.moves.clear()
		for direction in self.directions:
			self.get_next_square(direction, self.coordinates, board)

		return self.moves

	def get_next_square(self, direction, coordinates, board):
		if direction == "N" and coordinates[0] > 1:
			if coordinates[1] != 0:
				x, y = coordinates[0] - 2, coordinates[1] - 1

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

			if coordinates[1] != 7:
				x, y = coordinates[0] - 2, coordinates[1] + 1

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

		if direction == "S" and coordinates[0] < 6:
			if coordinates[1] != 0:
				x, y = coordinates[0] + 2, coordinates[1] - 1

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

			if coordinates[1] != 7:
				x, y = coordinates[0] + 2, coordinates[1] + 1
				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

		if direction == "E" and coordinates[1] < 6:
			if coordinates[0] != 0:
				x, y = coordinates[0] - 1, coordinates[1] + 2

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

			if coordinates [0] != 7:
				x, y = coordinates[0] + 1, coordinates[1] + 2

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

		if direction == "W" and coordinates[1] > 1:
			if coordinates[0] != 0:
				x, y = coordinates[0] - 1, coordinates[1] - 2

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

			if coordinates[0] != 7:
				x, y = coordinates[0] + 1, coordinates[1] - 2

				if board[x][y] == []:
					self.moves.append((x,y))

				elif board[x][y].color != self.color:
					self.moves.append((x,y))

class Bishop:
	def __init__(self, color, coordinates):
		self.color = color
		self.pieceType = "bishop"
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.directions = ["NE", "NW", "SE", "SW"]
		self.image = pygame.image.load(f"images\\{self.color}_bishop.png")

	def get_possible_moves(self, board):
		self.moves.clear()
		for direction in self.directions:
			self.get_next_square(direction, self.coordinates, board)

		return self.moves

	def get_next_square(self, direction, coordinates, board):
		if direction == "NE" and coordinates[0] != 0 and coordinates[1] != 7:
			x, y = coordinates[0] - 1, coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		if direction == "SE" and coordinates[0] != 7 and coordinates[1] != 7:
			x, y = coordinates[0] + 1, coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))


		if direction == "NW" and coordinates[0] != 0 and coordinates[1] != 0:
			x, y = coordinates[0] - 1, coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		if direction == "SW" and coordinates[0] != 7 and coordinates[1] != 0:

			x, y = coordinates[0] + 1, coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

class Queen:
	def __init__(self, color, coordinates):
		self.color = color
		self.pieceType = "queen"
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.directions = ["N", "E", "S", "W", "NE", "NW", "SE", "SW"]
		self.image = pygame.image.load(f"images\\{self.color}_queen.png")

	def get_possible_moves(self, board):
		self.moves.clear()
		for direction in self.directions:
			self.get_next_square(direction, self.coordinates, board)

		return self.moves

	def get_next_square(self, direction, coordinates, board):
		if direction == "NE" and coordinates[0] != 0 and coordinates[1] != 7:
			x, y = coordinates[0] - 1, coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "NW" and coordinates[0] != 0 and coordinates[1] != 0:
			x, y = coordinates[0] - 1, coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "SE" and coordinates[0] != 7 and coordinates[1] != 7:
			x, y = coordinates[0] + 1, coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "SW" and coordinates[0] != 7 and coordinates[1] != 0:
			x, y = coordinates[0] + 1, coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "N" and coordinates[0] != 0:
			x, y = coordinates[0] - 1, coordinates[1]
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)


			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "E" and coordinates[1] != 7:
			x, y = coordinates[0], coordinates[1] + 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "W" and coordinates[1] != 0:
			x, y = coordinates[0], coordinates[1] - 1
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))

		elif direction == "S" and coordinates[0] != 7:
			x, y = coordinates[0] + 1, coordinates[1]
			if board[x][y] == []:
				self.moves.append((x,y))
				self.get_next_square(direction, (x,y), board)

			elif board[x][y].color != self.color:
				self.moves.append((x,y))


class King:
	def __init__(self, color, coordinates, hasMoved = False):
		self.color = color
		self.pieceType = "king"
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.movelist = []
		self.hasMoved = hasMoved
		self.directions = ["N", "E", "S", "W", "NE", "NW", "SE", "SW", "O-O", "O-O-O"]
		self.image = pygame.image.load(f"images\\{self.color}_king.png")


	def get_possible_moves(self, board):
		self.moves.clear()
		for direction in self.directions:
			self.get_next_square(direction, board)

		return self.moves

	def get_squares(self, board):
		squares = []
		for row in board:
			for col in row:
				if col != []:
					if col.pieceType == "king" and col.color != self.color:
						x = board.index(row)
						y = row.index(col)
						if x == 0:
							if y == 0:
								squares = [(x+1, y), (x, y+1), (x+1, y+1)]

							elif y == 7:
								squares = [(x+1, y), (x, y-1), (x+1, y-1)]

							else:
								squares = [(x+1, y), (x, y-1), (x, y+1), (x+1, y+1), (x+1, y-1)]

						elif x == 7:
							if y == 0:
								squares = [(x-1, y), (x, y+1), (x-1, y+1)]

							elif y == 7:
								squares = [(x-1, y), (x, y-1), (x-1, y-1)]

							else:
								squares = [(x-1, y), (x, y-1), (x, y+1), (x-1, y+1), (x-1, y-1)]

						elif y == 0:
							squares = [(x+1, y), (x-1, y), (x, y+1), (x+1, y+1), (x-1, y+1)]

						elif y == 7:
							squares = [(x+1, y), (x-1, y), (x, y-1), (x+1, y-1), (x-1, y-1)]

						else:
							squares = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x+1, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1)]

		return squares


	def get_next_square(self, direction, board):
		x, y = self.coordinates
		squares = self.get_squares(board)
		if direction == "N" and x != 0:
			if board[x-1][y] != []:
				piece = board[x-1][y]
				if piece.color == self.color:
					return

			if not (x-1, y) in squares:
				self.moves.append((x-1, y))
			

		elif direction == "S" and x != 7:
			if board[x+1][y] != []:
				piece = board[x+1][y]
				if piece.color == self.color:
					return

			if not (x+1, y) in squares:
				self.moves.append((x+1, y))

		elif direction == "E" and y != 7:
			if board[x][y+1] != []:
				piece = board[x][y+1]
				if piece.color == self.color:
					return

			if not (x, y+1) in squares:
				self.moves.append((x, y+1))


		elif direction == "W" and y != 0:
			if board[x][y-1] != []:
				piece = board[x][y-1]
				if piece.color == self.color:
					return

			if not (x, y-1) in squares:
				self.moves.append((x, y-1))

		elif direction == "NE" and x != 0 and y != 7:
			if board[x-1][y+1] != []:
				piece = board[x-1][y+1]
				if piece.color == self.color:
					return

			if not (x-1, y+1) in squares:
				self.moves.append((x-1, y+1))

		elif direction == "NW" and x != 0 and y != 0:
			if board[x-1][y-1] != []:
				piece = board[x-1][y-1]
				if piece.color == self.color:
					return

			if not (x-1, y-1) in squares:
				self.moves.append((x-1, y-1))

		elif direction == "SE" and x != 7 and y != 7:
			if board[x+1][y+1] != []:
				piece = board[x+1][y+1]
				if piece.color == self.color:
					return

			if not (x+1, y+1) in squares:
				self.moves.append((x+1, y+1))

		elif direction == "SW" and x != 7 and y != 0:
			if board[x+1][y-1] != []:
				piece = board[x+1][y-1]
				if piece.color == self.color:
					return

			if not (x+1, y-1) in squares:
				self.moves.append((x+1, y-1))


		elif direction == "O-O":
			if not self.hasMoved and board[x][y+3] != [] and board[x][y+1] == [] and board[x][y+2] == []:
				rook = board[x][y+3]
				if rook.pieceType == "rook" and not rook.hasMoved and rook.color == self.color and not (x, y+2) in squares:
					self.moves.append("O-O")


		elif direction == "O-O-O":
			if not self.hasMoved and board[x][y-4] != [] and board[x][y-1] == [] and board[x][y-2] == [] and board[x][y-3] == []:
				rook = board[x][y-4]
				if rook.pieceType == "rook" and not rook.hasMoved and rook.color == self.color and not (x, y-2) in squares:
					self.moves.append("O-O-O")



class Pawn:
	def __init__(self, color, coordinates):
		self.pieceType = "pawn"
		self.color = color
		self.highlight = False
		self.coordinates = coordinates
		self.starting_coordinates = coordinates
		self.moves = []
		self.threats = []
		self.directions = ["N", "S", "NE", "SE", "NW", "SW"]
		self.image = pygame.image.load(f"images\\{self.color}_pawn.png")
		self.hasMoved = False

	def get_possible_moves(self, board, onlythreats=False):
		self.moves.clear()
		self.threats.clear()
		for direction in self.directions:
			self.get_next_square(direction, board)

		if onlythreats:
			return self.threats

		return self.moves

	def get_next_square(self, direction, board):
		x, y = self.coordinates
		if self.color == "white":
			if direction == "N" and x != 0:
				if board[x-1][y] == []:
					self.moves.append((x-1,y))
					if not self.hasMoved and board[x-2][y] == []:
						self.moves.append((x-2,y))

			elif direction == "NE" and x != 0 and y != 7:
				if board[x-1][y+1] == []:
					self.threats.append((x-1, y+1))

				elif board[x-1][y+1] != []:
					if board[x-1][y+1].color != self.color:
						self.threats.append((x-1, y+1))
						self.moves.append((x-1,y+1))

			elif direction == "NW" and x != 0 and y != 0:
				if board[x-1][y-1] == []:
					self.threats.append((x-1, y-1))

				elif board[x-1][y-1] != []:
					if board[x-1][y-1].color != self.color:
						self.moves.append((x-1,y-1))
						self.threats.append((x-1, y-1))	

		elif self.color == "black": 
			if direction == "S" and x != 7:
				if board[x+1][y] == []:
					self.moves.append((x+1,y))
					if not self.hasMoved and board[x+2][y] == []:
						self.moves.append((x+2,y))

			elif direction == "SE" and x != 7 and y != 7:
				if board[x+1][y+1] == []:
					self.threats.append((x+1, y+1))

				elif board[x+1][y+1] != []:
					if board[x+1][y+1].color != self.color:
						self.moves.append((x+1,y+1))
						self.threats.append((x+1, y+1))


			elif direction == "SW" and x != 7 and y != 0:
				if board[x+1][y-1] == []:
					self.threats.append((x+1, y-1))

				elif board[x+1][y-1] != []:
					if board[x+1][y-1].color != self.color:
						self.moves.append((x+1,y-1))
						self.threats.append((x+1, y-1))