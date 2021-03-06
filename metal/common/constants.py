
# Types for logic spec
OR_TYPE = 0
AND_TYPE = 1
XOR_TYPE = 2
NOT_TYPE = 3
VAR_TYPE = 4

NUM_OF_TYPE = 5

OP_NAMES = ['or', 'and', 'xor', 'not']
OP_NAME2IND = {'or':0, 'and':1, 'xor':2, 'not':3}

TYPES_IN_SPEC = [OR_TYPE, AND_TYPE, XOR_TYPE, NOT_TYPE, VAR_TYPE]

# Types for grammar graph
OR_DERIVE_TYPE = 0
AND_DERIVE_TYPE = 2
XOR_DERIVE_TYPE = 4
NOT_DERIVE_TYPE = 6

OP_NAME2TYPE= {"or":OR_DERIVE_TYPE, "and":AND_DERIVE_TYPE, "xor":XOR_DERIVE_TYPE, "not":NOT_DERIVE_TYPE}

T_DERIVE_TYPE = 8
NT_DERIVE_TYPE = 10

OR_GLOBAL_LINK = 12
AND_GLOBAL_LINK = 14
XOR_GLOBAL_LINK = 16
NOT_GLOBAL_LINK = 18
OP_GLOBAL_N2T = {"or":OR_GLOBAL_LINK, "and":AND_GLOBAL_LINK, "xor":XOR_GLOBAL_LINK, "not":NOT_GLOBAL_LINK}

SPEC_COVER_TYPE = 20 # used for spec embedding

NUM_GRAMMAR_EDGE_TYPES = 22 # 10 edge types x 2 directions

TYPE2NAME = {
    # OR_DERIVE_TYPE : "OR_DERIVE_TYPE(F)",
    # OR_DERIVE_TYPE+1 : "OR_DERIVE_TYPE(B)",
    # AND_DERIVE_TYPE : "AND_DERIVE_TYPE(F)",
    # AND_DERIVE_TYPE+1 : "AND_DERIVE_TYPE(B)",
    # XOR_DERIVE_TYPE : "XOR_DERIVE_TYPE(F)",
    # XOR_DERIVE_TYPE+1 : "XOR_DERIVE_TYPE(B)",
    # NOT_DERIVE_TYPE : "NOT_DERIVE_TYPE(F)",
    # NOT_DERIVE_TYPE+1 : "NOT_DERIVE_TYPE(B)",
    # T_DERIVE_TYPE : "T_DERIVE_TYPE(F)",
    # T_DERIVE_TYPE+1 : "T_DERIVE_TYPE(B)",
    # NT_DERIVE_TYPE : "NT_DERIVE_TYPE(F)",
    # NT_DERIVE_TYPE+1 : "NT_DERIVE_TYPE(B)",
    # OR_GLOBAL_LINK : "OR_GLOBAL_LINK(F)",
    # OR_GLOBAL_LINK+1 : "OR_GLOBAL_LINK(B)",
    # XOR_GLOBAL_LINK : "XOR_GLOBAL_LINK(F)",
    # XOR_GLOBAL_LINK+1 : "XOR_GLOBAL_LINK(B)",
    # AND_GLOBAL_LINK : "AND_GLOBAL_LINK(F)",
    # AND_GLOBAL_LINK+1 : "AND_GLOBAL_LINK(B)",
    # NOT_GLOBAL_LINK : "NOT_GLOBAL_LINK(F)",
    # NOT_GLOBAL_LINK+1 : "NOT_GLOBAL_LINK(B)",    

    OR_DERIVE_TYPE : "OR_DERIVE(F)",
    OR_DERIVE_TYPE+1 : "OR_DERIVE(B)",
    AND_DERIVE_TYPE : "AND_DERIVE(F)",
    AND_DERIVE_TYPE+1 : "AND_DERIVE(B)",
    XOR_DERIVE_TYPE : "XOR_DERIVE(F)",
    XOR_DERIVE_TYPE+1 : "XOR_DERIVE(B)",
    NOT_DERIVE_TYPE : "NOT_DERIVE(F)",
    NOT_DERIVE_TYPE+1 : "NOT_DERIVE(B)",
    T_DERIVE_TYPE : "T_DERIVE(F)",
    T_DERIVE_TYPE+1 : "T_DERIVE(B)",
    NT_DERIVE_TYPE : "NT_DERIVE(F)",
    NT_DERIVE_TYPE+1 : "NT_DERIVE(B)",
    OR_GLOBAL_LINK : "OR_GLOBAL(F)",
    OR_GLOBAL_LINK+1 : "OR_GLOBAL(B)",
    XOR_GLOBAL_LINK : "XOR_GLOBAL(F)",
    XOR_GLOBAL_LINK+1 : "XOR_GLOBAL(B)",
    AND_GLOBAL_LINK : "AND_GLOBAL(F)",
    AND_GLOBAL_LINK+1 : "AND_GLOBAL(B)",
    NOT_GLOBAL_LINK : "NOT_GLOBAL(F)",
    NOT_GLOBAL_LINK+1 : "NOT_GLOBAL(B)",    
    SPEC_COVER_TYPE : "SPEC_COVER_TYPE(F)",
    SPEC_COVER_TYPE+1 : "SPEC_COVER_TYPE(B)",

}

# Types for program graph 
AST_EDGE_TYPE = 0
CONTROL_EDGE_TYPE = 2
VAR_LINK_TYPE = 4

NUM_EDGE_TYPES = 6 # 3 edge types x 2 directions

# kinds of counterexamples
CE_KEYS = ("T", "F")
