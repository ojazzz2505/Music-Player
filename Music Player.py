import pygame
import os

# Initialize Pygame
pygame.init()

# Define the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Set up the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Music Player")

# Define the font for displaying text
font = pygame.font.Font(None, 30)

# Define the directory where the music files are stored
music_dir = "C:/Users/Ojast/Music"

# Get a list of all the music files in the directory
music_files = []
for root, dirs, files in os.walk(music_dir):
    for file in files:
        if file.endswith(".mp3"):
             music_files.append(os.path.join(root, file))

# Set the initial track index
track_index = 0

# Load the first track
pygame.mixer.music.load(music_files[track_index])

# Play the track
pygame.mixer.music.play()

# The main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Display the current track name
    current_track_name = os.path.basename(music_files[track_index])
    track_name_text = font.render(current_track_name, True, (0, 0, 0))
    screen.blit(track_name_text, (10, 10))

    # Display the track list
    track_list_text = font.render("Tracks:", True, (0, 0, 0))
    screen.blit(track_list_text, (10, 50))
    for i, music_file in enumerate(music_files):
        track_text = font.render(os.path.basename(music_file), True, (0, 0, 0))
        screen.blit(track_text, (10, 80 + i * 30))

    # Get user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        # Move up in the track list
        if track_index > 0:
            track_index -= 1
            pygame.mixer.music.load(music_files[track_index])
            pygame.mixer.music.play()
    elif keys[pygame.K_DOWN]:
        # Move down in the track list
        if track_index < len(music_files) - 1:
            track_index += 1
            pygame.mixer.music.load(music_files[track_index])
            pygame.mixer.music.play()

    # Update the display
    pygame.display.flip()
