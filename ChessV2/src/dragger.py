import pygame
from const import *


class Dragger:

    def __init__(self):

        self.piece = None

        self.dragging = False

        self.mouse_x = 0.0
        self.mouse_y = 0.0

        self.initial_row = 0.0
        self.initial_col = 0.0

    def update_blit(self, surface):

        # Making the dragged piece a bit bigger
        self.piece.set_texture(size=128)

        texture = self.piece.texture

        img = pygame.image.load(texture)
        img_center = (self.mouse_x, self.mouse_y)

        self.piece.texture_rect = img.get_rect(center=img_center)

        #  Blitting the image
        surface.blit(img, self.piece.texture_rect)

    def update_mouse(self, pos):

        # tuple for mouse cursor coords (mouse_x, mouse_y)
        self.mouse_x, self.mouse_y = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQ_SIZE
        self.initial_col = pos[0] // SQ_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
