
try:
    from MKUL.ToolChain_MyLL1L_of_MKUL import toolchain_MKUL




except Exception as err:
    print(err)
    input('error')
    raise
else:
    input('success')
