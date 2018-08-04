

'''
internal use only
    for public class:
        see LeftScanIterParser 

NOTE:
    ID to ConRule with n children will be associated with (n+1) ConChildID's
        the last one points to a null rule, others to copy rule
    
    ConChildID will not present in FlatOutputGrammar

super_id = InputID(output_id)



bug:
    once I call .calc__child_wanted2prev_instances() before .feeds()!!!!
    
'''

__all__ = '''

LParser

WantingToWantedEvent
    WantedIDCreatedEvent
WantedInstanceCreatedEvent
    CompletedWantedIDFoundEvent
        DeadWantedIDFoundEvent
    WantingToWantedInstanceEvent


'''.split()

from .ParserCommon import ParseError, IterParserBase
from .IDTypes_and_RuleTypes import * # id2rule_fmap rule_fmap ...
from sand.big.MessageManager import Event, MessageManager
from sand.types.Newtype import Newtype, NewtypeWithMultiArgs
from collections import defaultdict
from types import MappingProxyType



VERBOSE = False
def xprint(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)


class WantingToWantedEvent(Event):
    def __init__(self, wanting_id, wanted_id):
        assert isinstance(wanting_id, WantedID)
        assert isinstance(wanted_id, WantedID)
        self.wanting_id = wanting_id
        self.wanted_id = wanted_id
class WantedIDCreatedEvent(Event):
    def __init__(self, wanted_id):
        assert isinstance(wanted_id, WantedID)
        self.wanted_id = wanted_id


class WantedInstanceCreatedEvent(Event):
    def __init__(self, output_id):
        assert isinstance(output_id, OutputID)
        self.wanted_instance = output_id
class CompletedWantedIDFoundEvent(Event):
    def __init__(self, wanted_id):
        assert isinstance(wanted_id, WantedID)
        self.wanted_id = wanted_id
class DeadWantedIDFoundEvent(Event):
    def __init__(self, wanted_id):
        assert isinstance(wanted_id, WantedID)
        self.wanted_id = wanted_id

class WantingToWantedInstanceEvent(Event):
    def __init__(self, wanting_id, wanted_instance):
        assert isinstance(wanting_id, WantedID)
        assert isinstance(wanted_instance, OutputID)
        self.wanting_id = wanting_id
        self.wanted_instance = wanted_instance
















class LParser(IterParserBase, MessageManager):
    'L - left - scan terminals from left to right'
    def __init__(self, input_id2rule, main_id, *,
                 begin_pos = 0,
                 undefined_IDs_allowed=False,
                 to_clean_id2rule=True):
        for input_id, rule in input_id2rule.items():
            assert isinstance(input_id, InputID)
            assert isinstance(rule, Rule)
            assert type(rule) in (AltRule, ConRule, Terminal)

        assert isinstance(main_id, InputID)

        self.input_id2rule = dict(input_id2rule)
        self.main_id = main_id
        self.pos = self.begin_pos = begin_pos

        if not undefined_IDs_allowed:
            undefineds = collect_undefined_IDs(self.input_id2rule, self.main_id)
            if undefineds:
                raise ValueError('id2rule contains undefined IDs')
        if to_clean_id2rule:
            inplace_clean(self.input_id2rule, self.main_id)
