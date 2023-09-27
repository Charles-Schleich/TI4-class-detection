import os
# for (dir_path, dirnames, filenames) in os.walk("./data/images"):
#     print(filenames)

for filename in os.listdir("./data/images"):
    x = filename.split(".")
    x=x[0]
    # x = ".".join(x)
    print(x)
    