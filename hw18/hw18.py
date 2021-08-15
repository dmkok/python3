from PIL import Image
import os
#снижает размер ффайла за счет изменения параметра quality
def resize_quality(size, new_filename='target_quality.jpg'):
    def getSize(filename):
        st = os.stat(filename)
        return st.st_size
    with Image.open("dolina_ozero.jpg", 'r') as source:
        quality = 100
        source.save(new_filename, quality=quality, optimize=True, progressive=True)
        print("Исходный размер: ",getSize("dolina_ozero.jpg"), "Байт, размер:",source.size)
        while getSize(new_filename) > size: #поиск нужного размера файла по его качеству
            source.save(new_filename, quality=quality-1, optimize=True, progressive=True)
            quality -= 2
        print("Размер после изменения: ", getSize(new_filename), "Байт, размер:",source.size)
# метод thumbnail (эскиз), который устанавливает размер в пикселях
def resize_h_w(size, new_filename='target_size_h_w.jpg'):
    def getSize(filename):
        st = os.stat(filename)
        return st.st_size
    with Image.open("dolina_ozero.jpg", 'r') as source:
        source.save(new_filename, quality=100, optimize=True, progressive=True)
        print("Исходный размер: ", getSize("dolina_ozero.jpg"), "Байт, размер:", source.size)
        source.thumbnail(size)
        source.save(new_filename)
        print("Размер после изменения: ", getSize(new_filename), "Байт, размер:",source.size)
#считает долго, но изменяет на нужный размер в байтах и уменьшает размер картинки в пикселях
def resize(size, new_filename='target_size.jpg'):
    def getSize(filename):
        st = os.stat(filename)
        return st.st_size
    with Image.open("dolina_ozero.jpg", 'r') as source:
        quality = 100
        source.save(new_filename, quality=quality, optimize=True, progressive=True)
        w=source.size[0]
        h=source.size[1]
        print("Исходный размер: ",getSize("dolina_ozero.jpg"), "Байт, размер:",source.size)
        while getSize(new_filename) > size: #поиск нужного размера файла по его размеру в пикселях
            w -= 120
            h -= 120
            source = source.resize((w-2, h-2), Image.ANTIALIAS)
            source.save(new_filename, quality=quality, optimize=True, progressive=True)
            # print(source.size, getSize(new_filename))
        print("Размер после изменения: ", getSize(new_filename), "Байт, размер:",source.size)

import time
start_time = time.time()
#изменяет разрешение (указываем нужный размер картинки в пикселях)
resize_h_w((300,300))
print("resizing-size(h-w): %s seconds\n" % (time.time() - start_time))

#изменяет quality (указываем нужный размер файла в байтах) меньше 15 sec, thumbnail может сам подгонять соотношение сторон
start_time = time.time()
resize_quality(2500000)
print("resizing-quality: %s seconds\n" % (time.time() - start_time))

#считает около 20-30 сек из-за операции сохранения после изменения размера файла
#изменяет разрешение (указываем нужный размер файла в байтах)
# start_time = time.time()
# resize(2900000)
# print("resizing-size: %s seconds\n" % (time.time() - start_time))


