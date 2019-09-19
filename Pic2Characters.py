from PIL import Image
import os

input_file_name = ""
# the program continuously read image to transfrom it to characters until read an exit
while input_file_name != "exit":
    input_file_name = input("Please input file name of the picture(input exit to exit):\n")
    try:
        im = Image.open(input_file_name)
        print(im.format, im.size, im.mode)

        im.show()

        wished_height = 0
        wished_width = 0
        # read output height of characters
        while wished_height == 0:
            try:
                wished_height = int(input("Please input height (recommend value: 60 - 80):\n"))
                while wished_height < 1:
                    wished_height = int(input("Please input height (recommend value: 60 - 80):\n"))
            except:
                print("invalid value")

        # read output width of characters
        while wished_width == 0:
            try:
                wished_width = int(input("Please input width (recommend value: " + str(
                    int(wished_height * im.size[0] / im.size[1] * 2)) + "):\n"))
                while wished_width < 1:
                    wished_width = int(input("Please input width (recommend value: " + str(
                        int(wished_height * im.siz[0] / im.size[1] * 2)) + ":\n"))
            except:
                print("invalid value")

        # transform the image to the size so each pixel corresponding to one character
        new_im = im.resize((wished_width, wished_height)).convert('L')
        width = new_im.size[0]
        height = new_im.size[1]

        # get the name for the output file
        output_file_name = ""
        while output_file_name == "":
            output_file_name = input("Please input file name for output(txt):\n")
            try:
                out_file = open(output_file_name, 'w')
            except:
                output_file_name = ""
                print("invalid file name")

        # read the corresponding darkness for each character
        dat_file = open("all_list.dat", 'r')
        all_list = []
        for i in range(256):
            all_list.append(int(dat_file.readline()))
        dat_file.close()

        # do the transform
        for h in range(height):
            s = ""
            for w in range(width):
                s += chr(all_list[255 - new_im.getpixel((w, h))])
            out_file.write(s + "\n")
        out_file.close()
        print(
            "the picture has been outputed into " + output_file_name + ", please set the font as Courier New to view the picture")
        os.system(output_file_name)
    except:
        if input_file_name != "exit":
            print("File does not exist")
