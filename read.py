data = []    #建立空清單
count = 0
with open('reviews.txt', 'r') as f: #打開txt檔
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:       # % 求餘數
			print(len(data))        
print(len(data))
print(data[0].strip()) 
print('------------')
print(data[1])