
e ../../python3_src/seed/recognize/README.txt


[[
@20260521
泛用型:
===
中文标识+支持运算符
view ../../python3_src/seed/recognize/toy/simple_recognizer.py
view ../../python3_src/seed/recognize/toy/simple_recognizer_/test.py
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.test!

===
输入快照+传入解锁器{子部件内部解锁}
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/IRecognizerLLoo.py
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/doctest4IRecognizerLLoo.py
py -m nn_ns.app.doctest_cmd    seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo:__doc__     seed.recognize.recognizer_LLoo__ver2_.doctest4IRecognizerLLoo:__doc__    -ht -ff

===
需求反转:所需接口皆由用户输入提供
view ../../python3_src/seed/recognize/rgnr/example/example4SimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/rgnrs/SimpleRecognizer.py


===
文本:显式文本范围+未步进型失败可容忍+识别器自带大量构造器{允许对象式构造而不只函数式构造}
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py
py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.ITextRecognizer__doctest:__doc__ -ht # -ff -df


===
文本:读词器
view ../../python3_src/seed/recognize/tokenizer_/Tokenizer4Text.py
py -m nn_ns.app.doctest_cmd seed.recognize.tokenizer_.Tokenizer4Text:__doc__ -ht





===
xxx:慢！
输入快照+半途声明步进{迭代器中途返回父部件外部解锁}
view ../../python3_src/seed/recognize/recognizer_LLoo_/IRecognizerLLoo.py
view ../../python3_src/seed/recognize/recognizer_LLoo_/Factory4RecognizerLLoo.py
view ../../python3_src/seed/recognize/recognizer_LLoo_/_test.py
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_._test:__doc__ -ht

为啥很慢:构造bundle4referred_funcs4simplified_grammar4LLoo
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.grammar -x

]]

[[
@20260521
专用型:
===
正则表达式:构造+表达
view ../../python3_src/seed/recognize/regex/regex_utilities.py

===
xml:极简模式
view ../../python3_src/seed/recognize/xml/SimpleParser4XML.py
view ../../python3_src/seed/recognize/xml/Visitor4ParseResult4XML.py
]]
