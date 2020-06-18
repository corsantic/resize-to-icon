from PIL import Image
import os


class imageSize:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height


print("Please copy for file in the directory and give its name")

image_file = input("enter your file name for resize: ")
image1 = Image.open(image_file)

sizes = []
sizes.append(imageSize('size48', 48, 48))
sizes.append(imageSize('size72', 72,  72))
sizes.append(imageSize('size96', 96,  96))
sizes.append(imageSize('size144', 144, 144))
sizes.append(imageSize('size192', 192, 192))
sizes.append(imageSize('size512', 512, 512))

folder_name = image_file.split(".")[0]
try:
    os.mkdir(folder_name)
except OSError:
    print("Creation of the directory %s failed" % folder_name)
else:
    print("Successfully created the directory %s " % folder_name)
for size in sizes:
    im5 = image1.resize((size.width, size.height), Image.ANTIALIAS)
    ext = ".png"
    file_name = f'{folder_name}/{size.name}{ext}'
    im5.save(file_name)
    print(file_name)

input("Press enter to continue")
