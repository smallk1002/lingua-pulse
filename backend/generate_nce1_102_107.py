#!/usr/bin/env python3
import json
import os

OUT = '/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/earthworm/nce1'

def V(eng, chn, sm):
    return {"english": eng, "chinese": chn, "soundmark": sm}

def S(chn, eng, sm, grammar):
    return {"chinese": chn, "english": eng, "soundmark": sm, "grammar": grammar}

def G(text, role, phonetic):
    return {"text": text, "role": role, "phonetic": phonetic}

# Lesson 102: At least
L102 = [
    V("least", "最少", "/liːst/"),
    V("effort", "努力", "/ˈefərt/"),
    V("improve", "改善", "/ɪmˈpruːv/"),
    V("situation", "情况", "/ˌsɪtʃuˈeɪʃən/"),
    V("appreciate", "感激", "/əˈpriːʃieɪt/"),
    S("至少我们尽力了", "At least we tried our best", "/ət liːst wiː traɪd aʊər best/",
      [G("At", "P", "/ət/"), G("least", "O", "/liːst/"), G("we", "S", "/wiː/"), G("tried", "V", "/traɪd/"), G("our", "Det", "/aʊər/"), G("best", "O", "/best/")]),
    S("情况至少没有变得更糟", "The situation is at least no worse", "/ðə ˌsɪtʃuˈeɪʃən ɪz ə liːst noʊ wɜːrs/",
      [G("The", "Art", "/ðə/"), G("situation", "S", "/ˌsɪtʃuˈeɪʃən/"), G("is", "V", "/ɪz/"), G("at", "P", "/ət/"), G("least", "A", "/liːst/"), G("no", "Adv", "/noʊ/"), G("worse", "C", "/wɜːrs/")]),
    S("你至少可以道歉吧", "You could at least apologize", "/juː kʊd ə liːst ˈæpəlɑːdʒaɪz/",
      [G("You", "S", "/juː/"), G("could", "V", "/kʊd/"), G("at", "P", "/ət/"), G("least", "A", "/liːst/"), G("apologize", "V", "/ˈæpəlɑːdʒaɪz/")]),
    S("至少我们应该感激", "We should appreciate it at least", "/wiː ʃʊd əˈpriːʃieɪt ɪt ə liːst/",
      [G("We", "S", "/wiː/"), G("should", "V", "/ʃʊd/"), G("appreciate", "V", "/əˈpriːʃieɪt/"), G("it", "O", "/ɪt/"), G("at", "P", "/ət/"), G("least", "A", "/liːst/")]),
    S("这至少是个开始", "It's at least a start", "/ɪts ə liːst ə stɑːrt/",
      [G("It", "S", "/ɪt/"), G("'s", "V", "/s/"), G("at", "P", "/ət/"), G("least", "A", "/liːst/"), G("a", "Art", "/ə/"), G("start", "C", "/stɑːrt/")]),
    V("minimum", "最小值", "/ˈmɪnɪməm/"),
    V("something", "某事", "/ˈsʌmθɪŋ/"),
]

# Lesson 103: The French test
L103 = [
    V("French", "法语", "/frentʃ/"),
    V("test", "测试", "/test/"),
    V("difficult", "困难的", "/ˈdɪfɪkəlt/"),
    V("prepare", "准备", "/prɪˈper/"),
    V("grammar", "语法", "/ˈɡræmər/"),
    V("vocabulary", "词汇", "/voʊˈkæbjəleri/"),
    S("法语考试很难", "The French test was very difficult", "/ðə frentʃ test wʌz ˈveri ˈdɪfɪkəlt/",
      [G("The", "Art", "/ðə/"), G("French", "Det", "/frentʃ/"), G("test", "S", "/test/"), G("was", "V", "/wʌz/"), G("very", "Adv", "/ˈveri/"), G("difficult", "C", "/ˈdɪfɪkəlt/")]),
    S("我需要为考试做准备", "I need to prepare for the test", "/aɪ niːd tə prɪˈper fɔːr ðə test/",
      [G("I", "S", "/aɪ/"), G("need", "V", "/niːd/"), G("to", "P", "/tə/"), G("prepare", "V", "/prɪˈper/"), G("for", "P", "/fɔːr/"), G("the", "Art", "/ðə/"), G("test", "O", "/test/")]),
    S("我的法语语法很差", "My French grammar is poor", "/maɪ frentʃ ˈɡræmər ɪz pʊr/",
      [G("My", "Det", "/maɪ/"), G("French", "Det", "/frentʃ/"), G("grammar", "S", "/ˈɡræmər/"), G("is", "V", "/ɪz/"), G("poor", "C", "/pʊr/")]),
    S("我在学习新词汇", "I'm learning new vocabulary", "/aɪm ˈlɜːrnɪŋ nuː voʊˈkæbjəleri/",
      [G("I", "S", "/aɪ/"), G("'m", "V", "/m/"), G("learning", "V", "/ˈlɜːrnɪŋ/"), G("new", "Det", "/nuː/"), G("vocabulary", "O", "/voʊˈkæbjəleri/")]),
    S("考试包括听力和写作", "The test includes listening and writing", "/ðə test ɪnˈkluːdz ˈlɪsənɪŋ ənd ˈraɪtɪŋ/",
      [G("The", "Art", "/ðə/"), G("test", "S", "/test/"), G("includes", "V", "/ɪnˈkluːdz/"), G("listening", "O", "/ˈlɪsənɪŋ/"), G("and", "P", "/ənd/"), G("writing", "O", "/ˈraɪtɪŋ/")]),
    V("practice", "练习", "/ˈpræktɪs/"),
    V("pronunciation", "发音", "/prəˌnʌnsiˈeɪʃən/"),
]

