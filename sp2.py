import pyparsing as pp

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


SMILES = Atom + pp.ZeroOrMore(pp.Or([Chain, Branch]))
Chain <<= pp.Optional(Bond) + pp.Or([Atom, RingClosure])
Branch <<= pp.Literal('(').suppress() + pp.Group(pp.Optional(Bond) + pp.OneOrMore(SMILES)) + pp.Literal(')').suppress()
Atom <<= pp.Or([OrganicSymbol, AromaticSymbol, AtomSpec, WILDCARD])
Bond <<= pp.Or(map(pp.Literal, ['-', '=', '#', '$', ':', '/', '\\', '.']))

OrganicSymbol <<= (pp.Literal('B') + pp.Optional(pp.Literal('r'))) | \
                (pp.Literal('C') + pp.Optional(pp.Literal('l'))) | \
                pp.Literal('N') | \
                pp.Literal('O') | \
                pp.Literal('P') | \
                pp.Literal('S') | \
                pp.Literal('F') | \
                pp.Literal('I')
AromaticSymbol <<= pp.Or(map(pp.Literal, ['b', 'c', 'n', 'o', 'p', 's']))


## Needs to be defined down here to work...?
AtomSpec <<= pp.Literal('[').suppress() + pp.Group( \
    pp.Optional(Isotope) + \
    pp.Or([pp.Literal('se'), pp.Literal('as'), AromaticSymbol, ElementSymbol, WILDCARD]) + \
    pp.Optional(ChiralClass) + \
    pp.Optional(HCount) + \
    pp.Optional(Charge) + \
    pp.Optional(Class) ) + \
    pp.Literal(']').suppress()

WILDCARD <<= '*'
ElementSymbol <<= pp.Group(pp.Word(pp.srange('[A-Z_]'), exact=1) + pp.Optional(pp.Word(pp.srange('[a-z]'), exact=1)))
RingClosure <<= pp.Or([pp.Literal('%') + pp.Word(pp.srange('[1-9]'), exact=1) + pp.Word(pp.srange('[0-9]'), exact=1), pp.Word(pp.srange('[0-9]'), exact=1)])
ChiralClass <<= pp.Optional( pp.Literal('@') + pp.Optional(pp.Or([
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
                               pp.Word(pp.srange('[4-9]'), exact=1)])])))

HCount <<= pp.Literal('H') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1))

Charge <<= pp.Or([
    pp.Literal('-') + pp.Optional(pp.Or([pp.Literal('-'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)])),
    pp.Literal('+') + pp.Optional(pp.Or([pp.Literal('+'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)]))])

Class <<= pp.Literal(':') + pp.Word(pp.srange('[0-9]'), exact=1)



Isotope <<= pp.Word(pp.srange('[1-9]'), exact=1) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1))

print SMILES.parseString('CCC(C(C)C)C[Br+]CC')
print SMILES.parseString('CC(=NO)C(C)=NO')
print SMILES.parseString('c1ccccc1')
