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
translator: one who translates'

list_from_text = text_analyzed.split()

print(list_from_text)
#
# x = re.findall(r"\w*tion|\w*sion\b", text_analyzed)
# print(x)
#
# if not x:
#     print("No match found")
#
# else:
#     print("match found")

pattern = 'w*tion|w*sion|w*ment|w*ence|w*ance|w*or'
count = 0
for match in re.finditer(pattern, text_analyzed):
   count += 1

print(count)