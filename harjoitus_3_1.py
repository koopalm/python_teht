
import requests
# Hae JSON-dataa osoitteesta https://api.github.com/search/repositories?q=language:python (voit ensin kurkata vaikka
# selaimella millaista dataa osoitteesta löytyy)
data = requests.get('https://api.github.com/search/repositories?q=language:python')
data_dict = data.json()
#Tulosta data rivi kerrallaan, seuraavassa muodossa:
# {forks}. {name}: {description}
for row in data_dict["items"]:
    print(f"{row['forks']}. {row['name']}: {row['description']}")
# ⭐Järjestä tuloksena saadut vastaukset ”forks” –arvon mukaan laskevassa järjestyksessä
forks_sort = []
for row in data_dict["items"]:
    forks_sort.append([row['forks'], row['name'], row['description']])
forks_sorted = sorted(forks_sort, key=lambda tup: tup[0])
for row in forks_sorted:
    print(f"{row[0]}. {row[1]}: {row[2]}")




