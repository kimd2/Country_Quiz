"""
Component Game Play - Data
Diane Kim
5/08/21
"""
import random


# Data
nz = {
    'name': 'New Zealand',
    'capital city': ['Wellington'],
    'continent': ['Oceania'],
    'official language': ['Maori', 'English', 'NZ Sign Language'],
    'flag': ['Images\\01a.png', "New Zealand"],
    'national bird': ['Images\\01a.png', "Kiwi"],
    'national flower': ['Images\\01a.png', "New Zealand"],
    'national animal': ['Images\\01a.png', "New Zealand"],
    'population': '4.92m',
    'currency': 'NZD',
    'area': '268,021 km²'
}

rok = {
    'name': 'South Korea',
    'capital city': ['Seoul'],
    'continent': ['Asia'],
    'official language': ['Korean'],
    'flag': ['Images\\01a.png', "Korea"],
    'national bird': ['Images\\01a.png', "Korean Magpie"],
    'national flower': ['Images\\01a.png', "Korea"],
    'national animal': ['Images\\01a.png', "Korea"],
    'population': '51.7m',
    'currency': 'KRW',
    'area': '100,210 km²'
}

nld = {
    'name': 'Netherlands',
    'capital city': ['Amsterdam'],
    'continent': ['Europe'],
    'official language': ['Dutch'],
    'flag': ['Images\\01a.png', "Netherlands"],
    'national bird': ['Images\\01a.png', "Black Tailed-Godwit"],
    'national flower': ['Images\\01a.png', "Netherlands"],
    'national animal': ['Images\\01a.png', "Netherlands"],
    'population': '17.3m',
    'currency': 'Euro',
    'area': '41,542 km²'
}

fra = {
    'name': 'France',
    'capital city': ['Paris'],
    'continent': ['Europe'],
    'official language': ['French'],
    'flag': ['Images\\01a.png', "France"],
    'national bird': ['Images\\01a.png', "Gallic Rooster"],
    'national flower': ['Images\\01a.png', "France"],
    'national animal': ['Images\\01a.png', "France"],
    'population': '67.1m',
    'currency': 'Euro',
    'area': '643,801 km²'
}

jpn = {
    'name': 'Japan',
    'capital city': ['Tokyo'],
    'continent': ['Asia'],
    'official language': ['Japanese'],
    'flag': ['Images\\01a.png', "Japan"],
    'national bird': ['Images\\01a.png', "Green Pheasant"],
    'national flower': ['Images\\01a.png', "Japan"],
    'national animal': ['Images\\01a.png', "Japan"],
    'population': '126.3m',
    'currency': 'Yen',
    'area': '377,975 km²'
}

chn = {
    'name': 'China',
    'capital city': ['Beijing'],
    'continent': ['Asia'],
    'official language': ['Mandarin'],
    'flag': ['Images\\01a.png', "China"],
    'national bird': ['Images\\01a.png', "Red-Crowned Crane"],
    'national flower': ['Images\\01a.png', "China"],
    'national animal': ['Images\\01a.png', "China"],
    'population': '1.4b',
    'currency': 'Yuan',
    'area': '9.6m km²'
}

jam = {
    'name': 'Jamaica',
    'capital city': ['Kingston'],
    'continent': ['North America'],
    'official language': ['English'],
    'flag': ['Images\\01a.png', "Jamaica"],
    'national bird': ['Images\\01a.png', "Jamaica"],
    'national flower': ['Images\\01a.png', "Jamaica"],
    'national animal': ['Images\\01a.png', "Jamaica"],
    'population': '2.9m',
    'currency': 'JMD',
    'area': '10,991 km²'
}

ind = {
    'name': 'India',
    'capital city': ['New Delhi'],
    'continent': ['Asia'],
    'official language': ['Hindi', 'English'],
    'flag': ['Images\\01a.png', "India"],
    'national bird': ['Images\\01a.png', "India"],
    'national flower': ['Images\\01a.png', "India"],
    'national animal': ['Images\\01a.png', "India"],
    'population': '1.4b',
    'currency': 'Rupee',
    'area': '3.3m km²'
}

col = {
    'name': 'Colombia',
    'capital city': ['Bogota'],
    'continent': ['South America'],
    'official language': ['Spanish'],
    'flag': ['Images\\01a.png', "Colombia"],
    'national bird': ['Images\\01a.png', "Colombia"],
    'national flower': ['Images\\01a.png', "Colombia"],
    'national animal': ['Images\\01a.png', "Colombia"],
    'population': '50.3m',
    'currency': 'Peso',
    'area': '1.1m km²'
}

fij = {
    'name': 'Fiji',
    'capital city': ['Suva'],
    'continent': ['Oceania'],
    'official language': ['Fijian', 'Fiji Hindi', 'English'],
    'flag': ['Images\\01a.png', "Fiji"],
    'national bird': ['Images\\01a.png', "Fiji"],
    'national flower': ['Images\\01a.png', "Fiji"],
    'national animal': ['Images\\01a.png', "Fiji"],
    'population': '889,953',
    'currency': 'FJD',
    'area': '18,333 km²'
}

type = {
    'capital city': 'short answer',
    'continent': 'short answer',
    'official language': 'short answer',
    'flag': 'image multichoice',
    'national bird': 'image multichoice',
    'national flower': 'image multichoice',
    'national animal': 'image multichoice',
    'population': 'multichoice',
    'currency': 'multichoice',
    'area': 'multichoice'
}

rand = {
    'name': "Random"
}

dictionaries = [rand, nz, rok, nld, fra, jam, jpn, col, chn, ind, fij]

# Modes available
modes = ('Random', 'New Zealand', 'South Korea', 'Netherlands', 'France', 'Japan', 'China', 'Jamaica', 'India', 'Colombia', 'Fiji')


def give_dictionary(selected):
    for item in dictionaries:
        if item['name'] == selected:
            return item


def random_country(selected, key):
    global country_1, country_2, country_3, options
    options = [selected]
    valid = False
    while not valid:
        country_1 = dictionaries[random.randint(1, 10)]
        if country_1[key] != selected:
            valid = True
            options.append(country_1[key])
    valid = False
    while not valid:
        country_2 = dictionaries[random.randint(1, 10)]
        if country_2[key] not in options:
            valid = True
            options.append(country_2[key])
    valid = False
    while not valid:
        country_3 = dictionaries[random.randint(1, 10)]
        if country_3[key] not in options:
            valid = True
    return [country_2[key], country_1[key], country_3[key], selected]
