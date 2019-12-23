with open(path) as f:
    line = f.readline()
    while line:
        print(line)
        line= f.readline()

def deal_txt(path):
    file_object= open(path)
    file_content =file_object.read()
    file_split = file_content.splitlines()
    print(file_split[0])




