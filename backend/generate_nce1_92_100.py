#!/usr/bin/env python3
import json
import os

OUT = '/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/earthworm/nce1'
os.makedirs(OUT, exist_ok=True)

def V(eng, chn, sm):
    return {"english": eng, "chinese": chn, "soundmark": sm}

def S(chn, eng, sm, grammar):
    return {"chinese": chn, "english": eng, "soundmark": sm, "grammar": grammar}

def G(text, role, phonetic):
    return {"text": text, "role": role, "phonetic": phonetic}

# Lesson 92: Asking for information
L92 = [
    V("information", "信息", "/ˌɪnfərˈmeɪʃən/"),
    V("ask", "询问", "/æsk/"),
    V("direction", "方向", "/dəˈrekʃən/"),
    V("location", "位置", "/loʊˈkeɪʃən/"),
    V("polite", "礼貌的", "/pəˈlaɪt/"),
    V("excuse", "打扰", "/ɪkˈskjuːz/"),
    S("请问，图书馆在哪里？", "Excuse me, where is the library?", "/ɪkˈskjuːz miː, wer ɪz ðə ˈlaɪbrəri/",
      [G("Excuse", "V", "/ɪkˈskjuːz/"), G("me", "O", "/miː/"), G("where", "A", "/wer/"), G("is", "V", "/ɪz/"), G("the", "Art", "/ðə/"), G("library", "S", "/ˈlaɪbrəri/")]),
    S("你能告诉我怎么去火车站吗？", "Could you tell me how to get to the railway station?", "/kʊd juː tel miː haʊ tə get tə ðə ˈreɪlweɪ ˈsteɪʃən/",
      [G("Could", "V", "/kʊd/"), G("you", "S", "/juː/"), G("tell", "V", "/tel/"), G("me", "O", "/miː/"), G("how", "A", "/haʊ/"), G("to", "P", "/tə/"), G("get", "V", "/get/"), G("to", "P", "/tə/"), G("the", "Art", "/ðə/"), G("railway", "Det", "/ˈreɪlweɪ/"), G("station", "O", "/ˈsteɪʃən/")]),
    S("请问附近有银行吗？", "Is there a bank near here?", "/ɪz ðer ə bæŋk nɪr hɪr/",
      [G("Is", "V", "/ɪz/"), G("there", "S", "/ðer/"), G("a", "Art", "/ə/"), G("bank", "C", "/bæŋk/"), G("near", "P", "/nɪr/"), G("here", "A", "/hɪr/")]),
    S("我想问一下营业时间", "I'd like to ask about the business hours", "/aɪd laɪk tə æsk əˈbaʊt ðə ˈbɪznəs ˈaʊərz/",
      [G("I", "S", "/aɪ/"), G("'d", "V", "/d/"), G("like", "V", "/laɪk/"), G("to", "P", "/tə/"), G("ask", "V", "/æsk/"), G("about", "P", "/əˈbaʊt/"), G("the", "Art", "/ðə/"), G("business", "Det", "/ˈbɪznəs/"), G("hours", "O", "/ˈaʊərz/")]),
    S("打扰了，这附近有邮局吗？", "Excuse me, is there a post office around here?", "/ɪkˈskjuːz miː, ɪz ðer ə poʊst ˈɔːfɪs əˈraʊnd hɪr/",
      [G("Excuse", "V", "/ɪkˈskjuːz/"), G("me", "O", "/miː/"), G("is", "V", "/ɪz/"), G("there", "S", "/ðer/"), G("a", "Art", "/ə/"), G("post", "Det", "/poʊst/"), G("office", "C", "/ˈɔːfɪs/"), G("around", "P", "/əˈraʊnd/"), G("here", "A", "/hɪr/")]),
    V("stranger", "陌生人", "/ˈstreɪndʒər/"),
    V("helpful", "乐于助人的", "/ˈhelpfəl/"),
    V("address", "地址", "/əˈdres/"),
]

