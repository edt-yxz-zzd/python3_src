
TODO

from abc import ABCMeta, abstractmethod
import socket
import subprocess
import time

class TimeoutErrorABC(Exception, metaclass=ABCMeta): pass
TimeoutErrorABC.register(TimeoutError)
TimeoutErrorABC.register(socket.timeout)
TimeoutErrorABC.register(subprocess.TimeoutExpired)

class URLx:
    # redirect??
    @abstractmethod
    def get_original_url(self):
        raise NotImplementedError
    @abstractmethod
    def get_direct_url(self):
        raise NotImplementedError

def __http_fecth1(url, begin, end, timeout):
    # timeout = None | uint -- in seconds
    if timeout is not None and timeout < 0:
        raise ValueError('timeout should be None or >= 0')


class HttpDownload:
    @abstractmethod
    def __on_timeout__(self, url, begin, end):
        # remain task: (url, begin, end)
        # @return:
        #   raise ...
        #   ('fail', None) - fail
        #   ('wait', seconds_to_retry) - will call __resume__
        raise NotImplementedError
    @abstractmethod
    def __resume__(self, url, begin, end):
        # @return: (new_url, new_begin, new_end)
        raise NotImplementedError
    @abstractmethod
    def __get_timeout__(self, url, begin):
        # to implement backoff
        # timeout == 0 ==>> block mode
        # timeout < 0 ==>> fire
        raise NotImplementedError
    @abstractmethod
    def __get_block_size__(self, url, begin, end):
        # call this method before each time to read url data
        raise NotImplementedError
    @abstractmethod
    def __write__(self, bytes, url, begin):
        # bytes = get_content(url)[begin:len(bytes)]
        # overwrite this method to
        #   write downloaded data to file
        #   recalc block_size
        #   determine fname later while downloading
        raise NotImplementedError
    def http_fetch1(self, url, begin, end, timeout):
        # @return:
        #   raise TimeoutErrorABC/TimeoutError
        #   data :: bytes
        raise NotImplementedError
    def http_fetch(self, url, begin, end):
        # end should < len(get_content(url))
        while begin < end:
            block_size = self.__get_block_size__(url, begin, end)
            if block_size <= 0:
                raise ValueError('block_size = {} < 0'.format(block_size))
            timeout = self.__get_timeout__(url, begin)
            # assert timeout > 0
            if timeout is None or timeout == 0:
                timeout = None
            elif timeout < 0:
                raise TimeoutError

            try:
                data = self.http_fetch1(url, begin, begin+block_size, timeout)
            except TimeoutErrorABC as e:
                (case, data) = self.__on_timeout__(url, begin, end)
                if case == 'fail':
                    raise TimeoutError(
                        dict( url=url
                            , begin=begin
                            , end=end
                            , block_size=block_size
                            , timeout=timeout
                            , err=e
                            )
                        )
                elif case == 'wait':
                    seconds = data
                    time.sleep(seconds)
                    continue
                else:
                    raise Exception('unknown case from __on_timeout__', e)

            self.__write__(data, url, begin)
            begin += block_size

