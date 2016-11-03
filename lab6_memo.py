import random    

n = 10
calls = 0
 
l1 = random.sample(xrange(1, 20), n+1)
l2 = random.sample(xrange(1, 20), n+1)
l3 = random.sample(xrange(1, 20), n+1)

# line = [[8,9,11,7,9],[9,7,9,10,12],[7,9,8,11,10]]
# trans = [[13,4,10,11,12],[10,5,7,11,12],[11,12,13,11,9]]

line = [l1,l2,l3]

t1 = random.sample(xrange(1, 20), n+1)
t2 = random.sample(xrange(1, 20), n+1)
t3 = random.sample(xrange(1, 20), n+1)

trans = [t1,t2,t3]

def assembly_line(si,sj):
	global calls
	calls += 1
	if(sj == 0):
		return line[si][sj]

	loc = str(3)+str(sj-1)
	if not(loc in dict):
		#Computer comming from the same transfer belt
		t1 = assembly_line(1,sj-1) + line[si][sj]
		dict[loc] = t1
	else:
		t1 = dict[loc]

	loc = str(1)+str(sj-1)
	if not(loc in dict):
		#Computer comming from transfer belt 1
		t2 = assembly_line(1,sj-1) + trans[si][sj]
		dict[loc] = t2
	else:
		t2 = dict[loc]

	loc = str(2)+str(sj-1)
	if not(loc in dict):
		#Computer comming from transfer belt 2
		t3 = assembly_line(2,sj-1) + trans[si][sj]
		dict[loc] = t3
	else:
		t3 = dict[loc]

	return min(t1,t2,t3)


#dictionary for memoization
dict = {}
print "Best Solution for assembly line 1: ",assembly_line(0,n)
dict = {}# resetting the dictionary
print "Best Solution for assembly line 2: ",assembly_line(1,n)
dict = {}# resetting the dictionary
print "Best Solution for assembly line 3: ",assembly_line(2,n)
print "Recursive Calls: ",calls