# Lesson 104: It isn't mine!
L104 = [
    V("mine", "我的", "/maɪn/"),
    V("yours", "你的", "/jʊrz/"),
    V("his", "他的", "/hɪz/"),
    V("hers", "她的", "/hɜːrz/"),
    V("belong", "属于", "/bɪˈlɔːŋ/"),
    S("这不是我的，是你的", "It isn't mine, it's yours", "/ɪt ˈɪzənt maɪn, ɪts jʊrz/",
      [G("It", "S", "/ɪt/"), G("isn't", "V", "/ˈɪzənt/"), G("mine", "C", "/maɪn/"), G("it", "S", "/ɪt/"), G("'s", "V", "/s/"), G("yours", "C", "/jʊrz/")]),
    S("这本书属于谁？", "Who does this book belong to?", "/huː dʌz ðɪs bʊk bɪˈlɔːŋ tə/",
      [G("Who", "S", "/huː/"), G("does", "V", "/dʌz/"), G("this", "Det", "/ðɪs/"), G("book", "S", "/bʊk/"), G("belong", "V", "/bɪˈlɔːŋ/"), G("to", "P", "/tə/")]),
    S("那是她的，不是他的", "That's hers, not his", "/ðæts hɜːrz, nɒt hɪz/",
      [G("That", "S", "/ðæt/"), G("'s", "V", "/s/"), G("hers", "C", "/hɜːrz/"), G("not", "Adv", "/nɒt/"), G("his", "C", "/hɪz/")]),
    S("这些是我的书", "These are mine books", "/ðiːz ɑːr maɪn bʊks/",
      [G("These", "S", "/ðiːz/"), G("are", "V", "/ɑːr/"), G("mine", "Det", "/maɪn/"), G("books", "C", "/bʊks/")]),
    S("那不是我们的，是他们的", "That isn't ours, it's theirs", "/ðæt ˈɪzənt aʊərz, ɪts ðerz/",
      [G("That", "S", "/ðæt/"), G("isn't", "V", "/ˈɪzənt/"), G("ours", "C", "/aʊərz/"), G("it", "S", "/ɪt/"), G("'s", "V", "/s/"), G("theirs", "C", "/ðerz/")]),
    V("possession", "所有物", "/pəˈzeʃən/"),
    V("owner", "主人", "/ˈoʊnər/"),
]

# Lesson 105: Full of mistakes
L105 = [
    V("mistake", "错误", "/mɪˈsteɪk/"),
    V("correction", "纠正", "/kəˈrekʃən/"),
    V("careless", "粗心的", "/ˈkerləs/"),
    V("attention", "注意", "/əˈtenʃən/"),
    V("check", "检查", "/tʃek/"),
    S("我的作业充满了错误", "My homework is full of mistakes", "/maɪ ˈhoʊmwɜːrk ɪz fʊl əv mɪˈsteɪks/",
      [G("My", "Det", "/maɪ/"), G("homework", "S", "/ˈhoʊmwɜːrk/"), G("is", "V", "/ɪz/"), G("full", "C", "/fʊl/"), G("of", "P", "/əv/"), G("mistakes", "O", "/mɪˈsteɪks/")]),
    S("你应该更仔细", "You should be more careful", "/juː ʃʊd biː mɔːr ˈkerfəl/",
      [G("You", "S", "/juː/"), G("should", "V", "/ʃʊd/"), G("be", "V", "/biː/"), G("more", "Adv", "/mɔːr/"), G("careful", "C", "/ˈkerfəl/")]),
    S("老师纠正了我的错误", "The teacher corrected my mistakes", "/ðə ˈtiːtʃər kəˈrektɪd maɪ mɪˈsteɪks/",
      [G("The", "Art", "/ðə/"), G("teacher", "S", "/ˈtiːtʃər/"), G("corrected", "V", "/kəˈrektɪd/"), G("my", "Det", "/maɪ/"), G("mistakes", "O", "/mɪˈsteɪks/")]),
    S("你需要更加注意", "You need to pay more attention", "/juː niːd tə peɪ mɔːr əˈtenʃən/",
      [G("You", "S", "/juː/"), G("need", "V", "/niːd/"), G("to", "P", "/tə/"), G("pay", "V", "/peɪ/"), G("more", "Det", "/mɔːr/"), G("attention", "O", "/əˈtenʃən/")]),
    S("我检查了我的答案", "I checked my answers", "/aɪ tʃekt maɪ ˈænsərz/",
      [G("I", "S", "/aɪ/"), G("checked", "V", "/tʃekt/"), G("my", "Det", "/maɪ/"), G("answers", "O", "/ˈænsərz/")]),
    V("error", "错误", "/ˈerər/"),
    V("improve", "改善", "/ɪmˈpruːv/"),
]

