import pyparsing as pp

class AST:

  class SMILES:
    def __init__(self, smiles):
      self.smiles = smiles
    def __getitem__(self, item):
      if item == 0:
        return self.smiles
      else:
        raise IndexError
    def __repr__(self):
      return ''.join(map(str, self.smiles))

  class Chain:
    def __init__(self, chain):
      self.chain = chain
    def __getitem__(self, item):
      if item == 0:
        return self.chain
      else:
        raise IndexError
    def __repr__(self):
      return ''.join(map(str, self.chain))

  class Branch:
    def __init__(self, branch):
      self.branch = branch
    def __getitem__(self, item):
      if item == 0:
        return self.branch
      else:
        raise IndexError
    def __repr__(self):
      return '(' + ''.join(map(str, self.branch)) + ')'

  class Atom:
    def __init__(self, atom):
      self.atom = atom
    def __getitem__(self, item):
      if item == 0:
        return self.atom
      else:
        raise IndexError
    def __repr__(self):
      return str(self.atom)

  class Bond:
    def __init__(self, bond):
      self.bond = bond
    def __getitem__(self, item):
      if item == 0:
        return self.bond
      else:
        raise IndexError
    def __repr__(self):
      return str(bond)

  class OrganicSymbol:
    def __init__(self, organic_symbol):
      self.organic_symbol = organic_symbol
    def __getitem__(self, item):
      if item == 0:
        return self.organic_symbol
      else:
        raise IndexError
    def __repr__(self):
      return ''.join(map(str, self.organic_symbol))

  class AromaticSymbol:
    def __init__(self, aromatic_symbol):
      self.aromatic_symbol
    def __getitem__(self, item):
      if item == 0:
        return self.atomatic_symbol
      else:
        raise IndexError
    def __repr__(self):
      return str(self.aromatic_symbol)

  class AtomSpec:
    def __init__(self, atom_spec):
      self.atom_spec = atom_spec
    def __getitem__(self, item):
      if item == 0:
        return self.atom_spec
      else:
        raise IndexError
    def __repr__(self):
      return str(self.atom_spec)

  class ElementSymbol:
    def __init__(self, element_symbol):
      self.element_symbol
    def __getitem__(self, item):
      if item == 0:
        return self.element_symbol
      else:
        raise IndexError
    def __repr__(self):
      return str(self.element_symbol)

  class RingClosure:
    def __init__(self, ring_closure):
      self.ring_closure
    def __getitem__(self, item):
      if item == 0:
        return self.ring_closure
      else:
        raise IndexError
    def __repr__(self):
      return str(self.ring_closure)

  class ChiralClass:
    def __init__(self, chiral_class):
      self.chiral_class
    def __getitem__(self, item):
      if item == 0:
        return self.chiral_class
      else:
        raise IndexError
    def __repr__(self):
      return str(self.chiral_class)

  class HCount:
    def __init__(self, hcount):
      self.hcount = hcount
    def __getitem__(self, item):
      if item == 0:
        return self.hcount
      else:
        raise IndexError
    def __repr__(self):
      return str(self.hcount)

  class Charge:
    def __init__(self, charge):
      self.charge = charge
    def __getitem__(self, item):
      if item == 0:
        return self.charge
      else:
        raise IndexError
    def __repr__(self):
      return str(self.charge)

  class Class:
    def __init__(self, class_):
      self.class_ = class_
    def __getitem__(self, item):
      if item == 0:
        return self.class_
      else:
        raise IndexError
    def __repr__(self):
      return str(self.class_)

  class Isotope:
    def __init__(self, isotope):
      self.items = isotope
    def __getitem__(self, item):
      if item == 0:
        return self.isotope
      else:
        raise IndexError
    def __repr__(self):
      return str(self.isotope)

def smiles_fn(s,l,t):
  print "smiles_fn", 's=', s, 'l=', l, 't=', t
  return AST.SMILES(t[0])

