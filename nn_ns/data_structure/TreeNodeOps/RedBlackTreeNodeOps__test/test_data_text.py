

'''
see: "def - test_data_text.txt"
see:
    test_data_text2iter_test_data.py
'''


__all__ = ['test_data_text']

# test_data_text ::= Case*
# Case ::= '=====' initial_tree_text ActionResult+
# ActionResult ::= '-----' action_text '-----' result_tree_text
test_data_text = '''
=====
()
-----
    root = 0
-----
        (black, 0, (), ())



=====
(black, 1, (), ())
-----
    root.left = 0
-----
        (black, 1, (red, 0, (), ()), ())
-----
    root.right = 2
-----
        (black, 1, (), (red, 2, (), ()))

=====

(black, 3, (), (red, 5, (), ()))
-----
    root.right.left = 4
-----
        (black, 4, (red, 3, (), ()), (red, 5, (), ()))
-----
    root.right.right = 6
-----
        (black, 5, (red, 3, (), ()), (red, 6, (), ()))

=====

(black, 3, (red, 1, (), ()), ())
-----
    root.left.left = 0
-----
        (black, 1, (red, 0, (), ()), (red, 3, (), ()))
-----
    root.left.right = 2
-----
        (black, 2, (red, 1, (), ()), (red, 3, (), ()))

=====

(black, 3, (red, 1, (), ()), (red, 5, (), ()))
-----
    root.left.left = 0
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 5, (), ()))
-----
    root.left.right = 2
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 5, (), ()))
-----
    root.right.left = 4
-----
        (black, 3, (black, 1, (), ()), (black, 5, (red, 4, (), ()), ()))
-----
    root.right.right = 6
-----
        (black, 3, (black, 1, (), ()), (black, 5, (), (red, 6, (), ())))

=====
(black, 1, (black, 0, (), ()),
       (red, 3, (black, 2, (), ()),
                (black, 7, (red, 5, (), ()),
                           (red, 9, (), ()))))
-----
    root.right.right.left.left = 4
-----
        (black, 3, (red, 1, (black, 0, (), ()), (black, 2, (), ())),
                   (red, 7, (black, 5, (red, 4, (), ()), ()),
                            (black, 9, (), ())))




=====

(black, 0, (), (red, 1, (), ()))
-----
    del root.right.left
-----
        (black, 0, (), ())
-----
    del root.right.right
-----
        (black, 0, (), ())



=====

(black, 0, (), (red, 1, (), ()))
-----
    del root.left
-----
        (black, 1, (), ())



=====

(black, 0, (), ())
-----
    del root.left
-----
        ()

-----
    del root.right
-----
        ()



=====

(black, 3, (red, 1, (black, 0, (), ()), (black, 2, (), ())),
           (black, 4, (), ()))
-----
    del root.right.left
-----
        (black, 1, (black, 0, (), ()), (black, 3, (red, 2, (), ()), ()))

-----
    del root.right.right
-----
        (black, 1, (black, 0, (), ()), (black, 3, (red, 2, (), ()), ()))


=====

(black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.left.left
-----
        (black, 1, (), (red, 2, (), ()))
-----
    del root.right.left
-----
        (black, 1, (red, 0, (), ()), ())

-----
    del root.left.right
-----
        (black, 1, (), (red, 2, (), ()))
-----
    del root.right.right
-----
        (black, 1, (red, 0, (), ()), ())




=====

(black, 3, (red, 1, (black, 0, (), ()),
                    (black, 2, (), ())),
           (black, 4, (), ()))
-----
    del root.left.left.left
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 4, (), ()))
-----
    del root.left.right.left
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 4, (), ()))

-----
    del root.left.left.right
-----
        (black, 3, (black, 1, (), (red, 2, (), ())), (black, 4, (), ()))
-----
    del root.left.right.right
-----
        (black, 3, (black, 1, (red, 0, (), ()), ()), (black, 4, (), ()))









=====



(black, 7, (red, 3, (black, 1, (black, 0, (), ()),
                               (black, 2, (), ())),
                    (black, 5, (black, 4, (), ()),
                               (black, 6, (), ()))),
           (black, 9, (black, 8, (), ()),
                      (black, 10, (), ())))
-----
    del root.left.left.left.left
-----
    (black, 7, (black, 3, (black, 1, (),
                                     (red, 2, (), ())),
                          (red, 5, (black, 4, (), ()),
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()),
                          (black, 10, (), ())))
-----
    del root.left.left.right.left
-----
    (black, 7, (black, 3, (black, 1, (red, 0, (), ()),
                                     ()),
                          (red, 5, (black, 4, (), ()),
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()),
                          (black, 10, (), ())))


-----
    del root.left.left.left.right
-----
    (black, 7, (black, 3, (black, 1, (),
                                     (red, 2, (), ())),
                          (red, 5, (black, 4, (), ()),
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()),
                          (black, 10, (), ())))
-----
    del root.left.left.right.right
-----
    (black, 7, (black, 3, (black, 1, (red, 0, (), ()),
                                     ()),
                          (red, 5, (black, 4, (), ()),
                                   (black, 6, (), ()))),
               (black, 9, (black, 8, (), ()),
                          (black, 10, (), ())))







=====





(black, 2, (black, 0, (), (red, 1, (), ())), (black, 3, (), ()))
-----
    del root.right.left
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.right.right
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
=====
(black, 2, (black, 1, (red, 0, (), ()), ()), (black, 3, (), ()))
-----
    del root.right.left
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))
-----
    del root.right.right
-----
        (black, 1, (black, 0, (), ()), (black, 2, (), ()))





=====




(black, 4, (red, 2, (black, 0, (), (red, 1, (), ())),
                    (black, 3, (), ())),
           (black, 5, (), ()))
-----
    del root.left.right.left
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
-----
    del root.left.right.right
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
=====
(black, 4, (red, 2, (black, 1, (red, 0, (), ()), ()), (black, 3, (), ())), (black, 5, (), ()))
-----
    del root.left.right.left
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))
-----
    del root.left.right.right
-----
        (black, 4, (red, 1, (black, 0, (), ()), (black, 2, (), ())), (black, 5, (), ()))


















=====
(black, 2, (black, '2', (red, 4, (), ()), ()), (black, 0, (), ()))
-----
    del root.left.right
-----
    (black, 2, (black, 4, (), ()), (black, 0, (), ()))
=====
(black, 0, (black, 2, (red, 4, (), ()), ()), (black, '0', (), ()))
-----
    del root.right.left
-----
    (black, 2, (black, 4, (), ()), (black, 0, (), ()))
=====
(black, 1, (black, 2, (red, 4, (), ()), ()), (black, 0, (), ()))
-----
    del root.entity
-----
    (black, 2, (black, 4, (), ()), (black, 0, (), ()))
'''


