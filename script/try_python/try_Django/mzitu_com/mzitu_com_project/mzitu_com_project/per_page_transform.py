

__all__ = '''
    per_page_transform__url

    per_page_transform__page
    extract_mzitu_com__per_pages
    '''.split()

#from .home_page_transform import NotFoundError, find
from .DATA import website_per_page_img_url_regex
from nn_ns.internet.webpage.fetch_webpage import fetch_webpage
from bs4 import BeautifulSoup
#from seed.helper.repr_input import repr_helper
#import re
#from urllib.parse import urlparse, urlunparse
#from pathlib import PurePosixPath as Path

def per_page_transform__url(old_url):
    html_page = fetch_webpage(old_url)
    return per_page_transform__page(html_page)


def extract_mzitu_com__per_pages(html_page):
    # html_page -> (html_title, [img_url])
    #
    soup = BeautifulSoup(html_page, 'lxml')
    [html_title] = soup.head.find_all('title')
    html_title = html_title.get_text()

    [class_main_image] = soup.find_all('div', {'class': 'main-image'})
    [img_tag] = class_main_image.find_all('img')
    img_url = img_tag['src']
    img_url = img_url.lower()

    m = website_per_page_img_url_regex.fullmatch(img_url)
    if m is None: raise Exception(img_url)
    str_IMG_NUMBER = m['IMG_NUMBER']
    #assert str_IMG_NUMBER == '01'
    #   /169493/ disordered

    begin = m.start('IMG_NUMBER')
    end = m.end('IMG_NUMBER')
    init = img_url[:begin]
    tail = img_url[end:]


    [class_page_navigate] = soup.find_all('div', {'class': 'pagenavi'})
    children = class_page_navigate.find_all('a')
    children = list(children)
    assert len(children) >= 3

    last = children[-1]
    last2 = children[-2]
    #print(last.name)
    #print(repr(last))
    assert last.name == 'a'
    assert last2.name == 'a'
    assert '下一页' in last.get_text()
    str_IMG_TOTAL = last2.get_text()
    IMG_TOTAL = int(str_IMG_TOTAL)
    assert IMG_TOTAL < 100

    img_urls = []
    for i in range(0, IMG_TOTAL):
        n = i+1
        str_IMG_NUMBER = f'{n:0>2}'
        assert len(str_IMG_NUMBER) == 2
        img_url = init + str_IMG_NUMBER + tail
        img_urls.append(img_url)
    return html_title, img_urls





new_html_begin = r'''
<!DOCTYPE html>
<html>
<head>
    <title></title>

</head>

<body>
    <div>
    </div>
    <iframe id="ifa" style="display:none" />

    <script type='text/javascript'>
        var imgs=document.getElementsByTagName('img');
        var newimgarr=[];
        for(var i=0;i<imgs.length;i++){
            var g=imgs[i];
            if(g.getAttribute('data_type')=='loadimg'){
                newimgarr.push(g);
            }
        }

        var i=document.getElementById('ifa');
        var w=i.contentWindow;
        for(var j=0;j<newimgarr.length;j++){
            var k=newimgarr[j];
            (function(k){
                var imgurl=k.getAttribute('data_src');
                getImg(w.document,imgurl,function(){
                    k.src=imgurl;
                });
            })(k);

        }

        function getImg(doc,src,callback){
            var img=doc.createElement('img');
            img.src=src;
            img.onload=callback;
        }
    </script>
</body>
</html>
'''



new_html_begin = r'''
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>

<body>
    <div>
    </div>
</body>
</html>
'''


def per_page_transform__page(html_page):
    html_title, img_urls = extract_mzitu_com__per_pages(html_page)


    new_soup = BeautifulSoup(new_html_begin, 'lxml')
    [new_title_tag] = new_soup.find_all('title')
    new_title_tag.append(html_title)
    [new_div_tag] = new_soup.find_all('div')

    for img_url in img_urls:
        # http://bbs.hahacn.com/thread/5.html
        # [success]
        img_url = 'http://api.hahacn.com/other/getimg2?url=' + img_url

        # bug: new_tag('img', href=...)
        #   SHOULD-BE new_tag('img', src=...)
        new_img_tag = new_soup.new_tag(
            #'img', href=img_url, width="200", height="200"
            'img', src=img_url, style="max-width: 100%; height: auto;"
            )
        new_br_tag = new_soup.new_tag('br')

        new_div_tag.append(new_img_tag)
        new_div_tag.append(new_br_tag)

        #############################################
        #############################################
        '''
        [fail]
        from https://blog.csdn.net/qq_37788558/article/details/72636807
            js破解盗链
        <script type="text/javascript">showImg({img_url!r});</script>

            # need to def showImg()
            #   and the definition was broken
        new_img_script_tag = new_soup.new_tag(
            'script', type="text/javascript"
            )
        new_img_script_tag.append(f'showImg({img_url!r});')
        new_br_tag = new_soup.new_tag('br')

        new_div_tag.append(new_img_script_tag)
        new_div_tag.append(new_br_tag)
        '''

        #############################################
        #############################################
        '''
        [fail]
        http://www.cnblogs.com/BeInNight/p/6856684.html
        <img data_type="loadimg" data_src="***.jpg" />


        new_modified_img_tag = new_soup.new_tag(
            'img', data_type='loadimg', data_src=img_url
            )
        new_br_tag = new_soup.new_tag('br')

        new_div_tag.append(new_modified_img_tag)
        new_div_tag.append(new_br_tag)
        '''


        #############################################
        #############################################
        '''
        [fail]
        https://blog.csdn.net/shixin0510/article/details/80651678

        <meta name="referrer" content="never">
        <meta name="referer" content="never">


        <meta name="referrer" content="">
        <meta name="referer" content="">
        '''

    new_html_page = str(new_soup)
    return new_html_page

