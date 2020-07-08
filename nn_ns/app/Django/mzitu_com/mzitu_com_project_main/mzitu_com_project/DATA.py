


from pathlib import PurePosixPath as Path
import re

# website_ - old # other global
# project_ - new # mine local

website = Path('www.mzitu.com')
#https://www.mzitu.com/all/
#https://www.mzitu.com/old/
#https://www.mzitu.com/DDDDDDD

#http://localhost/all/
#http://localhost/old/
#http://localhost/new/
#http://localhost/per/DDDDDDD
#http://localhost/echo_image/?url=...

website_all_new = website / 'all'
website_all_old = website / 'old'
website_per_page_url_tpl = str(website) + '/{NUMBER}'
website_per_page_img_url_regex = re.compile(
    r"https://i[.]meizitu[.]net/\d{4}/\d{2}/\d{2}[a-z](?P<IMG_NUMBER>\d{2})(?:-\w+)?[.]jpg"
    )
assert website_per_page_img_url_regex.fullmatch('https://i.meizitu.net/2015/02/03t01.jpg')

#new: website_per_page_img_url_regex
website_per_page_img_url_regex = re.compile(
    r"https?://[^/]+/\d{4}/\d{2}/\d{2}[a-z](?P<IMG_NUMBER>\d{2})(?:-\w+)?[.]jpg"
    )
assert website_per_page_img_url_regex.fullmatch('https://i.meizitu.net/2015/02/03t01.jpg')
assert website_per_page_img_url_regex.fullmatch(r"https://i3.mmzztt.com/2020/06/27b01.jpg")


min_width_num_pages = 2
max_width_num_pages = 3
website_per_page_img_url_regex = re.compile(
    rf"https?://[^/]+/\d{{4}}/\d{{2}}/\d{{2}}[a-z](?P<IMG_NUMBER>\d{{{min_width_num_pages},{max_width_num_pages}}})(?:-\w+)?[.]jpg"
    )
assert website_per_page_img_url_regex.fullmatch(r"https://i5.mmzztt.com/2020/05/19b118.jpg")
	#https://www.mzitu.com/232347
	#http://127.0.0.1:8000/per/232347/




project_per_page_url_route = '/per/'
per_page_url_regex = re.compile(
    re.escape(project_per_page_url_route)
    + r'(?P<NUMBER>\d+)/'
    )

echo_proxy_name = 'echo_image'
echo_proxy_query_key = 'url'

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


