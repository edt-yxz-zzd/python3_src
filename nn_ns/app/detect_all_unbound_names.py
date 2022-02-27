
'''
unbounds.bat/
    @py -m nn_ns.app.detect_all_unbound_names %*
'''
from seed.pkg_tools.detect_all_unbound_names import main

if __name__ == "__main__":
    main()


