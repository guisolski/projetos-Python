import re

regex = r"^[aA-zZ][aA0-aZ9]?[@]{1}[aA-zZ]?[.]{1}[aA-zZ]{3}"
#r"[(][1-9]{2}[)]?[1-9]{4}-[1-9]{4}" #telefone
#regex = r"[0-9]{2}?[/]?[0-9]{2}?[/]?[0-9]{4}" #data
# cep [1-9]{5}[-][1-9]{3}
# email ^[aA-zZ]{1}[aA0-zZ9]*[@]{1}[aA-zZ]{1}[aA-zZ]*[.]{1}[aA-zZ]{3}


test_str = ("teste@gmail.com")
matches = re.finditer(regex,test_str,re.MULTILINE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum +1
    print("Match {matchNum} encontrado em {start} - {end}: {match}".format(matchNum = matchNum, start = match.start(),  end = match.end(),match = match.group()))