# Lesson 93: Narrow escape
L93 = [
    V("escape", "逃脱", "/ɪˈskeɪp/"),
    V("narrow", "狭窄的", "/ˈnæroʊ/"),
    V("accident", "事故", "/ˈæksɪdənt/"),
    V("brake", "刹车", "/breɪk/"),
    V("crash", "碰撞", "/kræʃ/"),
    V("lucky", "幸运的", "/ˈlʌki/"),
    S("他侥幸逃过了一场车祸", "He narrowly escaped a car accident", "/hiː ˈnæroʊli ɪˈskeɪpt ə kɑːr ˈæksɪdənt/",
      [G("He", "S", "/hiː/"), G("narrowly", "Adv", "/ˈnæroʊli/"), G("escaped", "V", "/ɪˈskeɪpt/"), G("a", "Art", "/ə/"), G("car", "Det", "/kɑːr/"), G("accident", "O", "/ˈæksɪdənt/")]),
    S("司机及时刹车避免了一场灾难", "The driver braked in time to avoid a disaster", "/ðə ˈdraɪvər breɪkt ɪn taɪm tə əˈvɔɪd ə dɪˈzæstər/",
      [G("The", "Art", "/ðə/"), G("driver", "S", "/ˈdraɪvər/"), G("braked", "V", "/breɪkt/"), G("in", "P", "/ɪn/"), G("time", "A", "/taɪm/"), G("to", "P", "/tə/"), G("avoid", "V", "/əˈvɔɪd/"), G("a", "Art", "/ə/"), G("disaster", "O", "/dɪˈzæstər/")]),
    S("那是一次九死一生的经历", "It was a narrow escape", "/ɪt wʌz ə ˈnæroʊ ɪˈskeɪp/",
      [G("It", "S", "/ɪt/"), G("was", "V", "/wʌz/"), G("a", "Art", "/ə/"), G("narrow", "Det", "/ˈnæroʊ/"), G("escape", "C", "/ɪˈskeɪp/")]),
    S("我们都很庆幸没有人受伤", "We were all relieved that no one was hurt", "/wiː wɜːr ɔːl rɪˈliːvd ðæt noʊ wʌn wʌz hɜːrt/",
      [G("We", "S", "/wiː/"), G("were", "V", "/wɜːr/"), G("all", "Adv", "/ɔːl/"), G("relieved", "V", "/rɪˈliːvd/"), G("that", "Conj", "/ðæt/"), G("no", "Det", "/noʊ/"), G("one", "S", "/wʌn/"), G("was", "V", "/wʌz/"), G("hurt", "V", "/hɜːrt/")]),
    S("真是太危险了！", "It was so dangerous!", "/ɪt wʌz soʊ ˈdeɪndʒərəs/",
      [G("It", "S", "/ɪt/"), G("was", "V", "/wʌz/"), G("so", "Adv", "/soʊ/"), G("dangerous", "C", "/ˈdeɪndʒərəs/")]),
    V("terrified", "恐惧的", "/ˈterɪfaɪd/"),
    V("relief", "宽慰", "/rɪˈliːf/"),
    V("close", "接近的", "/kloʊs/"),
]

