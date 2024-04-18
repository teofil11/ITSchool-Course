def convertor_masura():
    masura = float(input("Introduceti masura: "))
    unitati = {
"mm": {"cm": 0.1, "dm": 0.01, "m": 0.001, "dam": 0.0001, "hm": 0.00001, "km": 0.000001},
"cm": {"mm": 10, "dm": 0.1, "m": 0.01, "dam": 0.001, "hm": 0.0001, "km": 0.00001},
"dm": {"mm": 100, "cm": 10, "m": 0.1, "dam": 0.01, "hm": 0.001, "km": 0.0001},
"m": {"mm": 1000, "cm": 100, "dm": 10, "dam": 0.1, "hm": 0.01, "km": 0.001},
"dam": {"mm": 10000, "cm": 1000, "dm": 100, "m": 10, "hm": 0.1, "km": 0.01},
"hm": {"mm": 100000, "cm": 10000, "dm": 1000, "m": 100, "dam": 10, "km": 0.1},
"km": {"mm": 1000000, "cm": 100000, "dm": 10000, "m": 1000, "dam": 100, "hm": 10}
}
    unitate = input("Introduceti unitatea de masura(mm, cm, dm, m, dam, hm, km): ")
    for u in unitati[unitate]:
        print(f"{masura * unitati[unitate][u]} {u}")

convertor_masura()



