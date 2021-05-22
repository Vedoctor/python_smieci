# made by vedoctor on may 16th, 2021

# jak wywolujesz funkcje to jako argument string nazwa obrazka, koniecznie jpg
# bialy pixel to 0, czarny to 1, czerwony to 2
# najlepiej kolorki: biały (255, 255, 255), czarny (0, 0, 0), czerwony (255, 0, 0)

from PIL import Image  # biblioteka - najpierw musisz zrobic w terminalu pip install Pillow
# btw fajna biblioteka do processingu obrazow


def generate_map_array(img_name):

    im = Image.open(img_name).convert('RGB')  # wczytanie obrazka i konwersja na kolorki RGB

    width, height = im.size  # sprawdzenie rozmiaru

    map_array = []  # init tablicy ktora bedzie zapisywac mape
    for row in range(height):  # for - dla kazdego rzedu pixeli na obrazku
        row_array = []  # wyzerowanie tablicy przechowujacej tymczasowo jeden rzad
        for pixel in range(width):  # for - dla kazdego pixela w rzedzie
            color = im.getpixel((pixel, row))  # kolor pixela o adresie (pixel, row)
            if color < (20, 20, 20):  # jesli kolor pixela jest mniejszy niz 20, 20, 20 (czyli pixel jest ciemny)
                row_array.append(1)  # to zapisz do tymczasowej tablicy jeden
            elif color[0] > 200 and color[1] < 20 and color[2] < 20:  # jesli kolor pixela R jest wiekszy niz 200 i
                # jednoczesnie G i B sa mniejsze od 20 (czyli bardzo czerwony)
                row_array.append(2)  # to zapisz do tymczasowej tablicy dwa
            else:  # w kazdym innym przypadku (czyli pixel jasny)
                row_array.append(0)  # zapisz zero
        map_array.append(row_array)  # zapisz tymczasowa tablice to tej glownej, koncowej

    return map_array  # zwroc gotowa tablice


# ponizej tylko wypisywanie, mozesz pominac ofc
for row in generate_map_array('map2.jpg'):
    print(row)

# mam nadzieje ze wszystko zrozumiale
# pozdrawiam
