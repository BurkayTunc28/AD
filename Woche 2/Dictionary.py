#klassen dürfen nicht änderbar sein
hauptstaedte = {"Albanien": "Tirana",
            "Belgien": "Brüsseln",
            "Deutschland": "Berlin",
            "Schweiz": "Zürich"}


#Mit dem Schlüsselwert wird der tatsächliche Wert geholt
print(hauptstaedte.get("Albanien"))

if hauptstaedte.get("Schweiz"):
    print("Existiert")

else:
    print("Existiert nicht")

#Mit Update kann etwas hinzugefügt oder etwas existierendes geändert werden

hauptstaedte.update({"Irland": "Dublin"})
hauptstaedte.update({"Schweiz": "Bern"})

print(hauptstaedte)


#mit pop kann man ein ausgewähltes Key Item löschen

hauptstaedte.pop("Belgien")


print(hauptstaedte)

#mit popitem löscht man das zuletzt eingefügte ELement
hauptstaedte.popitem()

print(hauptstaedte)

#mit clear löscht man das komplette dictionary

#hauptstaedte.clear()

print(hauptstaedte)

#Key gibt die Keys zurück
keys = hauptstaedte.keys()

print(keys)

for key in hauptstaedte.keys():
    print(key)

#value gibt den Wert zurück
values = hauptstaedte.values()
print(values)

for value in hauptstaedte.values():
    print(value)

#items gibt es ähnlich wie ein 2d Array zurück
items = hauptstaedte.items()
print(items)

for key1, value2 in hauptstaedte.items():
    print(f"{key1}: {value2}")





