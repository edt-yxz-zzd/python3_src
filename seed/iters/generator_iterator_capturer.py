
#e ../../python3_src/seed/iters/generator_iterator_capturer.py
#from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer

class GeneratorIteratorCapturer:
    def __init__(sf, generator_iterator, /):
        sf._g = generator_iterator
        sf._may_either = None # (is_result, exc_or_result)
    def get_tmay_result(sf, /):
        if sf._may_either:
            (is_result, exc_or_result) = sf._may_either
            if is_result:
                result = exc_or_result
                tmay_result = (result,)
            else:
                exc = exc_or_result
                raise exc
        else:
                tmay_result = ()
        return tmay_result

    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        return sf.send(None)
    def send(sf, v, /):
        return sf._capture_(lambda:sf._g.send(v))
    def _capture_(sf, f, /):
        if sf._may_either:
            (is_result, exc_or_result) = sf._may_either
            if is_result:
                result = exc_or_result
                raise StopIteration(result)
            else:
                exc = exc_or_result
                raise exc
        try:
            return f()
        except StopIteration as e:
            result = e.value
            either = (True, result)

            sf._may_either = either
        except Exception as exc:
            either = (False, exc)
            sf._may_either = either
            raise

    def throw(sf, typ, val=None, tb=None, /):
        """Raise an exception in the generator.
        Return next yielded value or raise StopIteration.
        """
        return sf._capture_(lambda:sf._g.throw(typ, val, tb))

    def close(sf, /):
        """Raise GeneratorExit inside generator.
        """
        try:
            sf.throw(GeneratorExit)
        except (GeneratorExit, StopIteration):
            pass
        else:
            raise RuntimeError("generator ignored GeneratorExit")


from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
