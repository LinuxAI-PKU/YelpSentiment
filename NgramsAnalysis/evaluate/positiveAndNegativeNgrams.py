from __future__ import division
import csv

arrayNegative = []
arrayPositive = []
arrayPositiveNgrams = []
arrayPositiveNgramsWithFreq = []
arrayNegativeNgrams = []
arrayNegativeNgramsWithFreq = []

with open("PositiveNgramsFiltered", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayPositiveNgrams.append(str1)
        arrayPositiveNgramsWithFreq.append(line)
        
with open("NegativeNgramsFiltered", "r") as ins:
    for line in ins:
        lastIndex = line.rfind(':')
        str1 = line[:lastIndex]
        str1.strip()
        arrayNegativeNgrams.append(str1)
        arrayNegativeNgramsWithFreq.append(line)        
        
with open("../../data/partition/validate/yelp_restaurants_reviews_positive.csv", "r") as f0:
    ins = csv.DictReader(f0)
    for line in ins:
        text = line['text']
        arrayPositive.append(text)

with open("../../data/partition/validate/yelp_restaurants_reviews_negative.csv", "r") as f1:
    ins = csv.DictReader(f1)
    for line in ins:
        text = line['text']
        arrayNegative.append(text)

numTPMatches = 0 
for j in range(len(arrayPositive)):
    matchesP = False
    matchesN = False
    for i in range(len(arrayPositiveNgrams)):
	    w = arrayPositiveNgrams[i]

	    if arrayPositive[j].find(w) > -1:
	        matchesP = True
	        break
        
    #for i in range(len(arrayNegativeNgrams)):
	#    w = arrayNegativeNgrams[i]

	#    if arrayPositive[j].find(w) > -1:
	#        matchesN = True
	#        break
	                
    #if matchesP == True and matchesN == False:
    if matchesP == True:
        numTPMatches += 1
        
numTNMatches = 0 
for j in range(len(arrayNegative)):
    matchesP = False
    matchesN = False
    for i in range(len(arrayPositiveNgrams)):
	    w = arrayPositiveNgrams[i]

	    if arrayNegative[j].find(w) > -1:
	        matchesN = True
	        break
	
    #for i in range(len(arrayPositiveNgrams)):
	#    w = arrayPositiveNgrams[i]

	#    if arrayNegative[j].find(w) > -1:
	#        matchesP = False
	#        break
	        
    if matchesN == False:
        numTNMatches += 1
        
print "Accuracy = " + str((numTPMatches+numTNMatches)/(len(arrayPositive) + len(arrayNegative)))             
                        
print "ngram \t\t\t\t Positive \t\t Negative"
for i in range(len(arrayPositiveNgrams)):
    w = arrayPositiveNgrams[i]

    positiveMatches = 0;
    for j in range(len(arrayPositive)):
        if arrayPositive[j].find(w) > -1:
            positiveMatches += 1
            
    negativeMatches = 0;
    for j in range(len(arrayNegative)):
        if arrayNegative[j].find(w) > -1:
            negativeMatches += 1
    
    print arrayPositiveNgrams[i] + "\t\t\t" + str(positiveMatches) + "/" + str(len(arrayPositive)) + "\t\t\t" + str(negativeMatches) + "/" + str(len(arrayNegative))
    #print str(positiveMatches/len(arrayPositive)) + "\t\t" + str(negativeMatches/len(arrayNegative))
    	  
