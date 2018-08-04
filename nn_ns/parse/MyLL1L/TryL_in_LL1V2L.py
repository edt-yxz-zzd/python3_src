

mainID_LL1V2L_of_TryL = 'TryL_in_LL1V2L'
TryL_in_LL1V2L = r'''
# I'm comment
->  { self child }
  \ { filter list list_group list_child item item_group item_child default_value_factory }
  \ g_pre g2 g3
  
<-  { self child }
  \ { filter list list_group list_child item item_group item_child default_value_factory }
  \ g_post "afaslfjalj"

-> gp # as -> { self } { filter | list | item } gp
<- gp # as <- { self } { filter | list | item } gp


concept A
concept B
concept C : A B



TryL_in_LL1V2L , =  --this --will --not --discarded A , -- C + ,

a : C
    aa is t'type a.aa' { "attr" : "value" , }
    d = c ,

b = * c { 2 , 2 } # act as 'c , c ,'
    # ',' at beginning of line represent '\ ,'
    , c ?
        \ -> f_preb1 <- f_postb1 # '\' makes a multilines logic line
    ,
    -> f_pre_b
    <- f_post_b

c is t'dsds'


'''

