from PIL import Image,ImageFilter
from os import getcwd
from os.path import exists




def print_quit(s ):
    print(s)
    quit()


current_dir = getcwd()

if not exists(current_dir+"\config.txt"):
    print_quit("config file does not exist please create one")

x=-1
y=-1
end_x=-1
end_y=-1
focus=False
img_path = ""
blur_power = 5


with open(current_dir+"\config.txt") as file :
    for config in file.readlines():
        low = config.lower()
        if low.startswith("image"):
            img_path = config.split(":")[1]

        if low.startswith("x"):
            x= int(config.split(":")[1])

        if low.startswith("end x"):
            end_x= int(config.split(":")[1])

        if low.startswith("end y"):
            end_y= int(config.split(":")[1])

        if low.startswith("y"):
            y= int(config.split(":")[1])

        if low.startswith("focus"):
            focus= bool(config.split(":")[1])

        if low.startswith("blur"):
            blur_power= int(config.split(":")[1])

print(img_path)


if len(img_path)<2 :
    print_quit("please input a valid image file name")

if focus and (x==-1 or y==-1 or end_y==-1 or end_x == -1) :
    print_quit("you need to add the x and y values for the focus")

img = Image.open(current_dir+"\\"+img_path.strip())

if focus and x!=-1 and y!=-1 and end_x!=-1 and end_y!=-1 :
    crop = img.crop((x,y,end_x,end_y))
    blured= img.filter(ImageFilter.BoxBlur(blur_power))
    blured.paste(crop,(x,y,end_x,end_y))
    img=blured

img.show()
img.save("ps.png")

            




