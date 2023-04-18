import pygame, math, threading
from sys import maxsize as infinity
from pieces import *
from board import *


# DEPTH FOR BOT
DEPTH = 2

HIGHLIGHT_COLOR = (255,0,0)
FONT_COLOR = (0,0,0)
LIGHT_SQUARES = (204, 183, 174)
DARK_SQUARES = (112, 102, 119)

highlight = False
SIDE = 560
PS = SIDE // 8
pieces = {
	"black_rook_L":Rook("black", (0,0)),
	"black_rook_R":Rook("black", (0,7)),
	"white_rook_L":Rook("white", (7,0)),
	"white_rook_R":Rook("white", (7,7)),

	"black_knight_L":Knight("black", (0,1)),
	"black_knight_R":Knight("black", (0,6)),
	"white_knight_L":Knight("white", (7,1)),
	"white_knight_R":Knight("white", (7,6)),

	"black_bishop_L":Bishop("black", (0,2)),
	"black_bishop_R":Bishop("black", (0,5)),
	"white_bishop_L":Bishop("white", (7,2)),
	"white_bishop_R":Bishop("white", (7,5)),

	"black_queen":Queen("black", (0,3)),
	"white_queen":Queen("white", (7,3)),

	"black_king":King("black", (0,4)),
	"white_king":King("white", (7,4)),

	"black_pawn_1":Pawn("black", (1,0)),
	"black_pawn_2":Pawn("black", (1,1)),
	"black_pawn_3":Pawn("black", (1,2)),
	"black_pawn_4":Pawn("black", (1,3)),
	"black_pawn_5":Pawn("black", (1,4)),
	"black_pawn_6":Pawn("black", (1,5)),
	"black_pawn_7":Pawn("black", (1,6)),
	"black_pawn_8":Pawn("black", (1,7)),

	"white_pawn_1":Pawn("white", (6,0)),
	"white_pawn_2":Pawn("white", (6,1)),
	"white_pawn_3":Pawn("white", (6,2)),
	"white_pawn_4":Pawn("white", (6,3)),
	"white_pawn_5":Pawn("white", (6,4)),
	"white_pawn_6":Pawn("white", (6,5)),
	"white_pawn_7":Pawn("white", (6,6)),
	"white_pawn_8":Pawn("white", (6,7)),
}

moved = False
turn = "white"
game_board = Board(pieces)
pieces_in_play = game_board.reset()

screen = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("Chess")
pygame.font.init()
size = 40
game_over = False
got = ""
font = pygame.font.SysFont("Consolas", size)


def handle_pawn_promotion(piece):
	queen = Queen(turn, piece.coordinates)
	pieces_in_play.remove(piece)
	pieces_in_play.append(queen)
	game_board.set(piece, piece.coordinates)

def get_legal_moves(piece):
	moves = piece.get_possible_moves(game_board.board)
	legal_moves = moves.copy()

	for move in moves:
		if move == "O-O" or move == "O-O-O":
			if isAttacked(piece.color, piece.coordinates):
				legal_moves.remove(move)
			
		else:
			makeMove(piece, move)
			king = pieces[f"{piece.color}_king"]
			if isAttacked(piece.color, king.coordinates):
				legal_moves.remove(move)

			undoMove()

	return legal_moves

def isAttacked(color_of_self, coordinates):
	for piece in pieces_in_play:
		if color_of_self != piece.color:
			if piece.pieceType == "pawn":
				if coordinates in piece.get_possible_moves(game_board.board, True):
					return True

			elif coordinates in piece.get_possible_moves(game_board.board):
				return True

	return False


def reset_game(pieces):
	for piece in pieces.values():
		pieces_in_play.append(piece)
		r, c = piece.coordinates
		game_board.set(piece, (r,c))

def draw_board(screen):
	for row in range(8):
		for column in range(8):
			if (row + column) % 2 == 0:
				color = DARK_SQUARES
			else:
				color = LIGHT_SQUARES

			pygame.draw.rect(screen, color, pygame.rect.Rect(row*PS, column*PS, PS, PS))

def draw_pieces(screen, pieces):
	for piece in pieces_in_play:
		if piece.highlight:
			for move in get_legal_moves(piece):
				if move == "O-O":
					if piece.color == "white":
						x,y = (7, 6)
					else:
						x,y = (0,6)

				elif move == "O-O-O":
					if piece.color == "white":
						x,y = (7, 2)
					else:
						x,y = (0,2)

				else:
					x,y = move

				s = pygame.Surface((PS, PS))
				s.set_alpha(100)
				s.fill(HIGHLIGHT_COLOR)
				screen.blit(s, (y*PS, x*PS))

	for piece in pieces_in_play:
		x, y = piece.coordinates
		screen.blit(piece.image, (y*PS+4, x*PS+10))

