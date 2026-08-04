#!/usr/bin/env python3
"""批量生成 NCE2 第64-90课完整 JSON 数据文件"""
import json, os

OUT = "/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/earthworm/nce2"

def save(filename, data):
    path = os.path.join(OUT, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {filename}: {len(data)} entries")

# ==================== 64: The Channel Tunnel ====================
L64 = [
    {"chinese": "隧道(tunnel)", "english": "tunnel", "soundmark": "/ˈtʌnəl/"},
    {"chinese": "海峡(channel)", "english": "channel", "soundmark": "/ˈtʃænəl/"},
    {"chinese": "工程(engineering)", "english": "engineering", "soundmark": "/ˌendʒɪˈnɪərɪŋ/"},
    {"chinese": "连接(connect)", "english": "connect", "soundmark": "/kəˈnekt/"},
    {"chinese": "挖掘(dig)", "english": "dig", "soundmark": "/dɪɡ/"},
    {"chinese": "提议(propose)", "english": "propose", "soundmark": "/prəˈpoʊz/"},
    {"chinese": "完工的(completed)", "english": "completed", "soundmark": "/kəmˈpliːtɪd/"},
    {"chinese": "宏伟的(magnificent)", "english": "magnificent", "soundmark": "/mæɡˈnɪfɪsənt/"},
    {"chinese": "世纪(century)", "english": "century", "soundmark": "/ˈsentʃəri/"},
    {"chinese": "英吉利海峡", "english": "the English Channel", "soundmark": "/ði ˈɪŋɡlɪʃ ˈtʃænəl/"},
    {"chinese": "海底隧道", "english": "a tunnel under the sea", "soundmark": "/ə ˈtʌnəl ˈʌndər ðə siː/"},
    {"chinese": "连接英法两国", "english": "connect England and France", "soundmark": "/kəˈnekt ˈɪŋɡlənd ænd frɑːns/"},
    {"chinese": "如果当时知道", "english": "if I had known", "soundmark": "/ɪf aɪ hæd noʊn/"},
    {"chinese": "如果当初更努力", "english": "if I had worked harder", "soundmark": "/ɪf aɪ hæd wɜːrkt ˈhɑːrdər/"},
    {"chinese": "隧道连接了英国和法国", "english": "The tunnel connects England and France", "soundmark": "/ðə ˈtʌnəl kəˈnekts ˈɪŋɡlənd ænd frɑːns/", "grammar": [{"text": "The","role": "Art","phonetic": "/ðə/"},{"text": "tunnel","role": "S","phonetic": "/ˈtʌnəl/"},{"text": "connects","role": "V","phonetic": "/kəˈnekts/"},{"text": "England","role": "O","phonetic": "/ˈɪŋɡlənd/"},{"text": "and","role": "P","phonetic": "/ænd/"},{"text": "France","role": "O","phonetic": "/frɑːns/"}]},
    {"chinese": "如果我早知道我就去帮你了", "english": "If I had known I would have helped you", "soundmark": "/ɪf aɪ hæd noʊn aɪ wʊd hæv helpt juː/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "known","role": "V","phonetic": "/noʊn/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "helped","role": "V","phonetic": "/helpt/"},{"text": "you","role": "O","phonetic": "/juː/"}]},
    {"chinese": "如果他当时来了他会很开心的", "english": "If he had come he would have been very happy", "soundmark": "/ɪf hiː hæd kʌm hiː wʊd hæv biːn ˈveri ˈhæpi/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "he","role": "S","phonetic": "/hiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "come","role": "V","phonetic": "/kʌm/"},{"text": "he","role": "S","phonetic": "/hiː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "very","role": "Adv","phonetic": "/ˈveri/"},{"text": "happy","role": "C","phonetic": "/ˈhæpi/"}]},
    {"chinese": "如果当初更努力你就会通过考试的", "english": "If you had worked harder you would have passed the exam", "soundmark": "/ɪf juː hæd wɜːrkt ˈhɑːrdər juː wʊd hæv pæst ði ɪɡˈzæm/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "you","role": "S","phonetic": "/juː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "worked","role": "V","phonetic": "/wɜːrkt/"},{"text": "harder","role": "A","phonetic": "/ˈhɑːrdər/"},{"text": "you","role": "S","phonetic": "/juː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "passed","role": "V","phonetic": "/pæst/"},{"text": "the","role": "Art","phonetic": "/ði/"},{"text": "exam","role": "O","phonetic": "/ɪɡˈzæm/"}]},
    {"chinese": "如果我们早点出发就不会迟到了", "english": "If we had left earlier we would not have been late", "soundmark": "/ɪf wiː hæd left ˈɜːrliər wiː wʊd nɒt hæv biːn leɪt/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "we","role": "S","phonetic": "/wiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "left","role": "V","phonetic": "/left/"},{"text": "earlier","role": "A","phonetic": "/ˈɜːrliər/"},{"text": "we","role": "S","phonetic": "/wiː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "late","role": "C","phonetic": "/leɪt/"}]},
    {"chinese": "如果她没帮我我是不可能完成这项工作的", "english": "If she had not helped me I could not have finished the work", "soundmark": "/ɪf ʃiː hæd nɒt helpt miː aɪ kʊd nɒt hæv ˈfɪnɪʃt ðə wɜːrk/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "she","role": "S","phonetic": "/ʃiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "helped","role": "V","phonetic": "/helpt/"},{"text": "me","role": "O","phonetic": "/miː/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "could","role": "V","phonetic": "/kʊd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "finished","role": "V","phonetic": "/ˈfɪnɪʃt/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "work","role": "O","phonetic": "/wɜːrk/"}]},
    {"chinese": "如果天气好我们就去野餐了", "english": "If the weather had been good we would have gone for a picnic", "soundmark": "/ɪf ðə ˈweðər hæd biːn ɡʊd wiː wʊd hæv ɡɒn fɔːr ə ˈpɪknɪk/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "weather","role": "S","phonetic": "/ˈweðər/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "good","role": "C","phonetic": "/ɡʊd/"},{"text": "we","role": "S","phonetic": "/wiː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "gone","role": "V","phonetic": "/ɡɒn/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "a","role": "Art","phonetic": "/ə/"},{"text": "picnic","role": "A","phonetic": "/ˈpɪknɪk/"}]},
    {"chinese": "如果我有足够的时间我会把整本书读完", "english": "If I had had enough time I would have finished the whole book", "soundmark": "/ɪf aɪ hæd hæd ɪˈnʌf taɪm aɪ wʊd hæv ˈfɪnɪʃt ðə hoʊl bʊk/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "enough","role": "Det","phonetic": "/ɪˈnʌf/"},{"text": "time","role": "O","phonetic": "/taɪm/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "finished","role": "V","phonetic": "/ˈfɪnɪʃt/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "whole","role": "C","phonetic": "/hoʊl/"},{"text": "book","role": "O","phonetic": "/bʊk/"}]},
    {"chinese": "如果她接受了我的建议就不会有这些麻烦了", "english": "If she had taken my advice she would not have had all this trouble", "soundmark": "/ɪf ʃiː hæd ˈteɪkən maɪ ədˈvaɪs ʃiː wʊd nɒt hæv hæd ɔːl ðɪs ˈtrʌbəl/", "grammar": [{"text": "If","role": "P","phonetic": "/ɪf/"},{"text": "she","role": "S","phonetic": "/ʃiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "taken","role": "V","phonetic": "/ˈteɪkən/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "advice","role": "O","phonetic": "/ədˈvaɪs/"},{"text": "she","role": "S","phonetic": "/ʃiː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "all","role": "Det","phonetic": "/ɔːl/"},{"text": "this","role": "Det","phonetic": "/ðɪs/"},{"text": "trouble","role": "O","phonetic": "/ˈtrʌbəl/"}]},
    {"chinese": "隧道(tunnel)", "english": "tunnel", "soundmark": "/ˈtʌnəl/"},
    {"chinese": "海峡(channel)", "english": "channel", "soundmark": "/ˈtʃænəl/"},
    {"chinese": "挖掘(dig)", "english": "dig", "soundmark": "/dɪɡ/"},
    {"chinese": "连接(connect)", "english": "connect", "soundmark": "/kəˈnekt/"},
    {"chinese": "如果……就好了(if only)", "english": "if only", "soundmark": "/ɪf ˈoʊnli/"},
    {"chinese": "如果早知道(had I known)", "english": "had I known", "soundmark": "/hæd aɪ noʊn/"},
    {"chinese": "本可以做(could have done)", "english": "could have done", "soundmark": "/kʊd hæv dʌn/"},
]
save("64.json", L64)

# ==================== 65: Jumbo versus the police ====================
L65 = [
    {"chinese": "大象(elephant)", "english": "elephant", "soundmark": "/ˈelɪfənt/"},
    {"chinese": "警察(police)", "english": "police", "soundmark": "/pəˈliːs/"},
    {"chinese": "马戏团(circus)", "english": "circus", "soundmark": "/ˈsɜːrkəs/"},
    {"chinese": "训练员(trainer)", "english": "trainer", "soundmark": "/ˈtreɪnər/"},
    {"chinese": "街道(street)", "english": "street", "soundmark": "/striːt/"},
    {"chinese": "交通(traffic)", "english": "traffic", "soundmark": "/ˈtræfɪk/"},
    {"chinese": "体重(weight)", "english": "weight", "soundmark": "/weɪt/"},
    {"chinese": "应该(should)", "english": "should", "soundmark": "/ʃʊd/"},
    {"chinese": "应当(ought to)", "english": "ought to", "soundmark": "/ɔːt tuː/"},
    {"chinese": "过街", "english": "cross the street", "soundmark": "/krɒs ðə striːt/"},
    {"chinese": "阻挡交通", "english": "hold up the traffic", "soundmark": "/hoʊld ʌp ðə ˈtræfɪk/"},
    {"chinese": "把象带走", "english": "take the elephant away", "soundmark": "/teɪk ði ˈelɪfənt əˈweɪ/"},
    {"chinese": "你应该早点出发", "english": "You should leave earlier", "soundmark": "/juː ʃʊd liːv ˈɜːrliər/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "leave","role": "V","phonetic": "/liːv/"},{"text": "earlier","role": "A","phonetic": "/ˈɜːrliər/"}]},
    {"chinese": "你应当多喝些水", "english": "You ought to drink more water", "soundmark": "/juː ɔːt tuː drɪŋk mɔːr ˈwɔːtər/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "ought","role": "V","phonetic": "/ɔːt/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "drink","role": "V","phonetic": "/drɪŋk/"},{"text": "more","role": "Det","phonetic": "/mɔːr/"},{"text": "water","role": "O","phonetic": "/ˈwɔːtər/"}]},
    {"chinese": "你不应该对父母那样说话", "english": "You should not talk to your parents like that", "soundmark": "/juː ʃʊd nɒt tɔːk tuː jɔːr ˈperənts laɪk ðæt/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "talk","role": "V","phonetic": "/tɔːk/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "your","role": "Det","phonetic": "/jɔːr/"},{"text": "parents","role": "O","phonetic": "/ˈperənts/"},{"text": "like","role": "P","phonetic": "/laɪk/"},{"text": "that","role": "A","phonetic": "/ðæt/"}]},
    {"chinese": "我们应该帮助那些需要帮助的人", "english": "We should help those who are in need", "soundmark": "/wiː ʃʊd help ðoʊz huː ɑːr ɪn niːd/", "grammar": [{"text": "We","role": "S","phonetic": "/wiː/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "help","role": "V","phonetic": "/help/"},{"text": "those","role": "O","phonetic": "/ðoʊz/"},{"text": "who","role": "S","phonetic": "/huː/"},{"text": "are","role": "V","phonetic": "/ɑːr/"},{"text": "in","role": "P","phonetic": "/ɪn/"},{"text": "need","role": "A","phonetic": "/niːd/"}]},
    {"chinese": "你应当为你的行为道歉", "english": "You ought to apologize for your behavior", "soundmark": "/juː ɔːt tuː əˈpɒlədʒaɪz fɔːr jɔːr bɪˈheɪvjər/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "ought","role": "V","phonetic": "/ɔːt/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "apologize","role": "V","phonetic": "/əˈpɒlədʒaɪz/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "your","role": "Det","phonetic": "/jɔːr/"},{"text": "behavior","role": "A","phonetic": "/bɪˈheɪvjər/"}]},
    {"chinese": "我认为你不应该接受那份工作", "english": "I don't think you should accept that job", "soundmark": "/aɪ doʊnt θɪŋk juː ʃʊd əkˈsept ðæt dʒɒb/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "don't","role": "V","phonetic": "/doʊnt/"},{"text": "think","role": "V","phonetic": "/θɪŋk/"},{"text": "you","role": "S","phonetic": "/juː/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "accept","role": "V","phonetic": "/əkˈsept/"},{"text": "that","role": "Det","phonetic": "/ðæt/"},{"text": "job","role": "O","phonetic": "/dʒɒb/"}]},
    {"chinese": "我们应该每天锻炼来保持健康", "english": "We ought to exercise every day to stay healthy", "soundmark": "/wiː ɔːt tuː ˈeksərsaɪz ˈevri deɪ tuː steɪ ˈhelθi/", "grammar": [{"text": "We","role": "S","phonetic": "/wiː/"},{"text": "ought","role": "V","phonetic": "/ɔːt/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "exercise","role": "V","phonetic": "/ˈeksərsaɪz/"},{"text": "every","role": "Det","phonetic": "/ˈevri/"},{"text": "day","role": "A","phonetic": "/deɪ/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "stay","role": "V","phonetic": "/steɪ/"},{"text": "healthy","role": "C","phonetic": "/ˈhelθi/"}]},
    {"chinese": "你应该告诉我你要迟到了", "english": "You should have told me you would be late", "soundmark": "/juː ʃʊd hæv toʊld miː juː wʊd biː leɪt/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "told","role": "V","phonetic": "/toʊld/"},{"text": "me","role": "O","phonetic": "/miː/"},{"text": "you","role": "S","phonetic": "/juː/"},{"text": "would","role": "V","phonetic": "/wʊd/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "late","role": "C","phonetic": "/leɪt/"}]},
    {"chinese": "你应当准时这里不允许迟到", "english": "You ought to be on time being late is not allowed here", "soundmark": "/juː ɔːt tuː biː ɒn taɪm ˈbiːɪŋ leɪt ɪz nɒt əˈlaʊd hɪr/", "grammar": [{"text": "You","role": "S","phonetic": "/juː/"},{"text": "ought","role": "V","phonetic": "/ɔːt/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "on","role": "P","phonetic": "/ɒn/"},{"text": "time","role": "A","phonetic": "/taɪm/"},{"text": "being","role": "S","phonetic": "/ˈbiːɪŋ/"},{"text": "late","role": "C","phonetic": "/leɪt/"},{"text": "is","role": "V","phonetic": "/ɪz/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "allowed","role": "V","phonetic": "/əˈlaʊd/"},{"text": "here","role": "A","phonetic": "/hɪr/"}]},
    {"chinese": "大象(elephant)", "english": "elephant", "soundmark": "/ˈelɪfənt/"},
    {"chinese": "警察(police)", "english": "police", "soundmark": "/pəˈliːs/"},
    {"chinese": "交通(traffic)", "english": "traffic", "soundmark": "/ˈtræfɪk/"},
    {"chinese": "应该(should)", "english": "should", "soundmark": "/ʃʊd/"},
    {"chinese": "应当(ought to)", "english": "ought to", "soundmark": "/ɔːt tuː/"},
    {"chinese": "不应该(should not)", "english": "should not", "soundmark": "/ʃʊd nɒt/"},
]
save("65.json", L65)

# ==================== 66: Sweet as honey! ====================
L66 = [
    {"chinese": "飞机(airplane)", "english": "airplane", "soundmark": "/ˈerpleɪn/"},
    {"chinese": "收藏家(collector)", "english": "collector", "soundmark": "/kəˈlektər/"},
    {"chinese": "修复(restore)", "english": "restore", "soundmark": "/rɪˈstɔːr/"},
    {"chinese": "古董(antique)", "english": "antique", "soundmark": "/ænˈtiːk/"},
    {"chinese": "价值(value)", "english": "value", "soundmark": "/ˈvæljuː/"},
    {"chinese": "发动机(engine)", "english": "engine", "soundmark": "/ˈendʒɪn/"},
    {"chinese": "机翼(wing)", "english": "wing", "soundmark": "/wɪŋ/"},
    {"chinese": "修理(repair)", "english": "repair", "soundmark": "/rɪˈper/"},
    {"chinese": "我去理发了", "english": "I had my hair cut", "soundmark": "/aɪ hæd maɪ her kʌt/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "hair","role": "O","phonetic": "/her/"},{"text": "cut","role": "V","phonetic": "/kʌt/"}]},
    {"chinese": "他让人修了车", "english": "He had his car repaired", "soundmark": "/hiː hæd hɪz kɑːr rɪˈperd/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "his","role": "Det","phonetic": "/hɪz/"},{"text": "car","role": "O","phonetic": "/kɑːr/"},{"text": "repaired","role": "V","phonetic": "/rɪˈperd/"}]},
    {"chinese": "她让人打扫了房子", "english": "She had her house cleaned", "soundmark": "/ʃiː hæd hɜːr haʊs kliːnd/", "grammar": [{"text": "She","role": "S","phonetic": "/ʃiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "her","role": "Det","phonetic": "/hɜːr/"},{"text": "house","role": "O","phonetic": "/haʊs/"},{"text": "cleaned","role": "V","phonetic": "/kliːnd/"}]},
    {"chinese": "我们要让人粉刷房子", "english": "We are going to have the house painted", "soundmark": "/wiː ɑːr ˈɡoʊɪŋ tuː hæv ðə haʊs ˈpeɪntɪd/", "grammar": [{"text": "We","role": "S","phonetic": "/wiː/"},{"text": "are","role": "V","phonetic": "/ɑːr/"},{"text": "going","role": "V","phonetic": "/ˈɡoʊɪŋ/"},{"text": "to","role": "P","phonetic": "/tuː/"},{"text": "have","role": "V","phonetic": "/hæv/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "house","role": "O","phonetic": "/haʊs/"},{"text": "painted","role": "V","phonetic": "/ˈpeɪntɪd/"}]},
    {"chinese": "我昨天让人把窗户修好了", "english": "I had the window repaired yesterday", "soundmark": "/aɪ hæd ðə ˈwɪndoʊ rɪˈperd ˈjestərdeɪ/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "window","role": "O","phonetic": "/ˈwɪndoʊ/"},{"text": "repaired","role": "V","phonetic": "/rɪˈperd/"},{"text": "yesterday","role": "A","phonetic": "/ˈjestərdeɪ/"}]},
    {"chinese": "他把电脑拿去升级了", "english": "He had his computer upgraded", "soundmark": "/hiː hæd hɪz kəmˈpjuːtər ʌpˈɡreɪdɪd/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "his","role": "Det","phonetic": "/hɪz/"},{"text": "computer","role": "O","phonetic": "/kəmˈpjuːtər/"},{"text": "upgraded","role": "V","phonetic": "/ʌpˈɡreɪdɪd/"}]},
    {"chinese": "她让人把婚纱定制好了", "english": "She had her wedding dress made", "soundmark": "/ʃiː hæd hɜːr ˈwedɪŋ dres meɪd/", "grammar": [{"text": "She","role": "S","phonetic": "/ʃiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "her","role": "Det","phonetic": "/hɜːr/"},{"text": "wedding","role": "C","phonetic": "/ˈwedɪŋ/"},{"text": "dress","role": "O","phonetic": "/dres/"},{"text": "made","role": "V","phonetic": "/meɪd/"}]},
    {"chinese": "他们让人检查了屋顶", "english": "They had the roof checked", "soundmark": "/ðeɪ hæd ðə ruːf tʃekt/", "grammar": [{"text": "They","role": "S","phonetic": "/ðeɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "roof","role": "O","phonetic": "/ruːf/"},{"text": "checked","role": "V","phonetic": "/tʃekt/"}]},
    {"chinese": "我让人洗了车", "english": "I had my car washed", "soundmark": "/aɪ hæd maɪ kɑːr wɒʃt/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "car","role": "O","phonetic": "/kɑːr/"},{"text": "washed","role": "V","phonetic": "/wɒʃt/"}]},
    {"chinese": "飞机(airplane)", "english": "airplane", "soundmark": "/ˈerpleɪn/"},
    {"chinese": "修复(restore)", "english": "restore", "soundmark": "/rɪˈstɔːr/"},
    {"chinese": "古董(antique)", "english": "antique", "soundmark": "/ænˈtiːk/"},
    {"chinese": "发动机(engine)", "english": "engine", "soundmark": "/ˈendʒɪn/"},
    {"chinese": "机翼(wing)", "english": "wing", "soundmark": "/wɪŋ/"},
    {"chinese": "让人做(have sth done)", "english": "have something done", "soundmark": "/hæv ˈsʌmθɪŋ dʌn/"},
]
save("66.json", L66)

# ==================== 67: Volcanoes ====================
L67 = [
    {"chinese": "火山(volcano)", "english": "volcano", "soundmark": "/vɒlˈkeɪnoʊ/"},
    {"chinese": "喷发(erupt)", "english": "erupt", "soundmark": "/ɪˈrʌpt/"},
    {"chinese": "活跃的(active)", "english": "active", "soundmark": "/ˈæktɪv/"},
    {"chinese": "岩浆(lava)", "english": "lava", "soundmark": "/ˈlɑːvə/"},
    {"chinese": "毁灭(destroy)", "english": "destroy", "soundmark": "/dɪˈstrɔɪ/"},
    {"chinese": "灰烬(ash)", "english": "ash", "soundmark": "/æʃ/"},
    {"chinese": "火山口(crater)", "english": "crater", "soundmark": "/ˈkreɪtər/"},
    {"chinese": "科学家(scientist)", "english": "scientist", "soundmark": "/ˈsaɪəntɪst/"},
    {"chinese": "地震(earthquake)", "english": "earthquake", "soundmark": "/ˈɜːrθkweɪk/"},
    {"chinese": "火山爆发", "english": "volcanic eruption", "soundmark": "/vɒlˈkænɪk ɪˈrʌpʃən/"},
    {"chinese": "活火山", "english": "an active volcano", "soundmark": "/ən ˈæktɪv vɒlˈkeɪnoʊ/"},
    {"chinese": "已经一直在喷发", "english": "had been erupting", "soundmark": "/hæd biːn ɪˈrʌptɪŋ/"},
    {"chinese": "火山在喷发前已经冒烟好几天了", "english": "The volcano had been smoking for days before it erupted", "soundmark": "/ðə vɒlˈkeɪnoʊ hæd biːn ˈsmoʊkɪŋ fɔːr deɪz bɪˈfɔːr ɪt ɪˈrʌptɪd/", "grammar": [{"text": "The","role": "Art","phonetic": "/ðə/"},{"text": "volcano","role": "S","phonetic": "/vɒlˈkeɪnoʊ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "smoking","role": "V","phonetic": "/ˈsmoʊkɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "days","role": "A","phonetic": "/deɪz/"},{"text": "before","role": "P","phonetic": "/bɪˈfɔːr/"},{"text": "it","role": "S","phonetic": "/ɪt/"},{"text": "erupted","role": "V","phonetic": "/ɪˈrʌptɪd/"}]},
    {"chinese": "在我遇到他之前他已经在那家公司工作了十年", "english": "He had been working for that company for ten years before I met him", "soundmark": "/hiː hæd biːn ˈwɜːrkɪŋ fɔːr ðæt ˈkʌmpəni fɔːr ten jɪrz bɪˈfɔːr aɪ met hɪm/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "working","role": "V","phonetic": "/ˈwɜːrkɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "that","role": "Det","phonetic": "/ðæt/"},{"text": "company","role": "A","phonetic": "/ˈkʌmpəni/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "ten","role": "Det","phonetic": "/ten/"},{"text": "years","role": "A","phonetic": "/jɪrz/"},{"text": "before","role": "P","phonetic": "/bɪˈfɔːr/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "met","role": "V","phonetic": "/met/"},{"text": "him","role": "O","phonetic": "/hɪm/"}]},
    {"chinese": "她一直在等这个电话等了整整一天", "english": "She had been waiting for the call all day", "soundmark": "/ʃiː hæd biːn ˈweɪtɪŋ fɔːr ðə kɔːl ɔːl deɪ/", "grammar": [{"text": "She","role": "S","phonetic": "/ʃiː/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "waiting","role": "V","phonetic": "/ˈweɪtɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "call","role": "O","phonetic": "/kɔːl/"},{"text": "all","role": "Det","phonetic": "/ɔːl/"},{"text": "day","role": "A","phonetic": "/deɪ/"}]},
    {"chinese": "他们赶了几个小时的路所以非常疲惫", "english": "They had been driving for hours so they were very tired", "soundmark": "/ðeɪ hæd biːn ˈdraɪvɪŋ fɔːr aʊərz soʊ ðeɪ wɜːr ˈveri taɪərd/", "grammar": [{"text": "They","role": "S","phonetic": "/ðeɪ/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "driving","role": "V","phonetic": "/ˈdraɪvɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "hours","role": "A","phonetic": "/aʊərz/"},{"text": "so","role": "P","phonetic": "/soʊ/"},{"text": "they","role": "S","phonetic": "/ðeɪ/"},{"text": "were","role": "V","phonetic": "/wɜːr/"},{"text": "very","role": "Adv","phonetic": "/ˈveri/"},{"text": "tired","role": "C","phonetic": "/taɪərd/"}]},
    {"chinese": "地一直在震了好几个小时才停下来", "english": "The ground had been shaking for hours before it stopped", "soundmark": "/ðə ɡraʊnd hæd biːn ˈʃeɪkɪŋ fɔːr aʊərz bɪˈfɔːr ɪt stɒpt/", "grammar": [{"text": "The","role": "Art","phonetic": "/ðə/"},{"text": "ground","role": "S","phonetic": "/ɡraʊnd/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "shaking","role": "V","phonetic": "/ˈʃeɪkɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "hours","role": "A","phonetic": "/aʊərz/"},{"text": "before","role": "P","phonetic": "/bɪˈfɔːr/"},{"text": "it","role": "S","phonetic": "/ɪt/"},{"text": "stopped","role": "V","phonetic": "/stɒpt/"}]},
    {"chinese": "在我到这里之前雨已经下了三天了", "english": "It had been raining for three days before I arrived", "soundmark": "/ɪt hæd biːn ˈreɪnɪŋ fɔːr θriː deɪz bɪˈfɔːr aɪ əˈraɪvd/", "grammar": [{"text": "It","role": "S","phonetic": "/ɪt/"},{"text": "had","role": "V","phonetic": "/hæd/"},{"text": "been","role": "V","phonetic": "/biːn/"},{"text": "raining","role": "V","phonetic": "/ˈreɪnɪŋ/"},{"text": "for","role": "P","phonetic": "/fɔːr/"},{"text": "three","role": "Det","phonetic": "/θriː/"},{"text": "days","role": "A","phonetic": "/deɪz/"},{"text": "before","role": "P","phonetic": "/bɪˈfɔːr/"},{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "arrived","role": "V","phonetic": "/əˈraɪvd/"}]},
    {"chinese": "火山(volcano)", "english": "volcano", "soundmark": "/vɒlˈkeɪnoʊ/"},
    {"chinese": "喷发(erupt)", "english": "erupt", "soundmark": "/ɪˈrʌpt/"},
    {"chinese": "活跃的(active)", "english": "active", "soundmark": "/ˈæktɪv/"},
    {"chinese": "岩浆(lava)", "english": "lava", "soundmark": "/ˈlɑːvə/"},
    {"chinese": "灰烬(ash)", "english": "ash", "soundmark": "/æʃ/"},
    {"chinese": "地震(earthquake)", "english": "earthquake", "soundmark": "/ˈɜːrθkweɪk/"},
    {"chinese": "一直在做(had been doing)", "english": "had been doing", "soundmark": "/hæd biːn ˈduːɪŋ/"},
]
save("67.json", L67)

# ==================== 68: Persistent ====================
L68 = [
    {"chinese": "坚持的(persistent)", "english": "persistent", "soundmark": "/pərˈsɪstənt/"},
    {"chinese": "避免(avoid)", "english": "avoid", "soundmark": "/əˈvɔɪd/"},
    {"chinese": "喜欢(enjoy)", "english": "enjoy", "soundmark": "/ɪnˈdʒɔɪ/"},
    {"chinese": "介意(mind)", "english": "mind", "soundmark": "/maɪnd/"},
    {"chinese": "考虑(consider)", "english": "consider", "soundmark": "/kənˈsɪdər/"},
    {"chinese": "建议(suggest)", "english": "suggest", "soundmark": "/səˈdʒest/"},
    {"chinese": "练习(practice)", "english": "practice", "soundmark": "/ˈpræktɪs/"},
    {"chinese": "完成(finish)", "english": "finish", "soundmark": "/ˈfɪnɪʃ/"},
    {"chinese": "推迟(postpone)", "english": "postpone", "soundmark": "/poʊstˈpoʊn/"},
    {"chinese": "否认(deny)", "english": "deny", "soundmark": "/dɪˈnaɪ/"},
    {"chinese": "不停地说话", "english": "keep talking", "soundmark": "/kiːp ˈtɔːkɪŋ/"},
    {"chinese": "喜欢游泳", "english": "enjoy swimming", "soundmark": "/ɪnˈdʒɔɪ ˈswɪmɪŋ/"},
    {"chinese": "避免犯错", "english": "avoid making mistakes", "soundmark": "/əˈvɔɪd ˈmeɪkɪŋ mɪˈsteɪks/"},
    {"chinese": "我享受读书", "english": "I enjoy reading books", "soundmark": "/aɪ ɪnˈdʒɔɪ ˈriːdɪŋ bʊks/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "enjoy","role": "V","phonetic": "/ɪnˈdʒɔɪ/"},{"text": "reading","role": "V","phonetic": "/ˈriːdɪŋ/"},{"text": "books","role": "O","phonetic": "/bʊks/"}]},
    {"chinese": "你介意开窗吗", "english": "Do you mind opening the window", "soundmark": "/duː juː maɪnd ˈoʊpənɪŋ ðə ˈwɪndoʊ/", "grammar": [{"text": "Do","role": "V","phonetic": "/duː/"},{"text": "you","role": "S","phonetic": "/juː/"},{"text": "mind","role": "V","phonetic": "/maɪnd/"},{"text": "opening","role": "V","phonetic": "/ˈoʊpənɪŋ/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "window","role": "O","phonetic": "/ˈwɪndoʊ/"}]},
    {"chinese": "他避免回答我的问题", "english": "He avoided answering my question", "soundmark": "/hiː əˈvɔɪdɪd ˈænsərɪŋ maɪ ˈkwestʃən/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "avoided","role": "V","phonetic": "/əˈvɔɪdɪd/"},{"text": "answering","role": "V","phonetic": "/ˈænsərɪŋ/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "question","role": "O","phonetic": "/ˈkwestʃən/"}]},
    {"chinese": "她建议早点出发", "english": "She suggested leaving early", "soundmark": "/ʃiː səˈdʒestɪd ˈliːvɪŋ ˈɜːrli/", "grammar": [{"text": "She","role": "S","phonetic": "/ʃiː/"},{"text": "suggested","role": "V","phonetic": "/səˈdʒestɪd/"},{"text": "leaving","role": "V","phonetic": "/ˈliːvɪŋ/"},{"text": "early","role": "A","phonetic": "/ˈɜːrli/"}]},
    {"chinese": "我考虑换工作", "english": "I am considering changing my job", "soundmark": "/aɪ æm kənˈsɪdərɪŋ ˈtʃeɪndʒɪŋ maɪ dʒɒb/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "am","role": "V","phonetic": "/æm/"},{"text": "considering","role": "V","phonetic": "/kənˈsɪdərɪŋ/"},{"text": "changing","role": "V","phonetic": "/ˈtʃeɪndʒɪŋ/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "job","role": "O","phonetic": "/dʒɒb/"}]},
    {"chinese": "他一直在坚持学习英语从未放弃", "english": "He kept learning English and never gave up", "soundmark": "/hiː kept ˈlɜːrnɪŋ ˈɪŋɡlɪʃ ænd ˈnevər ɡeɪv ʌp/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "kept","role": "V","phonetic": "/kept/"},{"text": "learning","role": "V","phonetic": "/ˈlɜːrnɪŋ/"},{"text": "English","role": "O","phonetic": "/ˈɪŋɡlɪʃ/"},{"text": "and","role": "P","phonetic": "/ænd/"},{"text": "never","role": "A","phonetic": "/ˈnevər/"},{"text": "gave","role": "V","phonetic": "/ɡeɪv/"},{"text": "up","role": "A","phonetic": "/ʌp/"}]},
    {"chinese": "我做完作业了", "english": "I finished doing my homework", "soundmark": "/aɪ ˈfɪnɪʃt ˈduːɪŋ maɪ ˈhoʊmwɜːrk/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "finished","role": "V","phonetic": "/ˈfɪnɪʃt/"},{"text": "doing","role": "V","phonetic": "/ˈduːɪŋ/"},{"text": "my","role": "Det","phonetic": "/maɪ/"},{"text": "homework","role": "O","phonetic": "/ˈhoʊmwɜːrk/"}]},
    {"chinese": "他们推迟了开会", "english": "They postponed holding the meeting", "soundmark": "/ðeɪ poʊstˈpoʊnd ˈhoʊldɪŋ ðə ˈmiːtɪŋ/", "grammar": [{"text": "They","role": "S","phonetic": "/ðeɪ/"},{"text": "postponed","role": "V","phonetic": "/poʊstˈpoʊnd/"},{"text": "holding","role": "V","phonetic": "/ˈhoʊldɪŋ/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "meeting","role": "O","phonetic": "/ˈmiːtɪŋ/"}]},
    {"chinese": "避免(avoid)", "english": "avoid", "soundmark": "/əˈvɔɪd/"},
    {"chinese": "享受(enjoy)", "english": "enjoy", "soundmark": "/ɪnˈdʒɔɪ/"},
    {"chinese": "介意(mind)", "english": "mind", "soundmark": "/maɪnd/"},
    {"chinese": "考虑(consider)", "english": "consider", "soundmark": "/kənˈsɪdər/"},
    {"chinese": "建议(suggest)", "english": "suggest", "soundmark": "/səˈdʒest/"},
    {"chinese": "练习(practice)", "english": "practice", "soundmark": "/ˈpræktɪs/"},
]
save("68.json", L68)

# ==================== 69: But not murder! ====================
L69 = [
    {"chinese": "谋杀(murder)", "english": "murder", "soundmark": "/ˈmɜːrdər/"},
    {"chinese": "考试(exam)", "english": "exam", "soundmark": "/ɪɡˈzæm/"},
    {"chinese": "考官(examiner)", "english": "examiner", "soundmark": "/ɪɡˈzæmɪnər/"},
    {"chinese": "通过(pass)", "english": "pass", "soundmark": "/pæs/"},
    {"chinese": "驾驶(driving)", "english": "driving", "soundmark": "/ˈdraɪvɪŋ/"},
    {"chinese": "刹车(brake)", "english": "brake", "soundmark": "/breɪk/"},
    {"chinese": "自信的(confident)", "english": "confident", "soundmark": "/ˈkɒnfɪdənt/"},
    {"chinese": "紧张(nervous)", "english": "nervous", "soundmark": "/ˈnɜːrvəs/"},
    {"chinese": "驾照", "english": "driving licence", "soundmark": "/ˈdraɪvɪŋ ˈlaɪsəns/"},
    {"chinese": "驾驶考试", "english": "the driving test", "soundmark": "/ðə ˈdraɪvɪŋ test/"},
    {"chinese": "踩刹车", "english": "press the brake", "soundmark": "/pres ðə breɪk/"},
    {"chinese": "通过考试", "english": "pass the exam", "soundmark": "/pæs ði ɪɡˈzæm/"},
    {"chinese": "这封信必须今天寄出", "english": "This letter must be sent today", "soundmark": "/ðɪs ˈletər mʌst biː sent təˈdeɪ/", "grammar": [{"text": "This","role": "Det","phonetic": "/ðɪs/"},{"text": "letter","role": "S","phonetic": "/ˈletər/"},{"text": "must","role": "V","phonetic": "/mʌst/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "sent","role": "V","phonetic": "/sent/"},{"text": "today","role": "A","phonetic": "/təˈdeɪ/"}]},
    {"chinese": "这项工作应该立即完成", "english": "This work should be done immediately", "soundmark": "/ðɪs wɜːrk ʃʊd biː dʌn ɪˈmiːdiətli/", "grammar": [{"text": "This","role": "Det","phonetic": "/ðɪs/"},{"text": "work","role": "S","phonetic": "/wɜːrk/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "done","role": "V","phonetic": "/dʌn/"},{"text": "immediately","role": "A","phonetic": "/ɪˈmiːdiətli/"}]},
    {"chinese": "这些规则必须被遵守", "english": "These rules must be followed", "soundmark": "/ðiːz ruːlz mʌst biː ˈfɒloʊd/", "grammar": [{"text": "These","role": "Det","phonetic": "/ðiːz/"},{"text": "rules","role": "S","phonetic": "/ruːlz/"},{"text": "must","role": "V","phonetic": "/mʌst/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "followed","role": "V","phonetic": "/ˈfɒloʊd/"}]},
    {"chinese": "考试可以被再次安排", "english": "The exam can be arranged again", "soundmark": "/ði ɪɡˈzæm kæn biː əˈreɪndʒd əˈɡen/", "grammar": [{"text": "The","role": "Art","phonetic": "/ði/"},{"text": "exam","role": "S","phonetic": "/ɪɡˈzæm/"},{"text": "can","role": "V","phonetic": "/kæn/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "arranged","role": "V","phonetic": "/əˈreɪndʒd/"},{"text": "again","role": "A","phonetic": "/əˈɡen/"}]},
    {"chinese": "这道门不应该被锁上", "english": "This door should not be locked", "soundmark": "/ðɪs dɔːr ʃʊd nɒt biː lɒkt/", "grammar": [{"text": "This","role": "Det","phonetic": "/ðɪs/"},{"text": "door","role": "S","phonetic": "/dɔːr/"},{"text": "should","role": "V","phonetic": "/ʃʊd/"},{"text": "not","role": "Neg","phonetic": "/nɒt/"},{"text": "be","role": "V","phonetic": "/biː/"},{"text": "locked","role": "V","phonetic": "/lɒkt/"}]},
    {"chinese": "考试(exam)", "english": "exam", "soundmark": "/ɪɡˈzæm/"},
    {"chinese": "通过(pass)", "english": "pass", "soundmark": "/pæs/"},
    {"chinese": "自信的(confident)", "english": "confident", "soundmark": "/ˈkɒnfɪdənt/"},
    {"chinese": "紧张(nervous)", "english": "nervous", "soundmark": "/ˈnɜːrvəs/"},
    {"chinese": "必须被(must be)", "english": "must be", "soundmark": "/mʌst biː/"},
    {"chinese": "应该被(should be)", "english": "should be", "soundmark": "/ʃʊd biː/"},
]
save("69.json", L69)

# ==================== 70: Red for danger ====================
L70 = [
    {"chinese": "危险的(dangerous)", "english": "dangerous", "soundmark": "/ˈdeɪndʒərəs/"},
    {"chinese": "红色的(red)", "english": "red", "soundmark": "/red/"},
    {"chinese": "斗牛(bullfight)", "english": "bullfight", "soundmark": "/ˈbʊlfaɪt/"},
    {"chinese": "公牛(bull)", "english": "bull", "soundmark": "/bʊl/"},
    {"chinese": "斗牛士(bullfighter)", "english": "bullfighter", "soundmark": "/ˈbʊlfaɪtər/"},
    {"chinese": "披风(cape)", "english": "cape", "soundmark": "/keɪp/"},
    {"chinese": "为……感到自豪", "english": "proud of", "soundmark": "/praʊd əv/"},
    {"chinese": "对……感兴趣", "english": "interested in", "soundmark": "/ˈɪntrəstɪd ɪn/"},
    {"chinese": "害怕……", "english": "afraid of", "soundmark": "/əˈfreɪd əv/"},
    {"chinese": "擅长……", "english": "good at", "soundmark": "/ɡʊd æt/"},
    {"chinese": "对……感到惊讶", "english": "surprised at", "soundmark": "/sərˈpraɪzd æt/"},
    {"chinese": "对……感到满意", "english": "satisfied with", "soundmark": "/ˈsætɪsfaɪd wɪð/"},
    {"chinese": "对……感到厌烦", "english": "bored with", "soundmark": "/bɔːrd wɪð/"},
    {"chinese": "忙于……", "english": "busy with", "soundmark": "/ˈbɪzi wɪð/"},
    {"chinese": "他为他儿子感到自豪", "english": "He is proud of his son", "soundmark": "/hiː ɪz praʊd əv hɪz sʌn/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "is","role": "V","phonetic": "/ɪz/"},{"text": "proud","role": "C","phonetic": "/praʊd/"},{"text": "of","role": "P","phonetic": "/əv/"},{"text": "his","role": "Det","phonetic": "/hɪz/"},{"text": "son","role": "A","phonetic": "/sʌn/"}]},
    {"chinese": "她对这个故事很感兴趣", "english": "She is interested in the story", "soundmark": "/ʃiː ɪz ˈɪntrəstɪd ɪn ðə ˈstɔːri/", "grammar": [{"text": "She","role": "S","phonetic": "/ʃiː/"},{"text": "is","role": "V","phonetic": "/ɪz/"},{"text": "interested","role": "C","phonetic": "/ˈɪntrəstɪd/"},{"text": "in","role": "P","phonetic": "/ɪn/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "story","role": "A","phonetic": "/ˈstɔːri/"}]},
    {"chinese": "我害怕蛇", "english": "I am afraid of snakes", "soundmark": "/aɪ æm əˈfreɪd əv sneɪks/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "am","role": "V","phonetic": "/æm/"},{"text": "afraid","role": "C","phonetic": "/əˈfreɪd/"},{"text": "of","role": "P","phonetic": "/əv/"},{"text": "snakes","role": "A","phonetic": "/sneɪks/"}]},
    {"chinese": "汤姆擅长数学", "english": "Tom is good at math", "soundmark": "/tɒm ɪz ɡʊd æt mæθ/", "grammar": [{"text": "Tom","role": "S","phonetic": "/tɒm/"},{"text": "is","role": "V","phonetic": "/ɪz/"},{"text": "good","role": "C","phonetic": "/ɡʊd/"},{"text": "at","role": "P","phonetic": "/æt/"},{"text": "math","role": "A","phonetic": "/mæθ/"}]},
    {"chinese": "我们对结果很满意", "english": "We are satisfied with the result", "soundmark": "/wiː ɑːr ˈsætɪsfaɪd wɪð ðə rɪˈzʌlt/", "grammar": [{"text": "We","role": "S","phonetic": "/wiː/"},{"text": "are","role": "V","phonetic": "/ɑːr/"},{"text": "satisfied","role": "C","phonetic": "/ˈsætɪsfaɪd/"},{"text": "with","role": "P","phonetic": "/wɪð/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "result","role": "A","phonetic": "/rɪˈzʌlt/"}]},
    {"chinese": "他对这个消息感到惊讶", "english": "He was surprised at the news", "soundmark": "/hiː wʌz sərˈpraɪzd æt ðə njuːz/", "grammar": [{"text": "He","role": "S","phonetic": "/hiː/"},{"text": "was","role": "V","phonetic": "/wʌz/"},{"text": "surprised","role": "C","phonetic": "/sərˈpraɪzd/"},{"text": "at","role": "P","phonetic": "/æt/"},{"text": "the","role": "Art","phonetic": "/ðə/"},{"text": "news","role": "A","phonetic": "/njuːz/"}]},
    {"chinese": "我对这个游戏感到厌烦了", "english": "I am bored with this game", "soundmark": "/aɪ æm bɔːrd wɪð ðɪs ɡeɪm/", "grammar": [{"text": "I","role": "S","phonetic": "/aɪ/"},{"text": "am","role": "V","phonetic": "/æm/"},{"text": "bored","role": "C","phonetic": "/bɔːrd/"},{"text": "with","role": "P","phonetic": "/wɪð/"},{"text": "this","role": "Det","phonetic": "/ðɪs/"},{"text": "game","role": "A","phonetic": "/ɡeɪm/"}]},
    {"chinese": "危险的(dangerous)", "english": "dangerous", "soundmark": "/ˈdeɪndʒərəs/"},
    {"chinese": "自豪的(proud)", "english": "proud", "soundmark": "/praʊd/"},
    {"chinese": "感兴趣的(interested)", "english": "interested", "soundmark": "/ˈɪntrəstɪd/"},
    {"chinese": "害怕的(afraid)", "english": "afraid", "soundmark": "/əˈfreɪd/"},
    {"chinese": "擅长的(good at)", "english": "good at", "soundmark": "/ɡʊd æt/"},
    {"chinese": "满意的(satisfied with)", "english": "satisfied with", "soundmark": "/ˈsætɪsfaɪd wɪð/"},
]
save("70.json", L70)

print("Batch 2 done: 64-70 updated")
