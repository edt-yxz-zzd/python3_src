
'''
<<Machine Learning>>

lattic:
    more-general-than: <

FIND-S

assume one class occupy one corner of the cubic space (how to generalize)
that is the class space is a direct-product of subsets of each attributes

trains:
class space = attr2values
sample = (attr2value, class_id)
if sample.attr2value[attr]=value
then class[sample.class_id][attr].add(value)

classify:
instance = attr2value
for each class:
    score = sum(instance[attr] in class[attr] for each attr)
    if score == len(attrs):
        SHOULD_BE_BY_ASSUME[instance].add(class)
    else:
        MAY_BE[instance][score].add(class)
if len(SHOULD_BE_BY_ASSUME[instance]) == 1:
    DONE
elif == 0:
    ALL_MAY_BE
    we may find out classes with highest score
else > 1:
    COLLISION
    assume failed

'''

from copy import deepcopy


SHOULD_BE_BY_ASSUME = 'SHOULD_BE_BY_ASSUME'
ALL_MAY_BE = 'ALL_MAY_BE'
COLLISION = 'COLLISION'

class DiscreteCubicCornerClassifier:
    def __init__(self, attrs, classes, examples=()):
        self.attrs = tuple(attrs)
        self.classes = tuple(classes)
        self.attr2idx = dict((attr, i) for i, attr in enumerate(self.attrs))
        assert len(self.attr2idx) == len(self.attrs)
        #attr2values = {attr:set() for attr in self.attrs}
        attr_idx2values = [set() for _ in self.attrs]
        self.class2attr_idx2values = {class_id:deepcopy(attr_idx2values) for class_id in classes}

        self.update(examples)
        
    def update(self, examples):
        for attr2value, class_id in examples:
            assert len(attr2value) == len(self.attrs)
            attr_idx2values = self.class2attr_idx2values[class_id]
            for attr, idx in self.attr2idx.items():
                attr_idx2values[idx].add(attr2value[attr])
        return
    
    def classify(self, attr2value):
        class2score = {}
        for class_id, attr_idx2values in self.class2attr_idx2values.items():
            score = sum(attr2value[attr] in attr_idx2values[idx]
                        for attr, idx in self.attr2idx.items())
            class2score[class_id] = score

        highest = max(class2score.values())
        classes = [class_id for class_id, score in class2score.items()
                   if score == highest]
        if highest == len(self.attrs):
            if len(classes) == 1:
                return SHOULD_BE_BY_ASSUME, class2score, classes
            assert len(classes) > 1
            return COLLISION, class2score, classes
        else:
            return ALL_MAY_BE, class2score, classes
        pass


def test_DiscreteCubicCornerClassifier():
    T = DiscreteCubicCornerClassifier
    
    data = [
        [range(4), # attrs
         (False, True), # classes
         [([0,1,1,0], False), ([1,0,0,1], False),
          ([2,1,1,0], True), ([1,2,0,2], True)], # examples
         [([0,0,0,0], False), ([1,1,1,1], False),
          ([2,2,1,0], True), ([1,2,1,0], True)], # testdata
         ],
    ]
    
    for attrs, classes, examples, testdata in data:
        t = T(attrs, classes, examples)
        for attr2value, class_id in testdata:
            case, class2score, _classes = t.classify(attr2value)
            assert len(_classes) == 1
            _class, = _classes
            assert _class == class_id
    return

test_DiscreteCubicCornerClassifier()




































