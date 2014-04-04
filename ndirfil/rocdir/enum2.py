from numpy import *
import re
from sklearn import svm
#Enumerator for vectorising data


diclist = []
numlist = []
titlefile = open("parselog2","r")
for line in titlefile:
	if line in diclist:
		numlist.append(diclist.index(line))
	else:
		diclist.append(line)
		numlist.append(len(diclist)-1)
# for item in numlist:
# 	print item


ldiclist = []
lnumlist = []
localefile = open("localelog2","r")
for line in localefile:
	if line in ldiclist:
		lnumlist.append(ldiclist.index(line))
	else:
		ldiclist.append(line)
		lnumlist.append(len(ldiclist)-1)

prds_diclist = []
prds_numlist = []
prdsfile = open("prdslog2","r")
for line in prdsfile:
	if line in prds_diclist:
		prds_numlist.append(prds_diclist.index(line))
	else:
		prds_diclist.append(line)
		prds_numlist.append(len(prds_diclist)-1)


stldiclist = []
stlnumlist = []
stltitlefile = open("stlog2","r")
for line in stltitlefile:
	if line in stldiclist:
		stlnumlist.append(stldiclist.index(line))
	else:
		stldiclist.append(line)
		stlnumlist.append(len(stldiclist)-1)

ddiclist = []
dnumlist = []
dtitlefile = open("dlog2","r")
for line in dtitlefile:
	line = re.sub('[^0-9]','', line)
	dnumlist.append(line)

delnum = min(len(stlnumlist),len(numlist),len(prds_numlist),len(lnumlist),len(dnumlist))
print "smallest number:", delnum

delnum = delnum-1

delnum = 500

del stlnumlist[delnum:]
del numlist[delnum:]
del prds_numlist[delnum:]
del lnumlist[delnum:]
del dnumlist[delnum:]

arnum = array(numlist)
arstl = array(stlnumlist)
arprds = array(prds_numlist)
arlnum = array(lnumlist)
artarg = array(dnumlist)

fullarr = column_stack((arnum,arstl,arprds,arlnum))
print fullarr

print "titlelist length:"
print len(numlist)

print "localelist length:"
print len(lnumlist)

print "prdslist length:"
print len(prds_numlist)

print "stl length"
print len(stlnumlist)
sum = 0
svc = svm.SVC(kernel='poly',degree=3)
svc.fit(fullarr[::5],artarg[::5])
nlist = []
alist = []
for i in range(0,100):
	nlist.append(svc.predict(fullarr[i]))
	alist.append(artarg[i])
for i in range(len(nlist)):
	 # if(abs(int(nlist[i][0])-int(alist[i]))<5):
	 # 	sum = sum + 1
	 print nlist[i] ,artarg[i]

print sum
leswag = sum
for i in range(200,300):
	nlist.append(svc.predict(fullarr[i]))
	alist.append(artarg[i])
for i in range(len(nlist)):
	 if(abs(int(nlist[i][0])-int(alist[i]))<5):
	 	sum = sum + 1

print sum
print sum - leswag
leswag = sum 
sum = 0
for i in range(200,300):
	nlist.append(svc.predict(fullarr[i]))
	alist.append(artarg[i])
for i in range(len(nlist)):
	 if(abs(int(nlist[i][0])-int(alist[i]))<5):
	 	sum = sum + 1

print sum
print sum - leswag
leswag = sum 
sum = 0
for i in range(300,400):
	nlist.append(svc.predict(fullarr[i]))
	alist.append(artarg[i])
for i in range(len(nlist)):
	if(artarg[i] == ''):
		continue
	if(abs(int(nlist[i][0])-int(alist[i]))<5):
	 	sum = sum + 1

print sum
print sum - leswag
leswag = sum 
sum = 0
for i in range(400,500):
	nlist.append(svc.predict(fullarr[i]))
	alist.append(artarg[i])
for i in range(len(nlist)):
	 if(abs(int(nlist[i][0])-int(alist[i]))<5):
	 	sum = sum + 1
print sum
print sum - leswag
leswag = sum 