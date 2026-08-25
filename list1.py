list_1 = []
print(list_1)
print(type(list_1))


list_2 = [1,5.7,True,"pythonlife",[1,2,3],(1,2,3),{3,4,5},25,25,25,25]
print(list_2)
print(type(list_2))


list_3 = list()
print(list_3)
print(type(list_3))


my_list = [10, 20, 30, 40, 50]
print(len(my_list))


my_list = [10, 20, 30, 40, 50]
#syntax
#seq[indexvalue]
print(my_list[2])#30
print(my_list[-3])#30
print(my_list[4])#50
print(my_list[-1])#50
print(my_list[0])#10
print(my_list[-5])#10


my_list = [10, 20, 30, 40, 50, 60, 70, 80]
#seq[s:s:s]
print(my_list[0:8:1])
print(my_list[::])


my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[2:5])
print(my_list[:3])
print(my_list[5:8])
print(my_list[3:6])



my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[-4:-1])
print(my_list[-8:-5])
print(my_list[-4:-2])
print(my_list[-2:])



my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(my_list[7:4:-1])
print(my_list[-1:-4:-1])
print(my_list[2::-1])
print(my_list[-6::-1])
print(my_list[4:2:-1])
print(my_list[-4:-6:-1])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 # print(len(matrix))
print(matrix[1][2])
print(matrix[0][2])
print(matrix[2][0])