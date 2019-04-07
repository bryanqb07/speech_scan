# sample code from wall street days
# analyzes the frequency of positive words : negative words
# in a company's quarterly earnings speech
# then writes them to a file

from sys import argv
import os.path

script  = argv

quarters = ["Q1", "Q2", "Q3", "Q4"]
companies = ["IP", "KS", "PKG","RKT","BCC","LPX","MAS","MHK","MLM","NBD", "OC","USG","VMC","PCH","PCL","RYN","WY", "CLW", "GLT","MWV","RYAM","UFS", 
             "VRTV","ATR","BLL","BMS","CCK","OI","REX","SEE","SLGN","SON"]
company_matrix = []

for quarter in quarters:
    for company in companies:
        if os.path.isfile(company + " " + quarter + " " + "2014.txt"): 
            text = open(company + " " + quarter + " " + "2014.txt", 'r')
    goodcount = 0 #number of pos words
    badcount = 0 #number of neg words
    positive = ["record", "pleasant", "strong", "solid", "pleased", "above", "success", "exceeded", "confident", "optimistic", "satisfied", "stronger", "strengthening"]
    negative = ["unexpected", "slower", "weak", "weaker", "weakening", "trying", "hopeful", "difficulties", "overcome", "issues", "unfortunately", "however"]
    for line in text:
        words = line.split()
        #print words
        for word in words:
            if word in positive:
                goodcount = goodcount + 1.0
            if word in negative:
                badcount = badcount + 1.0
    print "Positive indicators: %d" % goodcount
    print "Negative indicators: %d" % badcount
    management_score = round(goodcount/(goodcount + badcount),3)
    print "Management score for %s: %f" % (company, management_score)
    company_matrix.append([company,quarter, management_score])
else:
    print company + " " + quarter + " file does not exist."

print company_matrix
final_list = open("Results.txt",'w')
for lists in company_matrix:
    for things in lists:
        final_list.write("%s\t" % things)
        final_list.write("\n")
