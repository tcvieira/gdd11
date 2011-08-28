Provinha de Progamação do Google Developer Dat 2011
===================================================

gdd1:
-----

Esses pergaminhos estão no antigo e misterioso idioma Googlon. Após muitos anos de estudo, os linguistas já conhecem algumas características desse idioma.
Primeiramente, as letras Googlon são classificadas em dois grupos: as letras r, x, w, j e m são chamadas "letras tipo foo", enquanto que as demais são conhecidas como "letras tipo bar".
Os linguistas descobriram que as preposições em Googlon são as palavras de 3 letras que não terminam numa letra tipo foo, mas onde não ocorre a letra l. Portanto, é fácil ver que existem 61 preposições no Texto A. E no Texto B, quantas preposições existem?

gdd2:
-----

Um outro fato interessante descoberto pelos linguistas é que, no Googlon, os verbos sempre são palavras de 8 ou mais letras que não terminam numa letra tipo foo. Além disso, se um verbo começa com uma letra tipo foo, o verbo está em primeira pessoa.
Assim, lendo o Texto A, é possível identificar 75 verbos no texto, dos quais 12 estão em primeira
pessoa.

gdd3.py
-------

Um professor universitário utilizará os textos A e B para ensinar o Googlon aos alunos. Para ajudar os alunos a compreender o texto, esse professor precisa criar uma lista de vocabulário para cada texto, isto é, uma lista ordenada (e sem repetições) das palavras que aparecem em cada um dos textos.
Essas listas devem estar ordenadas e não podem conter repetições de palavras. No Googlon, assim como no nosso alfabeto, as palavras são ordenadas lexicograficamente, mas o problema é que no Googlon, a ordem das letras no alfabeto é diferente da nossa. O alfabeto Googlon, em ordem, é vrxwfkphqljcnsmgtdbz. Assim, ao fazer essas listas, o professor deve respeitar a ordem alfabética Googlon.
O professor preparou a lista de vocabulário para o Texto A:

	vvm vvmqhlh vrkf vxrhk vxc vwvm vwht vklhsnvs vpgr vhx vhcls vhn vqfslkfz vldprhqx vjf vjkvxhfc vjh vjznkbwr vnzhw vmwpf vms vgtkrq vtrln vtfwzl vbhr vbmgc vzds vzbfvfj rvkvv rrr rrsptlbh rxm rxgkltrf rwh rwmbw rfmrnn rkkg rklmmsn rhvf rhkzznmr rhg rqtbc rlnkrjp rlsqvn rczrhs rnknfh rndjkd rnbsb rshsf rsnn rmwp rtfhbnm rtht rdn rdmr rdb rbjr rbmhdtq rbbjw rzxdmr xvv xrhtkgw xrtvfjk xxxx xwvwt xwcxkrwk xwdkxv xfrfj xfkqvggj xpgsm xpzwzkj xhjgm xhtwdx xlhqbhtz xldq xldlbzb xjpvvclw xcxrnxx xcd xswjkchz xsfk xsflsfs xsljrsf xsnbvpn xgnxwn xtcjnqx xbrgcwg wvqtj wvt wrz wxl wxsrjjc wwfdkfr wwgmhw wfwlfb wfq wprtjcw wphcsq wplw wpbcgz whlhvg whbcwc wqk wlpr wlhz wcjdqmx wnrd wnjrwt wsp wsjw wstsfpl wmmjg wmgh wmdvnv wgxhf wtf wblvm wbmhtwq wbggs wzrq wzffvpkn wzgj wzdwk fvw fvdnrctj frgk fxvj fxxzt fxfhwp fxczhkp fxspz fxmg fwwxsbjc fwfdpdcq fwhw fwqfjz fkcllw fplhghlf fpm fhkxwfvg fhkhkrv flhsq fcj fcdp fnw fnhkcftn fmgcsq fgqwwn fgnfvgv fdvtnkfc fdfpzn kvl kvb krjq kxtmmktl kwlnmzgk kwzcnwz kfbfhtx kkrwxp khl klx klkc klj klzlgdj kcbsksg ksfkv ksphpdgf ksldpm ksjjpmzs ksdpx kmmc kgpb ktxctzbv ktcflzhv kbv kbbhmrpt kbz kzs pvmjbh prxssdzj prkg przf pxvqjlgw pwklgdl pwqntn pwnzmtk pwmkf pwtgxpx pfvqq pplwqzf ppmvd pqgrt plxqlv pjwdnjsv pjf pjpkrh pjc pcnbmq pcdbfhlh pskd pspwbr pmwz pmh pgblh ptcctdjz pdptb pdhm pdb pbhgzd pzjftvpz pzcx pzsvfz pzmm hvrzqg hvpdm hvlhb hvtbdmqw hvdn hrb hxfmj hxqpnx hwbknxgn hkhbsqh hkc hpwzk hpsc hhqvs hhdlbrp hqvsrdf hqp hlxth hjv hjndwwdz hjtx hcnpt hcgr hnv hnlgzng hsgv hmhtjq htnvbf hbrpf hzkqjx hzsmwl hzdhjzrs qvpn qvhx qvqrmkm qrhhfbvf qxbnqc qwsbsvs qfkc qfqh qfjmb qfmmp qktmhz qpkjl qptxdvv qhbdzd qqszr qltdms qjxvvn qjgkzdtd qszhnl qmv qmpdvmt qmqmgdjg qmbp qmbqkblr qtdstx qdvj qzbdxs lvxkghw lvttwtvq lrsf lxjj lxspvzs lxg lwf lfbq lfbstj lkvmwgd lksmjbwq lkdms lkbdz lppkl lpchg lpsqgn lhnmjq lqp lqtjf lllzzj ljv ljfq ljkgrqm ljljnfm ljclsq lcwx lchfw lctp lnrmmhd lnfmqdj lntkhwx lsjvntbw lmxgkk lmz lgv lgnlfj lgbwhp ltrprnm ltn ldq ldmwj lzj lznxx jvwh jrqjs jxshqrg jwp jwzhtvkd jfgjdk jkxr jkjw jkscl jpxfc jpbwsrn jpzd jhx jqxnz jjqvq jctvs jslszfzj jmksrk jmtljb jmdt jgsp jtn jdrjkxx jdjrxw jdt jbm jbmct jzwmwwq jzht jzlxj jzmvvz jzgvsrtz cvf crsxrlbt cwvdgm cwstmnx cwd cfsm cfdtvzx ckpcx cktrvqpv chn cqcvsb cjm ccvxtn cnqr csmgwjbl cmbpcn cgbdpjh cgzgbqf cdgkxkd cdzmnw cbhlgnhp cbgxbgjp czqbj cztphth nrqdhch nrjhgz nrd nxbwprnc nwr nwqqnjkq nwd nfwbkt nkwkfn nhtgzhd nqmmncx nllxdlhx nlsmfds nltbmh njzc ncllht ncdmr nnrthfcl nnqnrdch nns nshlxtl nsgkpbcs nmdvqfk ngvhgcs ntkbf ntjg nbhtcrt nbthqd nzdgbfj srhcp sxlt swzgfl sfpbd skvjwpb sqlcfkbc sqct sjnz sjdh ssf sssdhz sstfprlj sgz stvftslx stp stlndmw stcrrdml stb sbkxjfvs sbkdvf szcnqncp szmp mvpxz mvj mvsrwkc mvzmnmqw mrnnz mxjzpr mwfqhlln mflwmfbx mkw mkhcltkv mpnhbnxb mpdcqkxr mhtv mhz mqbq mlm mnvrbq mnntj msfs msq mmrjz mgwwfck mgfx mtjjpr mtb mbdrh mzvwdnpq gvncb grn gwcv gknlj gpwwp gpjk ghpv gqhd gqlpxhr gqbtpkb gltrdj gjpmr gjbbwh gcm gcgcj gnxlzb gnfg gnhkkglf gnsfxq gntdd gmjjgxbd gmn gmtnxzwm gtvkjk gth gtqjqg gdcnbq gbhcfmmm gbswjrn gzw gzsppxlt gzsmq gzzkh tvw tvsfd tfz tpcndct thfbvklf thsk thgxppj tqrcvqr tqwmbvd tlr tjrhm tjqgxmv tjcsh tjdsz tckjwx tcjb tndlp tndz tsksjkf tsj tmsxtc tmt tmzq tgt tdq tznl tzdf drfpdz drlz dxssj dxdghj dkcmhjlh dkbk dpxndgk dhvrscbd dhrk dqvf dqwhpt dqcpqzbw dlfh dljrm dltnrq djmgslf djzzx dcgbtd dcdlktm dsj dsm dmlttwr dmjqjxpw dmjn dtf dtldhxr dzfw bvrhpc bvfvlvjp bvp bvbqwrq brrzlmt bkrhffgt bpfbcgz bpklgmnf bpmkg bpdjhw bhpc bhgwng bqrlzk bqw bqj bjwddmg bjjbpztg bjnnqmfj bjgqnsnl bjt bcpsgkpt bcn bng bsnj bsdktv bmlvkzw bmglc bttrt btdpjlz btzzxm bbljd bzfgb bzhsbth bzdmstvv bzblj bzznnzdd bzzbrtks zvjgrlzt zvtjvmv zrlktljv zxxhksnl zxc zwwvm zwtbsbpc zwdptkz zfhmwsd zptp zhgml zqtctfx zlphnj zclngtpl zccjp znrjr zsvgrrkr zscfjkls zmvsx zmr zmqkb zgpxccp ztlp ztcs zbkxhpbr zztgvdl zzd

gdd4.py:
--------

Mas como os Googlons escrevem números? Bem, no Googlon, as palavras também são números dados em base 20, onde cada letra é um dígito, e os dígitos são ordenados do menos significativo para o mais significativo (o inverso do nosso sistema). Ou seja, a primeira posição é a unidade, a segunda posição vale 20, a terceira vale 400, e assim por diante. Os valores das letras são dados pela ordem em que elas aparecem no alfabeto Googlon (que é diferente da nossa ordem, como vimos acima). Ou seja, a primeira letra do alfabeto Googlon representa o dígito 0, a segunda representa o dígito 1, e  assim por diante.
#alterar Por exemplo, a palavra ppj tem o valor numérico de 3999.
OBS: os números nesse problema podem ser grandes, então se você está usando um tipo de dados de tamanho limitado, tenha cuidado com possíveis overflows.
Os Googlons consideram um número bonito se ele satizfaz essas duas propriedades:

	- é maior ou igual a 574908
	- é divisível por 5

Ao consideramos o Texto A como uma lista de números (isto é, interpretando cada palavra como um número usando a convenção explicada acima), notamos que existem 69 números bonitos distintos.
E no Texto B, quantos números bonitos distintos existem?

