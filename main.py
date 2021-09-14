import re


text_analyzed = """The debate over how to address Little Cottonwood Canyon's traffic problem — a reality that during snowstorms or holidays can result in the 8-mile drive taking several hours — has been charged. Both Snowbird and Alta ski resorts have thrown their support behind the gondola, while Salt Lake County Mayor Jenny Wilson and groups like Wasatch Backcountry Alliance favor some kind of enhanced bus service.

However, Wilson says there are other options she wants to see explored first — like a "user-friendly" hub for public transportation at the bottom of the canyon, improved buses, tolling and a system that rewards carpooling.

"I don't like either choice, and frankly I think what we've done is chase the wrong thing for years," Wilson said during a press conference in September. "It's sort of like a Jenga game — if everything is stacked up perfectly, every assumption plays out, you're going to be fine. But you pull one piece out and the Jenga pieces fall to the ground."

Van Jura says it's too early to say if there is a favorite among the public comments.

"I will say there is a lot of support for the gondola. There is a lot of support for the bus. And there's also support for no action, which is always an alternative in the NEPA process."

NEPA refers to the National Environmental Policy Act, a law passed in 1970 that dictates how government agencies assess the environmental impacts of proposed projects.

Wilson and Salt Lake County Councilman Jim Bradley both said that while it's still hard to truly gauge public opinion, they think most side with the enhanced bus option.

"I think if you were to take a poll in Salt Lake County and say here are the two choices, and here's what they're going to cost, here's how they serve you, I think it would be significantly in favor of the bus," Bradley said. """


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