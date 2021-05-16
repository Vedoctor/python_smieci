# made by vedoctor on may 16th, 2021

# jak wywolujesz funkcje to jako argument string nazwa obrazka, koniecznie jpg
# obrazek musi byc idealnie kwadratowy
# czarny piksel to 1, bialy to 0

from PIL import Image  # biblioteka - najpierw musisz zrobic w terminalu pip install Pillow
# btw fajna biblioteka do processingu obrazow


def generate_map_array(img_name):

    im = Image.open(img_name).convert('RGB')  # wczytanie obrazka i konwersja na kolorki RGB

    size = im.size[0]  # sprawdzenie rozmiaru

    map_array = []  # init tablicy ktora bedzie zapisywac mape

    for row in range(size):  # for - dla kazdego rzedu pixeli na obrazku
        row_array = []  # wyzerowanie tablicy przechowujacej tymczasowo jeden rzad
        for pixel in range(size):  # for - dla kazdego pixela w rzedzie
            if im.getpixel((pixel, row)) < (127, 127, 127):  # jesli kolor pixela o adresie (pixel, row) jest
                # mniejszy niz 127, 127, 127 (czyli pixel jest ciemny)
                row_array.append(1)  # to zapisz do tymczasowej tablicy jeden
            else:  # jesli jest wiekszy niz 127 (czyli pixel jasny)
                row_array.append(0)  # zapisz zero
        map_array.append(row_array)  # zapisz tymczasowa tablice to tej glownej, koncowej

    return map_array


# ponizej tylko wypisywanie, mozesz pominac ofc
for row in generate_map_array('map.jpg'):
    print(row)

# mam nadzieje ze wszystko zrozumiale
# pozdrawiam