# Lesson 94: Future plans
L94 = [
    V("future", "未来", "/ˈfjuːtʃər/"),
    V("plan", "计划", "/plæn/"),
    V("career", "职业", "/kəˈrɪr/"),
    V("goal", "目标", "/ɡoʊl/"),
    V("ambition", "抱负", "/æmˈbɪʃən/"),
    V("achieve", "实现", "/əˈtʃiːv/"),
    S("我打算明年去美国留学", "I plan to study in the USA next year", "/aɪ plæn tə ˈstʌdi ɪn ðə juːˌesˈeɪ nekst jɪr/",
      [G("I", "S", "/aɪ/"), G("plan", "V", "/plæn/"), G("to", "P", "/tə/"), G("study", "V", "/ˈstʌdi/"), G("in", "P", "/ɪn/"), G("the", "Art", "/ðə/"), G("USA", "O", "/juːˌesˈeɪ/"), G("next", "Det", "/nekst/"), G("year", "T", "/jɪr/")]),
    S("她的目标是成为一名医生", "Her goal is to become a doctor", "/hɜːr ɡoʊl ɪz tə bɪˈkʌm ə ˈdɑːktər/",
      [G("Her", "Det", "/hɜːr/"), G("goal", "S", "/ɡoʊl/"), G("is", "V", "/ɪz/"), G("to", "P", "/tə/"), G("become", "V", "/bɪˈkʌm/"), G("a", "Art", "/ə/"), G("doctor", "C", "/ˈdɑːktər/")]),
    S("他希望将来能自己创业", "He hopes to start his own business in the future", "/hiː hoʊps tə stɑːrt hɪz oʊn ˈbɪznəs ɪn ðə ˈfjuːtʃər/",
      [G("He", "S", "/hiː/"), G("hopes", "V", "/hoʊps/"), G("to", "P", "/tə/"), G("start", "V", "/stɑːrt/"), G("his", "Det", "/hɪz/"), G("own", "Det", "/oʊn/"), G("business", "O", "/ˈbɪznəs/"), G("in", "P", "/ɪn/"), G("the", "Art", "/ðə/"), G("future", "O", "/ˈfjuːtʃər/")]),
    S("我们计划买一栋新房子", "We are planning to buy a new house", "/wiː ɑːr ˈplænɪŋ tə baɪ ə nuː haʊs/",
      [G("We", "S", "/wiː/"), G("are", "V", "/ɑːr/"), G("planning", "V", "/ˈplænɪŋ/"), G("to", "P", "/tə/"), G("buy", "V", "/baɪ/"), G("a", "Art", "/ə/"), G("new", "Det", "/nuː/"), G("house", "O", "/haʊs/")]),
    S("他们打算明年结婚", "They intend to get married next year", "/ðeɪ ɪnˈtend tə get ˈmærid nekst jɪr/",
      [G("They", "S", "/ðeɪ/"), G("intend", "V", "/ɪnˈtend/"), G("to", "P", "/tə/"), G("get", "V", "/get/"), G("married", "V", "/ˈmærid/"), G("next", "Det", "/nekst/"), G("year", "T", "/jɪr/")]),
    V("opportunity", "机会", "/ˌɑːpərˈtuːnəti/"),
    V("preparation", "准备", "/ˌprepəˈreɪʃən/"),
    V("determination", "决心", "/dɪˌtɜːrmɪˈneɪʃən/"),
]

# Lesson 95: A taxi home
L95 = [
    V("taxi", "出租车", "/ˈtæksi/"),
    V("home", "家", "/hoʊm/"),
    V("driver", "司机", "/ˈdraɪvər/"),
    V("meter", "计价器", "/ˈmiːtər/"),
    V("fare", "车费", "/fer/"),
    V("tip", "小费", "/tɪp/"),
    S("我打车回家", "I took a taxi home", "/aɪ tʊk ə ˈtæksi hoʊm/",
      [G("I", "S", "/aɪ/"), G("took", "V", "/tʊk/"), G("a", "Art", "/ə/"), G("taxi", "O", "/ˈtæksi/"), G("home", "A", "/hoʊm/")]),
    S("司机按计价器收费", "The driver charged according to the meter", "/ðə ˈdraɪvər ˈtʃɑːrdʒd əˈkɔːrdɪŋ tə ðə ˈmiːtər/",
      [G("The", "Art", "/ðə/"), G("driver", "S", "/ˈdraɪvər/"), G("charged", "V", "/ˈtʃɑːrdʒd/"), G("according", "Adv", "/əˈkɔːrdɪŋ/"), G("to", "P", "/tə/"), G("the", "Art", "/ðə/"), G("meter", "O", "/ˈmiːtər/")]),
    S("我给了司机一些小费", "I gave the driver a tip", "/aɪ geɪv ðə ˈdraɪvər ə tɪp/",
      [G("I", "S", "/aɪ/"), G("gave", "V", "/geɪv/"), G("the", "Art", "/ðə/"), G("driver", "O", "/ˈdraɪvər/"), G("a", "Art", "/ə/"), G("tip", "O", "/tɪp/")]),
    S("车费比我预期的要贵", "The fare was more expensive than I expected", "/ðə fer wʌz mɔːr ɪkˈspensɪv ðæn aɪ ɪkˈspektɪd/",
      [G("The", "Art", "/ðə/"), G("fare", "S", "/fer/"), G("was", "V", "/wʌz/"), G("more", "Adv", "/mɔːr/"), G("expensive", "C", "/ɪkˈspensɪv/"), G("than", "Conj", "/ðæn/"), G("I", "S", "/aɪ/"), G("expected", "V", "/ɪkˈspektɪd/")]),
    S("到家时已经很晚了", "It was very late when I got home", "/ɪt wʌz ˈveri leɪt wen aɪ gɑːt hoʊm/",
      [G("It", "S", "/ɪt/"), G("was", "V", "/wʌz/"), G("very", "Adv", "/ˈveri/"), G("late", "C", "/leɪt/"), G("when", "Conj", "/wen/"), G("I", "S", "/aɪ/"), G("got", "V", "/gɑːt/"), G("home", "A", "/hoʊm/")]),
    V("traffic", "交通", "/ˈtræfɪk/"),
    V("rush hour", "高峰期", "/rʌʃ ˈaʊər/"),
    V("passenger", "乘客", "/ˈpæsɪndʒər/"),
]

