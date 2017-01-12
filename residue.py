import sys
from Bio.PDB import *
#for 1	N1	N3	2.89	0.11	T
2	N2	O2	2.77	0.15	T
3	O6	N4	2.96	0.17	T
"""
#for AU
""" 
Bond	A	U	Length Ave	Length Std	Attribute
1	N1	N3	2.84	0.12	T
2	N6	O4	3.00	0.17	T
"""
""" 
if __name__ == "__main__":
	z = sys.argv[1]
	parser = PDBParser()
	structure = parser.get_structure('nazwa',z)
	num=0
	for residue1 in structure.get_residues():		       
		       	 num+=1
	for residue1 in structure.get_residues():
		       k=0
		       for residue2 in structure.get_residues():
		       	k+=1
		        resseq1 = residue1.get_full_id()[3][1]
		        resseq2 = residue2.get_full_id()[3][1]
		        if k==num and (  residue1.get_resname()=='  C' or  residue1.get_resname()=='  G' or  residue1.get_resname()=='  U' or  residue1.get_resname()=='  A'):
		        	print resseq1, residue1.get_resname(),0
		        	break
		        elif residue1.get_resname()=='  C' and residue2.get_resname()=='  G':
				 	
				 	 if residue1['N3']-residue2['N1']<=(2.89+(3*0.11))  or residue1['O2']-residue2['N2']<=(2.77+(3*0.15)) or residue1['N4']-residue2['O6']<=(2.96+(3*0.17)):
				 	 	print resseq1, residue1.get_resname(),resseq2
					 	break
		        elif residue1.get_resname()=='  G' and residue2.get_resname()=='  C':
			         
			         if residue1['N1']-residue2['N3']<=(2.89+(3*0.11)) or residue1['N2']-residue2['O2']<=(2.77+(3*0.15)) or  residue1['O6']-residue2['N4']<=(2.96+(3*0.17)) :
				        print resseq1, residue1.get_resname(),resseq2
				        break  	 
		        elif residue1.get_resname()=='  U' and residue2.get_resname()=='  A':
		        
		        	if residue1['N3']-residue2['N1']<=(2.84+(3*0.12)) or residue1['O4']-residue2['N6']<=(3.0+(3*0.17)) :
			 	 		print resseq1, residue1.get_resname(),resseq2
			 	 		break 
		        elif residue1.get_resname()=='  A' and residue2.get_resname()=='  U':
					if residue1['N1']-residue2['N3']<=(2.84+(3*0.12))  or residue1['N6']-residue2['O4']<=(3.0+(3*0.17)) :
			 	 		print resseq1, residue1.get_resname(),resseq2
			 	 		break