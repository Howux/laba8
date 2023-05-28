from PIL import Image, ImageDraw, ImageFont


def one():
    img = Image.open("uyt_vecher.jpg")
    img.show("uyt_vecher.jpg")

    crop = img.crop((60, 40, 360, 280))

    crop.save("cropped_img.png")
    crop.show("cropped_img.png")


def two():
    holiday = {
        "ДЕНЬ ПОБЕДЫ": "9maya.jpg",
        "НОВЫЙ ГОД": "ng.jpg",
        "8 МАРТА": "8marta.jpg",
        "23 ФЕВРАЛЯ": "23fev.jpg",
        "ДЕНЬ ОГУРЧИКА": "ogurec.jpg",
        "ДЕНЬ БАТОНА": "baton.jpg",
        "ДЕНЬ ПРИСОЕДИНЕНИЯ КРЫМА": "krim_nash.jpg",
        "ДЕНЬ ПИВА": "pivo.jpg"
    }

    anwser = input("К какому празднику нужна открытка: ").upper()
    if anwser in holiday:

        image_path = holiday[anwser]
        img = Image.open(image_path)
        img.show()
    else:
        print("Приздника нет в словаре")


def three():
    img = Image.open("dr.jpg")

    crop = img.crop((10, 20, 940, 1000))

    draw = ImageDraw.Draw(crop)

    name = input("Кого вы хотите поздравить: ")
    txt = f"{name}, поздравляю!"
    font = ImageFont.truetype("ariblk.ttf", 40)
    pos = (crop.width / 2 - 240, crop.height / 10)

    draw.text(pos, txt, fill=(255, 0, 0), font=font)

    crop.save("sdr.png")
    crop.show("sdr.png")
# one()
# two()
# three()