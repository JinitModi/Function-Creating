def swapFileData():
    data_a=input("Enter the file name  :")
    num=0
    file=open(data_a, 'r')
    with open(file, 'r') as a:
        data_a = a.read()
    print("number of words:")
    print(num)


swapFileData()