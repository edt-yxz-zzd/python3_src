@find %* -maxdepth 1 -mindepth 1 -printf """""%%p""""\0" | xargs -0 du -s -b -- | sort -n
