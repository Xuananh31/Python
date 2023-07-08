a = int(input("Nhập chiều cao : "))
for i in range(a):
    for j in range(0,19):
        if j==0 or j==6 or j==12 or j==14 or j==18 :
            print('.',end=" ")
        elif i==0 and j==4:
            print('.', end=" ")
        elif i==1 and j==7:
            print('.', end=" ")
        elif i==2 and j in (4,8):
            print('.', end=" ")
        elif i==3 and j in (4,9,15,16,17):
            print('.', end=" ")
        elif i==4 and j in(4,10):
            print('.', end=" ")
        elif i==5 and j in (4,11):
            print('.', end=" ")
        elif i==6 and j in (1,2):
            print('.', end=" ")
        elif i==6 and j==4:
            print('.', end=" ")
        else:
            print(" ", end=" ")
    print()





