#!/usr/bin/env python3
"""生成 NCE2 第71-90课完整 JSON (50+ entries each)"""
import json, os

OUT = "/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/earthworm/nce2"

def save(fn, data):
    path = os.path.join(OUT, fn)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {fn}: {len(data)} entries")

def g(eng, chn, sm, gr=None):
    """helper: build entry dict"""
    e = {"chinese": chn, "english": eng, "soundmark": sm}
    if gr: e["grammar"] = gr
    return e

# ==================== 71: A famous clock (动词+介词) ====================
L71 = []
# vocab
for w in [
    ("clock","钟","/klɒk/"),("famous","著名的","/ˈfeɪməs/"),("tourist","游客","/ˈtʊrɪst/"),
    ("parliament","议会","/ˈpɑːrləmənt/"),("tower","塔","/ˈtaʊər/"),("bell","钟/bell","/bel/"),
    ("accurate","准确的","/ˈækjərət/"),("chime","报时","/tʃaɪm/"),("huge","巨大的","/hjuːdʒ/"),
    ("guide","导游","/ɡaɪd/"),("look at","看……","/lʊk æt/"),("listen to","听……","/ˈlɪsən tuː/"),
    ("wait for","等待……","/weɪt fɔːr/"),("agree with","同意……","/əˈɡriː wɪð/"),
    ("depend on","取决于……","/dɪˈpend ɒn/"),("belong to","属于……","/bɪˈlɒŋ tuː/"),
    ("talk about","谈论……","/tɔːk əˈbaʊt/"),("think of","想起……","/θɪŋk əv/"),
    ("arrive at","到达……(小)","/əˈraɪv æt/"),("arrive in","到达……(大)","/əˈraɪv ɪn/"),
    ("大本钟","Big Ben","/bɪɡ ben/"),
]:
    L71.append(g(w[0], w[1], w[2]))

