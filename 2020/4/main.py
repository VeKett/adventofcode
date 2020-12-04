from string import hexdigits

# This code is really messy, I know.
validpassports = 0
validpassports2 = 0
valideyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
with open("input") as file:
	passports = [x.replace('\n', ' ') for x in file.read().split("\n\n")]
	for passport in passports:
		byrvalid = iyrvalid = eyrvalid = hgtvalid = hclvalid = eclvalid = pidvalid = False
		data = list(filter(None, passport.split(' ')))
		datad = {}
		for item in data:
			pair = item.split(':')
			datad[pair[0]] = pair[1]
		if (len(data) == 8) or (len(data) == 7 and 'cid' not in datad):
			byr = int(datad['byr'])
			byrvalid = byr >= 1920 and byr <= 2020
			iyr = int(datad['iyr'])
			iyrvalid = iyr >= 2010 and iyr <= 2020
			eyr = int(datad['eyr'])
			eyrvalid = eyr >= 2020 and eyr <= 2030
			hgt = datad['hgt']
			if hgt.endswith('in'):
				inthgt = int(hgt[:-2]) # would've done it further up but empty strings??
				hgtvalid = inthgt >= 59 and inthgt <= 76
			elif hgt.endswith('cm'):
				inthgt = int(hgt[:-2])
				hgtvalid = inthgt >= 150 and inthgt <= 193
			hcl = datad['hcl']
			if hcl.startswith('#') and len(hcl) == 7:
				hclvalid = len([x for x in hcl[1:] if x in hexdigits]) == 6
			eclvalid = datad['ecl'] in valideyecolors
			pid = datad['pid']
			pidvalid = len(pid) == 9 and pid.isdigit()
			validpassports += 1
			if byrvalid and iyrvalid and eyrvalid and hgtvalid and hclvalid and eclvalid and pidvalid:
				validpassports2 += 1

print(f"Part 1: {validpassports}")
print(f"Part 2: {validpassports2}")
