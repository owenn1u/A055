data = []
count = 0
length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆資料小於100字')
print(new[0])

big = []
for d in data:
	if 'big' in d:
		big.append(d)
print('共有', len(big), '筆資料提到 big')