import re
with open('phpdump.txt','r') as q:
		lines1 = q.read().splitlines()
		


q.close()

with open('pythondump.txt','r') as q:
		lines2 = q.read().splitlines()
		

q.close()

intersection = set(lines1) | set(lines2)
listofkey=list(intersection)

with open('outforaction.txt','w') as q:
	for item in listofkey:
	          q.write("%s\n" % item)  


q.close()


fin = open("outforaction.txt")
fout = open("outforresult.txt", "w+")
delete_list = ['work','organizations','organization','agent','government agency','owl#Thing','organisation']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)


fin.close()
fout.close()

with open('outforresult.txt','r') as q:
		lines = q.read().splitlines()
		filtered = filter(lambda x: not re.match(r'^\s*$', x), lines)


q.close()

with open('outforresult.txt','w') as q:
	for item in filtered:
		q.write("%s\n" % item)	


q.close()


