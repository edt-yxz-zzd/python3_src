r'''[[[

py -m nn_ns.app.grep_between -s -u -ptn "'[^']*'" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py

e ../../python3_src/bash_script/app/grep_between
grep_between -s -u -ptn "'[^']*'" -begin '#begin-grammar4IRecognizerLLoo' -end '#end-grammar4IRecognizerLLoo' -i ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/grammar4IRecognizerLLoo.py

#]]]'''#'''
if __name__ == "__main__":
    from nn_ns.txt.grep_between import main
    main()

