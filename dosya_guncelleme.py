# with open("newfile.txt", "r+", encoding="utf-8") as file:
#   file.seek(20)
#   file.write("deneme")

# with open("newfile.txt" , "r+", encoding="utf-8") as file:
#   print(file.read())

# **************** Sayfa Sonunda Güncelleme ***********************

# with open("newfile.txt", "a", encoding="utf-8") as file:
#   file.write("\nBuse Kılıç")


# **************** Sayfa Başında Güncelleme ***********************

# with open("newfile.txt" , "r+", encoding="utf-8") as file:
#   content= file.read()
#   content= "Sude Kılıç\n" + content
#   file.seek(0)
#   file.write(content)


# **************** Sayfa Ortasında Güncelleme ***********************

with open("newfile.txt" , "r+", encoding="utf-8") as file:
  list= file.readlines()
  list.insert(1,"Taha Kılıç\n")
  file.seek(0)
  file.writelines(list)


  # for i in list:
  #   file.write(i)

with open("newfile.txt" , "r", encoding="utf-8") as file:
  print(file.read())

