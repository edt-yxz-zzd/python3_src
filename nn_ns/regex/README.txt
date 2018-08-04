
term definition:
    see: IFAOps.py

string regex pattern format:
    see: Simple.string_regex_pattern.py
    NOTE:
        meta symbol should be escaped:
            (|)?*+{}[^-].<>
            # "," in {} is not a meta symbol
        the only normal char that must be escaped is "\\"
string regex match example:
    see: Simple.example_app.py
    see: Simple.app.py | app/string_regex_app.py


main algorithm:
    # search_leftmost_substring_ex_ex
    # search_leftmost_substring_ex
    # does_accept_ex

    INFAOps__with_astate_dict
        search_leftmost_substring_ex_ex
        _nstate2cnstate_
        complete_astates
    IFAOps
        does_accept
        does_accept_ex
        search_prefix
        search_prefix_ex
        search_leftmost_substring
        search_leftmost_substring_ex
