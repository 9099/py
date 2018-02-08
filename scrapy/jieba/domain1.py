from Utils import fidder
import linecache
import random

line=linecache.getline('list.csv',random.randrange(1,4034))
line=line.strip().split(',')
sufix=['.com','.cn','.com.cn','.net','.org','.cc']
prefix=['i','51','52']
for ii in range(50):

	dom=random.choice(line)+random.choice(line)

	for i in sufix:

		# res=fidder.domain_ename(domin)
		# if res is True:
		# print(domin)
		with open('res.csv','a+') as f:
			domin = dom + i
			res = fidder.domain_ename(domin)
			if res is True:
				f.writelines(domin+',')
				if str(domin).endswith('com') or str(domin).endswith('cn'):
					print(domin)

			for iii in prefix:
				ss=(iii+domin)
				res1 = fidder.domain_ename(ss)
				if res1 is True:
					f.writelines(ss + ',')
					# print(ss)
					if str(ss).endswith('com') or str(ss).endswith('cn'):
						print(ss)
	#
	with open('res.csv', 'a+') as f1:
		f1.writelines('\n')