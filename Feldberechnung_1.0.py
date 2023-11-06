import math
import matplotlib.pyplot as plt
import numpy as np

anton = 100.0
delta_anton = 0.0
bernd = 100.0
delta_bernd = 0
christian = 100.0
delta_christian = 0.0
dieter = 100.0
delta_dieter = 0.0
monat = 0

while anton > 1 or bernd > 1 or christian > 1 or dieter > 1:
    monat = monat + 1
    # verzicht der neuberechnung
    if monat < 24:
        if delta_anton < 0.01:
            print("Anton's veränderung:" + str(delta_anton))
            print("Anton's Hof = " + str(anton))
        elif delta_bernd < 0.01:
            print("Bernd's veränderung:" + str(delta_bernd))
            print("Bernd's Hof = " + str(bernd))
        elif delta_christian < 0.01:
            print("Christian's veränderung:" + str(delta_christian))
            print("Christian's Hof = " + str(christian))
        elif delta_dieter < 0.01:
            print("Dieter's veränderung:" + str(delta_dieter))
            print("Dieter's Hof = " + str(dieter))

    # felddiverenz
    delta_anton = anton
    delta_bernd = bernd
    delta_christian = christian
    delta_dieter = dieter

    # grafische darstellung der nächsten 4 jahre
    ypoints = np.array([anton])
    xpoints = np.array([monat])
    plt.scatter(xpoints, ypoints, color='red')
    ypoints_two = np.array([bernd])
    xpoints_two = np.array([monat])
    plt.scatter(xpoints_two, ypoints_two, color='blue')
    ypoints_three = np.array([christian])
    xpoints_three = np.array([monat])
    plt.scatter(xpoints_three, ypoints_three, color='green')
    ypoints_four = np.array([dieter])
    xpoints_four = np.array([monat])
    plt.scatter(xpoints_four, ypoints_four, color='orange')
    plt.xlim(0, 48)
    plt.ylim(70, 130)
    plt.xlabel("Monate")
    plt.ylabel("Hofgröße")
    plt.legend(['Anton', 'Bernd', 'Christian', 'Dieter'])

    # monatliche berechnung
    anton = anton + (bernd * (1.0 / 10.0)) + (christian * (1.0 / 12.0)) + (dieter * (1.0 / 14.0))
    bernd = bernd * (9.0 / 10.0)
    christian = christian * (11.0 / 12.0)
    dieter = dieter * (13.0 / 14.0)

    bernd = bernd + (anton * (1.0 / 10.0)) + (christian * (1.0 / 12.0)) + (dieter * (1.0 / 14.0))
    anton = anton * (9.0 / 10.0)
    christian = christian * (11.0 / 12.0)
    dieter = dieter * (13.0 / 14.0)

    christian = christian + (anton * (1.0 / 10.0)) + (bernd * (1.0 / 12.0)) + (dieter * (1.0 / 14.0))
    anton = anton * (9.0 / 10.0)
    bernd = bernd * (11.0 / 12.0)
    dieter = dieter * (13.0 / 14.0)

    dieter = dieter + (anton * (1.0 / 10.0)) + (bernd * (1.0 / 12.0)) + (christian * (1.0 / 14.0))
    anton = anton * (9.0 / 10.0)
    bernd = bernd * (11.0 / 12.0)
    christian = christian * (13.0 / 14.0)

    # berechnung der felddiverenz
    delta_anton = math.fabs(delta_anton - anton)
    delta_bernd = math.fabs(delta_bernd - bernd)
    delta_christian = math.fabs(delta_christian - christian)
    delta_dieter = math.fabs(delta_dieter - dieter)

    # ausschlussverfahren aus der svflg
    if anton < 1:
        print("anton ist raus")
        anton = 0
    elif bernd < 1:
        print("bernd ist raus")
        bernd = 0
    elif christian < 1:
        print("christian ist raus")
        christian = 0
    elif dieter < 1:
        print("dieter ist raus")
        dieter = 0

    if monat == 120:
        print("anton: " + str(anton))
        print("bernd: " + str(bernd))
        print("christian: " + str(christian))
        print("dieter: " + str(dieter))
        print("Es sind " + str(monat) + " Monate vergangen!")
        plt.show()
        break
