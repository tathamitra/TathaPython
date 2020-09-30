mystr = "Tathagata is a good boy"

print(len(mystr))
#output:23
print(mystr[0:10])
#output:Tathagata
print(mystr[0:999])
#output:Tathagata is a good boy

print(mystr[0:23:1])
#output:Tathagata is a good boy

print(mystr[0:23:2])
#output:Ttaaai  odby

print(mystr[0::3])
#output:Tha  gdo

print(mystr[-4:])
#output:boy

print(mystr[::-1])
#output: yob doog a si atagahtaT (string reversed)


print(mystr.endswith("boy"))
print(mystr.count("ta"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.upper())
print(mystr.replace("is","are"))


