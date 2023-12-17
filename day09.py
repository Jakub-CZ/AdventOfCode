from itertools import pairwise

input_lines = """
14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54
12 27 47 68 92 149 343 943 2562 6504 15418 34500 73686 151710 303812 596709 1157888 2232401 4290657 8227316 15717112
-1 12 52 135 290 585 1167 2315 4511 8546 15696 28027 48918 83927 142167 238407 396167 652136 1062308 1710303 2718418
5 20 41 73 130 249 514 1092 2286 4613 8918 16538 29533 51004 85521 139687 222867 348114 533327 802679 1188356
4 -1 -6 -11 -16 -21 -26 -31 -36 -41 -46 -51 -56 -61 -66 -71 -76 -81 -86 -91 -96
17 19 24 49 132 341 793 1706 3535 7295 15259 32346 68692 144135 295652 589171 1137653 2127907 3859274 6798103 11652852
16 22 25 27 42 114 348 958 2336 5146 10447 19849 35706 61350 101370 161940 251200 379694 560869 811639 1153018
2 4 10 20 37 75 187 530 1502 4019 10054 23656 52851 113180 234277 472014 930586 1801798 3433154 6442636 11906905
8 22 38 54 68 88 164 455 1345 3632 8842 19775 41481 83000 160390 301820 555830 1004266 1781894 3105292 5314322
4 22 63 144 299 591 1136 2153 4054 7588 14053 25590 45573 79109 133662 219815 352184 550498 840859 1257196 1842927
6 13 22 44 98 205 391 721 1407 3076 7361 18108 43709 101432 225212 479319 981804 1943871 3734624 6985356 12754124
8 25 56 106 191 351 684 1418 3041 6523 13701 27970 55542 107713 204827 382958 704758 1276453 2273622 3979178 6837897
11 12 13 13 13 23 80 288 893 2417 5907 13437 29194 61894 130093 273458 575643 1208626 2514941 5154141 10354271
17 21 18 5 -24 -70 -112 -80 186 998 2913 6870 14387 27837 50825 88691 149167 243219 386108 598707 909114
4 12 24 38 63 133 320 746 1594 3118 5652 9618 15533 24015 35788 51686 72656 99760 134176 177198 230235
-3 11 47 113 228 443 886 1848 3942 8401 17640 36304 73200 144877 282435 544969 1046991 2015276 3906455 7646338 15104916
20 26 35 65 158 395 924 2025 4263 8821 18160 37222 75475 150196 291499 549740 1006070 1787060 3084489 5181567 8487060
3 12 39 91 186 366 726 1471 3014 6138 12269 23947 45637 85088 155518 278967 491205 848592 1437243 2384731 3874340
19 37 61 91 127 169 217 271 331 397 469 547 631 721 817 919 1027 1141 1261 1387 1519
14 20 35 59 85 104 126 232 679 2087 5744 14072 31304 64429 124469 228159 400108 675526 1103609 1751681 2710199
9 25 43 63 85 109 135 163 193 225 259 295 333 373 415 459 505 553 603 655 709
2 8 32 85 173 292 434 624 1028 2199 5556 14212 34271 76689 159726 311889 575062 1007218 1683688 2695399 4141761
5 2 -3 -1 39 180 528 1245 2563 4797 8366 13873 22401 36426 62308 116593 241137 537800 1244623 2895947 6644891
4 19 56 134 282 555 1056 1972 3652 6782 12759 24462 47816 94935 190357 383171 770012 1537433 3037698 5920442 11355046
-6 -10 -17 -31 -57 -100 -170 -294 -535 -1008 -1843 -2934 -3047 2731 29473 117660 367128 1009454 2556807 6098291 13872479
9 29 67 137 278 564 1112 2091 3733 6343 10299 16025 23910 34134 46348 59139 69193 70049 50315 -8807 -136866
7 2 -7 -10 20 126 358 753 1303 1914 2365 2284 1168 -1514 -6082 -12201 -18145 -19662 -8311 30882 122628
8 13 32 77 159 284 449 647 903 1382 2635 6080 14852 35199 78650 165236 328106 619947 1121690 1954063 3292637
17 28 41 54 57 37 -1 6 241 1104 3384 8601 19718 42627 89216 183610 374677 760736 1537998 3095953 6208677
28 41 65 111 199 382 795 1736 3782 7951 15955 30668 57093 104426 190420 350385 655208 1246346 2401747 4656396 9016415
15 28 50 96 189 365 695 1341 2671 5466 11260 22862 45117 85971 157913 279875 479679 797128 1287846 2027980 3119885
0 -2 -5 0 44 188 531 1228 2552 5080 10164 20983 44686 96460 206828 434143 885144 1747634 3340889 6191378 11143840
7 12 37 108 272 611 1270 2505 4767 8861 16268 29827 55204 104023 200351 393653 783743 1567254 3121671 6153442 11953216
7 22 51 94 151 222 307 406 519 646 787 942 1111 1294 1491 1702 1927 2166 2419 2686 2967
17 37 68 115 201 387 815 1796 3982 8686 18455 38089 76500 150244 290479 556993 1066793 2052462 3980624 7789694 15359333
12 29 70 158 338 695 1395 2758 5380 10356 19729 37409 70976 135004 256818 485919 908676 1670279 3006360 5287104 9077070
9 11 24 67 171 379 747 1347 2276 3678 5789 9018 14080 22200 35410 56964 91899 147773 235614 371117 576129
12 18 23 23 12 -15 -52 -65 34 437 1555 4282 10558 24471 54242 115563 237085 470195 910144 1750748 3435465
11 13 21 48 117 260 525 998 1849 3420 6390 12078 22981 43691 82394 153226 279847 500695 876499 1500764 2514093
15 27 48 91 194 427 895 1747 3214 5711 10060 17946 32844 61917 119904 237026 474887 958111 1936759 3908828 7860042
28 39 63 115 219 418 800 1556 3098 6286 12837 26019 51791 100682 190981 354344 645878 1162408 2075461 3690474 6552873
9 13 33 79 164 305 529 903 1616 3150 6594 14190 30270 62893 126848 249588 483914 936653 1834918 3677991 7576339
5 9 17 37 82 182 407 906 1967 4103 8187 15728 29550 55489 106425 211394 435528 922958 1988216 4308996 9326957
8 34 80 157 294 551 1038 1950 3634 6717 12348 22646 41504 75980 138614 251149 450308 796492 1386520 2371835 3983954
-6 -3 15 68 189 423 836 1550 2823 5196 9732 18375 34460 63408 113643 197771 334064 548295 875973 1365030 2079015
20 32 56 103 184 310 492 741 1068 1484 2000 2627 3376 4258 5284 6465 7812 9336 11048 12959 15080
13 26 66 145 274 462 712 1014 1335 1606 1706 1443 532 -1430 -4992 -10880 -20031 -33630 -53150 -80395 -117546
12 16 32 84 211 467 921 1657 2774 4386 6622 9626 13557 18589 24911 32727 42256 53732 67404 83536 102407
7 23 66 153 308 576 1051 1919 3517 6424 11651 21115 38810 73491 144388 292746 604513 1254817 2596354 5338361 10913870
17 26 41 68 129 269 563 1125 2131 3902 7175 13854 28828 63941 146002 331965 736249 1577770 3257753 6483824 12461119
20 30 56 107 198 360 650 1161 2032 3458 5700 9095 14066 21132 30918 44165 61740 84646 114032 151203 197630
0 -6 -17 -24 -7 75 298 787 1726 3360 5985 9922 15471 22841 32052 42805 54316 65110 72771 73644 62485
19 34 53 76 116 211 441 957 2045 4291 8996 19126 41284 89472 191784 401649 815839 1602184 3040807 5583720 9938820
4 -1 0 32 146 444 1128 2596 5625 11701 23587 46285 88693 166561 307939 563420 1025614 1866587 3410998 6281670 11693720
15 30 55 94 160 288 556 1126 2329 4840 10036 20736 42755 88199 182458 378976 790214 1651973 3455552 7215569 15003665
0 -5 -13 -17 -2 61 225 579 1262 2484 4576 8143 14529 27108 54533 118225 268384 616097 1394301 3068215 6527388
21 41 82 156 282 487 814 1340 2202 3624 5933 9547 14913 22368 31891 42709 52715 57651 50004 17558 -58460
25 36 41 47 83 223 621 1558 3501 7174 13641 24401 41495 67625 106285 161904 240001 347352 492169 684291 935387
14 37 73 138 275 569 1162 2268 4188 7325 12199 19462 29913 44513 64400 90904 125562 170133 226613 297250 384559
0 -5 -10 -15 -20 -25 -30 -35 -40 -45 -50 -55 -60 -65 -70 -75 -80 -85 -90 -95 -100
18 40 76 143 285 599 1287 2755 5795 11916 23947 47149 91316 174867 333008 634137 1212496 2331704 4504734 8713171 16794919
7 18 33 54 79 98 89 14 -185 -590 -1311 -2490 -4305 -6974 -10759 -15970 -22969 -32174 -44063 -59178 -78129
11 11 13 30 90 246 601 1358 2908 5977 11864 22809 42535 77053 136050 235979 408212 721139 1337516 2654482 5625835
24 49 104 203 359 592 945 1506 2428 3942 6384 10335 17167 30723 61753 138430 329304 790167 1854528 4200107 9142735
3 8 19 44 92 189 416 975 2290 5152 10926 21868 41673 76521 137145 242859 429109 761008 1356557 2424916 4327258
4 20 49 98 184 338 616 1124 2064 3808 7007 12742 22724 39550 67022 110536 177548 278124 425581 637226 935200
11 16 24 33 39 42 69 224 774 2282 5804 13188 27575 54344 103004 190924 350224 639347 1160147 2078478 3638934
14 32 69 139 259 456 782 1340 2325 4085 7208 12642 21856 37051 61431 99545 157712 244542 371567 553997 811617
-2 -2 12 56 162 407 968 2229 4989 10851 22911 46913 93091 178982 333565 603160 1059608 1811348 3018110 4910054 7812304
21 29 39 52 77 159 421 1122 2738 6082 12494 24159 44662 79979 140242 242794 417206 712882 1209188 2025725 3324402
-2 -4 -7 -3 25 105 287 688 1607 3760 8715 19675 42907 90433 185245 371578 735253 1443981 2827368 5536788 10868414
5 10 33 103 273 631 1327 2631 5037 9428 17317 31179 54889 94281 157843 257563 409941 637182 968585 1442143 2106369
7 13 26 63 156 367 823 1776 3702 7473 14671 28167 53171 99102 182906 335019 610305 1108441 2012048 3657355 6662686
14 30 47 65 82 93 90 61 -10 -133 -273 -250 470 3160 10482 27516 63310 133124 261575 486927 866810
0 -3 -10 -29 -56 -62 19 306 1001 2449 5251 10461 19907 36686 65894 115664 198598 333693 548876 884279 1396402
13 28 43 58 73 88 103 118 133 148 163 178 193 208 223 238 253 268 283 298 313
25 36 50 71 107 171 279 453 758 1447 3369 8924 24050 62057 150699 344900 749324 1557871 3121525 6061842 11454110
4 13 32 63 113 198 350 627 1126 1999 3472 5867 9627 15344 23790 35951 53064 76657 108592 151111 206885
9 33 68 122 220 417 815 1597 3109 6039 11761 22938 44522 85367 160804 296741 536177 949493 1650546 2821490 4750432
4 10 22 53 129 294 635 1340 2809 5850 12013 24155 47404 90822 170284 313426 568010 1015754 1794632 3133921 5407923
11 9 2 -9 -18 2 132 565 1710 4390 10227 22375 46861 94943 187142 360066 678053 1253455 2282820 4112523 7358424
-10 -6 17 74 181 351 590 893 1240 1592 1887 2036 1919 1381 228 -1777 -4918 -9530 -16003 -24786 -36391
27 50 83 126 179 242 315 398 491 594 707 830 963 1106 1259 1422 1595 1778 1971 2174 2387
2 12 36 73 129 231 462 1031 2387 5377 11435 22772 42516 74726 124175 195764 293392 418066 564990 719323 850243
13 35 70 121 191 287 428 663 1117 2111 4467 10240 24360 58086 135883 308552 677687 1441081 2978636 6020619 11989491
5 29 70 144 289 574 1109 2056 3641 6167 10028 15724 23877 35248 50755 71492 98749 134033 179090 235928 306841
22 42 85 161 280 452 687 995 1386 1870 2457 3157 3980 4936 6035 7287 8702 10290 12061 14025 16192
13 37 85 166 297 522 953 1850 3776 7896 16536 34179 69150 136331 261350 486805 881215 1551535 2660231 4448084 7264079
4 -4 -2 27 99 225 407 634 878 1090 1196 1093 645 -321 -2019 -4708 -8696 -14344 -22070 -32353 -45737
1 7 13 19 25 31 37 43 49 55 61 67 73 79 85 91 97 103 109 115 121
24 44 76 119 172 248 395 719 1410 2794 5490 10865 22178 47110 102809 225145 484564 1011728 2036984 3948547 7375008
18 35 62 94 136 228 491 1202 2901 6522 13521 25942 46310 77162 119920 172672 226248 257721 220032 25630 -479544
9 26 59 111 183 274 392 595 1100 2527 6389 16004 38100 85536 181863 369173 722534 1378883 2598862 4903168 9372460
11 37 83 154 266 459 810 1446 2557 4409 7357 11858 18484 27935 41052 58830 82431 113197 152663 202570 264878
10 14 34 88 214 496 1115 2433 5127 10416 20483 39314 74409 140282 265631 508144 985432 1940186 3877340 7849784 16042512
2 9 36 98 222 456 872 1558 2606 4140 6499 10808 20370 43675 100495 233729 531604 1167609 2468728 5024552 9846664
7 5 9 38 131 359 845 1794 3531 6552 11617 19963 33803 57420 99363 176460 320479 588213 1075805 1939698 3434027
-3 7 26 62 129 254 506 1074 2440 5718 13261 29675 63422 129243 251687 470093 845439 1469545 2477196 4061836 6495575
6 12 18 35 81 177 347 638 1192 2431 5468 12952 30738 71143 159309 345729 730982 1514298 3087518 6213025 12352235
26 43 77 147 288 563 1075 1979 3494 5915 9625 15107 22956 33891 48767 68587 94514 127883 170213 223219 288824
9 23 43 81 159 317 632 1263 2548 5192 10600 21426 42428 81740 152695 276358 484955 826413 1370257 2215143 3498341
9 22 31 37 49 85 167 313 547 980 2070 5262 14361 38229 95754 224554 495597 1036890 2070673 3970211 7344377
11 33 76 159 313 602 1164 2275 4434 8462 15617 27791 48060 82371 144294 267164 532755 1134976 2514665 5633815 12515751
17 21 24 26 27 27 26 24 21 17 12 6 -1 -9 -18 -28 -39 -51 -64 -78 -93
9 12 9 -2 -14 -4 83 367 1102 2829 6724 15391 34645 77424 172118 379775 828729 1782963 3775587 7868555 16158866
1 0 9 29 54 80 125 260 651 1612 3669 7635 14696 26508 45305 74018 116405 177192 262225 378633 535002
6 4 2 8 44 152 408 966 2178 4875 10950 24459 53552 113665 232548 457875 868382 1589710 2816394 4841738 8097652
9 23 62 142 287 534 942 1613 2753 4842 9060 18265 39112 86487 192583 425142 923397 1967249 4106934 8399320 16826385
16 23 46 106 239 514 1078 2257 4752 9989 20734 42209 84215 165294 320895 619043 1189419 2275534 4325877 8150883 15193278
10 9 -1 -17 -16 67 372 1162 2893 6316 12624 23660 42205 72368 120103 193881 305548 471403 713533 1061445 1554038
11 19 23 21 23 65 223 627 1475 3047 5719 9977 16431 25829 39071 57223 81531 113435 154583 206845 272327
11 23 53 129 296 621 1202 2195 3882 6825 12211 22622 43706 87655 180149 373736 772873 1579651 3175453 6263703 12114176
-1 -3 -2 16 86 269 648 1322 2427 4250 7557 14342 29357 63076 137304 295658 622899 1279963 2566028 5025708 9629292
13 13 10 -2 -21 -28 22 209 657 1543 3106 5656 9583 15366 23582 34915 50165 70257 96250 129346 170899
3 15 37 80 173 371 776 1596 3275 6741 13859 28269 56964 113246 222107 429622 818599 1533471 2818173 5071426 8924315
4 9 8 1 -2 28 147 448 1081 2311 4697 9602 20510 46142 107299 250961 577774 1293109 2797954 5844727 11795570
25 42 67 118 231 468 944 1897 3836 7829 16046 32755 66079 130948 253802 479689 882415 1578288 2743689 4636120 7617427
14 36 75 146 277 510 901 1531 2554 4322 7641 14226 27437 53392 102567 192007 348286 611368 1039535 1715562 2754333
-5 6 40 106 218 414 787 1525 2957 5604 10241 17990 30487 50205 81091 129836 208435 339366 565970 972814 1724484
6 3 9 48 161 411 893 1753 3225 5717 10024 17822 32699 62091 120575 234955 451340 843767 1522591 2638460 4373689
15 21 36 70 133 235 386 596 875 1233 1680 2226 2881 3655 4558 5600 6791 8141 9660 11358 13245
23 33 51 89 159 273 443 681 999 1409 1923 2553 3311 4209 5259 6473 7863 9441 11219 13209 15423
15 24 31 39 57 114 292 793 2063 5005 11330 24149 49069 96462 186504 360585 706895 1416642 2904797 6063523 12781761
13 40 81 147 273 548 1165 2496 5196 10338 19585 35433 61644 104182 173343 288434 487439 845780 1510745 2761663 5110755
13 25 37 46 58 109 307 906 2420 5797 12715 26149 51505 98839 186991 350881 653751 1206809 2199553 3945040 6945532
0 -6 -10 -5 22 100 291 714 1576 3210 6120 11033 18958 31252 49693 76560 114720 167722 239898 336471 463670
0 1 -1 -6 -14 -25 -39 -56 -76 -99 -125 -154 -186 -221 -259 -300 -344 -391 -441 -494 -550
2 -1 -2 13 77 265 729 1756 3874 8059 16151 31680 61440 118338 226328 428780 802914 1486164 2728269 5001239 9239357
26 40 56 79 111 151 202 298 576 1440 3917 10420 26345 63267 144973 318149 670134 1356592 2641942 4954485 8955747
3 10 41 120 290 627 1265 2437 4537 8208 14461 24830 41568 67889 108261 168755 257455 384934 564801 814324 1155134
14 33 55 74 95 147 304 722 1700 3773 7845 15370 28589 50831 86886 143458 229706 357881 544067 809034 1179211
15 37 86 181 358 679 1234 2141 3570 5849 9753 17131 32091 63039 125955 249387 481753 901661 1632088 2859401 4858356
2 16 45 105 221 427 766 1290 2060 3146 4627 6591 9135 12365 16396 21352 27366 34580 43145 53221 64977
15 27 37 58 130 331 799 1777 3699 7346 14121 26528 49013 89509 162531 295978 546916 1038429 2043527 4168957 8741395
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
19 41 72 112 161 219 286 362 447 541 644 756 877 1007 1146 1294 1451 1617 1792 1976 2169
-7 -8 8 51 124 235 425 815 1679 3563 7498 15404 30858 60508 116563 220982 412229 755762 1359788 2398249 4143512
7 16 35 74 156 326 660 1274 2333 4060 6745 10754 16538 24642 35714 50514 69923 94952 126751 166618 216008
8 5 8 25 69 165 353 682 1201 1989 3337 6310 14092 34793 86871 209194 479406 1047293 2195266 4447395 8763831
14 24 30 38 64 136 303 670 1505 3504 8355 19825 45742 101543 216699 446731 896635 1768371 3459847 6773799 13357499
11 10 10 21 63 168 388 819 1671 3444 7319 15969 35202 77295 167805 359473 760296 1589178 3283975 6707163 13530974
5 13 33 84 206 469 990 1975 3811 7242 13681 25752 48242 89796 165932 304311 553689 998619 1782769 3144676 5470854
-4 -5 -3 -1 4 32 134 417 1107 2714 6424 14930 34018 75315 160620 328062 639778 1189605 2107043 3549937 5672236
20 24 24 32 70 167 358 685 1200 1970 3084 4662 6866 9913 14090 19771 27436 37692 51296 69180 92478
9 12 30 92 241 534 1042 1850 3057 4776 7134 10272 14345 19522 25986 33934 43577 55140 68862 84996 103809
18 37 57 80 123 235 518 1150 2423 4837 9333 17805 34104 65837 127372 244587 462048 853469 1536497 2693078 4596897
13 33 78 165 321 589 1034 1755 2922 4889 8496 15776 31438 65715 139458 292734 598659 1184777 2264994 4185903 7492303
-2 6 19 36 55 73 86 89 76 40 -27 -134 -291 -509 -800 -1177 -1654 -2246 -2969 -3840 -4877
14 38 73 119 176 244 323 413 514 626 749 883 1028 1184 1351 1529 1718 1918 2129 2351 2584
5 3 5 25 93 256 592 1265 2674 5798 12931 29166 65276 143141 305730 635100 1284275 2532733 4881281 9211319 17047183
-3 -3 1 24 91 245 564 1188 2372 4621 9046 18229 38128 81924 177258 379108 791771 1605344 3155293 6019159 11174049
5 23 50 93 165 294 548 1079 2199 4520 9218 18518 36543 70725 134040 248402 449633 794517 1370546 2309075 3802721
19 32 55 104 206 399 732 1265 2069 3226 4829 6982 9800 13409 17946 23559 30407 38660 48499 60116 73714
-4 -4 4 21 42 57 64 112 399 1461 4506 11976 28473 62302 128168 252247 482409 909717 1714123 3260434 6295019
6 18 36 61 97 157 278 556 1217 2758 6232 13819 29927 63223 130271 262026 515676 996954 1903304 3608201 6824609
9 30 67 121 193 284 395 527 681 858 1059 1285 1537 1816 2123 2459 2825 3222 3651 4113 4609
12 5 -4 -13 -20 -23 -20 -9 12 45 92 155 236 337 460 607 780 981 1212 1475 1772
-2 2 19 65 169 381 789 1545 2910 5345 9703 17637 32485 61250 119140 240063 500670 1074228 2347719 5167713 11338385
21 37 56 78 107 164 318 754 1911 4736 11112 24529 51077 100849 189850 342515 594945 998975 1627192 2579024 3988023
11 24 53 106 185 286 415 643 1237 2921 7353 17977 41563 91037 190695 385672 758695 1458798 2748941 5082492 9222453
10 19 30 37 46 92 260 710 1706 3649 7114 12891 22030 35890 56192 85076 125162 179615 252214 347425 470478
4 7 23 68 180 429 923 1809 3268 5503 8719 13094 18740 25653 33651 42299 50820 57991 62023 60424 49844
26 53 96 163 281 519 1022 2061 4116 8038 15402 29305 56147 109464 217837 440608 898232 1829837 3701403 7408696 14659085
-8 -2 11 42 126 332 786 1733 3678 7660 15727 31694 62280 118734 219074 391077 676172 1134402 1850635 2942218 4568282
10 22 51 116 244 487 967 1971 4141 8853 18975 40365 84757 175160 355704 709274 1388765 2672256 5060462 9449432 17437899
15 32 57 101 204 446 965 2004 4026 7958 15651 30672 59575 113830 212621 386755 683953 1175820 1966813 3205543 5098758
14 18 32 70 155 340 737 1547 3091 5862 10652 18864 33219 59263 108486 204742 397534 789596 1593802 3248596 6646237
17 31 54 84 116 149 198 313 617 1392 3260 7528 16831 36443 77356 164169 355445 794257 1827106 4268652 9961370
3 22 67 145 254 392 575 859 1361 2274 3871 6493 10516 16292 24059 33815 45151 57038 67563 73609 70474
14 27 45 72 128 271 634 1495 3414 7499 15926 32979 67167 135533 272295 545819 1091322 2172971 4300619 8447566 16453590
10 20 44 92 183 345 615 1039 1672 2578 3830 5510 7709 10527 14073 18465 23830 30304 38032 47168 57875
19 38 75 144 283 583 1238 2628 5457 10979 21350 40133 72955 128302 218554 361903 587431 949724 1568577 2728286 5107675
3 12 38 103 238 483 887 1508 2413 3678 5388 7637 10528 14173 18693 24218 30887 38848 48258 59283 72098
20 42 83 151 254 400 597 853 1176 1574 2055 2627 3298 4076 4969 5985 7132 8418 9851 11439 13190
16 21 31 67 177 451 1051 2268 4610 8912 16441 28946 48575 77548 117437 167861 224356 275127 296331 245477 52461
16 15 21 56 163 419 953 1982 3902 7514 14541 28726 58047 119055 245250 503149 1022956 2056693 4087257 8030328 15602435
10 20 35 60 114 243 533 1123 2218 4102 7151 11846 18786 28701 42465 61109 85834 118024 159259 211328 276242
15 19 23 27 31 35 39 43 47 51 55 59 63 67 71 75 79 83 87 91 95
14 8 -3 -19 -40 -66 -97 -133 -174 -220 -271 -327 -388 -454 -525 -601 -682 -768 -859 -955 -1056
14 16 14 7 -6 -26 -54 -91 -138 -196 -266 -349 -446 -558 -686 -831 -994 -1176 -1378 -1601 -1846
21 40 61 94 169 339 682 1314 2435 4440 8145 15229 29124 56865 112927 226919 458261 922696 1837689 3596360 6882391
2 9 24 47 78 117 164 219 282 353 432 519 614 717 828 947 1074 1209 1352 1503 1662
18 39 70 109 156 208 258 317 489 1140 3213 8752 21709 49119 102739 201258 373196 660621 1123824 1847103 2945818
2 8 24 54 108 212 431 928 2093 4801 10925 24391 53406 115159 245503 518181 1081488 2225438 4500282 8918564 17289020
3 20 60 143 306 607 1132 2024 3574 6442 12108 23686 47265 93967 182930 345431 630357 1111208 1894772 3131545 5027876
12 36 75 136 246 465 899 1713 3144 5514 9243 14862 23026 34527 50307 71471 99300 135264 181035 238500 309774
19 32 45 58 71 84 97 110 123 136 149 162 175 188 201 214 227 240 253 266 279
12 26 40 54 68 82 96 110 124 138 152 166 180 194 208 222 236 250 264 278 292
11 19 30 59 141 351 828 1800 3607 6719 11746 19437 30665 46395 67632 95346 130371 173275 224198 282655 347301
8 6 4 2 0 -2 -4 -6 -8 -10 -12 -14 -16 -18 -20 -22 -24 -26 -28 -30 -32
10 15 15 2 -34 -104 -210 -316 -278 315 2473 8430 22707 53773 116505 235821 452390 832619 1487855 2612966 4563720
12 12 18 49 141 350 747 1415 2476 4207 7371 14029 29364 65506 149083 335340 733288 1548610 3154124 6201669 11794547
6 22 64 152 324 657 1297 2514 4826 9273 17979 35256 69772 138925 277940 559112 1132508 2310987 4744434 9769217 20093966
11 22 42 72 112 161 217 277 337 392 436 462 462 427 347 211 7 -278 -658 -1148 -1764
-7 -12 -21 -42 -81 -141 -224 -319 -331 133 2267 9125 27765 73581 179143 412320 913153 1967454 4149807 8592952 17479171
-9 -6 -1 -3 -17 -36 -21 148 774 2543 6916 16900 38546 83790 175685 357737 710017 1375988 2605465 4820519 8711817
26 36 49 75 137 293 671 1518 3264 6602 12585 22741 39207 64883 103607 160352 241446 354816 510257 719727 997669
14 15 18 32 82 220 533 1148 2234 4001 6696 10596 15998 23206 32515 44192 58454 75443 95198 117624 142458
-2 -2 0 7 29 82 191 417 938 2224 5375 12788 29584 66835 148874 329326 724781 1582691 3413771 7243900 15085694
3 3 9 21 35 41 30 31 223 1205 4559 13907 36743 87415 191740 393857 766059 1422495 2537797 4371865 7302235
""".strip().splitlines(False)
history = [list(map(int, line.split())) for line in input_lines]


# PART 1
def extrapolate(seq: list[int]):
    return seq[-1] + next_level_diff(seq, extrapolate)


def next_level_diff(seq: list[int], extrapolation_fn):
    diffs = [b - a for a, b in pairwise(seq)]
    if any(diffs):  # not all zeros
        return extrapolation_fn(diffs)
    return 0


# PART 2
def extrapolate_back(seq: list[int]):
    return seq[0] - next_level_diff(seq, extrapolate_back)


if __name__ == '__main__':
    print(f"Sum of extrapolated values: {sum(map(extrapolate, history))}")
    print(f"Sum of backwards extrapolated values: {sum(map(extrapolate_back, history))}")