##        try:
##            assert self.input_id2rule == input_id2rule
##        except:
##            print(self.input_id2rule)
##            raise
        
        main_ex = OrgID(main_id)
        main_wanted = WantedID(main_ex, begin_pos)
        self.main_wanted = main_wanted

        
        self.wanted2wantings = {}
        self.wanting2wanteds = {}
        # completed : all instances have been found
        #    if not instances then fail/dead
        # lived : incompleted or completed with nonempty instances
        self.completed_wanted_set = set()
        self.created_wanted_instances = set()
        self.wanted2wanted_instances = {}
        self.wanting2wanted_instances = {}
        self.shifted_pos2expected_terminals = [set()] # begin_pos -> 0 as list idx
        # before and after feed(), holds:
        #   len(shifted_pos2expected_terminals) == self.shift_pos(self.pos+1)


        # cache for cachedcalc__child_wanted2prev_instances__ge
        self.__pos2child_wanted2prev_instances = {}

        super().__init__()
        self.__wanted_main()

    def shift_pos(self, pos=None):
        if pos is None:
            pos = self.pos
        shifted_pos = pos - self.begin_pos
        return shifted_pos

    def expects_at(self, pos=None):
        shifted_pos = self.shift_pos(pos)
        if shifted_pos < 0:
            raise ValueError('pos < self.begin_pos')
        return self.shifted_pos2expected_terminals[shifted_pos]
            
    def feed(self, terminal):
        T = terminal
        begin = self.pos
        end = begin+1
        
        if not self.is_terminal(T):
            raise TypeError('not self.is_terminal(T)')
        wtT = WantedID(OrgID(T), begin)
        wantings = self.wanted2wantings.get(wtT, None)
        if wantings is None:
            raise ParseError('expects: {}'.format(
                self.expects_at(begin)))

        shifted_pos2expected_terminals = self.shifted_pos2expected_terminals
        assert len(shifted_pos2expected_terminals) == self.shift_pos(end)
        shifted_pos2expected_terminals.append(set()) # to collect terminals


        # make a instance for the input terminal
        outT = OutputID(wtT, end)
        self.wanted_instance_created(outT)
        self.process_messages()
        
        self.pos = end
        return


















  # even create and handle
        
    def wanting_wanted_pair_created(self, wanting, wanted):
        wanted2wantings = self.wanted2wantings
        self.wanted_id_created(wanting)
        self.wanted_id_created(wanted)
        if wanting not in wanted2wantings[wanted]:
            wanted2wantings[wanted].add(wanting)
            self.wanting2wanteds[wanting].add(wanted)
            self.throw_message(WantingToWantedEvent(wanting, wanted))
    def on_WantingToWantedEvent(self, event):
        wanting = event.wanting_id
        wanted = event.wanted_id
        xprint('>>>> {} -> {}'.format(wanting, wanted))
        
        for instance in self.wanted2wanted_instances[wanted]:
            self.wanting_wanted_instance_pair_created(wanting, instance)







    def __wanted_main(self):
        # no wanting
        wanted = self.main_wanted
        assert wanted not in self.wanted2wantings
        self.wanted_id_created(wanted)

        self.process_messages()
        
    def wanted_id_created(self, wanted):
        wanted2wantings = self.wanted2wantings
        if wanted not in wanted2wantings:
            wanted2wantings[wanted] = set()
            self.wanted2wanted_instances[wanted] = set()

            new_wanting = wanted
            #self.wanting_created(new_wanting)
            self.wanting2wanted_instances[new_wanting] = set()
            self.wanting2wanteds[new_wanting] = set()
            self.throw_message(WantedIDCreatedEvent(wanted))

    def on_WantedIDCreatedEvent(self, event):
        wanted = event.wanted_id
        begin = wanted.begin
        ex_id = wanted.ex_id
        input_id = ex_id.input_id
        if self.is_WantedID_to_DeadRule(wanted):
            self.dead_wanted_id_found(wanted)
            pass
        elif self.is_WantedID_to_AltRule(wanted):
            # OrgID alt_id | ConChildID {..not end..}
            alt_ex_id = ex_id
            new_wanting = wanted
            for alt in self.ex_id2input_rule(alt_ex_id).alts:
                ex_alt = OrgID(alt)
                new_wanted = WantedID(ex_alt, begin)
                self.wanting_wanted_pair_created(new_wanting, new_wanted)
        elif self.is_WantedID_to_ConRule(wanted):
            # OrgID con_id | ConChildID {..end..}
            if self.is_WantedID_to_ConChildRule(wanted):
                # ConChildID {..end..}
                end = begin
                out = OutputID(wanted, end)
                self.wanted_instance_created(out)
            else:
                # OrgID con_id
                new_wanting = wanted
                con_id = input_id
                ex_fst = ConChildID(con_id, 0) # may be null child
                
                new_wanted = WantedID(ex_fst, begin)
                self.wanting_wanted_pair_created(new_wanting, new_wanted)


        elif self.is_WantedID_to_Terminal(wanted):
            T = terminal = input_id
            expects = self.expects_at(begin)
            expects.add(T)
            pass
        else:
            raise logic-error








    
    def wanted_instance_created(self, wanted_instance):
        assert isinstance(wanted_instance, OutputID)
        if wanted_instance in self.created_wanted_instances:
            return

        wanted = wanted_instance.wanted_id
        self.created_wanted_instances.add(wanted_instance)
        self.wanted2wanted_instances[wanted].add(wanted_instance)
        self.throw_message(WantedInstanceCreatedEvent(wanted_instance))
        
    def on_WantedInstanceCreatedEvent(self, event):
        'wanted_instance is output_id'
        wanted_instance = event.wanted_instance
        assert isinstance(wanted_instance, OutputID)
        wanted = wanted_instance.wanted_id
        begin = wanted.begin

        if self.is_WantedID_to_Terminal(wanted):
            expects = self.expects_at(begin)
            T = terminal = wanted.ex_id.input_id
            
            # other terminal marks dead at curr pos
            for dead_T in expects - {T}:
                deat_wtT = WantedID(OrgID(dead_T), begin)
                self.dead_wanted_id_found(deat_wtT)
            self.completed_wanted_id_found(wanted)
            assert self.calc__is_completed_wanted(wanted)
            assert self.wanted2wanted_instances[wanted]
            assert self.calc__is_lived_wanted(wanted)
            
        wantings = self.wanted2wantings[wanted_instance.wanted_id]
        for wanting in wantings:
            self.wanting_wanted_instance_pair_created(wanting, wanted_instance)








    def completed_wanted_id_found(self, wanted):
        if wanted not in self.completed_wanted_set:
            self.completed_wanted_set.add(wanted)
            self.throw_message(CompletedWantedIDFoundEvent(wanted))
    def on_CompletedWantedIDFoundEvent(self, event):
        wanted = event.wanted_id
        wantings = self.wanted2wantings
        if not self.wanted2wanted_instances[wanted]:
            self.dead_wanted_id_found(wanted)
            
        calc__is_completed = self.calc__is_completed_wanted
        for wanting in wantings:
            calc__is_completed(wanting) # may create completed event






        
    def dead_wanted_id_found(self, dead_wanted):
        if not self.is_in_known_dead_wanted_set(dead_wanted):
            self.add_to_known_dead_wanted_set(dead_wanted)
            self.throw_message(DeadWantedIDFoundEvent(dead_wanted))
        
    def on_DeadWantedIDFoundEvent(self, event):
        return
        dead_wanted = event.wanted_id
        wantings = self.wanted2wantings
        is_known_dead = self.is_in_known_dead_wanted_set
        is_lived = calc__is_lived_wanted
        for wanting in wantings:
            if not is_known_dead(wanting) and \
               not is_lived(wanting):
                self.dead_wanted_id_found(wanting)
        #raise NotImplementedError


    def is_in_known_dead_wanted_set(self, wanted):
        return (wanted in self.completed_wanted_set and
                not self.wanted2wanted_instances[wanted])
    def add_to_known_dead_wanted_set(self, wanted):
        if self.wanted2wanted_instances[wanted]:
            raise ValueError('not a dead wanted: has nonempty instances')
        #self.completed_wanted_set.add(wanted)
        self.completed_wanted_id_found(wanted)







    def wanting_wanted_instance_pair_created(self, wanting, wanted_instance):
        if wanted_instance not in self.wanting2wanted_instances[wanting]:
            self.wanting2wanted_instances[wanting].add(wanted_instance)
            self.throw_message(WantingToWantedInstanceEvent(wanting, wanted_instance))
            
    def on_WantingToWantedInstanceEvent(self, event):
        wanting = event.wanting_id
        wanted_instance = event.wanted_instance
        xprint('<<<< {} -> {}'.format(wanting, wanted_instance))
        self.handle_wanting_wanted_instance_pair(wanting, wanted_instance)

    def handle_wanting_wanted_instance_pair(self, wanting, wanted_instance):
        end = wanted_instance.end
        if self.is_WantedID_to_AltRule(wanting):
            # OrgID alt_id | ConChildID {..not end..}
            out = OutputID(wanting, end)
            self.wanted_instance_created(out)
        elif self.is_WantedID_to_ConRule(wanting):
            # OrgID con_id | ConChildID {..end..}
            if self.is_WantedID_to_ConChildRule(wanting):
                # ConChildID {..end..}
                raise logic-error

            # OrgID con_id
            curr_child_id = wanted_instance.wanted_id.ex_id
            curr_child_end = end

            is_null_child = self.is_null_child_id(curr_child_id)
            if is_null_child:
                # new parent instance
                out = OutputID(wanting, end)
                self.wanted_instance_created(out)
                return
            
            # wanted next child
            next_child_id = self.next_child_id(curr_child_id)
            next_child_begin = curr_child_end
            wanted_next_child_id = WantedID(next_child_id, next_child_begin)
            # may be wanted_curr_child_id = parent_id[end:end]

            #self.wanted_id_created(wanted_next_child_id)
            self.wanting_wanted_pair_created(wanting, wanted_next_child_id)
                
        else:
            raise logic-error



























  ################# calc ################



    def calc__expected_terminals(self, pos=None):
        if pos is None:
            pos = self.pos
        if not self.begin_pos <= pos <= self.pos:
            raise ValueError('not self.begin_pos <= pos <= self.pos')

        s = set()
        for wanted in self.wanted2wantings:
            if self.is_WantedID_to_Terminal(wanted):
                if wanted.begin == pos:
                    T = wanted.ex_id.input_id
                    s.add(T)
        assert s == self.expects_at(pos)
        return s
    
            

    def calc__is_lived_wanted(self, wanted):
        return not self.calc__is_completed_wanted(wanted) or \
               bool(self.wanted2wanted_instances[wanted])
    def calc__is_completed_wanted(self, wanted):
        if wanted not in self.wanted2wantings:
            raise ValueError('wanted not in self.wanted2wantings')
        return self.__is_completed_wanted__entry(wanted, set())
    
    def __is_completed_wanted__entry(self, wanted, assume_completeds):
        if wanted in self.completed_wanted_set:
            return True

        if wanted in assume_completeds:
            # to avoid infinite recur
            return True

        assume_completeds.add(wanted)
        completed = self.__is_completed_wanted__impl(wanted, assume_completeds)
        assume_completeds.remove(wanted)
        if completed:
            self.completed_wanted_id_found(wanted)
        return completed
    def __is_completed_wanted__impl(self, wanted, assume_completeds):
        # FIXME: dead loop may occur

        is_completed = lambda wanted:\
                       self.__is_completed_wanted__entry(wanted, assume_completeds)
        if self.is_WantedID_to_DeadRule(wanted):
            # undefined or OrgID null_alt_id
            return True

        new_wanting = wanted
        new_wanteds = self.wanting2wanteds[new_wanting]
        if self.is_WantedID_to_AltRule(wanted):
            # OrgID alt_id | ConChildID {..not end..}
            return all(map(is_completed, new_wanteds))
        elif self.is_WantedID_to_ConRule(wanted):
            # OrgID con_id | ConChildID {..end..}
            return all(map(is_completed, new_wanteds))
        elif self.is_WantedID_to_Terminal(wanted):
            assert wanted not in self.completed_wanted_set
            return False
        else:
            raise logic-error

            








  ################### output grammar ########################

    def flatten_super_id(self, super_id):
        unbox = super_id.unbox()
        if isinstance(unbox, ConToAltID):
            return unbox

        assert isinstance(unbox, OutputID)
        i = instance = unbox
        wanted = i.wanted_id
        ex = wanted.ex_id
        
        end = i.end
        begin = wanted.begin
        assert isinstance(ex, OrgID) # not ConChildID
        input_id = ex.input_id

        return PlacedID(input_id, begin, end)
    def flatten_super_rule(self, super_rule, flatten_super_id=None):
        if flatten_super_id is None:
            flatten_super_id = self.flatten_super_id
        return rule_map(flatten_super_id, super_rule)
    
        if isinstance(super_rule, AltRule):
            return AltRule(map(flatten_super_id, super_rule.alts))
        elif isinstance(super_rule, ConRule):
            return ConRule(map(flatten_super_id, super_rule.children))
        elif isinstance(super_rule, Terminal):
            return super_rule
        else:
            raise logic-error
        
        
    def flatten_output_grammar(self, super_id2super_rule, flatten_super_id=None):
        if flatten_super_id is None:
            flatten_super_id = self.flatten_super_id
        return id2rule_fmap(flatten_super_id, super_id2super_rule)

    

    def make_main_output_id(self, pos=None):
        if pos is None:
            pos = self.pos

        main_end = pos
        main_wanted = self.main_wanted
        main_out = OutputID(main_wanted, main_end)
        return main_out

    def make_main_super_id(self, pos=None):
        main_out = self.make_main_output_id(pos)
        main_super = InputID(main_out)
        return main_super
    def build_output_grammar_end_at(self, pos=None):
        main_super_id = self.make_main_super_id(pos)
        child_wanted2prev_instances = self.cachedcalc__child_wanted2prev_instances__ge(pos)
        super_id2super_rule = self.build_output_grammar_rooted_by(main_super_id, child_wanted2prev_instances)
        return super_id2super_rule
            
    def build_output_grammar_rooted_by(self, main_super_id, child_wanted2prev_instances):
        assert isinstance(main_super_id, InputID)
        output_id = main_super_id.unbox()
        wanted = output_id.wanted_id
        instances = self.wanted2wanted_instances.get(wanted, ())
        if output_id not in instances:
            return {}

        def collect(self, super_id, D):
            instance = super_id.unbox()
            new_wanting = wanted = instance.wanted_id
            if self.is_WantedID_to_AltRule(wanted):
                # OrgID alt_id | ConChildID {..not end..}
                alts = self.alt_instance2all_instance_alts(instance)
        
                super_rule = AltRule(map(InputID, alts))
                maybe_news = set(super_rule.alts)
                G = {super_id: super_rule}
                return maybe_news, G
                
            elif self.is_WantedID_to_ConRule(wanted):
                # OrgID con_id | ConChildID {..end..}
                alts = self.con_instance2all_children_instances_alts(instance, D)
                alts = tuple(alts)
                
                f = self.all_children_instances_alt2src_copy_instances
                
                super_alts = tuple(map(self.all_children_instances_alt2super_id, alts))
                direct_alts = tuple(map(f, alts))
                
