from PIL import Image
import os


def rea(pdf_name):
    file_list = os.listdir('.')
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)

    pic_name.sort()
    new_pic = []

    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)

    for x in pic_name:
        if "png" in x:
            new_pic.append(x)

    print("hec", new_pic)

    im1 = Image.open(new_pic[0])
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(i)
        im_list.append(Image.open(i))
        print(img)
        #if img.mode == "RGBA":
        #    img = img.convert('RGB')
        #    im_list.append(img)
        #else:
        #    im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)

if __name__ == '__main__':
    pdf_name = 'book.pdf'
    if ".pdf" in pdf_name:
        rea(pdf_name=pdf_name)
    else:
        rea(pdf_name="{}.pdf".format(pdf_name))