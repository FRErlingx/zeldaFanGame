import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, player_group):
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3
        self.add(player_group)

    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_z] or keys[pygame.K_w]:
            dy = -1
        elif keys[pygame.K_s]:
            dy = 1
        if keys[pygame.K_q] or keys[pygame.K_a]:
            dx = -1
        elif keys[pygame.K_d]:
            dx = 1

        self.rect.move_ip(dx, dy)

        # Ensure the player does not go off-screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

