"""
Driver File.
Responsible for handling user input and displaying the current GameState object
"""
# Imports
import pygame
import chess_engine


# Basic variables for PyGame
WIDTH = 400
HEIGHT = 400
DIMENSION = 8  # dimension of the chess board(8x8)
SQ_SIZE = HEIGHT // DIMENSION  # Square size for the grid on the board
FPS = 60  # For animations
# Images for the ches pieces
IMAGES = {}


"""
Initialising a global dictionary of images using a function.
This function should be called only once as it is a heavy task. It can make the program
laggy if called multiple times
"""


def load_images():
    # storing the notations of pieces in a list
    pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bp',
              'wR', 'wN', 'wB', 'wK', 'wQ', 'wp']

    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load(
            f"C:\\Users\\Yash\\Desktop\\Chess-Python\\Chess\\images\\{piece}.png"), (SQ_SIZE, SQ_SIZE))
    # Images can be accesed using IMAGES[piece]. e.g. IMAGES['wp']


"""
The main driver for the game.
This will handle the user inputs and handle the graphics for the game
"""


def main():
    pygame.init()  # initialise pygame

    # screen variable
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # for animations
    clock = pygame.time.Clock()
    # background color
    screen.fill(pygame.Color("white"))

    # Creating a gamestate object using a variable --> gs
    gs = chess_engine.GameState()
    # print(gs.board)

    # Loading the images
    load_images()

    # running Main loop
    running = True

    while running:
        # reading inputs during the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # drawing the board
        draw_game_state(screen, gs)
        clock.tick(FPS)
        pygame.display.flip()


"""
Responsible for the graphics of the current game state
"""


def draw_game_state(screen, gs):
    draw_board(screen)  # Draw the grid pattern on the board
    # Can be used for move suggesion, piece highlighting
    draw_pieces(screen, gs.board)  # Draw pieces on the square or the grid


"""
Drawing the grid of the square on the board. The top-left square is always LIGHT
"""


def draw_board(screen):
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            # the addition of light sq. coords. is always even
            color = colors[((row+column) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(
                column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Drawing the pieces on the square of the chess board
"""


def draw_pieces(screen, board):

    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]  # accessing the board from chess_engine
            if piece != "--":  # checking for non-empty squares
                screen.blit(IMAGES[piece], pygame.Rect(
                    column*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
