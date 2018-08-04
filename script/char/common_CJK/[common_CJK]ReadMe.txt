

common_CJK
    to find out a subset of Hanzi which can be encoded in many charset.
    to use in project like "与佛论禅"/"佛曰"

steps:
    1) find out which encodings contains '一'
        common_CJK_chars.encodings_CJK
    2) calc their intersection
        # use [rng] as set to calc intersection
        encoding2ranges :: encoding -> [rng]
            gb2312_ranges = encoding2ranges 'gb2312'
        common_char_ord_ranges :: [encoding] -> [rng]
            common_CJK_ranges = common_CJK_ranges encodings_CJK
    3) exclude non-Hanzi
        common_CJK_chars_exclude_nonHanzi
    4) exclude han chars which has multi-simplified/tranditional variants
        # data from
        #   http://www.qqxiuzi.cn/wz/jiantizi-fantizi/226.htm
        #   http://www.qqxiuzi.cn/wz/jiantizi-fantizi/227.htm
        common_CJK_han_chars_exclude_multiST
    5) exclude han chars which has similar chars
        # data from
        #   http://kanji-database.sourceforge.net/variants/similar-chars.html
        common_CJK_uniqueST_han_chars_exclude_similars
    6) exclude han chars which has variants
        # data from Unicode 9.0::UniHan database::Unihan_Variants.txt
        1) exclude vary_charss.vary_chars
            vary_chars = chars with multi simplified/tranditional variants
                        + other variant types
            common_CJK_noSimilar_han_chars_exclude_vary_chars
        or 2) exclude all_chars_with_variant // using
            all chars presented in the Unihan_Variants.txt
            common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant
    7) exclude han chars which are in some banned words
        # data from web 敏感词库
        # see chars_in_banned_words.u8
        common_CJK_noVariant_han_chars_exclude_banned
    8) exclude numeric han chars
        # data from Unicode 9.0::UniHan database::Unihan_NumericValues.txt
        no changes!
        common_CJK_nonBanned_han_chars_exclude_numeric

    9) reserve the lesser frequency chars
        # data from
        #   http://lingua.mtsu.edu/chinese-computing/statistics/
        #       Combined character frequency list of Classical and Modern Chinese
        #       汉字单字字频总表.txt
        unique_and_sorted_by_frequency.py
        freq_sorted_nonBanned_nonNum_han_chars.gb
            86 矣郡惟淮荷哉嗣撰巳朕癸亥椅衙旱俺簿旬癌蕃猩塘擢薨懿裳脊稷葡憾蝗梗萄揖晏棠喀梢藩暑膊胤株筵棚沼弧敞榻殆鄂沮璋敖邸嗟膨黜悖逵漕攸蔬蛟嵌俸瘢嗜哺蕉杉侈梭麾胥汾掖琢戟甥荀斛耆隅茵檄
            256 竺笙翊釉宸潼徇礁僖臾泗瑾羲渥拷壕脯壑瑛孺熄瑚琶斡渤爰甄恁苔芍嗔偈褥痰裨舷磐勺簪蟠橡嫦逋珀佃夙濠肪枷剔薇椿蹙茄涓溥衢茸翌窒穹蛾卞衾陟琵菁雉猝曙酵邯懋眸曷瀑焙悸蛭珂揆瑁喙陂淙舫斫麝燮桔愆庠跛黍佚癖蹇曦湍蒜磬珥橙娑怏暹瓢逡嵋跏燧昴疵爻麒橄寤幄胛淞滓狎窈湫帑芹拌荻嬖盂碇燔倨皿瘠蚌祉淅洵楹秧咫筮蚣瞑攫悌跣趺褶灸樟魃倬翡傀殄岬菽俳槁蒿羸侏裟暝袈痘俑稔畛粕翕濂甑蜈葺柑楔椽匐樗嵬溟噫蔗琥匍碣嗾纛禳醵艮戡萸瓠雎槿侑枋肄暾慝梏楮檎汐豌蕨逑桎枳楸慊螟佶畦稗酊圄菖揄孱疥蓍蹉痍枸枇茯廛猊酩荏擘苒眄茱痂篁腱膈筌埴醍柝酎莪疝茴堀檗疳蒡嚆


total chars:
    total_gb2312_chars = 7573
    total_common_CJK_chars = 3065
    total_common_CJK_chars_exclude_nonHanzi = 2513
    total_common_CJK_han_chars_exclude_multiST = 2340
    total_common_CJK_uniqueST_han_chars_exclude_similars = 2259
    total_common_CJK_noSimilar_han_chars_exclude_vary_chars = 1520
    total_common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant = 1518
    total_common_CJK_noVariant_han_chars_exclude_banned = 342
    total_common_CJK_nonBanned_han_chars_exclude_numeric = 342





