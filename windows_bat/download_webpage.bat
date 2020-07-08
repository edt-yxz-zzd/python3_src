@echo:help: -P ./output/ --tries=10
wget -E -H -k -K -p --random-wait -e robots=off -N --dont-remove-listing -U "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4" %*
