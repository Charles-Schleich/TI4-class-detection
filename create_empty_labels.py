import os

# /data/images/img1.jpg -> /data/labels/img1.txt
# /data/images/img2.jpg -> /data/labels/img2.txt

# os.makedirs("./data/labels")
for filename in os.listdir("./data/images"):
    split = filename.split(".")
    split[1] = "txt" 
    label_file = ".".join(split)
    label_path = "./data/labels/" + label_file
    open(label_path, 'a').close()
