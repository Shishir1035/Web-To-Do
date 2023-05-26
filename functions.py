def write(path,str,mode):
    with open(path,mode) as file:
        file.writelines(str)

def read(path):
    with open(path,'r') as file:
        return file.readlines()  