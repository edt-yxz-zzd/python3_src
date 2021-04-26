
r'''

========
    , IRepositorySetting__using_file_cmp__file_patch_ver1


#'''



__all__ = '''
    IRepositorySetting__using_file_cmp__file_patch_ver1

    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...


from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting
from nn_ns.filedir.dir_cmp import IPseudoFile4MkIsSameFile, bytes2PseudoFile4MkIsSameFile
from nn_ns.filedir.file_cmp import file_patch

from seed.abc.abc import override

___end_mark_of_excluded_global_names__0___ = ...


class IRepositorySetting__using_file_cmp__file_patch_ver1(IRepositorySetting):
    def contentfile_patch(sf, old_contentfile_bytes, patch_bytes, /):
        'old_contentfile_bytes -> patch_bytes -> new_contentfile_bytes'
        lhs_bytes = old_contentfile_bytes
        patch_bytes_ex = patch_bytes
        rhs_bytes = file_patch(lhs_bytes, patch_bytes_ex, ver=1)
        new_contentfile_bytes = rhs_bytes
        return new_contentfile_bytes

    @override
    def ___open_patch_idx___(sf, iter_tpl5s, /):
        r'''Iter (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) -> IPseudoFile4MkIsSameFile
        see: open_patch_idx_ex
        allow to close content_binary_ifile
        #'''
        ls = []
        for (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) in iter_tpl5s:
            with content_binary_ifile as fin:
                bs = fin.read()
            ls.append(bs)
        if not ls: raise logic-err

        contentfile_bytes = ls.pop()
        while ls:
            patch_bytes = ls.pop()
            contentfile_bytes = sf.contentfile_patch(contentfile_bytes, patch_bytes)
        contentfile_bytes

        return bytes2PseudoFile4MkIsSameFile(contentfile_bytes)


