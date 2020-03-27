'''
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。
'''
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        if not words or not chars:
            return 0
        sumlen = 0
        d1, d2 = {}, {}
        for i in chars:
            d1.setdefault(i, 0)
            d1[i] += 1
        print(d1)
        for w in words:
            d2 = {}
            flag = True
            for j in w:
                d2.setdefault(j, 0)
                d2[j] += 1
            if (set(d1) & set(d2)) == set(d2):
                print(d2)
                for k in d2:
                    if d2[k] > d1[k]:
                        flag = False
                if flag:
                    sumlen += len(w)
        return sumlen

    # use collection
    def countCharacters1(self, words, chars):
        import collections
        ans = 0
        cnt = collections.Counter(chars)
        print(type(cnt))
        for w in words:
            c = collections.Counter(w)
            if all(c[i] <= cnt[i] for i in c):
                ans += len(w)
        return ans


# words = ["cat", "bt", "hat", "tree"]
# chars = "atach"
s = Solution()

words = ["jdimdfzbygjgdrsisgblztowvwzewvrwuizaihnctoonlykrbzncqvbzjahxvyswdzcbwaqliiyzbddtsxrwb",
         "ybdhccgznflezzvifoshbatwedohwwhyajylprerarbsjcll",
         "febacfxkrwnkyoyhykzbfuueohtkvqjkrmclmiinmpwhumaummpxjqmvqnvlwkmiizewfnqnmjqmnxacrhgxodyglvzyyii",
         "tcymwrytgfnbggzqptaqwzpkjhleisuwsfzhna",
         "rdvuvrrqerihadnurdfkzfiwtodnzcwvrmuwkyjhgkdjtnuwlclnhttidukyhfdzozix",
         "mjoryzsbvkqlmtmcmsjljloabfaliecpmmiumq", "iwzpczbknmqrankiypxjxthlzsvhchpqv", "dqpgxyspa",
         "igsvidvyonqyprvkoaphuvqaxcceefckypojgfdiyubagihkztnhindjcdpolt",
         "iamvwzvdbfonuurfdzcnvohqrpyxgmjvbyiyovvccsilkblgpojmwvhdsewldgzvdlnecfudjjkmgmil",
         "lbtjpakidwtavvtllcpekgcmqigmrfkvfjyzbxlpxtnklqrfoasnocjnlhzafcjqdjqgmuardsifyrlkvrndat",
         "tfqdhgvduounzgbdnipofenkqzqrlntcppwkk", "dwtuwpqugxvkjnhxvpxsdxyeurkldhxnpmicxmntiokhcclptbbbamzcrwachvzi",
         "pdnmdakvxnwdmibwqclesycgomztyowtjskvwiwuaumwubrmkli",
         "sxabmaciwtbbtwwawfhqisthjqxsxslsptcxqgsrzxiirxmzzmoulqmwzwatkrjqgpelkenulstuxwzjno",
         "enhtapuuyildahjyryubmjqdhbtfhjzhwppqbzriytu", "momfgjhyxzpsp",
         "hhdyxizwufxjewqvbforsauqgexpqgrhbmycwcaxbwldljuhclpyfawbhypinsfjepgded",
         "cgowwwhvlaziuptfsxqygxxnqxbregcwaodyklkkywpdtofrupmeeaeoemmpdwltdzbvebuzfumfdbdqu",
         "xspywgpzetvfdzeyterumsweldzsdarwshssaxlfgqqlckcyeealjqdfkjdncoivvgkmcvaod", "ubuubimfvxvplgikclwilovjdkns",
         "luzrzwfwzlunkwlvpjqpwckboxhgufsjlpmklxxtiuvlvaydkdvqumhiospabiemygntpfotocufttzzewkbxf",
         "mqqktykhjxtebccvpwttybgvkkxndvxfagdnjmbezlmdgw",
         "opcobbidwttpeisekgmowtgcozeinvfliqbkbrtkvwxdobavjyrknsadjijwybtbayfytxeotfp", "c", "cefqqjft",
         "ijavryhszfeevxvrcubkvpobxajzfjhnyffkdnucigmisvalwfngwahy", "pzfkcxeehzytxrtbdqqcoaccnqiynsjypfrcablnznvmthga",
         "tlekyalvnyxsvr", "jsahgkicszfcheyqafvflufycicegxclqpbmvmakjbhtuwhcxerxwspgzsrubfqblbhavlwfhx",
         "tvzrvrsnjetkoxbliawcvzzakpmhhvnjubczcpgobuqjqffsrdxtxjarzgsuryajuatcyfbroginvjhlauzbrkhssf",
         "dqbrdlmkhkrdzecilmfuavrphuxbqjo",
         "pmdpypebaobezmcfazewjbabjqjvrefyravwrvneyfpesbwnbbymuvovjvqgfwmzcsweifbpkuzicpjsj", "wfobqlvkmehlrh",
         "soormzqclvrrhftinorqqtfprxqufqsadalczqgbdnirkohqvzucsuunzjvbcfrryzztgy",
         "lfpvzygoenywdaddtsnrtmdhqnrkuyydwbwmzbwxzmoxwxvyttomlqdsekhyoaltxjhdtggwxrueelgh",
         "sikbegcpidcsnbierikpueovdqaxzis", "bchfnjcxqkfavrpotyghvhdzfsnigpgeuen",
         "igcpbhexbrhqgvzbjuvgehqrntbdfluouysupmtykobvkxzhumwxtntmbnyditvjmgoqtbiabkzfx",
         "xlgxysycbrskihoxiolefjhgdluugsuvvlhxlbqxzcqgqoxrmhmrylpfbarrplqgpvep",
         "oivjponqitutsacujnlmwotbeinwfygnzdzqet",
         "yktuffealtkznzvccxuzejpruspfldidkheondsmdbgwrabkmwgtbguayqhyiynfjfqgbpxoizlhottxeqbauj",
         "sxghynxeletecuqbafmqmlmiwlaenuujfipfkeylcyfjxkznpkc", "gxekcfwgn",
         "zitnbxgfpnzdoaahksuajugypfdlzwzadmksgtuqoevnqjkwoybabozgovuzlazwlopcuofwnqpkcpyupnh",
         "oydlvwonusmqypnlpwhdakzdoft", "kphotdvwvjypd",
         "cdcwreimmvstaytgnlwrdzumkilseqrorlsgzmmogjixszokypjalqmexhjesknsnpgjowypsno",
         "bbfbbepyutonbnmtbmmdrgxnhoifxluendcayelykgoglnrucegkhoczbajaobdggmusdbdllz",
         "tmelbseagubuvjjvpzkyvbxcyxzoxjvhcqwmesdwi",
         "twbedagexfuyyghuqxgwxmtbckchmiknghoaswufihzcmcdkyiqphjwpgpqsavoiiejfoqoucmvcahxmshu",
         "aqnipfzpclcsyuecagdfho", "cfcigrykqaeclkckntqkioexxvzvqfyirgqiwsbamtigxewdgpbhxsrwiofxzakvofqzbznbkfpfqpnns",
         "uoyzgkluftocnmbdrpyrmaywyyevbfcebzfxqljgigcgfmoeznqpkbmiwmziqlmdealiknlfzdwbadyjunth",
         "pniwsxvfxlsfhkhijuwcdvzahgzjmxdjpggcmynlfeitrggpgfudhfsswqaxapmkalrmiikrdcqyovqqyiasc", "hjoff",
         "zchyafrvstjxrpcrjtxrzqtgemtnbioizjvrsbmmwsqfcqtovk",
         "rqopixeyjdtwekhdilymtmbvpllrbcfkfojwyzgvhlhxvflywzqiiqlnwooudmwjtfikdgecxsbwxnmmyaxkqyxbqsgn",
         "jrjjoqkpqfjslcklltztyhkmrqmlmvjczidsswyhmyowxuunogxomhxtireakdfheffjaarcmonvxxuhvlnpujenrvjpsdrngsif",
         "oluqeooumhfdizvbmzzxznccypdfqeibvhhbbknqcvdryuiqzmheivglczcxcneypm",
         "odiyjnibfvnmojenjmtnawnnsatslheoqliyqtsmrxojxlsqep", "xodhotsxujcannmgvmszwnpvlyxrvfntk", "pal",
         "pfuaarkhepsjjtljpdhne", "cmravobrplecnohwhfcxbgsmkqkqjmdrpz", "rhwlfbsjnoileeuatpwpzxsqssfxbakasvvhrnfvsnji",
         "cprpqsoavnarqcyjhuxeeapjwkbrignbhgkufpdbentazdgfrjksrmbvcbwypcrh",
         "ouxsbfsvuihlhjcsiccibxvxtpwuzhrthhotbinvclelxhujtxqnpzoylzatzgdvawmfjwychqeopcrdjnejdtfkdign", "zhoel",
         "jwcdwcwlljltoiepktkflngdsqeagqwowkbopjzwbruhzntusrixinwvf", "amn",
         "zpcniceupkondvpyjbckasmevmoxquumalzrnhpxskxugik", "cvefdfpkcctzpipaodrygoaoesgvihhhthygs",
         "bkohexejlvylwkrykmmcgcf", "olpytsjqlkdpwi", "qsidlbvlccnjtyrupfxprlwhcynoyxlbrxjojkiqrsawbaumnzkdkzchommc",
         "ixnpbwnjtpqczoybczviqfbjtuxjdibzgispvxdnjppranzldirjcxut",
         "zlzvegbitlzahbmkectimwpbaletlxpcotygzvwridoiswxiuawtz",
         "fhptimdesuoqzjiblcwnhhbaxptzraksykvfpunxfufrwcmvqnwjocoiy",
         "aiyorgqnkvdopapcjpenkymhnynpkzyntylozbydnpibdrpbvcutpxudrcsizoyk",
         "nmuyeikwomlcripugwjypkfvbvizvrmndhsacmdocjjdhtnqvuxmgrcfeczuxsa",
         "geulhswpnmyweuswggltxsguxnnvecovqxvteiuadxgdksmjtitwcpzmbxicwvclkndttsduxb",
         "tbdazbskpejjkquorhfdafdvlgglefjhqguriqaefpvhcqscfhtvkimqvjzxtaf",
         "ldnnyerfedgsffdhpbmbwuubrzsjibafxqccryuljvusadrlfxqw",
         "meylutslakssulbpvfonrfmvugblinwzrfgopxafnwwdcuufjuaimxrbheehjndxbiohskmvjrmpcewvvvrbaqbkfffgbb",
         "ygjmeswiarqiwkpuzjsfnbabtvgapaoazzkuafcpuuavzmvvhcnwedpgbizznkygooedxjggbdkrgkcyaautpvwwnvlfwikyl",
         "mjgnewabmklmzwazyhcdoyqowpgrdcnuzwoha", "nljceveqjwgwmylmbgkawzjdvueoglyxdbpdyqpgwgtmixlkxphtltijcm",
         "maunpmlrxvreydzpzllevzlxpbkeeyrsskuhtklrnmpytaugdnuvgotmptgprsfcrcenxg",
         "wxqdzhmffyesnlbweaipjgjojsvvfmyyrsxjuqgyseuojmsemhgxalbbdiepwbizkf", "ricbkdxnkujtlgnuzcx",
         "gttdwdoclpkcejljedytqilnrpgsphfetbxztwihmhhspvyfdtbavl", "srmlsxsnohyy", "lpg",
         "qpmfbycwecpgnthstqwcdwrfxlykjteonfqvgqfxgyjmnqfh", "guojktcpspmbtsfucyze", "uhkpgnmkewkhymqyfzxbb",
         "qifzafbdvmjgfmzdotznlbzsllakihgzdpmwliwmmyoyovofyhxupehqjryccvzsejvnfebbyaxtwji",
         "xifotcwgywruiymsgmkamaaqnawvooilhqflxptbiewtzcufqvlldsxapunlbbzurwlegvspxhkjnivmeuxu",
         "ewpkblzobahkxvmaorqxotmlszkjlnbbqhgfeoymxntpsilzzmgknzkpgwanlajbagyxdaxvgg", "xuxovygmkcyukmtsfwquiw",
         "otvowenq", "thfd", "upypegljhttngfmnrwoqunnysvaauywjppaqlqayfcpajnirjgwjmaeyfpkexyfhdztctsctgfyoyi",
         "pypgyhubkosgpcsiucjvocobhfiayxjydpjakwpduaybk",
         "zskfzaqcegxmcxjyyraaaskmurewhpdgeccdiqdruevkipfynevvgdwpmevxolczrssveyf",
         "qazabogdtspviktvigfumcliotxzlfgqdmnwnejdyuiaxdrhjpzpodjmk", "qozbqbokeous", "gwlvoonxjrhvzyqmnlwfykqex",
         "uaumnvenxonkofoquxkbevxhinefttwiymaeecwzlknmzljzcldmmpekrnfdql",
         "xzrghwbgmljjbboonroxerqkbuygiouaylhkdauoagnizfndqzabdbycwa",
         "wrmcoohqyiwguwxntxlaxlrcambhvughnujvqxtvxuiyvvbgdsqukkdrprcxk",
         "kajvhekqzmmolchwsnhwsotawzndwpoxxcphjxvjhwyqhzffyilcvwin",
         "osnjdwvjwtqplvovigvmkkuvzvyrnqbfpliyhvtbquiyucvfxzrvupjsaxisiqvdvjuavclfmbeddvype", "aa",
         "hzvczfzpteogbzckschfxooyybkkyodaoncwlfjrrozjedbniwhmrxbxgvsknpjtntia",
         "mnsplhfonlxqrfaoiqbroqrtvjdurciceuyazjslbxkznbjsaaiaiumshqmcdjrzkzkxskoiacnlwuumchanvp", "y",
         "llusbfpxolpcuxqlxsxusxljtvzoaukhebnimpaczhdgtlpdzmmxvqi",
         "cxxpgjxrfajufcyljmtomctdloifssgmqpdxnvnojtbczsunjirzmpavidwgvcrwioubusmrprda",
         "elyrktioorsgpmdogctdzoyumidyhkrcxjpsnqcjzqacpzsockdmpbobd",
         "cwklazpkfcycsdfjmjryxlikfpcjnjvjwckghqzhgcyhrfbfetmbakpnzjuvgmfngqluuxqvgprdmcclrdwkazvjciecidp",
         "jxgoqngvvdqgfzdtnlppzlpyxissnjpbcfvvdlzztbzspiwfglqbmvvqnpiscxzdmclnervesecqyyuppzeqnfzpddjn",
         "itprgrhysrwmhhaawatgzcoifzidwsmbubyigwcewvfsxipilgmyjoabnhovsr",
         "sdvroatgoiowdqxcchbkxuabrrxqrwqwaamebflbubghhdujyvjtrqjhs", "lcizmwl",
         "zbycvvwywvprknqomewgnukldcvzehmailqnpabcehjrsespzmcchlfiutwqhlcgvwwzgftqnsmmlxdot",
         "ycfajupfdilekjptftutzfultpjrupvajbtphxuxjacorflgh",
         "voeqeuorsrbostmivapuxevtmilhzxpeswivyiqkflxgdwpdieptpvplailynqsakhfnoluw",
         "qhaqtselyauycemuspozlctffeurfclumidaildhczgorkrvydqcraxhstswypcjktjzyijgbmozwfk",
         "cifmzmjvtuwzrvszvlkrfbxdztjtwttqxvwtrrdflwraygcnncq", "tqwdkiowbbeobixyurrlgzejkvrgpatwdfbkmexu",
         "qmohzsrkypncpinlhthrrjgalqhemwdliueqrnqbjqk",
         "jmuafzdxuyawoopckcihbgibuieaipjjuvelngmdwyhkthoeslmatibnxkexgiasuemzbbagijhuekilhguanvsi",
         "mcfttopijlwyiqjfddidkbrrznxiggspgrzv",
         "wkmpshoyvpcavisaluywwuxwggyguwyrewlsdxuhomkcipelifkzyremrdqnxriaddpzpqzfvdwyiuhkiyxlekpskkzawv",
         "qhcgluzepldgtcsyfquniwdy", "sqoxryxxgzqsjclmuvqiqawuidtihogggxjfzkniqjpyjwatpmecziomfgdkis",
         "istjakvtyzzaelduexpmnthzwgkwnhqtfdblilypkxirpnlnqrsjffthjdtbfwhxueboquotzvccnexwcre",
         "lrydfbliheallvpxasjfjfzeehxkxrgabcofnwetcjueolpgexetfieksdkeopci",
         "tptyttbimmijjnbciadfkwspfofbufpjuxcxylcbfdzoiqtsybxehtrryakqyptjkkkcsiqboreoiovoekelnx",
         "zavzklwqyzokxnunkhjylukjqcsrvlkuxs", "rtqyhcfhucrqadultzlumazicdu", "ohobdcictit",
         "xfganyznjxztlenimrljgyifwypjvmcxmjpdwfgspiyoyjetbrtrtxktiobhnzts",
         "fuvsdvoviyyzqzxliebnxpawtmczyiylnzvbyfilmbbgjoseyxbqawi", "kqtwdwcgtbgzmzejvskhevbokzdvomkawvqmsfwdhbnqdxlgy",
         "eplegvqtvywmbqtndpdcbbylonvowepnneqlywrtnryudbqorjasivuwkszxzfwqdqozrbubjuovkxehkenmlorvavznwoxbbj",
         "qjlynqakaxhvmbtzaymetjsilvmxfxjnlspufjxffwksiuyztzklwzvocatawrewicebujfgpq",
         "mghamvubjtiuviceyccpejehmumtaeejraargsbvfxsgbhigjejuvreuvgbjtzbrzmsrsgjhblzqoz",
         "zzvkiqrtyfssalidbudmgpjadfnvewcjxxeizrrkv", "wrsegnaznxixzhyhdmslgcgslrcmyvclh",
         "fujynwgcgocsbkzuvvppknspbvnitwbxnaf",
         "lihsicgcjuablnfflwuwifcrfwiioafxxbbqwgzibnwhoxzhvmhbgjafvcumjgthiqiuacojuycejodzghucnpogjyykzitugkcr",
         "wibifkhjooviuxbpucnreszrshiyfgcfywfncxiaodriejwrkskkwlgwxmzkrzfz",
         "pgmogxujiwkgusbriztdkzkoirswmxwmjjeomcbzg", "xzoksdragbjecrmropprjbtglqcsxzxaxfthhlkrcshobyisrlv",
         "gfgfhiljcgckutrrectpweexqmqntccqekojlbxsnvmkiareesbazlgsmunbagbmurgwzmb",
         "kldgnhosnhqdfpplqbpujzcpozokvyopbasgvkcevcwsrxjpgaksxybqsofsxzsdeflphvzpzqioflitssplfheepdraeketdj",
         "lrkykfzbqohzghvriwmwrtgptfdgwoclaehxujswufkmmuebvtozbhrjtpcmrwufrsjupoedgqsubbbvlbtkosrfdthrxbcq", "cuvkc",
         "qomgdgmepyktyexunnhirbqnarfdf", "rmvppwtfmeteylqons", "vdiqiavnkoxxqazrphttqhlevygfylfiyjkbmk",
         "nbeawufkicbfhwdohjmhalwxvnexleiarewaklpyrleygvqftnmtwhpxcbiajearbckhydjstlvwfeywdwcu",
         "fnwwldvonsrbqyfwecjclbodmzrgydejnsbshzbzosptoyugmvizkupntxffjzyijcjvnxhuzez",
         "imqfboyfcmbzjduerhkitmpopdaroi",
         "cukchstrkftlgefvyzpsujetytoebujmhwkipdgizdkipjcpvzzchqqrmqylmcszvemjbzgketpkzbrxguanvjbpxok",
         "bvyuoyqyryyeviocouoxdckpotoaklhalkxppvxwvzaxwh",
         "hkjlnprhizooehppsjxbsrbaxyuszevcukvoqffczvonstjiinxtwgzngctnkpbrpeohbxemlcjjgdlcvtfdodpqavcxftmnczk",
         "twzzzushasnqjxzfdtizajegksbhljakizojgausnhkxdfrypiriwmrraqnrhloctrvukkqons",
         "bizlpbpvdkcbcavxogrkaxmzbsujecqphusdxlhprrfokhbkgeapghdclkfgutfhkckoozolsyequrgnrndybvofuzca", "uhlgrpshm",
         "fffblhiue", "uxfxwhhhzwubnpkshnetkvmokzsnalh",
         "xzbqhsjmkkxkpreqdrooiifvkrxquxwlpytwbmespaqdknxcwfhnjesuwdujghoxznrlxelmi",
         "ljbdlnpjvzbiywyjqmxdxbqiwqkkvqslfklugpzithhviczc",
         "kqhattassqwlrxhpzaytmazlyfgvbglxgiqnrrghdjoclhhleqqlwdeblsviwkciqehcjypozryajlngeqrloxufpuryncat",
         "kyptacgghycdhhnhmlndjaqsrtjudnhwixqvuamkaguagzacczyirfqarfuklvjf",
         "tsuinonhxpreonbxzaztfeffdcymrxngqeuthmzojldodqlhpxpremc", "bvejqokgmvsxfugorsldmalka",
         "fxlloyqelywmhiwdtxvtttddthfzbajrgeznmxxgmwzvtmnnwjebeylwjspxygveswxtzefrfhlyhyyambt",
         "wuhqhyxfpsoaoyssbjwjxqzhckfyfsvonlmyphloyoagoxycirdriaramwxsrswbxptxzvdjticaacwnx",
         "vtgnhypjamsfxyvnzghqrmntherndth", "fmavnsloegrtcibrbifuibqvjvusppgmprqmibm",
         "prfyttezajzqbcccrhqdevnazibcpznkxouwegpbbapxlrmhkfhoihv", "hoaerkgvqbhssdrujbrtmlvwbnhqx",
         "ozerhqqdwfwduyxrjmtxrevbdtgmwpbhkxqjsnlssmestosukzlglqdfi", "gthdnp",
         "nukyujeknoixksgludcsmxbbsrqjbpnbtvuawtbihdo", "xflmwpjo", "eb", "uujqhzyytjv",
         "jgowebswpjsggcahajdxzlratrocfghnplpkabnzitmhfhwspgshvpamgqpilgortzvzuoexbaxcalxsxlzsdejgjgihulwxoabq",
         "sytmzzwifklxsrpyldonjbqchisdjfhpmhzjea", "eithdxqoyza",
         "sqozuxpdhuaqttpwvyilgjtrtttlmeabuxacxhhjmxfpunzdmxeghuukyutlfkk",
         "njsirzxawbzktvdyrhxzjkqgnipmjffsabonsdmkinjwqhmwngwcravsctcuglkk",
         "dmbkpmbvcklftvucfzjfagowavptxbezhrnkrvnfhauhfrdnfnxuneznqnjlwxxyhfcxrq",
         "cwdnifexgdpqqecqwktngwzqtqvbcywdphfxfnzoavileuflvkcnzirqdkpulrvmgjrqjblwfjdqacmwzytcqrxrspmlleolt"]
chars = "owqugdlpqrnasodvbemfhuzctbibeboxgdklfyzyucomprzzoxwwxm"
print(s.countCharacters1(words, chars))
print(s.countCharacters1(words, ""))
print(s.countCharacters1("", chars))
