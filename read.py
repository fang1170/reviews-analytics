data = []    #建立空清單
count = 0
with open('reviews.txt', 'r') as f: #打開txt檔
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:       # % 求餘數
			print(len(data))
print('總共有', len(data), '筆資料')
print(data[2])

sum_d = 0
for d in data:
	sum_d = len(d) + sum_d 
print('每筆留言的平均長度:', sum_d / len(data))	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new),  '筆長度<100的留言')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])

bad = [d for d in data if 'bad' in d]   #快寫法 把有bad的留言裝進清單中
print(bad)




#文字計數
wc = {} #word_count
for d in data:
	words = d.split()    #括號內預設為空白鍵
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1
for word in wc:			
	if wc[word] > 1000000:
		print(word, wc[word])	
print(len(wc))
print(wc['Jonny'])	
while True:
	word = input('請問想查詢什麼字: ')
	if word == 'q':
		print('感謝使用!')
		break
	if word in wc:
		print(word, '總共出現', wc[word], '次')
	else:
		print(word, '沒有出現過喔!')
					




