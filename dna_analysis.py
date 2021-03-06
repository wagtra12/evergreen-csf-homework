# Name: Kevin Kim.
# Evergreen Login: Kimkev08
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
c_count = 0
t_count = 0
g_count = 0
a_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    if bp =='A' or bp == 'T':
        at_count = at_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

at_content = float(at_count) / total_count

# Print the answer
print 'GC-content:', gc_content

print 'AT-content:', at_content


for bp in seq:
    # increment the total number of bps we've seen

    # next, if the bp is a G or a C,
    if bp == 'C':
        # increment the count of gc
        c_count = c_count + 1
    if bp == 'T':
        t_count = t_count + 1
    if bp == 'G':
        g_count = g_count + 1
    if bp == 'A':
        a_count = a_count + 1

c_content = float(c_count)
print 'c_content:', c_content

g_content = float(g_count)
print 'G_content:', g_content

t_content = float(t_count)
print 'T_content:', t_content

a_content = float(a_count)
print 'A_content:', a_content

gcat_count = c_content + g_content + t_content + a_content
print 'GCAT_content:', gcat_count
print 'total count:', total_count
print 'total length', len(seq)

AT_Ratio = (a_count + t_count) / (g_count +c_count)
print 'AT Ratio:', AT_Ratio

if gc_content > (total_count * .6):
    print 'High GC Content'
if gc_content < (total_count * .4):
    print 'Low GC Content'
else:
    print 'Moderate GC Content'
    

#Create a variable that takes the gc_content and times it by 100 to get it out of a float.
#Then use that variable to check if its bigger or lesser that the count of the gc_content.
#Like this

#per= gc_content * 100
#if per > 60:
    #print 'high'
#if per < 40:
    #print 'low'
#else:
    #print 'moderate' 
