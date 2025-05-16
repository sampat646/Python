#slicing = create a substring by extracting elements from another string.
# indexing[] or slice()
# [start:stop:step]

name = "Sampat karehonna"

#some default knowing indexes.
first_name = name[:4]#samp
last_name = name[4:]#at karehonna

#(It exclude the first index).
slicing = name[1:6]#ampat
print(first_name)
print(last_name)

#step
funcky_name = name[:5:2]
print(funcky_name)#S m a

funcky_name2 = name[:6:3]
print(funcky_name2)#S  p

steping_eg = name[::2]
print(steping_eg)#S m a   a e o n

reverse_str = name[::-1]
print(reverse_str)#annoherak tapmaS

#slice()

website1 = "https//google.com"
website2 = "https//wikipedia.com"
slice = slice(7,-4)
print(website1[slice])#google
print(website2[slice])#wikipedia





