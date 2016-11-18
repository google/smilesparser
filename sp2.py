import pyparsing as pp
"""
SMILES   ::= Atom ( Chain | Branch )*
Chain    ::= ( Bond? ( Atom | RingClosure ) )+
Branch   ::= '(' Bond? SMILES+ ')'
Atom     ::= OrganicSymbol
           | AromaticSymbol
           | AtomSpec
           | WILDCARD
Bond     ::= '-'
           | '='
           | '#'
           | '$'
           | ':'
           | '/'
           | '\'
           | '.'
AtomSpec ::= '[' Isotope? ( 'se' | 'as' | AromaticSymbol | ElementSymbol | WILDCARD ) ChiralClass? HCount? Charge? Class? ']'
OrganicSymbol
         ::= 'B' 'r'?
           | 'C' 'l'?
           | 'N'
           | 'O'
           | 'P'
           | 'S'
           | 'F'
           | 'I'
AromaticSymbol
         ::= 'b'
           | 'c'
           | 'n'
           | 'o'
           | 'p'
           | 's'
WILDCARD ::= '*'
ElementSymbol
         ::= [A-Z] [a-z]?
RingClosure
         ::= '%' [1-9] [0-9]
           | [0-9]
ChiralClass
         ::= ( '@' ( '@' | 'TH' [1-2] | 'AL' [1-2] | 'SP' [1-3] | 'TB' ( '1' [0-9]? | '2' '0'? | [3-9] ) | 'OH' ( '1' [0-9]? | '2' [0-9]? | '3' '0'? | [4-9] ) )? )?
Charge   ::= '-' ( '-' | '0' | '1' [0-5]? | [2-9] )?
           | '+' ( '+' | '0' | '1' [0-5]? | [2-9] )?
HCount   ::= 'H' [0-9]?
Class    ::= ':' [0-9]+
Isotope  ::= [1-9] [0-9]? [0-9]?
"""

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
Chain <<= (pp.Optional(Bond) + pp.Or([Atom, RingClosure]))
Branch <<= pp.Literal('(') + pp.Optional(Bond) + pp.OneOrMore(SMILES) + pp.Literal(')')
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
AtomSpec <<= pp.Literal('[') + \
           pp.Optional(Isotope) + \
           pp.Or([pp.Literal('se'), pp.Literal('as'), AromaticSymbol, ElementSymbol, WILDCARD]) + \
           pp.Optional(ChiralClass) + \
           pp.Optional(HCount) + \
           pp.Optional(Charge) + \
           pp.Optional(Class) + \
           pp.Literal(']')
WILDCARD <<= '*'
ElementSymbol <<= pp.Word(pp.srange('[A-Z_]'), exact=1) + pp.Optional(pp.Word(pp.srange('[a-z]')))
RingClosure <<= pp.Or([pp.Literal('%') + pp.Word(pp.srange('[1-9]'), exact=1) + pp.Word(pp.srange('[0-9]'), exact=1), pp.Word(pp.srange('[0-9]'), exact=1)])
ChiralClass <<= pp.Optional(
    pp.Literal('@')) 

    
#     # pp.Optional(pp.Or(['@',
#     #                    'TH' + pp.Word(pp.srange('[1-2]'), exact=1),
#     #                    'AL' + pp.Word(pp.srange('[1-2]'), exact=1),
#     #                    'SP' + pp.Word(pp.srange('[1-3]'), exact=1),
#     #                    'TB' + pp.Or([ pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-9]'))),
#     #                                   pp.Literal('2') + pp.Optional(pp.Literal('0')),
#     #                                   pp.Word(pp.srange('[3-9]'), exact=1)]),
#     #                    'OH' + pp.Or([ pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)),
#     #                                   pp.Literal('2') + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)),
#     #                                   pp.Literal('3') + pp.Optional(pp.Literal('0')),
#     #                                   pp.Word(pp.srange('[4-9]'), exact=1)])])))
HCount <<= pp.Literal('H') + pp.Optional(pp.Word(pp.srange('[0-9]')))

Charge <<= pp.Or([
    pp.Literal('-') + pp.Optional(pp.Or([pp.Literal('-'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)])),
    pp.Literal('+') + pp.Optional(pp.Or([pp.Literal('+'), pp.Literal('0'), pp.Literal('1') + pp.Optional(pp.Word(pp.srange('[0-5]'), exact=1)), pp.Word(pp.srange('[2-9]'), exact=1)]))])

Class <<= pp.Literal(':') + pp.Word(pp.srange('[0-9]'), exact=1)



Isotope <<= pp.Word(pp.srange('[1-9]'), exact=1) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1)) + pp.Optional(pp.Word(pp.srange('[0-9]'), exact=1))


print Atom.parseString('*')
print Bond.parseString('-')
print AtomSpec.parseString("[Br]")
print AtomSpec.parseString("[Br+]")
print OrganicSymbol.parseString('B')
print OrganicSymbol.parseString('Br')
print AromaticSymbol.parseString('n')
print ElementSymbol.parseString('Aa')
#print RingClosure.parseString('xxx')
print ChiralClass.parseString("@")
print HCount.parseString('H3')
print Charge.parseString('-')
print Charge.parseString('+')
print Class.parseString(':0')
print Isotope.parseString('111')
