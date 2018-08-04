import os
from ..download_small_file import download_images, fname_url_list_filter




def _index2str(idx):
    return '{:0>4}'.format(idx)
def download_chapters(path, comic_url, begin, end, download_funcs):
    chapter_urls = download_funcs.comic_url2chapter_urls(comic_url)

    ch_ls = []
    for i, (name, url) in enumerate(chapter_urls[begin : end], begin):
        name = '{}_{}'.format(_index2str(i), name)
        ch_path = os.path.join(path, name)
        ch_ls.append((ch_path, url))


    img_ls = []
    for ch_path, ch_url in ch_ls:
        image_page_urls = download_funcs.chapter_url2image_page_urls(ch_url)
        for i, url in enumerate(image_page_urls):
            name = '{}.jpg'.format(_index2str(i))
            img_path = os.path.join(ch_path, name)
            img_ls.append((img_path, url))

    if not os.path.exists(path):
        os.makedirs(path)
    for ch_path, ch_url in ch_ls:
        if not os.path.exists(ch_path):
            os.mkdir(ch_path)

    img_ls = fname_url_list_filter(img_ls)
    img_ls = tuple((path, download_funcs.image_page_url2image_url(image_page_url))\
                   for path, image_page_url in img_ls)
    download_images(img_ls)