# Lesson 96: The Olympic Games
L96 = [
    V("Olympic", "奥林匹克的", "/oʊˈlɪmpɪk/"),
    V("Games", "运动会", "/ɡeɪmz/"),
    V("athlete", "运动员", "/ˈæθliːt/"),
    V("medal", "奖牌", "/ˈmedəl/"),
    V("competition", "比赛", "/ˌkɑːmpəˈtɪʃən/"),
    V("champion", "冠军", "/ˈtʃæmpiən/"),
    S("奥运会每四年举办一次", "The Olympic Games are held every four years", "/ði oʊˈlɪmpɪk ɡeɪmz ɑːr held ˈevri fɔːr jɪrz/",
      [G("The", "Art", "/ði/"), G("Olympic", "Det", "/oʊˈlɪmpɪk/"), G("Games", "S", "/ɡeɪmz/"), G("are", "V", "/ɑːr/"), G("held", "V", "/held/"), G("every", "Det", "/ˈevri/"), G("four", "Det", "/fɔːr/"), G("years", "T", "/jɪrz/")]),
    S("他梦想获得奥运金牌", "He dreams of winning an Olympic gold medal", "/hiː driːmz əv ˈwɪnɪŋ ən oʊˈlɪmpɪk ɡoʊld ˈmedəl/",
      [G("He", "S", "/hiː/"), G("dreams", "V", "/driːmz/"), G("of", "P", "/əv/"), G("winning", "V", "/ˈwɪnɪŋ/"), G("an", "Art", "/ən/"), G("Olympic", "Det", "/oʊˈlɪmpɪk/"), G("gold", "Det", "/ɡoʊld/"), G("medal", "O", "/ˈmedəl/")]),
    S("运动员们为比赛刻苦训练", "The athletes train hard for the competition", "/ði ˈæθliːts treɪn hɑːrd fɔːr ðə ˌkɑːmpəˈtɪʃən/",
      [G("The", "Art", "/ði/"), G("athletes", "S", "/ˈæθliːts/"), G("train", "V", "/treɪn/"), G("hard", "Adv", "/hɑːrd/"), G("for", "P", "/fɔːr/"), G("the", "Art", "/ðə/"), G("competition", "O", "/ˌkɑːmpəˈtɪʃən/")]),
    S("她为祖国赢得了一枚银牌", "She won a silver medal for her country", "/ʃiː wʌn ə ˈsɪlvər ˈmedəl fɔːr hɜːr ˈkʌntri/",
      [G("She", "S", "/ʃiː/"), G("won", "V", "/wʌn/"), G("a", "Art", "/ə/"), G("silver", "Det", "/ˈsɪlvər/"), G("medal", "O", "/ˈmedəl/"), G("for", "P", "/fɔːr/"), G("her", "Det", "/hɜːr/"), G("country", "O", "/ˈkʌntri/")]),
    S("奥运会是世界上最大的体育盛事", "The Olympic Games are the greatest sporting event in the world", "/ði oʊˈlɪmpɪk ɡeɪmz ɑːr ðə ˈɡreɪtɪst ˈspɔːrtɪŋ ɪˈvent ɪn ðə wɜːrld/",
      [G("The", "Art", "/ði/"), G("Olympic", "Det", "/oʊˈlɪmpɪk/"), G("Games", "S", "/ɡeɪmz/"), G("are", "V", "/ɑːr/"), G("the", "Art", "/ðə/"), G("greatest", "Det", "/ˈɡreɪtɪst/"), G("sporting", "Det", "/ˈspɔːrtɪŋ/"), G("event", "C", "/ɪˈvent/"), G("in", "P", "/ɪn/"), G("the", "Art", "/ðə/"), G("world", "O", "/wɜːrld/")]),
    V("stadium", "体育场", "/ˈsteɪdiəm/"),
    V("opening ceremony", "开幕式", "/ˈoʊpənɪŋ ˈserəmoʊni/"),
    V("record", "记录", "/ˈrekɔːrd/"),
]

