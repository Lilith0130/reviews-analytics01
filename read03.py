data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len (data))

print(len(data))#有沒有沒差

print(data[0])#印出0.1筆留言以及分隔線
print('-------')
print(data[1])