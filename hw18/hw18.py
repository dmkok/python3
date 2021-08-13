from PIL import Image
import os
def resize_quality(size, new_filename='target_quality.jpg'):
    def getSize(filename):
        st = os.stat(filename)
        return st.st_size
    with Image.open("dolina_ozero.jpg", 'r') as source:
        quality = 100
        source.save(new_filename, quality=quality, optimize=True, progressive=True)
        print("Исходный размер: ",getSize("dolina_ozero.jpg"), "Байт, размер: ",source.size)
        while getSize(new_filename) > size: #поиск нужного размера файла по его качеству
            source.save(new_filename, quality=quality-1, optimize=True, progressive=True)
            quality -= 1
        print("Размер после изменения: ", getSize(new_filename), "Байт, размер: ",source.size)

#считает долго ~ минуту
def resize(size, new_filename='target_size.jpg'):
    def getSize(filename):
        st = os.stat(filename)
        return st.st_size
    with Image.open("dolina_ozero.jpg", 'r') as source:
        quality = 100
        source.save(new_filename, quality=quality, optimize=True, progressive=True)
        w=source.size[0]
        h=source.size[1]
        print("Исходный размер: ",getSize("dolina_ozero.jpg"), "Байт, размер: ",source.size)
        while getSize(new_filename) > size: #поиск нужного размера файла по его размеру в пикселях
            w -= 50
            h -= 50
            source = source.resize((w-1, h-1), Image.ANTIALIAS)
            source.save(new_filename, quality=quality, optimize=True, progressive=True)
            # print(source.size, getSize(new_filename))
        print("Размер после изменения: ", getSize(new_filename), "Байт, размер: ",source.size)

import time
start_time = time.time()
resize_quality(2500000)
print("reizing-quality: %s seconds" % (time.time() - start_time))
resize(2500000)
print("reizing-size: %s seconds" % (time.time() - start_time))

