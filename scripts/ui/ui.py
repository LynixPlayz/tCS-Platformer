import pygame
from pathlib import Path
from collections import defaultdict


class UI:
    def __init__(self, player):
        self.keys: dict[pygame.Surface, str] = self.load_keys(size=(25, 25))
        self.x = 25
        self.y = 25
        self.player = player

    @staticmethod
    def load_keys(size: tuple) -> dict[pygame.Surface, str]:
        # Create container for keys
        move_keys: dict[pygame.Surface, str] = dict()
        # Start at content root for this key type
        root_movekeys_dir = sorted(Path(f"assets/keys").iterdir())

        for key_type_dir in root_movekeys_dir:
            for key_value in key_type_dir.iterdir():
                # Load the key
                img: pygame.Surface = pygame.image.load(key_value).convert_alpha()
                # Scale it
                img = pygame.transform.scale(img, size)
                # Add it to big key dictionary
                # How do I do this better than this
                # Manually create a dictionary with surface image and desc instead?
                key = key_value.name.rpartition(".")[0].upper()
                if key == "A":
                    move_keys[img] = "Move Left"
                elif key == "D":
                    move_keys[img] = "Move Right"
                elif key == "W":
                    move_keys[img] = "Jump"
                elif key == "J":
                    move_keys[img] = "Shoot"
                else:
                    move_keys[img] = "Desc of key"

        return move_keys

    def draw(self, screen):
        # No way in hell this is the best way to do it
        # But it works so fuck you
        i = 1
        for image, desc in self.keys.items():
            screen.blit(image, (self.x, i*self.y))
            font = pygame.font.Font("assets/dogicapixelbold.ttf", 12)
            text = font.render(desc, True, (255, 255, 255))
            screen.blit(text, dest=(
                self.x + 50,
                i*self.y + text.get_height() / 2))
            i += 1