def flip(lst):
	newlst = []
	for row in lst:
		newlst.insert(0, row)

	return newlst

def get_square_table(piece):
	if piece.pieceType == "king":
		table = [
			[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
			[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
			[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
			[-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
			[-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
			[-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
			[ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
			[ 8.0,  10.0,  1.0,  0.0,  0.0,  1.0, 10.0, 8.0]
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

	elif piece.pieceType == "queen":
		table = [
			[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
			[-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
			[-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
			[-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
			[ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
			[-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
			[-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
			[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

	elif piece.pieceType == "bishop":
		table = [
			[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
			[-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
			[-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
			[-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
			[-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
			[-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
			[-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
			[-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

	elif piece.pieceType == "knight":
		table = [
			[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
			[-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
			[-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
			[-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
			[-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
			[-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
			[-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
			[-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

	elif piece.pieceType == "rook":
		table = [
			[ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
			[ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
			[-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
			[-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
			[-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
			[-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
			[-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
			[-0.5,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0, -0.5],
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

	elif piece.pieceType == "pawn":
		table = [
			[ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
			[ 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
			[ 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
			[ 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
			[ 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
			[ 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
			[ 0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
			[ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
		]

		if piece.color == "white":
			return table

		else:
			return flip(table)

def evaluate(pieces_in_play, isMaximizing):
	if isCheckMate("white" if isMaximizing else "black"):
		if isMaximizing:
			return -infinity
		else:
			return infinity

	elif isDraw("black" if isMaximizing else "white"):
		return 0

	piece_points = {
		"pawn":1,
		"knight":3,
		"bishop":3,
		"rook":5,
		"queen":9,
		"king":0
	}
	white_eval = 0
	black_eval = 0

	for piece in pieces_in_play:
		x,y = piece.coordinates
		if piece.color == "white":
			white_eval += get_square_table(piece)[x][y] * 0.1
			white_eval += piece_points[piece.pieceType]

		else:
			black_eval += get_square_table(piece)[x][y] * 0.1
			black_eval += piece_points[piece.pieceType] 

	evaluation = white_eval - black_eval
	return evaluation

def gameover(text):
	global game_over, got
	game_over = True
	got = text

def isDraw(turn):
	all_moves = []
	for move, piece in get_moves(turn):
		all_moves.append(move)

	if all_moves == []:
		return True

	pieces = []
	for piece in pieces_in_play:
		if piece.pieceType != "king":
			pieces.append(piece.pieceType.capitalize() + "." + piece.color)

	if pieces == []:
		return True

	elif pieces == ["Bishop.black"] or pieces == ["Bishop.white"]:
		return True

	elif pieces == ["Knight.black"] or pieces == ["Knight.white"]:
		return True

	return False

	
def change_turn():
	global turn
	if turn == "white":
		turn = "black"
	else:
		turn = "white"

def isCheckMate(turn):
	all_moves = []
	for move, piece in get_moves(turn):
		all_moves.append(move)

	king = pieces[f"{turn}_king"]

	if all_moves == [] and isAttacked(king.color, king.coordinates):
		return True

	return False

def minmax(isMaximizing, depth, alpha, beta):
	if depth == 0:
		return evaluate(pieces_in_play, isMaximizing)

	elif isMaximizing:
		bestscore = -infinity
		for move, piece in get_moves("white"):
			makeMove(piece, move)

			score = minmax(False, depth-1, alpha, beta)

			undoMove()

			bestscore = max(score, bestscore)
			alpha = max(alpha, bestscore)
			if alpha >= beta:
				break

	elif not isMaximizing:
		bestscore = infinity
		for move, piece in get_moves("black"):
			makeMove(piece, move)

			score = minmax(True, depth-1, alpha, beta)
			
			undoMove()

			bestscore = min(score, bestscore)
			beta = min(beta, bestscore)
			if alpha >= beta:
				break

	return bestscore

def get_moves(color):
	moves = []
	for piece in pieces_in_play:
		if piece.color == color:
			for move in get_legal_moves(piece):
				if move == "O-O":
					moves.append([move, piece])
					continue

				elif move == "O-O-O":
					moves.append([move, piece])
					continue

				elif game_board.get(move) != []:
					if game_board.get(move).color != piece.color:
						moves.append([move, piece])

				elif piece.pieceType == "pawn" and game_board.get(move) == 7:
					moves.append([move, piece])

	for piece in pieces_in_play:
		if piece.color == color:
			for move in get_legal_moves(piece):
				if not move in moves:
					moves.append([move, piece])

	return moves


def play_computer_move():
	bestscore = infinity
	bestmove = None
	bestpiece = None

	for move, piece in get_moves("black"):
		makeMove(piece, move)

		score = minmax(True, DEPTH-1, -infinity, infinity)

		undoMove()

		if score < bestscore:
			bestmove = move
			bestscore = score
			bestpiece = piece

	if bestmove:
		makeMove(bestpiece, bestmove)

	pygame.display.set_caption("Chess")
	change_turn()

def undoMove():
	lastmove = game_board.lastmove[:]
	if lastmove[0] == "promotion":
		queen = game_board.get(lastmove[1][1])
		pawn = lastmove[1][2]
		pieces_in_play.remove(queen)
		pieces_in_play.append(pawn)

	old_piece = game_board.undoMove()
	if old_piece != []:
		pieces_in_play.append(old_piece)

	
	if len(lastmove) != 3:
		piece = lastmove[0][-1]
		if piece.pieceType == "king" or piece.pieceType == "rook":
			if len(piece.movelist) <= DEPTH-1:
				piece.hasMoved = False

			if piece.pieceType == "king":
				if piece.coordinates != piece.starting_coordinates:
					piece.hasMoved = True


def check_game_over():
	if isDraw('white' if turn == 'black' else 'black'):
		gameover("It's A Draw!")

	elif isCheckMate(turn):
		gameover(f"Checkmate! {'white' if turn == 'black' else 'black'} Wins!")


def makeMove(piece, move):
	old_piece = game_board.makeMove(piece, move)
	if old_piece != []:
		pieces_in_play.remove(old_piece)

	if piece.pieceType == "pawn" and (move[0] == 0 or move[0] == 7):
		queen = Queen(piece.color, piece.coordinates)
		game_board.set(queen, move)
		pieces_in_play.remove(piece)
		pieces_in_play.append(queen)
		game_board.lastmove = ["promotion", [game_board.lastmove[0][0], move, piece], old_piece]

	return old_piece

def get_captures(color):
	captures = []
	for move, piece in get_moves(color):
		if game_board.get(move) != [] and game_board.get(move).color != color:
			if not move in captures:
				captures.append(move)
	return captures


def mainloop():
	global moved
	running = True
	while running:
		draw_board(screen)
		draw_pieces(screen, pieces)
		if game_over:
			gof = font.render(got, True, FONT_COLOR)
			screen.blit(gof, (SIDE / 2 - len(got)/2 * (size/2+1), SIDE / 2 - size/2))
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and turn == "white":
				for piece in pieces_in_play:
					if piece.highlight:
						if turn == piece.color:
							x, y = pygame.mouse.get_pos()
							x = math.floor(x / PS)
							y = math.floor(y / PS)
							moves = get_legal_moves(piece)

							if ("O-O" in moves and x == piece.coordinates[1] + 2 and y == piece.coordinates[0]) or ("O-O-O" in moves and x == piece.coordinates[1] - 2 and y == piece.coordinates[0]) or ((y,x) in moves):
								for move in moves:
									if move == "O-O" and x == piece.coordinates[1] + 2 and y == piece.coordinates[0]:
										makeMove(piece, move)

									elif move == "O-O-O" and x == piece.coordinates[1] - 2 and y == piece.coordinates[0]:
										makeMove(piece, move)

									elif (y,x) == move:
										makeMove(piece, move)
							else:
								moved = True
								piece.highlight = False
								continue

							change_turn()
							check_game_over()
							moved = True
							piece.highlight = False
							pygame.display.set_caption("Thinking...")
							draw_board(screen)
							draw_pieces(screen, pieces)
							pygame.display.update()
							play_computer_move()

							
				if not moved:
					x, y = pygame.mouse.get_pos()
					x = math.floor(x / PS)
					y = math.floor(y / PS)
					piece = game_board.get(((y,x)))
					if piece != []:
						if turn == piece.color:
							piece.highlight = True

				moved = False
		pygame.display.update()

if __name__ == "__main__":
	mainloop()