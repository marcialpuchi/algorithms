def checkBrackets(str):

	bracket_chk = []
	open_backet=['(','{','[','<']
	close_bracket=[')','}',']','>']
    
	for ch in str:
        
		if ch in open_backet:
			bracket_chk.append(ch)

		elif ch in close_bracket:

			chk_size = len
			last_bracket=bracket_chk[len(bracket_chk)-1]

			if last_bracket == open_backet[close_bracket.index(ch)]:
				#the last bracket open matches the closing bracket
				bracket_chk.pop()

			else:
				return 0

	if len(bracket_chk) > 0:
		return 0
	else:
		return 1

test = '(h[e{loo}!]~)()()()('

print checkBrackets(test)
