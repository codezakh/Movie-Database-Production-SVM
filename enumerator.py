from numpy import *
from sklearn import svm
import pylab as pl

#Enumerator for vectorising data


diclist = []
numlist = []
titlefile = open("parselog","r")
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
localefile = open("localelog","r")
for line in localefile:
	if line in ldiclist:
		lnumlist.append(ldiclist.index(line))
	else:
		ldiclist.append(line)
		lnumlist.append(len(ldiclist)-1)

prds_diclist = []
prds_numlist = []
prdsfile = open("prdslog","r")
for line in prdsfile:
	if line in prds_diclist:
		prds_numlist.append(prds_diclist.index(line))
	else:
		prds_diclist.append(line)
		prds_numlist.append(len(prds_diclist)-1)


stldiclist = []
stlnumlist = []
stltitlefile = open("stlog","r")
for line in stltitlefile:
	if line in stldiclist:
		stlnumlist.append(stldiclist.index(line))
	else:
		stldiclist.append(line)
		stlnumlist.append(len(stldiclist)-1)

delnum = min(len(stlnumlist),len(numlist),len(prds_numlist),len(lnumlist))
print "smallest number:", delnum

delnum = delnum-1

del stlnumlist[delnum:]
del numlist[delnum:]
del prds_numlist[delnum:]
del lnumlist[delnum:]

arnum = array(numlist)
arstl = array(stlnumlist)
arprds = array(prds_numlist)
arlnum = array(lnumlist)

fullarr = column_stack((arnum,arstl,arprds,arlnum))
print fullarr


clf = svm.SVC(kernel="linear",gamma=10)
clf.fit = ()

print "titlelist length:"
print len(numlist)

print "localelist length:"
print len(lnumlist)

print "prdslist length:"
print len(prds_numlist)

print "stl length"
print len(stlnumlist)