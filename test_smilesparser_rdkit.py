# Copyright 2016 Google Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import smilesparser
from rdkit import Chem

serial = 0

element_number = {'C': 6,
                  'N': 7,
                  'O': 8,
                  'H': 1,
                  'S': 16
}

class SMILES:
  def __init__(self, smiles):
    self.mol = Chem.RWMol()
    self.parsed = smilesparser.SMILES.parseString(smiles)[0]
    self.prevAtomIdx = None
    self.prevBond = None
    self.atomStack = []
    self.ringClosures = {}
    self.iterate_smiles(self.parsed.smiles)
    
  def AddAtom(self, s): 
    a = Chem.Atom(element_number[s.upper()])

    if a.GetSymbol() == 'S':
      a.SetHybridization(Chem.rdchem.HybridizationType.SP2)
      a.SetNumRadicalElectrons(1)
      a.SetNoImplicit(True)
    else:
      if not self.prevBond:
        a.SetHybridization(Chem.rdchem.HybridizationType.SP3)
      elif self.prevBond == ':':
        bt = Chem.rdchem.BondType.SINGLE
        a.SetHybridization(Chem.rdchem.HybridizationType.SP2)
      elif self.prevBond == '=':
        bt = Chem.rdchem.BondType.DOUBLE
        a.SetHybridization(Chem.rdchem.HybridizationType.SP2)
      else:
        raise RuntimeError
      
    idx = self.mol.AddAtom(a)
    if self.prevAtomIdx is not None:
      self.AddBond(idx)
    self.prevAtomIdx = idx
    return a

  def AddBond(self, idx):
    bt = Chem.rdchem.BondType.SINGLE
    if self.prevBond:
      if self.prevBond == '=':
        bt = Chem.rdchem.BondType.DOUBLE
      if self.prevBond == '#':
        bt = Chem.rdchem.BondType.TRIPLE
      if self.prevBond == ':':
        bt = Chem.rdchem.BondType.AROMATIC
    self.mol.AddBond(self.prevAtomIdx, idx, bt)
    self.prevBond = None
    
  def inspect_organic_symbol(self, organic_symbol, indent=0):
    s = ''.join(organic_symbol)
    self.AddAtom(s)

  def inspect_aromatic_symbol(self, aromatic_symbol, indent=0):
    s = ''.join(aromatic_symbol)
    a = self.AddAtom(s)
    a.SetIsAromatic(True)
    self.prevBond = ":"

  def inspect_element_symbol(self, element_symbol, indent=0):
    s = ''.join(element_symbol)
    self.AddAtom(s)

  def inspect_chiral_class(self, chiral_class, indent=0):
    pass

  def inspect_hcount(self, hcount, indent=0):
    pass

  def inspect_charge(self, charge, indent=0):
    pass

  def inspect_atomspec(self, atomspec, indent=0):
    self.atomStack.append(self.prevAtomIdx)
    for item in atomspec:
      if isinstance(item, smilesparser.AST.AromaticSymbol):
        self.inspect_aromatic_symbol(item.aromatic_symbol, indent+1)
      elif isinstance(item, smilesparser.AST.ElementSymbol):
        self.inspect_element_symbol(item.element_symbol, indent+1)
      elif isinstance(item, smilesparser.AST.ChiralClass):
        self.inspect_chiral_class(item.chiral_class, indent+1)
      elif isinstance(item, smilesparser.AST.HCount):
        self.inspect_hcount(item.hcount, indent+1)
      elif isinstance(item, smilesparser.AST.Charge):
        self.inspect_charge(item.charge, indent+1)
      else:
        print "  " * indent + str(item), dir(item)
    self.prevAtomIdx = self.atomStack.pop()

  def inspect_atom(self, atom, indent=0):
    if isinstance(atom, smilesparser.AST.OrganicSymbol):
      self.inspect_organic_symbol(atom.organic_symbol, indent)
    elif isinstance(atom, smilesparser.AST.AromaticSymbol):
      self.inspect_aromatic_symbol(atom.aromatic_symbol, indent)
    elif isinstance(atom, smilesparser.AST.AtomSpec):
      self.inspect_atomspec(atom.atom_spec, indent)
    else:
      print "  " * indent + atom, dir(atom)

  def inspect_bond(self, bond, indent=0):
    self.prevBond = bond


  def inspect_ring_closure(self, ring_closure, indent=0):
    if ring_closure not in self.ringClosures:
      self.ringClosures[ring_closure] = self.prevAtomIdx
    else:
      idx = self.ringClosures[ring_closure]
      self.AddBond(idx)

  def inspect_chain(self, chain, indent=0):
    for item in chain:
      if isinstance(item, smilesparser.AST.Bond):
        self.inspect_bond(item.bond, indent)
      elif isinstance(item, smilesparser.AST.Atom):
        self.inspect_atom(item.atom, indent)
      elif isinstance(item, smilesparser.AST.RingClosure):
        self.inspect_ring_closure(item.ring_closure, indent)
      else:
        print "  " * indent + item, dir(item)

  def iterate_branch(self, branch, indent=0):
    self.atomStack.append(self.prevAtomIdx)
    for item in branch[0]:
      if isinstance(item, smilesparser.AST.Bond):
        self.inspect_bond(item.bond, indent+1)
      elif isinstance(item, smilesparser.AST.SMILES):
        self.iterate_smiles(item.smiles, indent+1)
      else:
        print "  " * indent + item, dir(item)
    self.prevAtomIdx = self.atomStack.pop()

  def iterate_smiles(self, smiles, indent=0):
    for item in smiles:
      if isinstance(item, smilesparser.AST.Atom):
        self.inspect_atom(item.atom, indent)
      elif isinstance(item, smilesparser.AST.Chain):
        self.inspect_chain(item.chain, indent)
      elif isinstance(item, smilesparser.AST.Branch):
        self.iterate_branch(item, indent+1)
      else:
        print "  " * indent + item, dir(item)

def print_mol(mol):
  for atom in mol.GetAtoms():
    atom.UpdatePropertyCache(strict=False)

    print (atom.GetIdx(),
           atom.GetAtomicNum(),
           atom.GetDegree(),
           atom.GetTotalDegree(),
           atom.GetTotalValence(),
           atom.GetImplicitValence(),
           atom.GetExplicitValence(),
           atom.GetFormalCharge(),
           atom.GetNumRadicalElectrons(),
           atom.GetHybridization(),
           atom.GetNoImplicit())
   
  for bond in mol.GetBonds():
      print (bond.GetBeginAtomIdx(),
             bond.GetEndAtomIdx(),
             bond.GetBondType())

if __name__ == '__main__':
  smiles=[
    # 'C',
    # 'CC',
    # 'CCCCC(CCC)CCC',
    # 'C1CCC(C1C)CCCC',
    # 'c1ccccc1',
    # 'Cc1ccccc1',
    # 'CCC[S]=O',
    # 'CC[S@](=O)c1ccc2c(c1)[nH]/c(=N/C(=O)OC)/[nH]2',
    'C=CCc1cc(OC)c2c(c1OC)OCO2'
    # 'CCC(=O)O[C@]1(CC[NH+](C[C@@H]1CC=C)C)c2ccccc2'
  ]
  for s in smiles:
    print s
    m = Chem.MolFromSmiles(s)
    s1 = Chem.MolToSmiles(m)
    print s1
    print_mol(m)
    print

    sm = SMILES(s1)
    print_mol(sm.mol)
    print Chem.MolToSmiles(sm.mol)
    print
