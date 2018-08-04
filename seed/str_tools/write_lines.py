
__all__ = '''
    write_lines
    '''.split()

#def write_lines(fout, lines, *, line_prefix='\t', line_sep='\n', line_suffix=''):
def write_lines(fout, lines, *, line_prefix, line_sep, line_suffix):
    lines = iter(lines)
    for head in lines:
        break
    else:
        return


    fout_write = fout.write
    if line_prefix:
        if line_suffix:
            def write_line(line):
                fout_write(line_prefix)
                fout_write(line)
                fout_write(line_suffix)
        else:
            def write_line(line):
                fout_write(line_prefix)
                fout_write(line)
    else:
        if line_suffix:
            def write_line(line):
                fout_write(line)
                fout_write(line_suffix)
        else:
            def write_line(line):
                fout_write(line)

    def write_nonhead_line(line):
        fout_write(line_sep)
        write_line(line)

    write_line(head)
    for line in lines:
        write_nonhead_line(line)
    return

