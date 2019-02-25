
r'''
using bs4&lxml to make_markup_node


bs4:
    PageElement = Tag | NavigableString
    NavigableString = NavigableString
                    | CData
                    | ProcessingInstruction
                    | XMLProcessingInstruction
                    | Declaration
                    | Doctype
                    | Comment


example:
    >>> doc_mknode = MakeHtmlRootNode()
    >>> doc_mknode.append_Doctype('HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"')

    #>>> doc_mknode.append_text('\n')
    >>> html_mknode = doc_mknode.get_append_tag__by_hand('html')
    >>> head_mknode = html_mknode.get_append_tag__by_hand('head')
    >>> body_mknode = html_mknode.get_append_tag__by_hand('body')

    ...
    # .get_append_tag__by_hand
    # .get_append_tag
    # .get_append_tag_ex

    >>> title_mknode = head_mknode.get_append_tag__by_hand('title')
    >>> title_mknode.append_text('an empty html')
    >>> doc_tag = doc_mknode.detach_tag()
    >>> html_page = str(doc_tag)
    >>> html_page
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html><head><title>an empty html</title></head><body></body></html>'


'''
__all__ = '''
    IBaseMakeMarkUp
    BaseMakeMarkUp
    MakeRootNode
    MakeHtmlRootNode
    MakeXmlRootNode

    global_features4html
    global_features4xml
    global_html_builder
    global_xml_builder
    '''.split()


from bs4 import (
    PageElement
        ,Tag
            ,BeautifulSoup
        ,NavigableString
            ,CData
            ,ProcessingInstruction
            ,Declaration
            ,Doctype
            ,Comment
    )
import lxml
from abc import abstractmethod, ABC
import copy

global_features4html = 'lxml'
global_features4xml = 'lxml-xml'
    # 'lxml' for html
    # 'lxml-xml' for xml
global_html_soup = BeautifulSoup('', global_features4html)
global_xml_soup = BeautifulSoup('', global_features4xml)
global_html_builder = global_html_soup.builder
global_xml_builder = global_xml_soup.builder

