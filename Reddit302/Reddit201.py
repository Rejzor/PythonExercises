symbols = open('symbols.txt','r').read().split(' ')
elements = open('elements.txt','r').read().split(' ')

symbols = [x.lower() for x in symbols]
# print(symbols)
dictonary = dict(zip(symbols,elements))


test = "poison"
final=[]
cursor1 = 0
cursor2 = 2
loop=1
for i in range(len(test)):
	if test[cursor1:cursor2] in symbols:
			final.append(test[cursor1:cursor2])
			cursor1 = cursor1 + 2
			cursor2 = cursor2 + 2
	elif test[cursor1:cursor2-1] in symbols:
			final.append(test[cursor1:cursor2-1])
			cursor1 = cursor1 + 1
			cursor2 = cursor2 + 1
for key in final:
	print(dictonary[key])