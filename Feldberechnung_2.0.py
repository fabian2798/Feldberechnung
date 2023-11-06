import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import fractional_matrix_power

# berechnung der feldgrößen mit vektoren und matrizen

# monatliche berechnung

# spalten der matrix
start_Vektor = np.array([100.0, 100.0, 100.0, 100.0])  # Anton, Bernd, Christian, Dieter

# zeilen der matrix mit beschriftung
matrix_Anton = np.array([[1.0, 1.0 / 10.0, 1.0 / 12.0, 1.0 / 14.0],  # Anton
                         [0, (1 - 1 / 10.0), 0, 0],  # Bernd
                         [0, 0, (1 - 1 / 12.0), 0],  # Christan
                         [0, 0, 0, (1 - 1 / 14.0)]])  # Dieter

matrix_Bernd = np.array([[(1 - 1 / 10.0), 0, 0, 0],  # Anton
                         [1 / 10.0, 1, 1 / 12.0, 1 / 14.0],  # Bernd
                         [0, 0, (1 - 1 / 12.0), 0],  # Christan
                         [0, 0, 0, (1 - 1 / 14.0)]])  # Dieter

matrix_Christian = np.array([[(1 - 1 / 10.0), 0, 0, 0],  # Anton
                             [0, (1 - 1 / 12.0), 0, 0],  # Bernd
                             [1 / 10.0, 1 / 12.0, 1, 1 / 14.0],  # Christan
                             [0, 0, 0, (1 - 1 / 14.0)]])  # Dieter

matrix_Dieter = np.array([[(1 - 1 / 10.0), 0, 0, 0],  # Anton
                          [0, (1 - 1 / 12.0), 0, 0],  # Bernd
                          [0, 0, (1 - 1 / 14.0), 0],  # Christan
                          [1 / 10.0, 1 / 12.0, 1 / 14.0, 1]])  # Dieter

matrix_V = matrix_Dieter @ matrix_Christian @ matrix_Bernd @ matrix_Anton  # durchschnittsmatrix
matrix_M = np.dot(matrix_V, start_Vektor)  # berechnung nach dem ersten monat

for monat in range(1, 121):
    vektor_Monat = np.linalg.matrix_power(matrix_V, monat).dot(start_Vektor)
    # np.linalg.matrix_power = exponentszieren von matrizen
    # np.dot = multiplizieren
    ypoints = np.array([vektor_Monat[0]])
    xpoints = np.array([monat])
    plt.scatter(xpoints, ypoints, color='red')
    ypoints_two = np.array([vektor_Monat[1]])
    xpoints_two = np.array([monat])
    plt.scatter(xpoints_two, ypoints_two, color='blue')
    ypoints_three = np.array([vektor_Monat[2]])
    xpoints_three = np.array([monat])
    plt.scatter(xpoints_three, ypoints_three, color='green')
    ypoints_four = np.array([vektor_Monat[3]])
    xpoints_four = np.array([monat])
    plt.scatter(xpoints_four, ypoints_four, color='orange')
    plt.xlim(0, 48)
    plt.ylim(70, 130)
    plt.xlabel("Monate")
    plt.ylabel("Hofgröße")
    plt.legend(['Anton', 'Bernd', 'Christian', 'Dieter'])
    if monat == 120:
        print("Anton:" + str(vektor_Monat[0]))
        print("Bernd:" + str(vektor_Monat[1]))
        print("Christian:" + str(vektor_Monat[2]))
        print("Dieter:" + str(vektor_Monat[3]))
        plt.show()