# Lesson 97: A small blue case
L97 = [
    V("small", "小的", "/smɔːl/"),
    V("blue", "蓝色的", "/bluː/"),
    V("case", "箱子", "/keɪs/"),
    V("belong", "属于", "/bɪˈlɔːŋ/"),
    V("owner", "主人", "/ˈoʊnər/"),
    V("return", "归还", "/rɪˈtɜːrn/"),
    S("这是一个小蓝箱子", "This is a small blue case", "/ðɪs ɪz ə smɔːl bluː keɪs/",
      [G("This", "S", "/ðɪs/"), G("is", "V", "/ɪz/"), G("a", "Art", "/ə/"), G("small", "Det", "/smɔːl/"), G("blue", "Det", "/bluː/"), G("case", "C", "/keɪs/")]),
    S("这个箱子属于谁？", "Who does this case belong to?", "/huː dʌz ðɪs keɪs bɪˈlɔːŋ tə/",
      [G("Who", "S", "/huː/"), G("does", "V", "/dʌz/"), G("this", "Det", "/ðɪs/"), G("case", "S", "/keɪs/"), G("belong", "V", "/bɪˈlɔːŋ/"), G("to", "P", "/tə/")]),
    S("我在地上发现了它", "I found it on the ground", "/aɪ faʊnd ɪt ɒn ðə ɡraʊnd/",
      [G("I", "S", "/aɪ/"), G("found", "V", "/faʊnd/"), G("it", "O", "/ɪt/"), G("on", "P", "/ɒn/"), G("the", "Art", "/ðə/"), G("ground", "O", "/ɡraʊnd/")]),
    S("让我们想办法找到主人", "Let's try to find the owner", "/lets traɪ tə faɪnd ðə ˈoʊnər/",
      [G("Let", "V", "/lets/"), G("'s", "O", "/s/"), G("try", "V", "/traɪ/"), G("to", "P", "/tə/"), G("find", "V", "/faɪnd/"), G("the", "Art", "/ðə/"), G("owner", "O", "/ˈoʊnər/")]),
    S("箱子可能是她的", "The case might be hers", "/ðə keɪs maɪt biː hɜːrz/",
      [G("The", "Art", "/ðə/"), G("case", "S", "/keɪs/"), G("might", "V", "/maɪt/"), G("be", "V", "/biː/"), G("hers", "C", "/hɜːrz/")]),
    V("lost", "丢失的", "/lɔːst/"),
    V("found", "被发现的", "/faʊnd/"),
    V("valuable", "有价值的", "/ˈvæljuəbəl/"),
]

