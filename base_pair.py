#!/usr/bin/python
import sys
import math

if __name__ == "__main__":
	with open(sys.argv[1], "r") as ins:
    		Sr =[]
		bool = False
    		for line in ins:
		 if 'Base-pairs' in line:
       		    		bool = True 
					
		 if bool:
                   if 'Base Triples' in line:
			bool = False
		   else:
			Sr.append(line.rstrip().split(' :', 1)[:1])

		Sr.pop(0)
		Sr=sum(Sr,[])
	with open(sys.argv[2], "r") as ins:
    		Sm =[]
		bool = False
    		for line in ins:
		 if 'Base-pairs' in line:
       		    		bool = True 
					
		 if bool:
                   if 'Base Triples' in line:
			bool = False
		   else:
			
			Sm.append(line.rstrip().split(' :', 1)[:1])

		Sm.pop(0);
		Sm=sum(Sm,[])

	TP = float(len(set(Sr).intersection(Sm)))
	FP = float(len(set(Sm).difference(Sr)))
	FN = float(len(set(Sr).difference(Sm)))

	PPV = TP/(TP+FP)
	STY = TP/(TP+FN)
	INF = math.sqrt(PPV*STY)
	print round(INF,2)



	



