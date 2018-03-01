def printDivs():
	nums = [x for x in range(1,26)]
	for n in nums:
		div = '''<div class="grid-item--{0}" id="{0}"></div>'''.format(n)
		print(div)


printDivs()