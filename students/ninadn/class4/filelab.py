'''Test'''

globlang = []
globlang2 = []
langlistmax = []
langcount = []
with open ('/Users/ninadnaik/Desktop/UWPython/github/IntroPython2016/Examples/Session01/students.txt', mode = 'r', encoding = 'utf-8') as a_file:
	#print (a_file.read())
	for line in a_file:
		lang = line.split(':')
		#globlang.append(lang[1])
		if len(lang) > 1:
			globlang.append(lang[1])
		#print (lang)
#print (globlang)

for i in globlang:
	sublist = i.split(',')
	for j in sublist:
		globlang2.append(j.strip())

for k in globlang2:
	if k in langlistmax:
		langcount[langlistmax.index(k)] = langcount[langlistmax.index(k)] + int(1)
	elif k != "":
		langlistmax.append(k)
		langcount.append(int(1))

#langsort = zip (langlistmax,langcount)
#langsort.sort()
#langlistmax_sorted = [langlistmax for langcount, langlistmax in langsort]
for a, b, in zip (langlistmax,langcount):
	print ('{:15}|{:>5}'.format(a, b))