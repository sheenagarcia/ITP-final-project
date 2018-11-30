import pygame.functionality

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set dimensions of button
        self.width, self.height = 200, 50
        self.button_colour = (22, 160, 133)
        self.text_colour = (254, 254, 254)
        self.font = pygame.font.SysFont (None, 48)

        #Build button's rect object and center it

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Button message needs to be prepped once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into rendered image and center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button, then msg
        self.screen.fill(self.button_colour, self.rect #draws rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect) #draws text