def chain_fn(s,l,t):
  print "chain_fn", 's=', s, 'l=', l, 't=', t
  return AST.Chain(t[0])

def branch_fn(s,l,t):
  print "branch_fn", 's=', s, 'l=', l, 't=', t
  return AST.Branch(t[0])

def atom_fn(s,l,t):
  print "atom_fn", 's=', s, 'l=', l, 't=', t
  return AST.Atom(t[0])

def bond_fn(s,l,t):
  print "bond_fn", 's=', s, 'l=', l, 't=', t
  return AST.Bond(t[0])

def organic_symbol_fn(s,l,t):
  print "organic_symbol_fn", 's=', s, 'l=', l, 't=', t
  return AST.OrganicSymbol(t[0])

def aromatic_symbol_fn(s,l,t):
  print "aromatic_symbol_fn", 's=', s, 'l=', l, 't=', t
  return AST.AromaticSymbol(t[0])

def atom_spec_fn(s,l,t):
  print "atom_spec_fn", 's=', s, 'l=', l, 't=', t
  return AST.AtomSpec(t[0])

def element_symbol_fn(s,l,t):
  print "element_symbol_fn", 's=', s, 'l=', l, 't=', t
  return AST.ElementSymbol(t[0])

def ring_closure_fn(s,l,t):
  print "ring_closure_fn", 's=', s, 'l=', l, 't=', t
  return AST.RingClosure(t[0])

def chiral_class_fn(s,l,t):
  print "chiral_class_fn", 's=', s, 'l=', l, 't=', t
  return AST.ChiralClass(t[0])

def hcount_fn(s,l,t):
  print "hcount_fn", 's=', s, 'l=', l, 't=', t
  return AST.HCount(t[0])

def charge_fn(s,l,t):
  print "charge_fn", 's=', s, 'l=', l, 't=', t
  return AST.Charge(t[0])

def class_fn(s,l,t):
  print "class_fn", 's=', s, 'l=', l, 't=', t
  return AST.Class(t[0])

def isotope_fn(s,l,t):
  print "isotope_fn", 's=', s, 'l=', l, 't=', t
  return AST.Isotope(t[0])

Atom = pp.Forward()
Chain = pp.Forward()
Branch = pp.Forward()
RingClosure = pp.Forward()
Bond = pp.Forward()
OrganicSymbol = pp.Forward()
AromaticSymbol = pp.Forward()
AtomSpec = pp.Forward()
WILDCARD = pp.Forward()
Isotope = pp.Forward()
ElementSymbol = pp.Forward()
ChiralClass = pp.Forward()
HCount = pp.Forward()
Charge = pp.Forward()
Class = pp.Forward()


SMILES = pp.Group(Atom + pp.ZeroOrMore(pp.Or([Chain, Branch])))
SMILES.setParseAction(smiles_fn)

Chain <<= pp.Group(pp.Optional(Bond) + pp.Or([Atom, RingClosure]))
Chain.setParseAction(chain_fn)

Branch <<= pp.Literal('(').suppress() + pp.Group(pp.Optional(Bond) + pp.OneOrMore(SMILES)) + pp.Literal(')').suppress()
Branch.setParseAction(branch_fn)

Atom <<= pp.Or([OrganicSymbol, AromaticSymbol, AtomSpec, WILDCARD])
Atom.setParseAction(atom_fn)

Bond <<= pp.Or(map(pp.Literal, ['-', '=', '#', '$', ':', '/', '\\', '.']))
Bond.setParseAction(bond_fn)

OrganicSymbol <<= (pp.Group(pp.Literal('B') + pp.Optional(pp.Literal('r'))) | \
                   pp.Group(pp.Literal('C') + pp.Optional(pp.Literal('l'))) | \
                   pp.Literal('N') | \
                   pp.Literal('O') | \
                   pp.Literal('P') | \
                   pp.Literal('S') | \
                   pp.Literal('F') | \
                   pp.Literal('I'))
OrganicSymbol.setParseAction(organic_symbol_fn)

