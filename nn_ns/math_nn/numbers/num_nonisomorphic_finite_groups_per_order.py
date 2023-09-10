#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups_per_order.py
    !mv ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups.py ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups_per_order.py
view  others/数学/algebra/order.txt
    https://oeis.org/A000001
        A000001 Number of groups of order n.
    https://oeis.org/A000001/b000001.txt
        H.-U. Besche and Ivan Panchenko, Table of n, a(n) for n = 0..2047 [Terms 1 through 2015 copied from Small Groups Library mentioned below. Terms 2016 - 2047 added by Ivan Panchenko, Aug 29 2009. 0 prepended by Ray Chandler, Sep 16 2015. a(1024) corrected by Benjamin Przybocki, Jan 06 2022]
view others/数学/algebra/group.txt
    view script/num_nonisomorphic_finite_groups_of_order_squarefree_.py







nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order -x
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order:__doc__ -ff -v
py_adhoc_call   nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order   @f
from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__

_data_txt = r'''
[[[
https://oeis.org/A000001/b000001.txt
  num_groups_of_order(n)
    [n <- [0..=2047]]
===
0 0
1 1
2 1
3 1
4 2
5 1
6 2
7 1
8 5
9 2
10 2
11 1
12 5
13 1
14 2
15 1
16 14
17 1
18 5
19 1
20 5
21 2
22 2
23 1
24 15
25 2
26 2
27 5
28 4
29 1
30 4
31 1
32 51
33 1
34 2
35 1
36 14
37 1
38 2
39 2
40 14
41 1
42 6
43 1
44 4
45 2
46 2
47 1
48 52
49 2
50 5
51 1
52 5
53 1
54 15
55 2
56 13
57 2
58 2
59 1
60 13
61 1
62 2
63 4
64 267
65 1
66 4
67 1
68 5
69 1
70 4
71 1
72 50
73 1
74 2
75 3
76 4
77 1
78 6
79 1
80 52
81 15
82 2
83 1
84 15
85 1
86 2
87 1
88 12
89 1
90 10
91 1
92 4
93 2
94 2
95 1
96 231
97 1
98 5
99 2
100 16
101 1
102 4
103 1
104 14
105 2
106 2
107 1
108 45
109 1
110 6
111 2
112 43
113 1
114 6
115 1
116 5
117 4
118 2
119 1
120 47
121 2
122 2
123 1
124 4
125 5
126 16
127 1
128 2328
129 2
130 4
131 1
132 10
133 1
134 2
135 5
136 15
137 1
138 4
139 1
140 11
141 1
142 2
143 1
144 197
145 1
146 2
147 6
148 5
149 1
150 13
151 1
152 12
153 2
154 4
155 2
156 18
157 1
158 2
159 1
160 238
161 1
162 55
163 1
164 5
165 2
166 2
167 1
168 57
169 2
170 4
171 5
172 4
173 1
174 4
175 2
176 42
177 1
178 2
179 1
180 37
181 1
182 4
183 2
184 12
185 1
186 6
187 1
188 4
189 13
190 4
191 1
192 1543
193 1
194 2
195 2
196 12
197 1
198 10
199 1
200 52
201 2
202 2
203 2
204 12
205 2
206 2
207 2
208 51
209 1
210 12
211 1
212 5
213 1
214 2
215 1
216 177
217 1
218 2
219 2
220 15
221 1
222 6
223 1
224 197
225 6
226 2
227 1
228 15
229 1
230 4
231 2
232 14
233 1
234 16
235 1
236 4
237 2
238 4
239 1
240 208
241 1
242 5
243 67
244 5
245 2
246 4
247 1
248 12
249 1
250 15
251 1
252 46
253 2
254 2
255 1
256 56092
257 1
258 6
259 1
260 15
261 2
262 2
263 1
264 39
265 1
266 4
267 1
268 4
269 1
270 30
271 1
272 54
273 5
274 2
275 4
276 10
277 1
278 2
279 4
280 40
281 1
282 4
283 1
284 4
285 2
286 4
287 1
288 1045
289 2
290 4
291 2
292 5
293 1
294 23
295 1
296 14
297 5
298 2
299 1
300 49
301 2
302 2
303 1
304 42
305 2
306 10
307 1
308 9
309 2
310 6
311 1
312 61
313 1
314 2
315 4
316 4
317 1
318 4
319 1
320 1640
321 1
322 4
323 1
324 176
325 2
326 2
327 2
328 15
329 1
330 12
331 1
332 4
333 5
334 2
335 1
336 228
337 1
338 5
339 1
340 15
341 1
342 18
343 5
344 12
345 1
346 2
347 1
348 12
349 1
350 10
351 14
352 195
353 1
354 4
355 2
356 5
357 2
358 2
359 1
360 162
361 2
362 2
363 3
364 11
365 1
366 6
367 1
368 42
369 2
370 4
371 1
372 15
373 1
374 4
375 7
376 12
377 1
378 60
379 1
380 11
381 2
382 2
383 1
384 20169
385 2
386 2
387 4
388 5
389 1
390 12
391 1
392 44
393 1
394 2
395 1
396 30
397 1
398 2
399 5
400 221
401 1
402 6
403 1
404 5
405 16
406 6
407 1
408 46
409 1
410 6
411 1
412 4
413 1
414 10
415 1
416 235
417 2
418 4
419 1
420 41
421 1
422 2
423 2
424 14
425 2
426 4
427 1
428 4
429 2
430 4
431 1
432 775
433 1
434 4
435 1
436 5
437 1
438 6
439 1
440 51
441 13
442 4
443 1
444 18
445 1
446 2
447 1
448 1396
449 1
450 34
451 1
452 5
453 2
454 2
455 1
456 54
457 1
458 2
459 5
460 11
461 1
462 12
463 1
464 51
465 4
466 2
467 1
468 55
469 1
470 4
471 2
472 12
473 1
474 6
475 2
476 11
477 2
478 2
479 1
480 1213
481 1
482 2
483 2
484 12
485 1
486 261
487 1
488 14
489 2
490 10
491 1
492 12
493 1
494 4
495 4
496 42
497 2
498 4
499 1
500 56
501 1
502 2
503 1
504 202
505 2
506 6
507 6
508 4
509 1
510 8
511 1
512 10494213
513 15
514 2
515 1
516 15
517 1
518 4
519 1
520 49
521 1
522 10
523 1
524 4
525 6
526 2
527 1
528 170
529 2
530 4
531 2
532 9
533 1
534 4
535 1
536 12
537 1
538 2
539 2
540 119
541 1
542 2
543 2
544 246
545 1
546 24
547 1
548 5
549 4
550 16
551 1
552 39
553 1
554 2
555 2
556 4
557 1
558 16
559 1
560 180
561 1
562 2
563 1
564 10
565 1
566 2
567 49
568 12
569 1
570 12
571 1
572 11
573 1
574 4
575 2
576 8681
577 1
578 5
579 2
580 15
581 1
582 6
583 1
584 15
585 4
586 2
587 1
588 66
589 1
590 4
591 1
592 51
593 1
594 30
595 1
596 5
597 2
598 4
599 1
600 205
601 1
602 6
603 4
604 4
605 7
606 4
607 1
608 195
609 3
610 6
611 1
612 36
613 1
614 2
615 2
616 35
617 1
618 6
619 1
620 15
621 5
622 2
623 1
624 260
625 15
626 2
627 2
628 5
629 1
630 32
631 1
632 12
633 2
634 2
635 1
636 12
637 2
638 4
639 2
640 21541
641 1
642 4
643 1
644 9
645 2
646 4
647 1
648 757
649 1
650 10
651 5
652 4
653 1
654 6
655 2
656 53
657 5
658 4
659 1
660 40
661 1
662 2
663 2
664 12
665 1
666 18
667 1
668 4
669 2
670 4
671 1
672 1280
673 1
674 2
675 17
676 16
677 1
678 4
679 1
680 53
681 1
682 4
683 1
684 51
685 1
686 15
687 2
688 42
689 2
690 8
691 1
692 5
693 4
694 2
695 1
696 44
697 1
698 2
699 1
700 36
701 1
702 62
703 1
704 1387
705 1
706 2
707 1
708 10
709 1
710 6
711 4
712 15
713 1
714 12
715 2
716 4
717 1
718 2
719 1
720 840
721 1
722 5
723 2
724 5
725 2
726 13
727 1
728 40
729 504
730 4
731 1
732 18
733 1
734 2
735 6
736 195
737 2
738 10
739 1
740 15
741 5
742 4
743 1
744 54
745 1
746 2
747 2
748 11
749 1
750 39
751 1
752 42
753 1
754 4
755 2
756 189
757 1
758 2
759 2
760 39
761 1
762 6
763 1
764 4
765 2
766 2
767 1
768 1090235
769 1
770 12
771 1
772 5
773 1
774 16
775 4
776 15
777 5
778 2
779 1
780 53
781 1
782 4
783 5
784 172
785 1
786 4
787 1
788 5
789 1
790 4
791 2
792 137
793 1
794 2
795 1
796 4
797 1
798 24
799 1
800 1211
801 2
802 2
803 1
804 15
805 1
806 4
807 1
808 14
809 1
810 113
811 1
812 16
813 2
814 4
815 1
816 205
817 1
818 2
819 11
820 20
821 1
822 4
823 1
824 12
825 5
826 4
827 1
828 30
829 1
830 4
831 2
832 1630
833 2
834 6
835 1
836 9
837 13
838 2
839 1
840 186
841 2
842 2
843 1
844 4
845 2
846 10
847 2
848 51
849 2
850 10
851 1
852 10
853 1
854 4
855 5
856 12
857 1
858 12
859 1
860 11
861 2
862 2
863 1
864 4725
865 1
866 2
867 3
868 9
869 1
870 8
871 1
872 14
873 4
874 4
875 5
876 18
877 1
878 2
879 1
880 221
881 1
882 68
883 1
884 15
885 1
886 2
887 1
888 61
889 2
890 4
891 15
892 4
893 1
894 4
895 1
896 19349
897 2
898 2
899 1
900 150
901 1
902 4
903 7
904 15
905 2
906 6
907 1
908 4
909 2
910 8
911 1
912 222
913 1
914 2
915 4
916 5
917 1
918 30
919 1
920 39
921 2
922 2
923 1
924 34
925 2
926 2
927 4
928 235
929 1
930 18
931 2
932 5
933 1
934 2
935 2
936 222
937 1
938 4
939 2
940 11
941 1
942 6
943 1
944 42
945 13
946 4
947 1
948 15
949 1
950 10
951 1
952 42
953 1
954 10
955 2
956 4
957 1
958 2
959 1
960 11394
961 2
962 4
963 2
964 5
965 1
966 12
967 1
968 42
969 2
970 4
971 1
972 900
973 1
974 2
975 6
976 51
977 1
978 6
979 2
980 34
981 5
982 2
983 1
984 46
985 1
986 4
987 2
988 11
989 1
990 30
991 1
992 196
993 2
994 6
995 1
996 10
997 1
998 2
999 15
1000 199
1001 1
1002 4
1003 1
1004 4
1005 2
1006 2
1007 1
1008 954
1009 1
1010 6
1011 2
1012 13
1013 1
1014 23
1015 2
1016 12
1017 2
1018 2
1019 1
1020 37
1021 1
1022 4
1023 2
1024 49487367289
1025 4
1026 66
1027 2
1028 5
1029 19
1030 4
1031 1
1032 54
1033 1
1034 4
1035 2
1036 11
1037 1
1038 4
1039 1
1040 231
1041 1
1042 2
1043 1
1044 36
1045 2
1046 2
1047 2
1048 12
1049 1
1050 40
1051 1
1052 4
1053 51
1054 4
1055 2
1056 1028
1057 1
1058 5
1059 1
1060 15
1061 1
1062 10
1063 1
1064 35
1065 2
1066 4
1067 1
1068 12
1069 1
1070 4
1071 4
1072 42
1073 1
1074 4
1075 2
1076 5
1077 1
1078 10
1079 1
1080 583
1081 2
1082 2
1083 6
1084 4
1085 2
1086 6
1087 1
1088 1681
1089 6
1090 4
1091 1
1092 77
1093 1
1094 2
1095 2
1096 15
1097 1
1098 16
1099 1
1100 51
1101 2
1102 4
1103 1
1104 170
1105 1
1106 4
1107 5
1108 5
1109 1
1110 12
1111 1
1112 12
1113 2
1114 2
1115 1
1116 46
1117 1
1118 4
1119 2
1120 1092
1121 1
1122 8
1123 1
1124 5
1125 14
1126 2
1127 2
1128 39
1129 1
1130 4
1131 2
1132 4
1133 1
1134 254
1135 1
1136 42
1137 2
1138 2
1139 1
1140 41
1141 1
1142 2
1143 5
1144 39
1145 1
1146 4
1147 1
1148 11
1149 1
1150 10
1151 1
1152 157877
1153 1
1154 2
1155 4
1156 16
1157 1
1158 6
1159 1
1160 49
1161 13
1162 4
1163 1
1164 18
1165 1
1166 4
1167 1
1168 53
1169 1
1170 32
1171 1
1172 5
1173 1
1174 2
1175 2
1176 279
1177 1
1178 4
1179 2
1180 11
1181 1
1182 4
1183 3
1184 235
1185 2
1186 2
1187 1
1188 99
1189 1
1190 8
1191 2
1192 14
1193 1
1194 6
1195 1
1196 11
1197 14
1198 2
1199 1
1200 1040
1201 1
1202 2
1203 1
1204 13
1205 2
1206 16
1207 1
1208 12
1209 5
1210 27
1211 1
1212 12
1213 1
1214 2
1215 69
1216 1387
1217 1
1218 16
1219 1
1220 20
1221 2
1222 4
1223 1
1224 164
1225 4
1226 2
1227 2
1228 4
1229 1
1230 12
1231 1
1232 153
1233 2
1234 2
1235 1
1236 15
1237 1
1238 2
1239 2
1240 51
1241 1
1242 30
1243 1
1244 4
1245 1
1246 4
1247 1
1248 1460
1249 1
1250 55
1251 4
1252 5
1253 1
1254 12
1255 2
1256 14
1257 1
1258 4
1259 1
1260 131
1261 1
1262 2
1263 2
1264 42
1265 3
1266 6
1267 1
1268 5
1269 5
1270 4
1271 1
1272 44
1273 1
1274 10
1275 3
1276 11
1277 1
1278 10
1279 1
1280 1116461
1281 5
1282 2
1283 1
1284 10
1285 1
1286 2
1287 4
1288 35
1289 1
1290 12
1291 1
1292 11
1293 1
1294 2
1295 1
1296 3609
1297 1
1298 4
1299 2
1300 50
1301 1
1302 24
1303 1
1304 12
1305 2
1306 2
1307 1
1308 18
1309 1
1310 6
1311 2
1312 244
1313 1
1314 18
1315 1
1316 9
1317 2
1318 2
1319 1
1320 181
1321 1
1322 2
1323 51
1324 4
1325 2
1326 12
1327 1
1328 42
1329 1
1330 8
1331 5
1332 61
1333 1
1334 4
1335 1
1336 12
1337 1
1338 6
1339 1
1340 11
1341 2
1342 4
1343 1
1344 11720
1345 1
1346 2
1347 1
1348 5
1349 1
1350 112
1351 1
1352 52
1353 1
1354 2
1355 2
1356 12
1357 1
1358 4
1359 4
1360 245
1361 1
1362 4
1363 1
1364 9
1365 5
1366 2
1367 1
1368 211
1369 2
1370 4
1371 2
1372 38
1373 1
1374 6
1375 15
1376 195
1377 15
1378 6
1379 2
1380 29
1381 1
1382 2
1383 1
1384 14
1385 1
1386 32
1387 1
1388 4
1389 2
1390 4
1391 1
1392 198
1393 1
1394 4
1395 8
1396 5
1397 1
1398 4
1399 1
1400 153
1401 1
1402 2
1403 1
1404 227
1405 2
1406 4
1407 5
1408 19324
1409 1
1410 8
1411 1
1412 5
1413 4
1414 4
1415 1
1416 39
1417 1
1418 2
1419 2
1420 15
1421 4
1422 16
1423 1
1424 53
1425 6
1426 4
1427 1
1428 40
1429 1
1430 12
1431 5
1432 12
1433 1
1434 4
1435 2
1436 4
1437 1
1438 2
1439 1
1440 5958
1441 1
1442 4
1443 5
1444 12
1445 2
1446 6
1447 1
1448 14
1449 4
1450 10
1451 1
1452 40
1453 1
1454 2
1455 2
1456 179
1457 1
1458 1798
1459 1
1460 15
1461 2
1462 4
1463 1
1464 61
1465 1
1466 2
1467 5
1468 4
1469 1
1470 46
1471 1
1472 1387
1473 1
1474 6
1475 2
1476 36
1477 2
1478 2
1479 1
1480 49
1481 1
1482 24
1483 1
1484 11
1485 10
1486 2
1487 1
1488 222
1489 1
1490 4
1491 3
1492 5
1493 1
1494 10
1495 1
1496 41
1497 2
1498 4
1499 1
1500 174
1501 1
1502 2
1503 2
1504 195
1505 2
1506 4
1507 1
1508 15
1509 1
1510 6
1511 1
1512 889
1513 1
1514 2
1515 2
1516 4
1517 1
1518 12
1519 2
1520 178
1521 13
1522 2
1523 1
1524 15
1525 4
1526 4
1527 1
1528 12
1529 1
1530 20
1531 1
1532 4
1533 5
1534 4
1535 1
1536 408641062
1537 1
1538 2
1539 60
1540 36
1541 1
1542 4
1543 1
1544 15
1545 2
1546 2
1547 1
1548 46
1549 1
1550 16
1551 1
1552 54
1553 1
1554 24
1555 2
1556 5
1557 2
1558 4
1559 1
1560 221
1561 1
1562 4
1563 1
1564 11
1565 1
1566 30
1567 1
1568 928
1569 2
1570 4
1571 1
1572 10
1573 2
1574 2
1575 13
1576 14
1577 1
1578 4
1579 1
1580 11
1581 2
1582 6
1583 1
1584 697
1585 1
1586 4
1587 3
1588 5
1589 1
1590 8
1591 1
1592 12
1593 5
1594 2
1595 2
1596 64
1597 1
1598 4
1599 2
1600 10281
1601 1
1602 10
1603 1
1604 5
1605 1
1606 4
1607 1
1608 54
1609 1
1610 8
1611 2
1612 11
1613 1
1614 4
1615 1
1616 51
1617 6
1618 2
1619 1
1620 477
1621 1
1622 2
1623 2
1624 56
1625 5
1626 6
1627 1
1628 11
1629 5
1630 4
1631 1
1632 1213
1633 1
1634 4
1635 2
1636 5
1637 1
1638 72
1639 1
1640 68
1641 2
1642 2
1643 1
1644 12
1645 1
1646 2
1647 13
1648 42
1649 1
1650 38
1651 1
1652 9
1653 2
1654 2
1655 2
1656 137
1657 1
1658 2
1659 5
1660 11
1661 1
1662 6
1663 1
1664 21507
1665 5
1666 10
1667 1
1668 15
1669 1
1670 4
1671 1
1672 34
1673 2
1674 60
1675 2
1676 4
1677 5
1678 2
1679 1
1680 1005
1681 2
1682 5
1683 2
1684 5
1685 1
1686 4
1687 1
1688 12
1689 1
1690 10
1691 1
1692 30
1693 1
1694 10
1695 1
1696 235
1697 1
1698 6
1699 1
1700 50
1701 309
1702 4
1703 2
1704 39
1705 7
1706 2
1707 1
1708 11
1709 1
1710 36
1711 2
1712 42
1713 2
1714 2
1715 5
1716 40
1717 1
1718 2
1719 2
1720 39
1721 1
1722 12
1723 1
1724 4
1725 3
1726 2
1727 1
1728 47937
1729 1
1730 4
1731 2
1732 5
1733 1
1734 13
1735 1
1736 35
1737 4
1738 4
1739 1
1740 37
1741 1
1742 4
1743 2
1744 51
1745 1
1746 16
1747 1
1748 9
1749 1
1750 30
1751 2
1752 64
1753 1
1754 2
1755 14
1756 4
1757 1
1758 4
1759 1
1760 1285
1761 1
1762 2
1763 1
1764 228
1765 1
1766 2
1767 5
1768 53
1769 1
1770 8
1771 2
1772 4
1773 2
1774 2
1775 4
1776 260
1777 1
1778 6
1779 1
1780 15
1781 1
1782 110
1783 1
1784 12
1785 2
1786 4
1787 1
1788 12
1789 1
1790 4
1791 5
1792 1083553
1793 1
1794 12
1795 1
1796 5
1797 1
1798 4
1799 1
1800 749
1801 1
1802 4
1803 2
1804 11
1805 3
1806 30
1807 1
1808 54
1809 13
1810 6
1811 1
1812 15
1813 2
1814 2
1815 9
1816 12
1817 1
1818 10
1819 1
1820 35
1821 2
1822 2
1823 1
1824 1264
1825 2
1826 4
1827 6
1828 5
1829 1
1830 18
1831 1
1832 14
1833 2
1834 4
1835 1
1836 117
1837 1
1838 2
1839 2
1840 178
1841 1
1842 6
1843 1
1844 5
1845 4
1846 4
1847 1
1848 162
1849 2
1850 10
1851 1
1852 4
1853 1
1854 16
1855 1
1856 1630
1857 2
1858 2
1859 2
1860 56
1861 1
1862 10
1863 15
1864 15
1865 1
1866 4
1867 1
1868 4
1869 2
1870 12
1871 1
1872 1096
1873 1
1874 2
1875 21
1876 9
1877 1
1878 6
1879 1
1880 39
1881 5
1882 2
1883 1
1884 18
1885 1
1886 4
1887 2
1888 195
1889 1
1890 120
1891 1
1892 9
1893 2
1894 2
1895 1
1896 54
1897 1
1898 4
1899 4
1900 36
1901 1
1902 4
1903 1
1904 186
1905 2
1906 2
1907 1
1908 36
1909 1
1910 6
1911 15
1912 12
1913 1
1914 8
1915 1
1916 4
1917 5
1918 4
1919 1
1920 241004
1921 1
1922 5
1923 1
1924 15
1925 4
1926 10
1927 1
1928 15
1929 2
1930 4
1931 1
1932 34
1933 1
1934 2
1935 4
1936 167
1937 1
1938 12
1939 1
1940 15
1941 1
1942 2
1943 1
1944 3973
1945 1
1946 4
1947 1
1948 4
1949 1
1950 40
1951 1
1952 235
1953 11
1954 2
1955 1
1956 15
1957 1
1958 6
1959 1
1960 144
1961 1
1962 18
1963 1
1964 4
1965 2
1966 2
1967 2
1968 203
1969 1
1970 4
1971 15
1972 15
1973 1
1974 12
1975 2
1976 39
1977 1
1978 4
1979 1
1980 120
1981 1
1982 2
1983 2
1984 1388
1985 1
1986 6
1987 1
1988 13
1989 4
1990 4
1991 1
1992 39
1993 1
1994 2
1995 5
1996 4
1997 1
1998 66
1999 1
2000 963
2001 1
2002 8
2003 1
2004 10
2005 2
2006 4
2007 4
2008 12
2009 2
2010 12
2011 1
2012 4
2013 2
2014 4
2015 2
2016 6538
2017 1
2018 2
2019 2
2020 20
2021 1
2022 6
2023 2
2024 46
2025 63
2026 2
2027 1
2028 88
2029 1
2030 12
2031 1
2032 42
2033 1
2034 10
2035 2
2036 5
2037 5
2038 2
2039 1
2040 175
2041 2
2042 2
2043 2
2044 11
2045 1
2046 12
2047 1
===
]]]
'''#'''
def _parse_data_txt_(_data_txt, /):
    _, rows, _ = _data_txt.split('===')
    idx_num_ls = [*map(int, rows.strip().split())]
    assert len(idx_num_ls) &1 == 0
    ls = []
    for idx, (group_order, num_nonisomorphic_finite_groups) in enumerate(zip(idx_num_ls[0::2], idx_num_ls[1::2])):
        assert group_order == idx == len(ls)
        ls.append(num_nonisomorphic_finite_groups)
    num_nonisomorphic_finite_groups5order = (*ls,)
    return num_nonisomorphic_finite_groups5order
num_nonisomorphic_finite_groups5order = _parse_data_txt_(_data_txt)
num_nonisomorphic_finite_groups5order_lt2048 = num_nonisomorphic_finite_groups5order
assert len(num_nonisomorphic_finite_groups5order_lt2048) == 2048




if __name__ == "__main__":
    pass
__all__


from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import num_nonisomorphic_finite_groups5order_lt2048
from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import num_nonisomorphic_finite_groups5order
from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import *
