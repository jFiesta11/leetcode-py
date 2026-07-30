# if __name__ == '__main__':
#     array = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         array.append([name,score])
#         nameArr, scoreArr = zip(*array)
#         print(nameArr)


array = [["JAY",30 ],["justine",21],["Mickey",51],['Skimpbidih',31 ],["ratatouwi",22 ]] 

oldest = max(array, key=lambda x : x[1])

print(oldest[0])

