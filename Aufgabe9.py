'''
Die beiden vorderen Reifen eines Autos sollten beide den gleichen Reifendruck haben.
 Ebenso sollten die beiden hinteren Reifen den gleichen Reifendruck haben, aber nicht
 unbedingt den gleichen wie die Vorderreifen. Schreiben Sie ein Programm, das den
 Reifendruck der vier Reifen einliest und dann eine Meldung ausgibt, ob der
 Reifendruck in Ordnung ist.

Reifendruck: rechter Vorderreifen: 38
Reifendruck: linker Vorderreifen: 38
Reifendruck: rechter Hinterreifen: 42
Reifendruck: linker Hinterreifen: 42

Reifendruck ist OK
'''

tire_front_left=input("linker Vorderreifen: ")
tire_front_right=input("rechter Vorderreifen: ")
tire_back_left=input("linker Hinterreifen: ")
tire_back_right=input("rechter Hinterreifen: ")

if tire_front_left == tire_front_right and tire_back_right==tire_back_left:
    print("Reifendruck ist OK")
else:
    print("Reifendruck nicht OK")


