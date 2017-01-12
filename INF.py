import sys
import math

def make_S(afile, S):
	for i in range (0, len(afile)):
			if 'Base-pairs' in afile[i]:
				flag = True #jestem
				i=i+1
				while(flag):
					if 'Base Triples' in afile[i]:
						flag = False
					else:
						afile[i].rstrip().split(' :', 1)[:1]
						S.append(afile[i].rstrip().split(' :', 1)[:1])
						i=i+1
	print S	
	S.pop()
	return sum(S,[])

def main(argv):
	file_r = open(sys.argv[1]).readlines()
	Sr =[]
	Sr = make_S(file_r, Sr)
	print Sr ,'Sr'
	file_m = open(sys.argv[2]).readlines()
	Sm =[]
	Sm = make_S(file_m, Sm)


	TP = set(Sr).intersection(Sm)
	FP = set(Sm).difference(Sr)
	FN = set(Sr).difference(Sm)

	PPV = len(TP)/float(len(TP)+len(FP))
	STY = len(TP)/float(len(TP)+len(FN))
	INF = math.sqrt(PPV*STY)
	print round(INF,2)

if __name__ == "__main__":
   main(sys.argv[1:])

