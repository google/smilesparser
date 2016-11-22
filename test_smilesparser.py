from smilesparser import SMILES

s = open("test.smi").readlines()
lines = [line.strip().split()[0] for line in s[1:]]
def check(smiles):
  parsed = SMILES.parseString(line)[0]
  if line != parsed and line != str(parsed) and line != str(str(parsed)):
    print "mismatch:"
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
