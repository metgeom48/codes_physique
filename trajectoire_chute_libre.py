########################################################
# Bibliothèques
########################################################
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

########################################################
# Résolution de la chute libre avec scipy
########################################################

# Initialiser le temps
instant_initial = 0
instant_final = 30
pas_temps = 0.01
temps = np.arange(instant_initial, instant_final, pas_temps)

# Champ de pesanteur
g = 9.81

# Vecteur position initial
x0 = 0
z0 = 0

# Vecteur vitesse initial
v0 = 10
alpha = 45 # Angle en degrés (Choisissez entre 0 et 180)
alpha = np.radians(alpha)

vx0 = v0 * np.cos(alpha)
vz0 = v0 * np.sin(alpha)

# Etat initial des composantes du vecteur position et du vecteur vitesse
etat_initial = [x0, vx0, z0, vz0]

# Function qui calcule la dérivée selon l'état actuel et l'instant t actuel
def chute_libre(etat,t):
    x,vx,z,vz=etat
    res=np.array([vx,0,vz,-g])
    return res

# Résolution équation différentielle
x, vx, z, vz = integrate.odeint(chute_libre, etat_initial, temps).T

# On ne garde les valeurs que pour les altitudes positives
indices_positifs = np.where(z > 0) 
x = x[indices_positifs]
vx = vx[indices_positifs]
z = z[indices_positifs]
vz = vz[indices_positifs]

########################################################
# Affichage avec matplotlib
########################################################

# Create the plot
plt.figure(figsize=(10, 6))

# Plot trajectory
plt.plot(x, z, label="Trajectoire", color="blue")

# Afficher certains vecteurs vitesse 
# Pas tous pour une meilleure lisibilité
facteur_echelle = 10
intervalle_afficher = 15
indices = np.arange(0, len(x), intervalle_afficher)
plt.quiver(
    x[indices], z[indices],  # Origine du vecteur
    vx[indices], vz[indices],  # Composantes du vecteur
    angles="xy", scale_units="xy", # Baser la taille du vecteur par rapport aux axes
    scale=facteur_echelle, color="red",
    label="Vecteurs vitesses successifs",
    headwidth=3, headlength=5
)

# Afficher un vecteur vitesse témoin
plt.quiver(
    [0], [0],  # Origine du vecteur
    [10], [0],  # Composantes du vecteur
    angles="xy", scale_units="xy", scale=facteur_echelle, color="green", label="Vecteur témoin (10 m/s)",
    headwidth=3, headlength=5
)

# Annoter les axes
plt.title("Trajectoire avec les vecteurs vitesse", fontsize=14)
plt.xlabel("x (m)", fontsize=12)
plt.ylabel("z (m)", fontsize=12)

# Mettre en valeur l'axe des abscisses et des ordonnées
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  # Axe des abscisses
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")  # Axe des ordonnées

# Afficher une grille
plt.grid(True, linestyle="--", alpha=0.6)

# Afficher la légende
plt.legend()

# Le repère est orthonormé
plt.axis("equal")  
plt.show()
