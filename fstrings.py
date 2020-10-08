
me = "tatha"
sur ="mitra"
sr = "hi this is %s" %me
sr1 = "hi this is %s %s" %(me,sur)
sam = "this  is {0} {1}"
print(sr)
print(sr1)
sr2=sam.format(me,sur)
print(sr2)

############fstring
sample = f"my name is {me}{sur}"
print(sample)
