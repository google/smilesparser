# Inspired by https://github.com/atrigent/smilesvis/blob/master/smiles.py
import pyparsing as pp

elements = map(pp.Literal, [ 'H', 'C', 'N', 'O', 'F', 'S', 'Br', 'Cl', 'I',  ])
substituent = pp.Forward()
atom = pp.Or(elements)
atom_chain = atom + pp.ZeroOrMore(pp.Or([atom, substituent]))
substituent <<= pp.Group(pp.Literal('(').suppress() + atom_chain + pp.Literal(')').suppress())

smiles = (pp.StringStart() +
          atom_chain +
          pp.StringEnd())

tests = [
    'C',
    'CC',
    'CClC',
    'C(C)C',
    'C(C(C)C)C'
    ]

# tests = [
#     'N#N',
#     'CN=C=O',
#     'OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@@H](O)1',
#     'CC[C@H](O1)CC[C@@]12CCCO2',
#     'CC(C)[C@@]12C[C@@H]1[C@@H](C)C(=O)C2',
#     '[2H]C(Cl)(Cl)Cl'
# ]
          
for test in tests:
    print(test)
    print(smiles.parseString(test))

# substituent_num = (pp.Word(pp.nums, exact=1) ^
#                    (pp.Literal('%').suppress() + pp.Word(pp.nums))
#                   )

# substituent <<= (pp.Group(pp.Literal('(').suppress() +
#                           bond_type + atom_chain +
#                           pp.Literal(')').suppress()) ^
#                  substituent_num)


# smiles = (pp.StringStart() +
#           pp.Group(atom_chain) + pp.ZeroOrMore(pp.Literal('.').suppress() + pp.Group(atom_chain)) +
#           pp.StringEnd())

