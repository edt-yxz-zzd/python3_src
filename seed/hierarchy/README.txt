
虚函数 需要 显式声明
  因为 并非 所有成员函数 都能被 假定为 虚函数
    覆盖后 语义很难统一，除非一开始就清楚必须使用 派生类的实现

direction:
  9:up: obj -> ops
  6:down obj -> ops
  #??? obj.9tower<.xxx> = (obj.ops.xxx, obj.ops.ops.xxx, ...)
  ops.6tower<.xxx> = (obj{.9[1]=ops}.xxx, obj{.9[2]=ops}.xxx, obj{.9[3]=ops}.xxx, ...)
    obj.9[0]=obj
    obj.9[n+1]=obj.9[n].ops
    obj{.9[n]=ops} <==> obj.9[n]=ops

最多两层原则:
  obj.xxx := obj.ops.6tower[0].xxx
    obj.xxx允许一直转发给ops
      必须转发！ops完全控制，除了 局部私有
    ops.6tower 的相关值 必须直接可得（允许惰性求值填充-包括不存在）
  ==>>浅层原则
    mro 结果 cache 包括 fail/miss
    detect/get -> auto set fail#cache
    get_or_set_fdefault
    pure_lookuo -> avoid auto set fail
    grow_only 只增原则
兼容原则:
  mro 兼容
  上下级 兼容
  兼容判断函数 横向/纵向 单个/多个/零个?

EqById <: Hashable
不直接使用 组合键
  可间接 使用:
  symbol <: Weakable&EqById
    WeakKeyDictionary<symbol,value>
  register:
    WeakValueDictionary<value,symbol>
  #register.get_or_register__value(weakable_hashable_value) -> symbol
  register.get_or_register__order(*symbol) -> symbol
  register.get_or_register__unorder_set(symbol_set) -> symbol
      #set, sorted by id
  register.get_or_register__unorder_dict(symbol2value) -> symbol
      #dict, sorted by id
  组合键 格式 描述
    naming:
      WeakValueDictionary<fmt4key,symbol4fmt>
      WeakKeyDictionary<symbol4fmt,fmt4key>
    register.get_or_register__fmt(symbol4fmt, value8combine_key) -> symbol4key

base = {
  ,pass_checks :: {symbol} #eg. detect fulfill/satisfy attached_ops, ...
  ,pass_checks_with_args :: {symbol:{args}}
  }

obj = {
  #,as_obj__ops #内嵌？
  ,as_obj__private_locals
  ,as_obj__attached_locals
  }
  #type.___get_ops___
ops = {
  #,as_ops__interpreter
  ,as_ops__public_6tower
      #def get_9ops(k, obj) := (get_ops^k)(obj)
      #def get_6tower(k, ops) := ops.as_ops__public_6tower[k]
      #     obj.xxx --query-->> for k in [0..]: get_6tower(k, get_9ops(k+1, obj)).xxx
  ,as_ops__private_locals_6tower4public_method
    #同层一一对应，是公开函数的实现细节
  ,as_ops__attached_locals_6tower
  }
  #type.___get_interpreter___
  grow_only
    # EqById&Weakable #not immutable
    # consider ops_set?? singleton-unique
    #   外挂？内嵌？
    #   外挂 则 by_value
    #   内嵌 则 by_id
    detect/get -> auto set fail#cache
    get_or_set_fdefault
    pure_lookuo -> avoid auto set fail
aops = attached_ops
eops = embedded_ops
interpreter4aops = intr4aops = {
  ,is_ops(intr4aops, aops) -> bool
  ,get_(intr4aops, aops, symbol)
      -> MemberError/PropertyError
      -> (0, 0, static_property_of_obj)
          #include staticmethod
          # (intr4aops, ops4obj, mro_info{.ops_which_store_this_method}, obj_ops_9tower, /, *args, **kwargs, ...)
      -> (0, 0b001, method, args)
      -> (0, 0b010, method, kwargs)
      -> (0, 0b011, method, args, kwargs)
      -> (0, 0b111, method, args, kwargs, symbol2arg)
      -> (0b00001, 0, intr4aops->...)
      -> (0b00011, 0, intr4aops->aops->...)
      -> (0b00111, 0, intr4aops->aops->obj->...)
      -> (0b01111, 0, (intr4aops->aops->obj->symbol-> (symbol2arg\-/...symbol2arg) -> (*args) -> ...args -> (**kwargs)), args, kwargs, symbol2arg)
      -> (0b01111, 0b0111, intr4aops->aops->obj->symbol->...)
      ...other combination in [1..15]*[1..7]
  ,get(intr4aops, aops, tmay_obj, symbol)
      #impl by get_
      -> property_of_obj
      -> partial_call<intr4aops, aops, obj> #like types.MethodType
  ,call(intr4aops, aops, tmay_obj, symbol, /, *, symbol2arg, args)
      #impl by get
      <==> get(intr4aops, aops, tmay_obj, symbol)(symbol2arg, args)
  }
interpreter4eops = intr4eops = {
  ,get_ops(intr4eops, obj) -> eops # Ellipsis -> sf
    ,is_obj(intr4eops, obj) -> bool
  #,get_interpreter
    ,is_ops
    ,get_
    ,get
  }

ops_obj = {
  #,as_ops__interpreter
  ,as_ops__public_6tower
  ,as_ops__private_locals_6tower4public_method
  ,as_obj__ops
  ,as_obj__private_locals
  }


@convert_symbol2arg_to_local_kwargs(N, name2symbolXname, name4unexpected_symbol2arg, name4unexpected_kwargs)
def f(*args, **kwargs):...
def convert_symbol2arg_to_local_kwargs(name2symbolXname, /):
  #check symbol2name__bijection
  check name2symbolXname
  check N
  symbolXname2names = ...
  check symbolXname2names injection with name4unexpected_kwargs,name4unexpected_symbol2arg
  def _(f, /):
    def _(*args, **kwargs0):
      symbol2arg = args[N]
      check kwargs0.keys()
      check symbol2arg.keys() #allow unexpected??

      kwargs1 = {name:arg for symbolXname, arg in symbol2arg.items() for name in symbolXname2names[symbolXname]}
      kwargs2 = {name:arg for symbolXname, arg in kwargs0.items() for name in symbolXname2names[symbolXname]}
      ??kwargs3 = {name4unexpected_kwargs:xxx,name4unexpected_symbol2arg:xx}
      return f(*args, **kwargs1, **kwargs2, **kwargs3)
    return _
  return _


symbol 取代 标识名 的 辅助工具:
class C:
  x = X(locals())
  @x[symbol]
  def f(...):pass
  #==>> locals()[symbol] = f
  #==>> f = the_default_abstract_obj
  assert f is the_default_abstract_obj
  del f
