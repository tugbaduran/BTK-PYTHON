# try:
#   file= open("newfile2.txt","r")
#   print(file)
# except FileNotFoundError:
#   print("Dosya Okuma Hatası")
# finally:
#   print("Dosya Kapandı")
#   file.close()

file= open("newfile.txt","r",encoding="utf-8")

#for döngüsü

# for i in file:
#   print(i,end="")

# ********read() fonksiyonu

# content1 = file.read()
# print("içerik 1 ")
# print(content1)


# content2 = file.read()
# print("içerik 2")
# print(content2)

# content= file.read(5)
# content= file.read(3)
# content= file.read(3)
# print(content)



# ********readline() fonksiyonu

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="")


# ********readlines() fonksiyonu

liste= file.readlines()
print(liste)

print(liste[0])
print(liste[1])
print(liste[2])


file.close()