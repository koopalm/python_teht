# Kerätään käyttäjältä luvut
lukulista_str = input("Syötä haluamasi luvut pilkulla erotettuna:")
lukulista_ennen_int = (lukulista_str.split(","))
print(lukulista_ennen_int)
# Muutetaan luvut numeroiksi
lukulista = []
try:
    for luku in lukulista_ennen_int:
        lukulista.append(float(luku))
except:
    print("Lukusarjasi sisältää kirjaimia, käytä pelkkiä numeroita!")
# Tulostetaan min ja max
maksimi = max(lukulista)
minimi = min(lukulista)
print(f'Maximi {maksimi}\nMinimi {minimi}')