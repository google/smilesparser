import smilesparser

def inspect_element_symbol(element_symbol, indent=0):
  print "  " * indent + "Element symbol:", ''.join(element_symbol)

def inspect_charge(charge, indent=0):
  print "  " * indent + "Charge:", ''.join(charge)

def inspect_atomspec(atomspec, indent=0):
  print "  " * indent + "AtomSpec", ''.join(map(str, atomspec))
  for item in atomspec:
    if isinstance(item, smilesparser.AST.AromaticSymbol):
      inspect_aromatic_symbol(item.aromatic_symbol, indent+1)
    elif isinstance(item, smilesparser.AST.ElementSymbol):
      inspect_element_symbol(item.element_symbol, indent+1)
    elif isinstance(item, smilesparser.AST.Charge):
      inspect_charge(item.charge, indent+1)
    else:
      print "  " * indent + str(item), dir(item)

def inspect_atom(atom, indent=0):
  if isinstance(atom, smilesparser.AST.OrganicSymbol) or \
     isinstance(atom, smilesparser.AST.AromaticSymbol):
    print "  " * indent + "Atom:", atom
  elif isinstance(atom, smilesparser.AST.AtomSpec):
    inspect_atomspec(atom.atom_spec)
  else:
    print "  " * indent + atom, dir(atom)

def inspect_bond(bond, indent=0):
  print "  " * indent + "Bond:", bond

def inspect_ring_closure(ring_closure, indent=0):
  print "  " * indent + "Ring Closure:", ring_closure

def inspect_chain(chain, indent=0):
  # print "  " * indent + "Chain"
  for item in chain:
    if isinstance(item, smilesparser.AST.Bond):
      inspect_bond(item.bond, indent)
    elif isinstance(item, smilesparser.AST.Atom):
      inspect_atom(item.atom, indent)
    elif isinstance(item, smilesparser.AST.RingClosure):
      inspect_ring_closure(item.ring_closure, indent)
    else:
      print "  " * indent + item, dir(item)

def iterate_branch(branch, indent=0):
  # print "  " * indent + "Branch"
  for item in branch[0]:
    if isinstance(item, smilesparser.AST.Bond):
      inspect_bond(item.bond, indent)
    elif isinstance(item, smilesparser.AST.SMILES):
      iterate_smiles(item.smiles, indent)
    else:
      print "  " * indent + item, dir(item)

def iterate_smiles(smiles, indent=0):
  # print "  " * indent + "SMILES"
  for item in smiles:
    if isinstance(item, smilesparser.AST.Atom):
      inspect_atom(item.atom, indent)
    elif isinstance(item, smilesparser.AST.Chain):
      inspect_chain(item.chain, indent)
    elif isinstance(item, smilesparser.AST.Branch):
      iterate_branch(item, indent+1)
    else:
      print "  " * indent + item, dir(item)

smiles=[
    # 'C(C)C',
    # 'C=C(CCCC)CBr',
    # 'CCC(C(C)C)C[Br+]CC',
    'CC(=NO)C(C)=NO',
    # 'c1ccccc1',
    # 'CCC[S@](=O)c1ccc2c(c1)[nH]/c(=N/C(=O)OC)/[nH]2',
]
for s in smiles:
  print s
  parsed = smilesparser.SMILES.parseString(s)[0]
  iterate_smiles(parsed.smiles)
