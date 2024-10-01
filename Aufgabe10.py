'''
Es genügt nicht, dass der Reifendruck der beiden Vorder- und Hinterräder der gleiche ist.
 Beide Reifendrücke müssen sich innerhalb eines bestimmten Bereichs befinden.
 Erweitern Sie das Pogramm aus Aufgabe 9. Es soll überprüfen, ob sich der Druck
 aller Reifen zwischen 35 und 45 befindet. Befindet sich ein Reifen außerhalb
 dieses Bereichs, wird sofort eine Warnmeldung ausgegeben. Danach fährt das
 Programm mit dem Einlesen und Verarbeiten der Werte fort.

Reifendruck: rechter Vorderreifen: 32
Warnung: Der Reifendruck ist außerhalb des erlaubten Bereichs
  3 
Reifendruck: linker Vorderreifen: 32
Warnung: Der Reifendruck ist außerhalb des erlaubten Bereichs

Reifendruck: rechter Hinterreifen: 42
Reifendruck: linker Hinterreifen: 42

Der Reifendruck ist nicht in Ordnung!

Kommt es zu einer Warnmeldung, dann gibt das Programm am Ende eine letzte
 Warnmeldung aus. Deklarieren Sie dafür eine boolesche Variable boolean druckOK.
Initialisieren Sie sie mit True und setzen Sie den Wert auf False, wenn sich
ein Reifen außerhalb des gültigen Bereichs befindet.
'''


pressure_OK=True

def check_tire_pressure(pressure):
    global pressure_OK
    if pressure<35 or pressure>45:
        print("Warnung: Der Reifendruck ist außerhalb des erlaubten Bereichs")
        pressure_OK=False

def read_tire_pressure(prompt):     # die Funktion bekommt ein Variable prompt übergeben
    pressure = int(input(prompt))   # das prompt wird ausgegeben und ein Input vom Typ int erwartet
    check_tire_pressure(pressure)   # für diesen wird check_tire_pressure_ aufgerufen
    return pressure                 # der eingegebene pressure wird an den "Aufrufer" als Antwort zurückgegeben


tire_front_left=read_tire_pressure("linker Vorderreifen: ")
tire_front_right=read_tire_pressure("rechter Vorderreifen: ")
tire_back_left=read_tire_pressure("linker Hinterreifen: ")
tire_back_right=read_tire_pressure("rechter Hinterreifen: ")

if tire_front_left == tire_front_right and tire_back_right==tire_back_left:
    print("Reifendruck ist OK")
else:
    print("Reifendruck nicht OK")

if not pressure_OK:
    print("Da stimmt was nicht")