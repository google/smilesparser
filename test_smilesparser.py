from smilesparser import SMILES

# print SMILES.parseString('C')[0]
# print SMILES.parseString('CC')[0]
# print SMILES.parseString('Br')[0]
# print SMILES.parseString('CCBr')[0]
# print SMILES.parseString('CC(CC)C')[0]
# print SMILES.parseString('CCC(C(C)C)C[Br+]CC')[0]
# print SMILES.parseString('CC(=NO)C(C)=NO')[0]
# print SMILES.parseString('c1ccccc1')[0]
# print SMILES.parseString('CCC[S@](=O)c1ccc2c(c1)[nH]/c(=N/C(=O)OC)/[nH]2')[0]

s = open("../13_p0.smi").readlines()
lines = [line.strip().split()[0] for line in s[1:]]
def check(smiles):
  parsed = SMILES.parseString(line)[0]
  if line != parsed and line != str(parsed) and line != str(str(parsed)):
    print "mismatch:"
    import pdb; pdb.set_trace()
    print line
    print parsed
    print
    return False
  return True

# from multiprocessing import Pool
# pool = Pool(12)
# results = pool.map(check, lines)
for line in lines:
  check(line)
