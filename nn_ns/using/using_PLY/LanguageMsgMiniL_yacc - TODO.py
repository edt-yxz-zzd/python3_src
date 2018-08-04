

from sand import CompileError
# Get the token map from the lexer.  This is required.
from .LanguageMsgMiniL_lex import tokens
from .parse_common import *

# main should be first or using start=...
start = r'MsgGraph'

r'''

MsgMiniL : OpTopStmt*           -- MsgMiniL = MsgMiniL [TopStmt]
OpTopStmt : TOP_STMT_HEAD TopStmt
TopStmt                         
    : SourceMsgsDecl            -- TopStmt  = SourceMsgsDecl [SrcMsg]
    | InterfaceDecl             --          | InterfaceDecl [Importer] Interface [Exporter]
    | DirectOutput              --          | DirectOutput Msg [OutMsg]
    | ImportView                --          | ImportView Importer [ImportStmt]

SourceMsgsDecl : OUTPUT OpOutMsg+ -- two OUTPUT at beginning
InterfaceDecl : Interface OpExporter+ OpImporter*
DirectOutput : Msg OpOutMsg+
ImportView : Importer ImportStmt+
ImportStmt : OpInterface ImplementedByStmt+     -- ImportStmt = ImportStmt Interface [ImplementedByStmt]
ImplementedByStmt : OpExporter OpOutMsg*        -- ImplementedByStmt = ImplementedByStmt Exporter [OutMsg]


OpOutMsg : OUTPUT OutMsg
OpExporter : EXPORTED_BY Exporter
OpImporter : IMPORTED_BY Importer
OpInterface : IMPORT Interface

OutMsg : Msg
Importer : Msg
Exporter : Msg
Msg : MConstructor [Word]           -- Msg = Msg MConstructor [Word]
Interface : IConstructor [Word]     -- Interface = Interface IConstructor [Word]
                                    -- MConstructor = IConstructor = Word = String
MConstructor    -- r"M\S*"
IConstructor    -- r"I\S*"
Word            -- r"[^MI\s]\S*"
OUTPUT          -- '-->'
IMPORT          -- '-<'
EXPORTED_BY     -- '<-'
IMPORTED_BY     -- '>-'
TOP_STMT_HEAD   -- ';'
# comment: "--" "{-" "-}"

'''
