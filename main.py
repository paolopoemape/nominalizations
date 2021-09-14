import re


text_analyzed = 'information, from “to inform" investigation, from “to investigate” \
collision, from “to collide” agreement, from “to agree” \
refusal, from “to refuse” \
acceptance, from “to accept”\
conference, from “to confer” \
failure, from “to fail” \
actor: one who acts \
inventor: one who invents \
sculptor: one who sculpts \
governor: one who governs \
translator: one who translates\
Hiking can be arduous.\
Writing is not for sissies.\
Loitering is not permitted.'

#ing
ing = re.findall(r"\w+ing\b", text_analyzed, flags=re.I)
print(ing)

#tion or sion
ion = re.findall(r"\w+[st]ion\b", text_analyzed, flags=re.I)
print(ion)

#or
find_or = re.findall(r"\w+or\b", text_analyzed, flags=re.I)
print(find_or)