# from app import weather_fetch, city_name_separater
# from dataclasses import replace
# from traceback import print_tb
#import requests


# states = ["Tanger-Tétouan-Al Hoceïma", "L'Orienta", "Fès-Meknès", "Rabat-Salé-Kénitra", "Béni Mellal-Khénifra", "Casablanca-Settat", "Marrakech-Safi", "Drâa-Tafilalet", "Souss-Massa", "Guelmim-Oued Noun", "Laâyoune-Sakia El Hamra", "Dakhla-Oued Ed Dahab"]
# result = ""
# for i in states:
#     result += f'<option value="{i}">{i}</option>'
# print(result)

# cities = ["Tifariti", "smara", "Béni Mellal", "Aguelmous", "Khénifra", "Qasbat Tadla", "Boujad", "Dar Ould Zidouh", "Demnat", "Oulad Yaïch", "Oued Zem", "Ayt Mohamed", "Zawyat ech Cheïkh", "Ouaoula", "Mrirt", "Aziylal", "Kouribga", "Oulad Zemam", "Douar Oulad Aj-jabri", "Benslimane", "Bouznika", "Mediouna", "Sidi Bennour", "Casablanca", "Zawyat an Nwaçer", "Douar Ouled Ayad", "Beni Yakhlef", "Mohammedia", "El Jadid", "Azemmour", "Settat", "Barrechid", "Douar Olad. Salem", "Bouskoura", "Oulad Said", "Ad Darwa", "Oulad Hammou", "Sidi Smai'il", "Moulay Abdallah", "Bou Ahmed", "Aïn Harrouda", "Douar Oulad Hssine", "Tit Mellil", "Dakhla", "Skoura", "Arfoud", "Tineghir", "Zagora", "Errachidia", "Midalt", "Warzat", "Fès", "Taounate", "Meknès", "Sabaa Aiyoun", "Fritissa", "Missour", "Taza", "Tahla", "Douar 'Ayn Dfali", "Aïn Taoujdat", "Bourdoud", "Bni Frassen", "Sefrou", "Ain Aicha", "Azrou", "El Hajeb", "Oulad Tayeb", "Tan-Tan", "Guelmim", "Laâyoune", "El Kelaa des Srarhna", "Echemmaia Est", "Marrakech", "Setti Fatma", "Oulad Hassoune", "Safi", "Essaouira", "Youssoufia", "Sa'ada", "Ben Guerir", "Ait Ourir", "Loudaya", "Tameslouht", "Chichaoua", "Aït Faska", "Lamzoudia", "El Ghiate", "Guercif", "Beni Enzar", "Bou Arfa", "Jerada", "Oujda-Angad", "Zaïo", "Al Aaroui", "Taourirt", "El Aïoun", "Nador", "Zeghanghane", "Berkane", "Rabat", "Bahharet Oulad Ayyad", "Sale", "Moulay Bousselham", "Ain El Aouda", "Sidi Slimane", "Dar Bel Hamri", "Mehdya", "Bouknadel", "Sidi Mohamed Lahmar", "Sidi Yahya Zaer", "Arbaoua", "Safsaf", "Al Khmissat", "Mechraa Bel Ksiri", "Mograne", "Skhirate", "Sidi Yahia El Gharb", "Khenichet-sur Ouerrha", "Lalla Mimouna", "Kenitra", "Sidi Qacem", "Souk et Tnine Jorf el Mellah", "Tiflet", "Temara", "Ksebia", "Aourir", "Zawit Al Bour", "Wislane", "Inezgane", "Oulad Teïma", "Oulad Barhil", "Biougra", "Temsia", "Ait Ali", "Tiznit", "Sidi Bibi", "Bellaa", "Taroudannt", "Agadir", "Ait Melloul", "Lqoliaa", "Mnasra", "Imzouren", "Zoumi", "Al Hoceïma", "Ouezzane", "M'diq", "Asilah", "Martil", "Larache", "Tamorot", "Taza", "Tétouan", "Ksar El Kebir", "Fnidq", "Gueznaia", "Chefchaouene", "Laouamra", "Boureït", "Tangier"]
# unworking_cities = []
# for city in cities:
#     print(city)
#     if weather_fetch(city) == None:
#         unworking_cities.append(city)


# print(unworking_cities, len(unworking_cities))
# pip install translators --upgrade
import translators as ts
crop = ["rice", "maize", "chickpea", "kidneybeans", "pigeonpeas", "haricots papillon", "mungbean", "blackgram", "lentil", "pomegranate", "banana", "mango", "grapes", "watermelon", "muskmelon", "apple", "orange", "papaya", "coconut", "cotton", "jute", "coffee"]

for cr in crop:
    a = ts.google(cr, from_language='en', to_language='fr')
    print(f"'{cr}' : '{a}',")
