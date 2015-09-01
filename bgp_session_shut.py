"""
This script takes the output from "sh ip bgp vrf all sum" 
on a Nexus 7770, filters "active" and "idle" states over 
all vrfs. It then creates the output to shutdown these sesssions"

Input file: bgp_sum.txt

"""
#display all idle, active sessions
with open('./bgp_sum.txt','r') as fh:
	counter = 0
	print ("router bgp 64775")
	#display only active and idle sessions (checking)
	for line in fh:
		if "Idle" in line or "Active" in line:
			counter += 1
			line = line.rstrip()
			print line
	print "\nEntries: " + str(counter) + "\n"
	linebreak = ("------------------------------------------------------------"
				 "-------------------\n")
	print linebreak

#create output to shut sessions
with open('./bgp_sum.txt','r') as fh:
	counter = 0
	print ("Formatting the output")
	for line in fh:
		if "VRF" in line:
			split = line.split()
			vrf = split[5]
			#remove last char from string vrf (comma)
			vrf = vrf[:-1]
			print "\nvrf " + vrf
		if "Idle" in line or "Active" in line:
			counter += 1
			split = line.split()
			print "neighbor " + split[0]
			print "shutdown"
	print "\nEntries: " + str(counter) + "\n"

