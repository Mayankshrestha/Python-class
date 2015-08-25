text_file = open('pg11.txt', 'r')
my_words = {'the' : 0, 'Alice': 0}
for line in text_file:
	line = line.strip('\n')
	words = line.split()
	for word in words:
		word = word.replace('.','').replace(',','').replace("'","").replace('!','').replace('(','').replace(')','').replace('#','').replace('/','')
		word = word.replace('?','').replace(';','').replace('-','').replace(':','').replace('[','').replace(']','').replace('*','')
		if word == 'the':
		    my_words['the'] = my_words['the'] +1
		if word == 'Alice':
		    my_words['Alice'] = my_words['Alice'] +1
print my_words		
text_file.close()



		

