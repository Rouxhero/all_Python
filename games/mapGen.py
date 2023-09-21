import pygame
from pygame.locals import *
import noise
import tkinter as tk
from tkinter import messagebox

# Dimensions de la fenêtre Pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Paramètres initiaux du bruit
SCALE = 50.0
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2.0

# Initialisation de Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bruit Perlin')

# Initialisation de Tkinter pour les paramètres du bruit
root = tk.Tk()
root.geometry('300x200')
root.title('Paramètres du bruit Perlin')

# Fonction pour mettre à jour les paramètres du bruit
def update_parameters():
    global SCALE, OCTAVES, PERSISTENCE, LACUNARITY
    SCALE = scale_var.get()
    OCTAVES = octaves_var.get()
    PERSISTENCE = persistence_var.get()
    LACUNARITY = lacunarity_var.get()

# Événement de fermeture de la fenêtre
def on_closing():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        root.destroy()
        pygame.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Création des contrôles Tkinter
scale_label = tk.Label(root, text='Scale')
scale_label.pack()
scale_var = tk.Scale(root, from_=0.1, to=100.0, resolution=0.1, orient=tk.HORIZONTAL)
scale_var.set(SCALE)
scale_var.pack()

octaves_label = tk.Label(root, text='Octaves')
octaves_label.pack()
octaves_var = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
octaves_var.set(OCTAVES)
octaves_var.pack()

persistence_label = tk.Label(root, text='Persistence')
persistence_label.pack()
persistence_var = tk.Scale(root, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
persistence_var.set(PERSISTENCE)
persistence_var.pack()

lacunarity_label = tk.Label(root, text='Lacunarity')
lacunarity_label.pack()
lacunarity_var = tk.Scale(root, from_=1.0, to=5.0, resolution=0.1, orient=tk.HORIZONTAL)
lacunarity_var.set(LACUNARITY)
lacunarity_var.pack()

update_button = tk.Button(root, text='Mettre à jour', command=update_parameters)
update_button.pack()

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements Pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Effacement de l'écran
    window.fill((0, 0, 0))

    # Génération du bruit Perlin
    for y in range(WINDOW_HEIGHT):
        for x in range(WINDOW_WIDTH):
            value = noise.pnoise2(x / SCALE,
                                 y / SCALE,
                                 octaves=OCTAVES,
                                 persistence=PERSISTENCE,
                                 lacunarity=LACUNARITY)
           
            # Mise à l'échelle de la valeur du bruit
            value = (value + 1) / 2

            # Conversion en niveau de gris
            grayscale = int(value * 255)

            # Affichage du pixel
            window.set_at((x, y), (grayscale, grayscale, grayscale))

    # Rafraîchissement de l'écran
    pygame.display.flip()
    clock.tick(30)

    # Mise à jour de Tkinter
    root.update()
pygame.quit()
root.destroy()