##                print('super_id = ', super_id)
##                print('super_alts = ', super_alts)

                
                
                G = {super_id: ConRule(map(InputID, direct_instances_alt))
                     for super_id, direct_instances_alt in zip(super_alts, direct_alts)}
                assert super_id not in G
                super_rule = AltRule(G.keys())
                G[super_id] = super_rule


                maybe_news = set()
                for direct_instances_alt in direct_alts:
                    maybe_news.update(direct_instances_alt)
                maybe_news = set(map(InputID, maybe_news))
                return maybe_news, G

            elif self.is_WantedID_to_Terminal(wanted):
                super_rule = ter_rule
                G = {super_id: super_rule}
                maybe_news = set()
                return maybe_news, G
                
            else:
                raise logic-error
            
            
        #main_super_id = InputID(output_id)
        super_id2super_rule = {}
        to_process = [main_super_id]
        known_super_ids = set(to_process) # only from wanted, not included AllConChildrenInstancesID
        D = child_wanted2prev_instances


        while to_process:
            super_id = to_process.pop()
            assert super_id not in super_id2super_rule
            
            maybe_news, G = collect(self, super_id, D)


            try:
                # may be bug:??
                assert set(G).isdisjoint(set(super_id2super_rule))
                # will fire if "A -> Null A; A -> ; Null -> ;"
                pass
            except:
                print(set(G) & (set(super_id2super_rule)))
                print(set(G))
                print(super_id)
                raise
            super_id2super_rule.update(G)
            news = maybe_news - known_super_ids
            known_super_ids |= news
            to_process.extend(news)

        L = len(super_id2super_rule)
        inplace_clean(super_id2super_rule, main_super_id)
        assert len(super_id2super_rule) == L
        return super_id2super_rule
        

    def alt_instance2all_instance_alts(self, alt_instance):
        new_wanting = wanted = alt_instance.wanted_id
        return (new_instance
                for new_instance in self.wanting2wanted_instances[new_wanting]
                if new_instance.end == alt_instance.end)

    def con_instance2all_children_instances_alts(self, con_instance, child_wanted2prev_instances):
        assert self.is_WantedID_to_ConRule(con_instance.wanted_id)
        assert not self.is_WantedID_to_ConChildRule(con_instance.wanted_id)
        
        null_child_instance = self.parent_instance2null_child_instance(con_instance)
        instances = [null_child_instance] # stack; child from right to left
        prev_instancess = []
        # from the end may not lead to same begin
        # but from the begin may not reach a end or same end
        begin = con_instance.wanted_id.begin 
        while instances:
            if len(instances) == len(prev_instancess) + 1:
                i = instances[-1]
                prev_instances = child_wanted2prev_instances.get(i.wanted_id, None)
                if prev_instances is not None:
                    prev_instancess.append(iter(prev_instances))
                    continue
                else:
                    try:
                        assert i.wanted_id.ex_id.is_first_child()
                    except:
                        print(i)
                        raise
                    
                    # basic case
                    if instances[-1].wanted_id.begin == begin:
                        # bug: once I do not add this condition
                        yield tuple(reversed(instances))
                    instances.pop()
                    continue

            assert len(instances) == len(prev_instancess)
            for prev_i in prev_instancess[-1]:
                instances.append(prev_i)
                break
            else:
                # iter over; return
                instances.pop()
                prev_instancess.pop()
                
    def all_children_instances_alt2super_id(self, all_children_instances_alt):
        assert all_children_instances_alt # at least the null child
        fst_child_wanted = all_children_instances_alt[0].wanted_id
        parent_input = fst_child_wanted.ex_id.input_id
        begins = (i.wanted_id.begin for i in all_children_instances_alt)
        ID = AllConChildrenInstancesID(parent_input, begins)
        return InputID(ID) # to super_id
        parent_begin = fst_child_wanted.begin
        parent_wanted = WantedID(OrgID(parent_input), parent_begin)

    def nonnull_child_instance2src_copy_instance(self, nonnull_child_instance):
        i = nonnull_child_instance
        wanted = i.wanted_id
        # not null ==>> CopyRule
        src_input_id, = self.wanted2input_rule(wanted).alts
        src_wanted = WantedID(OrgID(src_input_id), wanted.begin)
        src_instance = OutputID(src_wanted, i.end)
        return src_instance
    def all_children_instances_alt2src_copy_instances(self, all_children_instances_alt):
        assert all_children_instances_alt # at least the null child
        return tuple(map(self.nonnull_child_instance2src_copy_instance,
                         all_children_instances_alt[:-1]))
    

    def parent_instance2null_child_instance(self, parent_instance):
        assert isinstance(parent_instance, OutputID)
        parent_wanted = parent_instance.wanted_id
        assert self.is_WantedID_to_ConRule(parent_wanted) and\
               not self.is_WantedID_to_ConChildRule(parent_wanted)
        
        parent_ex = parent_wanted.ex_id
        parent_input = parent_ex.input_id
        
        rule = self.wanted2input_rule(parent_wanted)
        null_child_idx = L = len(rule.children)
        null_child_end = parent_instance.end
        null_child_begin = null_child_end
        child_id = ConChildID(parent_input, null_child_idx)
        child_wanted = WantedID(child_id, null_child_begin)
        child_instance = OutputID(child_wanted, null_child_end)
        return child_instance
        

    def cachedcalc__child_wanted2prev_instances__ge(self, pos=None):
        if pos == None:
            pos = self.pos
        if not self.begin_pos <= pos <= self.pos:
            raise ValueError('not self.begin_pos <= pos <= self.pos')
        cache = self.__pos2child_wanted2prev_instances

        recalc = True
        for _pos, d in cache.items():
            if _pos >= pos:
                recalc = False
            break
        
        if recalc:
            cache.clear()
            _pos = self.pos
            d = cache[_pos] = self.calc__child_wanted2prev_instances()
        
        assert _pos >= pos
        return MappingProxyType(d)
    

    def calc__child_wanted2prev_instances(self):
        child_wanted2prev_instances = defaultdict(set)
        for instance in self.created_wanted_instances:
            wanted = instance.wanted_id
            if not self.is_WantedID_to_ConChildRule(wanted):
                continue

            child_id = wanted.ex_id
            if self.is_null_child_id(child_id):
                # null child has no successor
                # fake prev_wanted
                continue

            prev_instance = instance
            curr_wanted = self.next_child_wanted(prev_instance)
            child_wanted2prev_instances[curr_wanted].add(prev_instance)
        return dict(child_wanted2prev_instances)








    

  # util methods


      ## child_id ##
  
    def __con_child_id2info(self, con_child_id):
        assert isinstance(con_child_id, ConChildID)
        parent_id = con_child_id.input_id
        parent_rule = self.input_id2rule[parent_id]
        L = len(parent_rule.children)
        
        curr_child_idx = con_child_id.child_idx
        assert 0 <= curr_child_idx <= L
        return parent_id, parent_rule, L, curr_child_idx
        
    def is_null_child_id(self, con_child_id):
        'is parent_rule[L:L]?? where L = len(parent_rule.children)'
        parent_id, parent_rule, L, curr_child_idx = \
                   self.__con_child_id2info(con_child_id)
        return curr_child_idx == L
    def calc__child_id(self, con_child_id, idx_transform):
        parent_id, parent_rule, L, curr_child_idx = \
                   self.__con_child_id2info(con_child_id)

        result_child_idx = curr_child_idx + 1
        if not 0 <= result_child_idx <= L:
            raise ValueError('not 0 <= result_child_idx <= L')
        return ConChildID(parent_id, result_child_idx)
    def next_child_id(self, con_child_id):
        return self.calc__child_id(con_child_id, lambda i:i+1)

    def prev_child_id(self, con_child_id):
        return self.calc__child_id(con_child_id, lambda i:i-1)

    def next_child_wanted(self, child_wanted_instance):
        assert isinstance(child_wanted_instance, OutputID)
        next_child = self.next_child_id(child_wanted_instance.wanted_id.ex_id)
        next_begin = child_wanted_instance.end
        next_wanted = WantedID(next_child, next_begin)
        return next_wanted



    
      ## RuleType
    
    def is_terminal(self, input_id):
        ex_id = OrgID(input_id)
        rule = self.ex_id2input_rule(ex_id)
        return isinstance(rule, Terminal)
        # bug : return isinstance(input_id, Terminal)

        
    def ex_id2input_rule(self, ex_id):
        # ex_id = wanted.ex_id | OrgID(input_id) | ConChildID(...)
        if isinstance(ex_id, OrgID):
            input_id = ex_id.input_id
            return self.input_id2rule.get(input_id, dead_rule)

        # ConChildID
        assert isinstance(ex_id, ConChildID)
        con_id = ex_id.input_id
        child_idx = ex_id.child_idx
        input_con_rule = self.input_id2rule[con_id]
        children = input_con_rule.children
        if child_idx < len(children):
            child = input_con_rule.children[child_idx]
            return AltRule([child])
        elif child_idx == len(children):
            return null_rule
        else:
            raise logic-error

    def wanted2input_rule(self, wanted):
        ex_id = wanted.ex_id
        rule = self.ex_id2input_rule(ex_id)
        return rule
        
    def is_WantedID_to_RuleType(self, wanted, RuleType):
        rule = self.wanted2input_rule(wanted)
        return isinstance(rule, RuleType)

    def is_WantedID_to_DeadRule(self, wanted):
        return self.is_WantedID_to_AltRule(wanted) and\
               not self.wanted2input_rule(wanted).alts
    
    def is_WantedID_to_AltRule(self, wanted):
        return self.is_WantedID_to_RuleType(wanted, AltRule)
    
    def is_WantedID_to_ConRule(self, wanted):
        return self.is_WantedID_to_RuleType(wanted, ConRule)

    def is_WantedID_to_ConChildRule(self, wanted):
        if isinstance(wanted.ex_id, ConChildID):
            assert (self.is_WantedID_to_AltRule(wanted) and
                    len(self.wanted2input_rule(wanted).alts) == 1 or
                    self.is_WantedID_to_ConRule(wanted) and
                    len(self.wanted2input_rule(wanted).children) == 0)
            return True
        return False
               
        #error: return self.is_WantedID_to_AltRule(wanted) and\
        #       isinstance(wanted.ex_id, ConChildID)
        # error: return self.is_WantedID_to_RuleType(wanted, ConChildRule)
    
    def is_WantedID_to_NullRule(self, wanted):
        return self.is_WantedID_to_ConRule(wanted) and \
               not self.wanted2input_rule(wanted).children
    
    def is_WantedID_to_Terminal(self, wanted):
        return self.is_WantedID_to_RuleType(wanted, Terminal)









if __name__ == "__main__":
    import doctest
    doctest.testmod()







