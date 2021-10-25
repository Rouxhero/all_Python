# All utile function
import os
from math import floor


def clear():
    if os.name != "posix":
        os.system("cls")
    else:
        os.system("clear")


def maxPerLine(table):
    listeMax = list(range(len(table[0])))
    colum = []
    for line in range(len(table[0])):
        linee = []
        for x in table:
            linee.append(str(x[line]))
            listeMax[line] = max(listeMax[line], len(str(x[line])))
        colum.append(linee)
    return listeMax, colum


def table_to_str(tab):
    listeMax, colum = maxPerLine(tab)
    tableau = ["+"]
    for i in listeMax:
        tableau[0] += "=" * i + "+"
    # Head
    tableau.append("|")
    tableau.append("+")
    for i in range(len(colum)):
        tableau[1] += colum[i][0] + " " * (listeMax[i] - len(colum[i][0])) + "|"
        tableau[2] += "=" * listeMax[i] + "+"
    if len(tab) > 1:
        # Body first line
        for i in range(1, len(colum[0])):
            tableau.append(
                "|" + colum[0][i] + " " * (listeMax[0] - len(colum[0][i])) + "|"
            )
        for i in range(1, len(colum)):
            for ii in range(1, len(colum[i])):
                tableau[2 + ii] += (
                    colum[i][ii] + " " * (listeMax[i] - len(colum[i][ii])) + "|"
                )

        # end
        tableau.append("+")
        for i in listeMax:
            tableau[len(tableau) - 1] += "-" * i + "+"
    return tableau


def afficheTableau(tableau):
    tab = table_to_str(tableau)
    if tab != None:
        for i in tab:
            print(i)


def Convert(chiffre):
    if abs(chiffre) < 1e3:
        return str(chiffre)
    elif abs(chiffre) < 1e6:
        return str(floor(chiffre / 1e3)) + "K"
    elif abs(chiffre) < 1e9:
        return str(floor(chiffre / 1e6)) + "M"
    elif abs(chiffre) < 1e12:
        return str(floor(chiffre / 1e9)) + "G"
    elif abs(chiffre) < 1e15:
        return str(floor(chiffre / 1e12)) + "B"
    elif abs(chiffre) < 1e18:
        return str(floor(chiffre / 1e15)) + "T"
    elif abs(chiffre) < 1e21:
        return str(floor(chiffre / 1e18)) + "aa"
    elif abs(chiffre) < 1e24:
        return str(floor(chiffre / 1e21)) + "ab"
    elif abs(chiffre) < 1e27:
        return str(floor(chiffre / 1e24)) + "ac"
    elif abs(chiffre) < 1e30:
        return str(floor(chiffre / 1e27)) + "ad"
    elif abs(chiffre) < 1e33:
        return str(floor(chiffre / 1e30)) + "ae"
    else:
        return str(chiffre)