AromaticSymbol <<= pp.Or(map(pp.Literal, ['b', 'c', 'n', 'o', 'p', 's']))
AromaticSymbol.setParseAction(aromatic_symbol_fn)

AtomSpec <<= pp.Literal('[').suppress() + \
  pp.Group( \
    pp.Optional(Isotope) + \
    pp.Or([pp.Literal('se'), pp.Literal('as'), AromaticSymbol, ElementSymbol, WILDCARD]) + \
    pp.Optional(ChiralClass) + \
    pp.Optional(HCount) + \
    pp.Optional(Charge) + \
    pp.Optional(Class)) + \
  pp.Literal(']').suppress()
AtomSpec.setParseAction(atom_spec_fn)

WILDCARD <<= '*'

ElementSymbol <<= pp.Group(pp.Word(pp.srange('[A-Z_]'), exact=1) + pp.Optional(pp.Word(pp.srange('[a-z]'), exact=1)))
ElementSymbol.setParseAction(element_symbol_fn)

RingClosure <<= pp.Or([pp.Group(pp.Literal('%') + pp.Word(pp.srange('[1-9]'), exact=1) + pp.Word(pp.srange('[0-9]'), exact=1)), pp.Word(pp.srange('[0-9]'), exact=1)])
RingClosure.setParseAction(ring_closure_fn)

ChiralClass <<= pp.Optional(
    pp.Group(
        pp.Literal('@') + pp.Optional(pp.Or([
            pp.Literal('@'),
            pp.Literal('TH') + pp.Word(pp.srange('[1-2]'), exact=1),
            pp.Literal('AL') + pp.Word(pp.srange('[1-2]'), exact=1),
            pp.Literal('SP') + pp.Word(pp.srange('[1-3]'), exact=1),
            pp.Literal('TB') + pp.Or([ pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)),
                                       pp.Literal('2') + pp.Optional(pp.Literal('0')),
                                       pp.Word(pp.srange('[3-9]'), exact=1)]),
            pp.Literal('OH') + pp.Or([ pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)),
                                       pp.Literal('2') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)),
                                       pp.Literal('3') + pp.Optional(pp.Literal('0')),
                                       pp.Word(pp.srange('[4-9]'), exact=1)])]))))
ChiralClass.setParseAction(chiral_class_fn)

HCount <<= pp.Group(pp.Literal('H') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)))
HCount.setParseAction(hcount_fn)

Charge <<= pp.Group(pp.Or([
    pp.Literal('-') + pp.Optional(pp.Or([pp.Literal('-'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)])),
    pp.Literal('+') + pp.Optional(pp.Or([pp.Literal('+'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)]))]))
Charge.setParseAction(charge_fn)

Class <<= pp.Group(pp.Literal(':') + pp.Word(pp.srange('[0-9]'), exact=1))
Class.setParseAction(class_fn)

Isotope <<= pp.Group(pp.Word(pp.srange('[1-9]'), exact=1) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)))
Isotope.setParseAction(isotope_fn)

print SMILES.parseString('C')
print SMILES.parseString('CC')
print SMILES.parseString('Br')
print SMILES.parseString('CCBr')
print SMILES.parseString('CC(CC)C')
# for seq in [
#     # 'C', \
#     # 'CC', \
#     'C(CC)C', \
#     # 'CC(C)C',
# ]:
#   print 'seq=', seq
#   print SMILES.parseString(seq)
# print SMILES.parseString('CCC(C(C)C)C[Br+]CC')
# print SMILES.parseString('CC(=NO)C(C)=NO')
# print SMILES.parseString('c1ccccc1')
# print SMILES.parseString('CCC[S@](=O)c1ccc2c(c1)[nH]/c(=N/C(=O)OC)/[nH]2')

# s = open("../13_p0.smi").readlines()
# lines = [line.strip().split()[0] for line in s[1:]]
# for line in lines:
#   print line
#   print SMILES.parseString(line)
#   print
