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
translator: one who translates \
Hiking can be arduous.\
Writing is not for sissies.\
Loitering is not permitted.\
legatee: the person who is to receive a legacy payee: the person who has the right to be paid \
employee: one who is employed evacuee: one who is evacuated parolee: one who is paroled agreement, from “to agree” \
acceptance, from “to accept” \
conference, from “to confer” \
failure, from “to fail” '


#ing
ing = re.findall(r"\w+ing\b", text_analyzed, flags=re.I)
print(ing)

#tion or sion
ion = re.findall(r"\w+[st]ion\b", text_analyzed, flags=re.I)
print(ion)

#or
find_or = re.findall(r"\w+or\b", text_analyzed, flags=re.I)
print(find_or)

#ee
ee = re.findall(r"\w+ee\b", text_analyzed, flags=re.I)
print(ee)

#ment
ment = re.findall(r"\w+ment\b", text_analyzed, flags=re.I)
print(ment)

#ence or ance

ence_or_ance = re.findall(r"\w+b?nce\b", text_analyzed, flags=re.I)
print(ence_or_ance)

#list of all the lists

lst = ing + ion + find_or + ee + ment + ence_or_ance

print("Here is a list of occurrences in the whole text: ")
print(lst)