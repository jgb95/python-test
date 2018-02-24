string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \nbmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \nsqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

translated = ""

for char in string:
	if char >= 'a' and char <= 'z':
		translated += chr( (ord(char) + 2 - ord('a') ) % 26 + ord('a') )
	else:
		translated += char

print translated