# Lesson 106: Too expensive
L106 = [
    V("expensive", "昂贵的", "/ɪkˈspensɪv/"),
    V("cheap", "便宜的", "/tʃiːp/"),
    V("price", "价格", "/praɪs/"),
    V("afford", "负担得起", "/əˈfɔːrd/"),
    V("discount", "折扣", "/ˈdɪskaʊnt/"),
    S("这太贵了", "This is too expensive", "/ðɪs ɪz tuː ɪkˈspensɪv/",
      [G("This", "S", "/ðɪs/"), G("is", "V", "/ɪz/"), G("too", "Adv", "/tuː/"), G("expensive", "C", "/ɪkˈspensɪv/")]),
    S("我负担不起这个价格", "I can't afford this price", "/aɪ kænt əˈfɔːrd ðɪs praɪs/",
      [G("I", "S", "/aɪ/"), G("can't", "V", "/kænt/"), G("afford", "V", "/əˈfɔːrd/"), G("this", "Det", "/ðɪs/"), G("price", "O", "/praɪs/")]),
    S("有更便宜的版本吗？", "Is there a cheaper version?", "/ɪz ðer ə ˈtʃiːpər ˈvɜːrʒən/",
      [G("Is", "V", "/ɪz/"), G("there", "S", "/ðer/"), G("a", "Art", "/ə/"), G("cheaper", "Det", "/ˈtʃiːpər/"), G("version", "C", "/ˈvɜːrʒən/")]),
    S("这个在打折", "This is on discount", "/ðɪs ɪz ɒn ˈdɪskaʊnt/",
      [G("This", "S", "/ðɪs/"), G("is", "V", "/ɪz/"), G("on", "P", "/ɒn/"), G("discount", "O", "/ˈdɪskaʊnt/")]),
    S("价格太高了", "The price is too high", "/ðə praɪs ɪz tuː haɪ/",
      [G("The", "Art", "/ðə/"), G("price", "S", "/praɪs/"), G("is", "V", "/ɪz/"), G("too", "Adv", "/tuː/"), G("high", "C", "/haɪ/")]),
    V("cost", "花费", "/kɒst/"),
    V("reasonable", "合理的", "/ˈriːzənəbəl/"),
]

# Lesson 107: It's small
L107 = [
    V("small", "小的", "/smɔːl/"),
    V("big", "大的", "/bɪɡ/"),
    V("size", "尺寸", "/saɪz/"),
    V("tiny", "微小的", "/ˈtaɪni/"),
    V("huge", "巨大的", "/hjuːdʒ/"),
    S("它很小", "It's small", "/ɪts smɔːl/",
      [G("It", "S", "/ɪt/"), G("'s", "V", "/s/"), G("small", "C", "/smɔːl/")]),
    S("这个太大了", "This one is too big", "/ðɪs wʌn ɪz tuː bɪɡ/",
      [G("This", "Det", "/ðɪs/"), G("one", "S", "/wʌn/"), G("is", "V", "/ɪz/"), G("too", "Adv", "/tuː/"), G("big", "C", "/bɪɡ/")]),
    S("我想要一个小一点的", "I want a smaller one", "/aɪ wɒnt ə ˈsmɔːlər wʌn/",
      [G("I", "S", "/aɪ/"), G("want", "V", "/wɒnt/"), G("a", "Art", "/ə/"), G("smaller", "Det", "/ˈsmɔːlər/"), G("one", "O", "/wʌn/")]),
    S("这个尺寸正好", "This size is just right", "/ðɪs saɪz ɪz dʒʌst raɪt/",
      [G("This", "Det", "/ðɪs/"), G("size", "S", "/saɪz/"), G("is", "V", "/ɪz/"), G("just", "Adv", "/dʒʌst/"), G("right", "C", "/raɪt/")]),
    S("那个是巨大的", "That one is huge", "/ðæt wʌn ɪz hjuːdʒ/",
      [G("That", "Det", "/ðæt/"), G("one", "S", "/wʌn/"), G("is", "V", "/ɪz/"), G("huge", "C", "/hjuːdʒ/")]),
    V("medium", "中等的", "/ˈmiːdiəm/"),
    V("fit", "适合", "/fɪt/"),
]

lessons = {
    '102.json': L102,
    '103.json': L103,
    '104.json': L104,
    '105.json': L105,
    '106.json': L106,
    '107.json': L107,
}

for filename, lesson in lessons.items():
    filepath = os.path.join(OUT, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(lesson, f, ensure_ascii=False, indent=2)
    print(f'✅ {filename}: {len(lesson)} entries')

print('\n✅ NCE1 L102-107 完成！')
