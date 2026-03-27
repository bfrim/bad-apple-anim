import pygame
import os

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("ressources/MUSIC.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

window = pygame.display.set_mode((600, 400))

# frame_one = pygame.image.load('1frameman.png')
frames = os.listdir("video-frames/frames")
frames = sorted(frames)
curr_frame = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    window.fill((0, 0, 0))

    filename = frames[curr_frame]
    frame = pygame.image.load("video-frames/frames/" + filename)
    frame = pygame.transform.scale(frame, (600, 400)) # hopefully this keeps the image looking good, code did not work without this line.

    i = 2
    while i < 600:
        j = 2
        while j < 400:
            color = frame.get_at((i, j))
            r, g, b = color[:3]
            brightness = (r + g + b) / 3
            if brightness >= 50:
                pygame.draw.circle(window, (255, 255, 255), [i, j], 1)
            j += 4
        i += 4

    pygame.display.flip()

    # could change this to make it stop after the last frame
    curr_frame += 1
    if curr_frame >= len(frames):
        curr_frame = 0

    clock.tick(10)

# Quit Pygame
pygame.quit()
