try:
    raise ValueError()
except:
    try:
        raise # success !!
    except:
        raise
    