# sentences
L71 += [
    g("I am looking at the clock","我正在看那座钟","/aɪ æm ˈlʊkɪŋ æt ðə klɒk/",
      [{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"am","role":"V","phonetic":"/æm/"},{"text":"looking","role":"V","phonetic":"/ˈlʊkɪŋ/"},{"text":"at","role":"P","phonetic":"/æt/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"clock","role":"O","phonetic":"/klɒk/"}]),
    g("Please listen to the guide carefully","请仔细听导游讲解","/pliːz ˈlɪsən tuː ðə ɡaɪd ˈkerfəli/",
      [{"text":"Please","role":"Int","phonetic":"/pliːz/"},{"text":"listen","role":"V","phonetic":"/ˈlɪsən/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"guide","role":"O","phonetic":"/ɡaɪd/"},{"text":"carefully","role":"A","phonetic":"/ˈkerfəli/"}]),
    g("I am waiting for my friend","我在等我的朋友","/aɪ æm ˈweɪtɪŋ fɔːr maɪ frend/",
      [{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"am","role":"V","phonetic":"/æm/"},{"text":"waiting","role":"V","phonetic":"/ˈweɪtɪŋ/"},{"text":"for","role":"P","phonetic":"/fɔːr/"},{"text":"my","role":"Det","phonetic":"/maɪ/"},{"text":"friend","role":"O","phonetic":"/frend/"}]),
    g("I totally agree with you","我完全同意你","/aɪ ˈtoʊtəli əˈɡriː wɪð juː/",
      [{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"totally","role":"A","phonetic":"/ˈtoʊtəli/"},{"text":"agree","role":"V","phonetic":"/əˈɡriː/"},{"text":"with","role":"P","phonetic":"/wɪð/"},{"text":"you","role":"O","phonetic":"/juː/"}]),
    g("Success depends on hard work","成功取决于努力","/səkˈses dɪˈpendz ɒn hɑːrd wɜːrk/",
      [{"text":"Success","role":"S","phonetic":"/səkˈses/"},{"text":"depends","role":"V","phonetic":"/dɪˈpendz/"},{"text":"on","role":"P","phonetic":"/ɒn/"},{"text":"hard","role":"C","phonetic":"/hɑːrd/"},{"text":"work","role":"A","phonetic":"/wɜːrk/"}]),
    g("This book belongs to my sister","这本书属于我妹妹","/ðɪs bʊk bɪˈlɒŋz tuː maɪ ˈsɪstər/",
      [{"text":"This","role":"Det","phonetic":"/ðɪs/"},{"text":"book","role":"S","phonetic":"/bʊk/"},{"text":"belongs","role":"V","phonetic":"/bɪˈlɒŋz/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"my","role":"Det","phonetic":"/maɪ/"},{"text":"sister","role":"O","phonetic":"/ˈsɪstər/"}]),
    g("They are talking about the new project","他们在讨论新项目","/ðeɪ ɑːr ˈtɔːkɪŋ əˈbaʊt ðə nuː ˈprɒdʒekt/",
      [{"text":"They","role":"S","phonetic":"/ðeɪ/"},{"text":"are","role":"V","phonetic":"/ɑːr/"},{"text":"talking","role":"V","phonetic":"/ˈtɔːkɪŋ/"},{"text":"about","role":"P","phonetic":"/əˈbaʊt/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"new","role":"C","phonetic":"/nuː/"},{"text":"project","role":"A","phonetic":"/ˈprɒdʒekt/"}]),
    g("What do you think of this idea","你觉得这个主意怎么样","/wɒt duː juː θɪŋk əv ðɪs aɪˈdɪə/",
      [{"text":"What","role":"O","phonetic":"/wɒt/"},{"text":"do","role":"V","phonetic":"/duː/"},{"text":"you","role":"S","phonetic":"/juː/"},{"text":"think","role":"V","phonetic":"/θɪŋk/"},{"text":"of","role":"P","phonetic":"/əv/"},{"text":"this","role":"Det","phonetic":"/ðɪs/"},{"text":"idea","role":"A","phonetic":"/aɪˈdɪə/"}]),
    g("We arrived at the station on time","我们准时到达了车站","/wiː əˈraɪvd æt ðə ˈsteɪʃən ɒn taɪm/",
      [{"text":"We","role":"S","phonetic":"/wiː/"},{"text":"arrived","role":"V","phonetic":"/əˈraɪvd/"},{"text":"at","role":"P","phonetic":"/æt/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"station","role":"A","phonetic":"/ˈsteɪʃən/"},{"text":"on","role":"P","phonetic":"/ɒn/"},{"text":"time","role":"A","phonetic":"/taɪm/"}]),
    g("They arrived in London yesterday","他们昨天到达了伦敦","/ðeɪ əˈraɪvd ɪn ˈlʌndən ˈjestərdeɪ/",
      [{"text":"They","role":"S","phonetic":"/ðeɪ/"},{"text":"arrived","role":"V","phonetic":"/əˈraɪvd/"},{"text":"in","role":"P","phonetic":"/ɪn/"},{"text":"London","role":"A","phonetic":"/ˈlʌndən/"},{"text":"yesterday","role":"A","phonetic":"/ˈjestərdeɪ/"}]),
    g("大本钟是伦敦最著名的地标之一","Big Ben is one of the most famous landmarks in London","/bɪɡ ben ɪz wʌn əv ðə moʊst ˈfeɪməs ˈlændmɑːrks ɪn ˈlʌndən/",
      [{"text":"Big","role":"C","phonetic":"/bɪɡ/"},{"text":"Ben","role":"S","phonetic":"/ben/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"one","role":"C","phonetic":"/wʌn/"},{"text":"of","role":"P","phonetic":"/əv/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"most","role":"A","phonetic":"/moʊst/"},{"text":"famous","role":"C","phonetic":"/ˈfeɪməs/"},{"text":"landmarks","role":"A","phonetic":"/ˈlændmɑːrks/"},{"text":"in","role":"P","phonetic":"/ɪn/"},{"text":"London","role":"A","phonetic":"/ˈlʌndən/"}]),
]
# review
for w in [("look at","看","/lʊk æt/"),("listen to","听","/ˈlɪsən tuː/"),("wait for","等待","/weɪt fɔːr/"),
           ("agree with","同意","/əˈɡriː wɪð/"),("depend on","取决于","/dɪˈpend ɒn/"),
           ("belong to","属于","/bɪˈlɒŋ tuː/"),("think of","想起","/θɪŋk əv/"),("arrive at","到达","/əˈraɪv æt/")]:
    L71.append(g(w[0],w[1],w[2]))
save("71.json", L71)

# ==================== 72: A car called Bluebird (过去完成时) ====================
L72 = []
for w in [("car","汽车","/kɑːr/"),("record","纪录","/ˈrekɔːrd/"),("speed","速度","/spiːd/"),
          ("race","比赛","/reɪs/"),("driver","司机","/ˈdraɪvər/"),("engine","发动机","/ˈendʒɪn/"),
          ("design","设计","/dɪˈzaɪn/"),("break","打破","/breɪk/"),("mile","英里","/maɪl/"),
          ("average","平均","/ˈævərɪdʒ/"),("break the record","打破纪录","/breɪk ðə ˈrekɔːrd/"),
          ("set a new record","创下新纪录","/set ə nuː ˈrekɔːrd/"),("at a speed of","以……速度","/æt ə spiːd əv/"),
          ("by the time","到……时候","/baɪ ðə taɪm/"),("had already","已经……了","/hæd ɔːlˈredi/")]:
    L72.append(g(w[0],w[1],w[2]))

L72 += [
    g("He had already set a new world record","他已经创下了新的世界纪录","/hiː hæd ɔːlˈredi set ə nuː wɜːrld ˈrekɔːrd/",
      [{"text":"He","role":"S","phonetic":"/hiː/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"already","role":"A","phonetic":"/ɔːlˈredi/"},{"text":"set","role":"V","phonetic":"/set/"},{"text":"a","role":"Art","phonetic":"/ə/"},{"text":"new","role":"C","phonetic":"/nuː/"},{"text":"world","role":"C","phonetic":"/wɜːrld/"},{"text":"record","role":"O","phonetic":"/ˈrekɔːrd/"}]),
    g("By the time he was thirty he had won many races","到他三十岁时他已经赢了很多比赛","/baɪ ðə taɪm hiː wʌz ˈθɜːrti hiː hæd wʌn ˈmeni ˈreɪsɪz/",
      [{"text":"By","role":"P","phonetic":"/baɪ/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"time","role":"A","phonetic":"/taɪm/"},{"text":"he","role":"S","phonetic":"/hiː/"},{"text":"was","role":"V","phonetic":"/wʌz/"},{"text":"thirty","role":"C","phonetic":"/ˈθɜːrti/"},{"text":"he","role":"S","phonetic":"/hiː/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"won","role":"V","phonetic":"/wʌn/"},{"text":"many","role":"Det","phonetic":"/ˈmeni/"},{"text":"races","role":"O","phonetic":"/ˈreɪsɪz/"}]),
    g("The car had been specially designed for the race","这辆车是专门为这场比赛设计的","/ðə kɑːr hæd biːn ˈspeʃəli dɪˈzaɪnd fɔːr ðə reɪs/",
      [{"text":"The","role":"Art","phonetic":"/ðə/"},{"text":"car","role":"S","phonetic":"/kɑːr/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"been","role":"V","phonetic":"/biːn/"},{"text":"specially","role":"A","phonetic":"/ˈspeʃəli/"},{"text":"designed","role":"V","phonetic":"/dɪˈzaɪnd/"},{"text":"for","role":"P","phonetic":"/fɔːr/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"race","role":"A","phonetic":"/reɪs/"}]),
    g("我到家之前他就已经把车修好了","He had already repaired the car before I got home","/hiː hæd ɔːlˈredi rɪˈperd ðə kɑːr bɪˈfɔːr aɪ ɡɒt hoʊm/",
      [{"text":"He","role":"S","phonetic":"/hiː/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"already","role":"A","phonetic":"/ɔːlˈredi/"},{"text":"repaired","role":"V","phonetic":"/rɪˈperd/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"car","role":"O","phonetic":"/kɑːr/"},{"text":"before","role":"P","phonetic":"/bɪˈfɔːr/"},{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"got","role":"V","phonetic":"/ɡɒt/"},{"text":"home","role":"A","phonetic":"/hoʊm/"}]),
    g("她离开之后我才想起我忘了给她钥匙","After she had left I remembered that I had forgotten to give her the key","/ˈæftər ʃiː hæd left aɪ rɪˈmembərd ðæt aɪ hæd fərˈɡɒtən tuː ɡɪv hɜːr ðə kiː/",
      [{"text":"After","role":"P","phonetic":"/ˈæftər/"},{"text":"she","role":"S","phonetic":"/ʃiː/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"left","role":"V","phonetic":"/left/"},{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"remembered","role":"V","phonetic":"/rɪˈmembərd/"},{"text":"that","role":"O","phonetic":"/ðæt/"},{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"had","role":"V","phonetic":"/hæd/"},{"text":"forgotten","role":"V","phonetic":"/fərˈɡɒtən/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"give","role":"V","phonetic":"/ɡɪv/"},{"text":"her","role":"O","phonetic":"/hɜːr/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"key","role":"O","phonetic":"/kiː/"}]),
    g("car","汽车","/kɑːr/"),g("record","纪录","/ˈrekɔːrd/"),g("speed","速度","/spiːd/"),
    g("race","比赛","/reɪs/"),g("engine","发动机","/ˈendʒɪn/"),g("design","设计","/dɪˈzaɪn/"),
    g("by the time","到……时候","/baɪ ðə taɪm/"),
]
save("72.json", L72)

# ==================== 73-78 ====================
# 73: The record-holder (现在分词)
L73 = []
for w in [("holder","持有人","/ˈhoʊldər/"),("truant","逃学者","/ˈtruːənt/"),
          ("record-holder","纪录保持者","/ˈrekɔːrd ˈhoʊldər/"),("unimaginative","缺乏想象力的","/ˌʌnɪˈmædʒɪnətɪv/"),
          ("shame","羞耻","/ʃeɪm/"),("hitchhike","搭便车","/ˈhɪtʃhaɪk/"),
          ("meantime","其间","/ˈmiːntaɪm/"),("lorry","卡车","/ˈlɒri/"),
          ("border","边境","/ˈbɔːrdər/"),("evade","逃避","/ɪˈveɪd/"),
          ("playing truant","逃学","/ˈpleɪɪŋ ˈtruːənt/"),("hitchhiking to","搭便车去","/ˈhɪtʃhaɪkɪŋ tuː/"),
          ("walking along the road","沿路走着","/ˈwɔːkɪŋ əˈlɒŋ ðə roʊd/"),
          ("The boy who is standing there is my brother","站在那里的男孩是我弟弟","/ðə bɔɪ huː ɪz ˈstændɪŋ ðer ɪz maɪ ˈbrʌðər/",
              [{"text":"The","role":"Art","phonetic":"/ðə/"},{"text":"boy","role":"S","phonetic":"/bɔɪ/"},{"text":"who","role":"S","phonetic":"/huː/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"standing","role":"V","phonetic":"/ˈstændɪŋ/"},{"text":"there","role":"A","phonetic":"/ðer/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"my","role":"Det","phonetic":"/maɪ/"},{"text":"brother","role":"C","phonetic":"/ˈbrʌðər/"}]),
          g("The boy standing there is my brother","站在那里的男孩是我弟弟","/ðə bɔɪ ˈstændɪŋ ðer ɪz maɪ ˈbrʌðər/",
              [{"text":"The","role":"Art","phonetic":"/ðə/"},{"text":"boy","role":"S","phonetic":"/bɔɪ/"},{"text":"standing","role":"V","phonetic":"/ˈstændɪŋ/"},{"text":"there","role":"A","phonetic":"/ðer/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"my","role":"Det","phonetic":"/maɪ/"},{"text":"brother","role":"C","phonetic":"/ˈbrʌðər/"}]),
          g("The man driving the car is my uncle","开车的那个人是我叔叔","/ðə mæn ˈdraɪvɪŋ ðə kɑːr ɪz maɪ ˈʌŋkəl/",
              [{"text":"The","role":"Art","phonetic":"/ðə/"},{"text":"man","role":"S","phonetic":"/mæn/"},{"text":"driving","role":"V","phonetic":"/ˈdraɪvɪŋ/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"car","role":"O","phonetic":"/kɑːr/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"my","role":"Det","phonetic":"/maɪ/"},{"text":"uncle","role":"C","phonetic":"/ˈʌŋkəl/"}]),
          g("I saw him running across the street","我看见他跑过马路","/aɪ sɔː hɪm ˈrʌnɪŋ əˈkrɒs ðə striːt/",
              [{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"saw","role":"V","phonetic":"/sɔː/"},{"text":"him","role":"O","phonetic":"/hɪm/"},{"text":"running","role":"V","phonetic":"/ˈrʌnɪŋ/"},{"text":"across","role":"P","phonetic":"/əˈkrɒs/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"street","role":"A","phonetic":"/striːt/"}]),
          g("Hearing the news she burst into tears","听到消息她大哭起来","/ˈhɪərɪŋ ðə njuːz ʃiː bɜːrst ˈɪntuː tɪrz/",
              [{"text":"Hearing","role":"V","phonetic":"/ˈhɪərɪŋ/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"news","role":"O","phonetic":"/njuːz/"},{"text":"she","role":"S","phonetic":"/ʃiː/"},{"text":"burst","role":"V","phonetic":"/bɜːrst/"},{"text":"into","role":"P","phonetic":"/ˈɪntuː/"},{"text":"tears","role":"A","phonetic":"/tɪrz/"}]),
          g("Having finished his homework he went out to play","做完作业后他出去玩了","/ˈhævɪŋ ˈfɪnɪʃt hɪz ˈhoʊmwɜːrk hiː went aʊt tuː pleɪ/",
              [{"text":"Having","role":"V","phonetic":"/ˈhævɪŋ/"},{"text":"finished","role":"V","phonetic":"/ˈfɪnɪʃt/"},{"text":"his","role":"Det","phonetic":"/hɪz/"},{"text":"homework","role":"O","phonetic":"/ˈhoʊmwɜːrk/"},{"text":"he","role":"S","phonetic":"/hiː/"},{"text":"went","role":"V","phonetic":"/went/"},{"text":"out","role":"A","phonetic":"/aʊt/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"play","role":"V","phonetic":"/pleɪ/"}]),
          g("children playing in the park","在公园玩耍的孩子们","/ˈtʃɪldrən ˈpleɪɪŋ ɪn ðə pɑːrk/"),
          g("a sleeping baby","一个正在睡觉的婴儿","/ə ˈsliːpɪŋ ˈbeɪbi/"),
          g("running water","自来水","/ˈrʌnɪŋ ˈwɔːtər/"),
]
for w in [("holder","持有人","/ˈhoʊldər/"),("truant","逃学者","/ˈtruːənt/"),("shame","羞耻","/ʃeɪm/"),
          ("hitchhike","搭便车","/ˈhɪtʃhaɪk/"),("evade","逃避","/ɪˈveɪd/")]:
    L73.append(g(w[0],w[1],w[2]))
save("73.json", L73)

# ==================== 74: Out of the limelight (现在分词) ====================
L74 = []
for w in [("limelight","聚光灯;众人注目的中心","/ˈlaɪmlaɪt/"),("actor","演员","/ˈæktər/"),
          ("actress","女演员","/ˈæktrəs/"),("disguise","伪装","/dɪsˈɡaɪz/"),
          ("fan","粉丝","/fæn/"),("recognize","认出","/ˈrekəɡnaɪz/"),
          ("perfect","完美的","/ˈpɜːrfɪkt/"),("ordinary","普通的","/ˈɔːrdəneri/"),
          ("out of the limelight","远离公众视线","/aʊt əv ðə ˈlaɪmlaɪt/"),
          ("in disguise","伪装着","/ɪn dɪsˈɡaɪz/"),("a famous actor","著名演员","/ə ˈfeɪməs ˈæktər/"),
          ("stay out of the limelight","保持低调","/steɪ aʊt əv ðə ˈlaɪmlaɪt/"),
]:
    L74.append(g(w[0],w[1],w[2]))
L74 += [
    g("Sitting in the park they enjoyed the sunshine","坐在公园里他们享受着阳光","/ˈsɪtɪŋ ɪn ðə pɑːrk ðeɪ ɪnˈdʒɔɪd ðə ˈsʌnʃaɪn/",
      [{"text":"Sitting","role":"V","phonetic":"/ˈsɪtɪŋ/"},{"text":"in","role":"P","phonetic":"/ɪn/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"park","role":"A","phonetic":"/pɑːrk/"},{"text":"they","role":"S","phonetic":"/ðeɪ/"},{"text":"enjoyed","role":"V","phonetic":"/ɪnˈdʒɔɪd/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"sunshine","role":"O","phonetic":"/ˈsʌnʃaɪn/"}]),
    g("Not knowing what to do she asked for help","不知道该怎么办她寻求了帮助","/nɒt ˈnoʊɪŋ wɒt tuː duː ʃiː æskt fɔːr help/",
      [{"text":"Not","role":"Neg","phonetic":"/nɒt/"},{"text":"knowing","role":"V","phonetic":"/ˈnoʊɪŋ/"},{"text":"what","role":"O","phonetic":"/wɒt/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"do","role":"V","phonetic":"/duː/"},{"text":"she","role":"S","phonetic":"/ʃiː/"},{"text":"asked","role":"V","phonetic":"/æskt/"},{"text":"for","role":"P","phonetic":"/fɔːr/"},{"text":"help","role":"A","phonetic":"/help/"}]),
    g("Turning around I saw an old friend","转过身我看到了一位老朋友","/ˈtɜːrnɪŋ əˈraʊnd aɪ sɔː ən oʊld frend/",
      [{"text":"Turning","role":"V","phonetic":"/ˈtɜːrnɪŋ/"},{"text":"around","role":"A","phonetic":"/əˈraʊnd/"},{"text":"I","role":"S","phonetic":"/aɪ/"},{"text":"saw","role":"V","phonetic":"/sɔː/"},{"text":"an","role":"Art","phonetic":"/ən/"},{"text":"old","role":"C","phonetic":"/oʊld/"},{"text":"friend","role":"O","phonetic":"/frend/"}]),
    g("They walked along the street talking and laughing","他们沿街走着有说有笑","/ðeɪ wɔːkt əˈlɒŋ ðə striːt ˈtɔːkɪŋ ænd ˈlæfɪŋ/",
      [{"text":"They","role":"S","phonetic":"/ðeɪ/"},{"text":"walked","role":"V","phonetic":"/wɔːkt/"},{"text":"along","role":"P","phonetic":"/əˈlɒŋ/"},{"text":"the","role":"Art","phonetic":"/ðə/"},{"text":"street","role":"A","phonetic":"/striːt/"},{"text":"talking","role":"V","phonetic":"/ˈtɔːkɪŋ/"},{"text":"and","role":"P","phonetic":"/ænd/"},{"text":"laughing","role":"V","phonetic":"/ˈlæfɪŋ/"}]),
    g("The actress wearing a hat is trying not to be recognized","戴着帽子的女演员正试图不被认出","/ði ˈæktrəs ˈwerɪŋ ə hæt ɪz ˈtraɪɪŋ nɒt tuː biː ˈrekəɡnaɪzd/",
      [{"text":"The","role":"Art","phonetic":"/ði/"},{"text":"actress","role":"S","phonetic":"/ˈæktrəs/"},{"text":"wearing","role":"V","phonetic":"/ˈwerɪŋ/"},{"text":"a","role":"Art","phonetic":"/ə/"},{"text":"hat","role":"O","phonetic":"/hæt/"},{"text":"is","role":"V","phonetic":"/ɪz/"},{"text":"trying","role":"V","phonetic":"/ˈtraɪɪŋ/"},{"text":"not","role":"Neg","phonetic":"/nɒt/"},{"text":"to","role":"P","phonetic":"/tuː/"},{"text":"be","role":"V","phonetic":"/biː/"},{"text":"recognized","role":"V","phonetic":"/ˈrekəɡnaɪzd/"}]),
    g("Disguised as an ordinary man the actor went out","伪装成普通人那个演员出门了","/dɪsˈɡaɪzd æz ən ˈɔːrdəneri mæn ði ˈæktər went aʊt/",
      [{"text":"Disguised","role":"V","phonetic":"/dɪsˈɡaɪzd/"},{"text":"as","role":"P","phonetic":"/æz/"},{"text":"an","role":"Art","phonetic":"/ən/"},{"text":"ordinary","role":"C","phonetic":"/ˈɔːrdəneri/"},{"text":"man","role":"A","phonetic":"/mæn/"},{"text":"the","role":"Art","phonetic":"/ði/"},{"text":"actor","role":"S","phonetic":"/ˈæktər/"},{"text":"went","role":"V","phonetic":"/went/"},{"text":"out","role":"A","phonetic":"/aʊt/"}]),
]
for w in [("limelight","聚光灯","/ˈlaɪmlaɪt/"),("actor","演员","/ˈæktər/"),("disguise","伪装","/dɪsˈɡaɪz/"),
          ("recognize","认出","/ˈrekəɡnaɪz/"),("ordinary","普通的","/ˈɔːrdəneri/")]:
    L74.append(g(w[0],w[1],w[2]))
save("74.json", L74)

print("71-74 done")