# Lesson 98: Saying goodbye
L98 = [
    V("goodbye", "再见", "/ˌɡʊdˈbaɪ/"),
    V("farewell", "告别", "/ˌferˈwel/"),
    V("miss", "想念", "/mɪs/"),
    V("keep in touch", "保持联系", "/kiːp ɪn tʌtʃ/"),
    V("soon", "很快", "/suːn/"),
    V("visit", "拜访", "/ˈvɪzɪt/"),
    S("再见，祝你一路平安！", "Goodbye, have a safe journey!", "/ˌɡʊdˈbaɪ, həv ə seɪf ˈdʒɜːrni/",
      [G("Goodbye", "Int", "/ˌɡʊdˈbaɪ/"), G("have", "V", "/həv/"), G("a", "Art", "/ə/"), G("safe", "Det", "/seɪf/"), G("journey", "O", "/ˈdʒɜːrni/")]),
    S("我们会想念你的", "We will miss you", "/wiː wɪl mɪs juː/",
      [G("We", "S", "/wiː/"), G("will", "V", "/wɪl/"), G("miss", "V", "/mɪs/"), G("you", "O", "/juː/")]),
    S("请保持联系", "Please keep in touch", "/pliːz kiːp ɪn tʌtʃ/",
      [G("Please", "Adv", "/pliːz/"), G("keep", "V", "/kiːp/"), G("in", "P", "/ɪn/"), G("touch", "O", "/tʌtʃ/")]),
    S("希望很快能再见到你", "Hope to see you again soon", "/hoʊp tə siː juː əˈɡen suːn/",
      [G("Hope", "V", "/hoʊp/"), G("to", "P", "/tə/"), G("see", "V", "/siː/"), G("you", "O", "/juː/"), G("again", "Adv", "/əˈɡen/"), G("soon", "A", "/suːn/")]),
    S("欢迎随时来拜访我们", "You are welcome to visit us anytime", "/juː ɑːr ˈwelkəm tə ˈvɪzɪt ʌs ˈenɪtaɪm/",
      [G("You", "S", "/juː/"), G("are", "V", "/ɑːr/"), G("welcome", "C", "/ˈwelkəm/"), G("to", "P", "/tə/"), G("visit", "V", "/ˈvɪzɪt/"), G("us", "O", "/ʌs/"), G("anytime", "A", "/ˈenɪtaɪm/")]),
    V("memorable", "难忘的", "/ˈmemərəbəl/"),
    V("warm", "温暖的", "/wɔːrm/"),
    V("friendship", "友谊", "/ˈfrendʃɪp/"),
]

# Lesson 99: Ow!
L99 = [
    V("pain", "疼痛", "/peɪn/"),
    V("hurt", "受伤", "/hɜːrt/"),
    V("ouch", "哎哟", "/aʊtʃ/"),
    V("careful", "小心的", "/ˈkerfəl/"),
    V("wound", "伤口", "/wuːnd/"),
    V("bandage", "绷带", "/ˈbændɪdʒ/"),
    S("哎哟！我撞到脚趾了！", "Ow! I hit my toe!", "/aʊtʃ! aɪ hɪt maɪ toʊ/",
      [G("Ow", "Int", "/aʊtʃ/"), G("I", "S", "/aɪ/"), G("hit", "V", "/hɪt/"), G("my", "Det", "/maɪ/"), G("toe", "O", "/toʊ/")]),
    S("小心！那里很危险", "Be careful! It's dangerous there", "/biː ˈkerfəl! ɪts ˈdeɪndʒərəs ðer/",
      [G("Be", "V", "/biː/"), G("careful", "C", "/ˈkerfəl/"), G("It", "S", "/ɪt/"), G("'s", "V", "/s/"), G("dangerous", "C", "/ˈdeɪndʒərəs/"), G("there", "A", "/ðer/")]),
    S("你伤到自己了吗？", "Did you hurt yourself?", "/dɪd juː hɜːrt jʊrˈself/",
      [G("Did", "V", "/dɪd/"), G("you", "S", "/juː/"), G("hurt", "V", "/hɜːrt/"), G("yourself", "O", "/jʊrˈself/")]),
    S("我割伤了我的手指", "I cut my finger", "/aɪ kʌt maɪ ˈfɪŋɡər/",
      [G("I", "S", "/aɪ/"), G("cut", "V", "/kʌt/"), G("my", "Det", "/maɪ/"), G("finger", "O", "/ˈfɪŋɡər/")]),
    S("让我帮你包扎一下", "Let me help you bandage it", "/let miː help juː ˈbændɪdʒ ɪt/",
      [G("Let", "V", "/let/"), G("me", "O", "/miː/"), G("help", "V", "/help/"), G("you", "O", "/juː/"), G("bandage", "V", "/ˈbændɪdʒ/"), G("it", "O", "/ɪt/")]),
    V("medicine", "药", "/ˈmedɪsn/"),
    V("recover", "康复", "/rɪˈkʌvər/"),
    V("accident", "意外", "/ˈæksɪdənt/"),
]

