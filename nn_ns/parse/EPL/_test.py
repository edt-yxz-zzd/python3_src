
try:
    from EPL.ToolChain_MyLL1L_of_EPL import toolchain_EPL
    from EPL.EPL2ETL import EPL2ETL
    import EPL.pretty_format_EPL

    EPL = r'''
    [main
        []
        [item1]
        []item2_tag
        [item3]item3_tag

        [[]]
        [[]tag]
        [[]tag[]]
        [[]tag[]tag]
    ]
    '''

    ts = toolchain_EPL.tokenize(EPL)
    #print(ts)
    r = toolchain_EPL.process_text(EPL)
    print(r)
except Exception as err:
    print(err)
    input('error')
    raise

else:
    input('success')

