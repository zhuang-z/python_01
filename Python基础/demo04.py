#文件的读写
text = input("请输入今天的心情：")
with open("日记.txt","w",encoding="utf8") as f:    # "w"是写入   "a"是追加 
#with open("日记.txt","a",encoding="utf8") as f: 
    f.write(text)