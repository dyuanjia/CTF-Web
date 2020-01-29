import md5
a=raw_input().strip()
for i in range(111111111):
	if md5.md5('kaibro'+str(i)).hexdigest()[0:5]==a:
		print i;
		break
		