# Lesson 100: A complaint
L100 = [
    V("complaint", "投诉", "/kəmˈpleɪnt/"),
    V("service", "服务", "/ˈsɜːrvɪs/"),
    V("manager", "经理", "/ˈmænɪdʒər/"),
    V("satisfied", "满意的", "/ˈsætɪsfaɪd/"),
    V("refund", "退款", "/ˈriːfʌnd/"),
    V("apologize", "道歉", "/əˈpɑːlədʒaɪz/"),
    S("我想投诉一下你们的服务", "I'd like to make a complaint about your service", "/aɪd laɪk tə meɪk ə kəmˈpleɪnt əˈbaʊt jʊr ˈsɜːrvɪs/",
      [G("I", "S", "/aɪ/"), G("'d", "V", "/d/"), G("like", "V", "/laɪk/"), G("to", "P", "/tə/"), G("make", "V", "/meɪk/"), G("a", "Art", "/ə/"), G("complaint", "O", "/kəmˈpleɪnt/"), G("about", "P", "/əˈbaʊt/"), G("your", "Det", "/jʊr/"), G("service", "O", "/ˈsɜːrvɪs/")]),
    S("我对产品很不满意", "I'm very dissatisfied with the product", "/aɪm ˈveri dɪsˈsætɪsfaɪd wɪð ðə ˈprɑːdʌkt/",
      [G("I", "S", "/aɪ/"), G("'m", "V", "/m/"), G("very", "Adv", "/ˈveri/"), G("dissatisfied", "C", "/dɪsˈsætɪsfaɪd/"), G("with", "P", "/wɪð/"), G("the", "Art", "/ðə/"), G("product", "O", "/ˈprɑːdʌkt/")]),
    S("经理为此道歉了", "The manager apologized for this", "/ðə ˈmænɪdʒər əˈpɑːlədʒaɪzd fɔːr ðɪs/",
      [G("The", "Art", "/ðə/"), G("manager", "S", "/ˈmænɪdʒər/"), G("apologized", "V", "/əˈpɑːlədʒaɪzd/"), G("for", "P", "/fɔːr/"), G("this", "O", "/ðɪs/")]),
    S("他们答应给我退款", "They promised to give me a refund", "/ðeɪ ˈprɑːmɪst tə ɡɪv miː ə ˈriːfʌnd/",
      [G("They", "S", "/ðeɪ/"), G("promised", "V", "/ˈprɑːmɪst/"), G("to", "P", "/tə/"), G("give", "V", "/ɡɪv/"), G("me", "O", "/miː/"), G("a", "Art", "/ə/"), G("refund", "O", "/ˈriːfʌnd/")]),
    S("希望问题能尽快解决", "I hope the problem can be resolved soon", "/aɪ hoʊp ðə ˈprɑːbləm kæn biː rɪˈzɑːlvd suːn/",
      [G("I", "S", "/aɪ/"), G("hope", "V", "/hoʊp/"), G("the", "Art", "/ðə/"), G("problem", "S", "/ˈprɑːbləm/"), G("can", "V", "/kæn/"), G("be", "V", "/biː/"), G("resolved", "V", "/rɪˈzɑːlvd/"), G("soon", "A", "/suːn/")]),
    V("frustrated", "沮丧的", "/ˈfrʌstreɪtɪd/"),
    V("unacceptable", "不可接受的", "/ˌʌnəkˈseptəbəl/"),
    V("solution", "解决方案", "/səˈluːʃən/"),
]

lessons = {
    '092.json': L92,
    '093.json': L93,
    '094.json': L94,
    '095.json': L95,
    '096.json': L96,
    '097.json': L97,
    '098.json': L98,
    '099.json': L99,
    '100.json': L100,
}

for filename, lesson in lessons.items():
    filepath = os.path.join(OUT, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)
    print(f'✅ {filename}: {len(lesson)} entries')

print('\n✅ NCE1 L92-100 完成！')
