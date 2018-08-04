
__all__ = ['CodecBase']

from sand import DecodeError, EncodeError
import io

class CodecBase:
    def wrap_file(self, file):
        return file
    def unwrap_file(self, file):
        return file
    
    def encode(self, value):
        file = io.BytesIO()
        file = self.wrap_file(file)
        
        self.encode_to_file(file, value)
        file = self.unwrap_file(file)
        return file.getvalue()

    def decode(self, bs):
        file = io.BytesIO(bs)
        file = self.wrap_file(file)
        
        value = self.decode_from_file(file)
        file = self.unwrap_file(file)
        
        if file.tell() != len(file.getbuffer()):
            raise DecodeError("decoded value from a proper prefix of input bytes")
        return value
    
    def try_encode_to_file(self, file, value):
        try:
            self.encode_to_file(file, value)
            return True
        except EncodeError:
            return False
    def try_decode_from_file(self, file):
        try:
            return self.decode_from_file(file)
        except DecodeError:
            return None
    
    def encode_to_file(self, file, value):
        self._encode_to_file(file, value)
        return None
    def decode_from_file(self, file):
        return self._decode_from_file(file)
        
    def _encode_to_file(self, file, value):
        raise NotImplementedError
    def _decode_from_file(self, file):
        raise NotImplementedError
