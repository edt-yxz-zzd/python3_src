


from pathlib import PurePosixPath as Path
import re

# website_ - old # other global
# project_ - new # mine local

website = Path('www.mzitu.com')
#https://www.mzitu.com/all/
#https://www.mzitu.com/old/

website_all_new = website / 'all'
website_all_old = website / 'old'
website_per_page_url_tpl = str(website) + '/{NUMBER}'
website_per_page_img_url_regex = re.compile(
    r"https://i[.]meizitu[.]net/\d{4}/\d{2}/\d{2}[a-z](?P<IMG_NUMBER>\d{2})[.]jpg"
    )
assert website_per_page_img_url_regex.fullmatch('https://i.meizitu.net/2015/02/03t01.jpg')

project_per_page_url_route = '/per/'
per_page_url_regex = re.compile(
    re.escape(project_per_page_url_route)
    + r'(?P<NUMBER>\d+)/'
    )


main_index_page = r'''
<!DOCTYPE html>
<html>
<head> <title>main_index</title> </head>
<body>
    <a href=/old/>old</a>
    <br />
    <a href=/new/>new</a>
    <a href=/all/>all-new</a>
</body>
</html>
'''


