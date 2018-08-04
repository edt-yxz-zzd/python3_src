

class StrictLeftScanIterParserBuilder:
        
    
    def __init__(self, ID2sub_IDs):
        # type(sub_IDs) = list | tuple  # i.e. ALT | CON
        ...
    def genParser(self, main_altIDs, main_conIDs):
        #return a StrictLeftScanIterParser
        ...


class StrictLeftScanIterParser:
    '''only 3+1 rule types: alternative and concatenate and terminal
ALT :: ID |= [ID,...] # using list
CON :: ID -> (ID,...) # using tuple
TER :: ID >> ...     # using ... # denote no children
## non-productive rule may be treated as undefined
## UND :: ID ?? None # unknown, undefined
## undefined ID ==>> as if ID |= []
# since prefer to use [A] than (A,) as copy rule
# ID |= [] <==> [undefined ID]

len of sub_IDs of con rule == 0 or 2 # copy rule should use alt rule
donot clean the rules since user was expected to do that though not required.

wanting/wanted
    wantingID requires wantedIDs
    when wantedID completed, callback wantingIDs
    assume wantingID/wantedID in form:
        (inAltID, begin, end=*)
        (inConID, child_idx, begin, end=*) # means inCon[idx:] # if child_idx == len(children of inConID) ==>> end=begin, always success
        (inTerID, begin, end=*) # when feed a terminal at pos "begin", it determine whether this wanted success

    when wanted is completed?
        completed means no more matches can be found.
        wantedAltID/wantedConID: all its children are completed
        wantedTerID: fed input[begin]

    pre_wanting2wanteds # pre_computed without begin
        # rename to pre_wanting2wanted_without_begin
        wanting2wanteds[inAltID] = sum(wanting2wanteds[child] for child in inAlt)
        wanting2wanteds[inConID] = wanting2wanteds[inCon[0:]]
        # inCon[idx:] is a implicit midConID
        # inConID -> ; or inConID -> inCon[0] inCon[1:];
        wanting2wanteds[inCon[idx:]] = wanting2wanteds[inCon[idx]] if idx != len else {}
        wanting2wanteds[inTerID] = {inTerID}

        wanteds will be configured by begin

        when a wanting be created(i.e. begin is assigned),
            not in wanting2wanteds
            create its wanteds
            wanting2wanteds[wanting] = wanteds

            for wanted in wanteds:
                if wanted not in wanted2wanting2args:
                    wanted2wanting2args[wanted] = {wanting:args}
                    for instance in wanted2instances[wanted]:
                        push_callback(wanting, args, wanted, instance)
                else:
                    wanted2wanting2args[wanted][wanting] = args

    nullConIDs = {...}
    wanted2instances
    wanted2wanting2args # dynamic builded
        when a wanted was created,
            if is a null ConID ==>> push_action(has a new instance)
            elif is a TerID ==>> add to expectedTerIDs
        when a wanted has a new instance(i.e. end is assigned),
            it will call all wantings that depend on it.
            for wanting, args in wanted2wanting2args[wanted].items():
                push_callback(wanting, args, wanted, instance)
        
        
        

'''
    ALT = 'alternative'
    CON = 'concatenate'
    TER = 'terminal'
    UND = 'undefined'
    definition_for_undefined = []

    def outID2inID(self, ID):
        return ID[0]
    def type_of_outID(self, ID):
        inID =  self.outID2inID(ID)
        return self.type_of_inID(inID)
    def type_of_inID(self, ID):
        definition = self.ID2def.get(ID, self.definition_for_undefined)
        if definition is ...:
            return TER
        
        t = type(definition)
        if t is list:
            return ALT
        elif t is tuple:
            return CON
        
        raise logic-error
    
    def isAltID(self, ID):
        t = type(sub_IDs)
        assert t in (list, tuple)
        assert t is list or len(sub_IDs) <= 2
        return t is list

    def makeWantedAltID(self, ID, begin, end):
        # begin and end can be None
        #   None means wild card
        #   for left scan, end usually be set to None
        #       new_ID = (ID, begin, end) to match the given input
        #       new_ID = (ID, begin, *) to search an prefix
        #       new_ID = (ID, *, *) to find a substring
        pass
    
    def __init__(self, ID2def, wanted_IDs, *, offset=0):
        # as if start from offset ... the first fed terminal was at pos 'offset'.
        # input grammar with inID
        # output grammar with outID
        # outAltID = (inAltID, begin, end)
        # outConID = (inConID, begin,)             if len(ID2children(outConID)) == 0
        #          | (inConID, begin, end)                                          1
        #          | (inConID, begin, middle, end)                                  2
        # outTerID = (inTerID, begin, end)
        self._feed_null()
        #(ID, begin, end, , is_head) | (ID, begin, end, None) | (ID, begin, None, None)
    def _feed_termainal(self, terminal):
        ...
    def _feed_null(self):
        ...
    def feed(self, terminal):
        # return +1 if is_end else -1 if is_error else 0 # 0-continue
        if terminal not in self.expected_terminals():
            # error
            return -1
        self._feed_termainal(terminal)
        self._feed_null()
        return +1 if self.is_end() else 0
    def expected_terminals(self):
        ...
    def is_end(self):
        ...
    def is_error(self):
        ...
    def had_prefix_sentences(self):
        ...
    
