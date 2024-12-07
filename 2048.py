import random

def commencer_partie():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    ajouter_nouvelle_tuile(mat)
    ajouter_nouvelle_tuile(mat)
    return mat

def ajouter_nouvelle_tuile(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        mat[i][j] = random.choice([2, 4])

def afficher_grille(mat):
    for row in mat:
        print("\t".join(str(num).rjust(4) for num in row))
    print()

def fusionner_ligne(ligne):
    nouvelle_ligne = [num for num in ligne if num != 0]
    for i in range(len(nouvelle_ligne) - 1):
        if nouvelle_ligne[i] == nouvelle_ligne[i + 1]:
            nouvelle_ligne[i] *= 2
            nouvelle_ligne[i + 1] = 0
    nouvelle_ligne = [num for num in nouvelle_ligne if num != 0]
    return nouvelle_ligne + [0] * (4 - len(nouvelle_ligne))

def deplacer_gauche(mat):
    nouvelle_mat = []
    for row in mat:
        nouvelle_mat.append(fusionner_ligne(row))
    return nouvelle_mat

def deplacer_droite(mat):
    return [fusionner_ligne(row[::-1])[::-1] for row in mat]

def deplacer_haut(mat):
    mat = list(zip(*mat))
    mat = deplacer_gauche(mat)
    return [list(row) for row in zip(*mat)]

def deplacer_bas(mat):
    mat = list(zip(*mat))
    mat = deplacer_droite(mat)
    return [list(row) for row in zip(*mat)]

def est_termine(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return False
            if j < 3 and mat[i][j] == mat[i][j + 1]:
                return False
            if i < 3 and mat[i][j] == mat[i + 1][j]:
                return False
    return True

def jouer():
    mat = commencer_partie()
    while True:
        afficher_grille(mat)
        if est_termine(mat):
            print("Game Over!")
            break
        mouvement = input("Déplacer (g= gauche, d= droite, h= haut, b= bas) : ").strip().lower()
        if mouvement == 'g':
            mat = deplacer_gauche(mat)
        elif mouvement == 'd':
            mat = deplacer_droite(mat)
        elif mouvement == 'h':
            mat = deplacer_haut(mat)
        elif mouvement == 'b':
            mat = deplacer_bas(mat)
        else:
            print("Entrée invalide. Réessayez.")
            continue
        ajouter_nouvelle_tuile(mat)

if __name__ == "__main__":
    jouer()