class IBaseMakeMarkUp(ABC):
    '''
immutable parent
    ==>> better topdown construct the whole tree

mknode :: IBaseMakeMarkUp
node :: PageElement <==> Tag|NavigableString
tag :: Tag
    underlying node for mknode MUST BE tag
'''

    def get_last_child_mknode(self):
        tag = self._get_tag_()
        contents = tag.contents
        if not contents: raise IndexError
        last_child_node = contents[-1]

        if not isinstance(last_child_node, Tag): raise TypeError
        last_child_tag = last_child_node
        last_child_mknode = BaseMakeMarkUp(self, last_child_tag, maybe_builder=None)
        return last_child_mknode

    @abstractmethod
    def _get_builder_(self):
        # -> bs4.soup.builder
        return global_xml_builder
        return global_html_builder
    @abstractmethod
    def _get_tag_(self):
        # -> Tag
        #
        # old:
        # -> PageElement
        # -> Tag|NavigableString
        pass
    @abstractmethod
    def _detach_tag_(self):
        pass
    def detach_tag(self):
        tag = self._detach_tag_()
        assert isinstance(tag, Tag)
        try:
            self._get_tag_()
        except:
            pass
        else:
            raise Exception('not detach_tag!')
        return tag

    def copy_whole_subtree(self):
        'O(n) # Tag.__copy__ <==> deepcopy'
        tag = self._get_tag_()
        assert isinstance(tag, Tag)
        return copy.copy(tag)

    def append_node(self, node):
        if not isinstance(node, PageElement): raise TypeError
        if node.parent is not None: raise ValueError
        self._get_tag_().append(node)

    def _append_text_(self, text, *, type):
        if not isinstance(text, str): raise TypeError
        self.append_node(type(text))

    def append_text(self, text):
        self._append_text_(text, type=NavigableString)
    def append_Comment(self, text):
        self._append_text_(text, type=Comment)
    def append_CData(self, text):
        self._append_text_(text, type=CData)
    def append_ProcessingInstruction(self, text):
        self._append_text_(text, type=ProcessingInstruction)
    def append_XMLProcessingInstruction(self, text):
        self._append_text_(text, type=XMLProcessingInstruction)
    def append_Declaration(self, text):
        self._append_text_(text, type=Declaration)
    def append_Doctype(self, text):
        self._append_text_(text, type=Doctype)


    '''xml_nsprefix is short-hand of xml_namespace

    'd' is xml_nsprefix
    'http://.../student' is xml_namespace
        <d:student xmlns:d='http://www.develop.com/student'>
          <d:id>3235329</d:id>
          <d:name>Jeff Smith</d:name>
          <d:language>C#</d:language>
          <d:rating>9.5</d:rating>
        </d:student>
    '''


    def get_append_tag__by_hand(self, __tag_name, __attrs=None, **attrs):
        self.append_tag__by_hand(__tag_name, __attrs, **attrs)
        return self.get_last_child_mknode()
    def append_tag__by_hand(self, __tag_name, __attrs=None, **attrs):
        if __attrs:
            attrs = {**__attrs, **attrs}
        self.append_tag(__tag_name, attrs)

    def get_append_tag(self, tag_name, attrs):
        self.append_tag(tag_name, attrs)
        return self.get_last_child_mknode()
    def append_tag(self, tag_name, attrs):
        self.append_tag_ex(tag_name, attrs, xml_namespace=None, xml_nsprefix=None)

    def get_append_tag_ex(self, tag_name, attrs, *
        , xml_namespace, xml_nsprefix
        ):
        self.append_tag_ex(tag_name, attrs
            ,xml_namespace=xml_namespace
            ,xml_nsprefix=xml_nsprefix
            )
        return self.get_last_child_mknode()
    def append_tag_ex(self, tag_name, attrs, *
        , xml_namespace, xml_nsprefix
        ):
        builder = self._get_builder_()
        tag = Tag(None, builder, tag_name, xml_namespace, xml_nsprefix, attrs)
        self.append_node(tag)

    def append_markup(self, markup:'str|file', *, features=None):
        builder = self._get_builder_()
        document_tag = BeautifulSoup(markup, features, builder)
        for child_node in document_tag.contents:
            self.append_node(child_node)

class BaseMakeMarkUp(IBaseMakeMarkUp):
    def __init__(self, maybe_parent_mknode, tag, *, maybe_builder):
        #bug: if not isinstance(node, PageElement): raise TypeError
        if not isinstance(tag, Tag): raise TypeError
        if not (maybe_parent_mknode is None or isinstance(maybe_parent_mknode, IBaseMakeMarkUp)): raise TypeError
        if maybe_builder is None and maybe_parent_mknode is None: raise TypeError

        if maybe_parent_mknode is not None:
            parent_mknode = maybe_parent_mknode
            builder = parent_mknode._get_builder_()

            parent_tag = parent_mknode._get_tag_()
            if not isinstance(parent_tag, Tag): raise TypeError
            if parent_tag is not tag.parent:
                parent_mknode.append_node(tag)
            assert parent_tag is tag.parent
        else:
            if maybe_builder is None:
                raise logic-error
            builder = maybe_builder

        self.__tag = tag
        self.__builder = builder

    def _get_builder_(self):
        return self.__builder
    def _get_tag_(self):
        return self.__tag
    def _detach_tag_(self):
        tag = self._get_tag_()
        if tag.parent is not None:
            raise ValueError('only root mknode can detach_tag')
        assert tag.name == '[document]'
        doc_tag = tag

        del self.__tag
        return doc_tag

class MakeRootNode(BaseMakeMarkUp):
    def __init__(self, *, features=None, builder=None):
        doc_tag = BeautifulSoup('', features, builder)
        builder = doc_tag.builder
        super().__init__(None, doc_tag, maybe_builder=builder)

class MakeHtmlRootNode(MakeRootNode):
    def __init__(self):
        super().__init__(
            features=global_features4html
            , builder=global_html_builder
            )
class MakeXmlRootNode(MakeRootNode):
    def __init__(self):
        super().__init__(
            features=global_features4xml
            , builder=global_xml_builder
            )




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

