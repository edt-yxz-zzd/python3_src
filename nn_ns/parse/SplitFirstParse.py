
r''
for example:
S = A B C ; split(S[i:j]) -> A,B,C = S[i:x], S[x:y], S[y:j]
S = A + ; split(S[i:j]) -> [A] = [S[xi:xii]...]

diff with LL: LL predict which or-node child to be used, so, unambiguous.
here we know how to split in a and-rule in only one way,
but may be ambiguous if two alternatives happen to apply to the same piece.


why split first?
because ambiguous are not in a language designed,
we often use some unify struct to avoid ambiguous,
so we can split it into some top-most elements,
that is a struct-awared tree-tokenize.
and then we recognize these tree-tokens.

O(n3) is avoided. a recoginze system or CFG with splitor.


top-most elements:
    statement:
        record-table(csv) / asm language / some command-line script
    group or token:
        math expression / html / C++ (a template maker <> is not a good group)
    head and body:
        section(ini) / XDR
        
for ini, we split to statements which starts with a token <head>.
    then for each statement, we cut into head and body.
    for each body, we cut into statements that is a line.
    for each line, we split use the first '='

for C, we first group up all pairs: {}[]() as a tree node;
    now at top view, a sequence of token or group, split it in statement-style,
    ends with a ';' or a group.
    then try to recognize each statement.


for html, group <|> then <>|</>


LL(1) can derive the table automatically,
can we make the group and state auto too?



'''
