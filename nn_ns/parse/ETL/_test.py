
try:
    from ETL.ToolChain_MyLL1L_of_ETL import toolchain_ETL

    etl = r'''
    qrrwr, ,,'', "afs ", 1 2 3,r' 4 4\'', 
    '''

    ts = toolchain_ETL.tokenize(etl)
    #print(ts)
    r = toolchain_ETL.process_text(etl)
    print(r)


except Exception as err:
    print(err)
    input('error')
    raise
else:
    input('success')
