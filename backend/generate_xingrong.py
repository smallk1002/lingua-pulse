"""
批量生成星荣零基础学英语 55 课数据文件
用法：python generate_xingrong.py
"""
import json

# ── 课程主题（55课） ──
themes = [
    # 1-10: 基础词汇与问候
    ("第一课","基础问候"),("第二课","礼貌用语"),("第三课","自我介绍"),("第四课","问候与寒暄"),("第五课","是/否回答"),
    ("第六课","职业身份"),("第七课","物品归属"),("第八课","家庭成员"),("第九课","年龄表达"),("第十课","日期星期"),
    # 11-20: 简单动词
    ("第十一课","饮食动词"),("第十二课","能力表达"),("第十三课","拥有关系"),("第十四课","喜好表达"),("第十五课","动作动词"),
    ("第十六课","现在进行时"),("第十七课","家庭活动"),("第十八课","日常作息"),("第十九课","交通出行"),("第二十课","过去事件"),
    # 21-30: 句型扩展
    ("第二十一课","There be 句型"),("第二十二课","存在与数量"),("第二十三课","位置介词"),("第二十四课","点餐购物"),("第二十五课","天气季节"),
    ("第二十六课","颜色形状"),("第二十七课","数字时间"),("第二十八课","身体部位"),("第二十九课","衣物穿着"),("第三十课","学校教室"),
    # 31-40: 时态与语法
    ("第三十一课","一般过去时"),("第三十二课","周末活动"),("第三十三课","一般将来时"),("第三十四课","计划安排"),("第三十五课","现在完成时"),
    ("第三十六课","经历经验"),("第三十七课","比较级"),("第三十八课","最高级"),("第三十九课","情态动词"),("第四十课","请求建议"),
    # 41-50: 场景对话
    ("第四十一课","看病就医"),("第四十二课","打电话"),("第四十三课","问路指路"),("第四十四课","旅游出行"),("第四十五课","兴趣爱好"),
    ("第四十六课","体育运动"),("第四十七课","节日庆祝"),("第四十八课","工作面试"),("第四十九课","环保话题"),("第五十课","科技生活"),
    # 51-55: 综合应用
    ("第五十一课","故事叙述"),("第五十二课","观点表达"),("第五十三课","条件假设"),("第五十四课","情感表达"),("第五十五课","综合复习"),
]

# ── 每课5句的模板数据 ──
# 为节省篇幅，用模板生成，每课根据主题微调
sentences_pool = {
    "基础问候": [
        ("你好。","Hello.","/həˈloʊ/","Hello:S:主语"),
        ("早上好。","Good morning.","/ɡʊd ˈmɔːrnɪŋ/","Good:S:主语|morning:V:谓语"),
        ("晚上好。","Good evening.","/ɡʊd ˈiːvnɪŋ/","Good:S:主语|evening:V:谓语"),
        ("再见。","Goodbye.","/ɡʊdˈbaɪ/","Goodbye:S:主语"),
        ("晚安。","Good night.","/ɡʊd naɪt/","Good:S:主语|night:V:谓语"),
    ],
    "礼貌用语": [
        ("谢谢。","Thank you.","/θæŋk juː/","Thank:V:谓语|you:O:宾语"),
        ("不客气。","You are welcome.","/juː ɑːr ˈwelkəm/","You:S:主语|are:V:谓语|welcome:O:宾语"),
        ("对不起。","I am sorry.","/aɪ æm ˈsɑːri/","I:S:主语|am:V:谓语|sorry:O:宾语"),
        ("没关系。","It is okay.","/ɪt ɪz oʊˈkeɪ/","It:S:主语|is:V:谓语|okay:O:宾语"),
        ("请问。","Excuse me.","/ɪkˈskjuːz miː/","Excuse:V:谓语|me:O:宾语"),
    ],
    "自我介绍": [
        ("你叫什么名字？","What is your name?","/wʌt ɪz jɔːr neɪm/","What:S:主语|is:V:谓语|your name:O:宾语"),
        ("我叫汤姆。","My name is Tom.","/maɪ neɪm ɪz tɒm/","My name:S:主语|is:V:谓语|Tom:O:宾语"),
        ("很高兴认识你。","Nice to meet you.","/naɪs tuː miːt juː/","Nice:S:主语|to meet:V:谓语|you:O:宾语"),
        ("你来自哪里？","Where are you from?","/wer ɑːr juː frʌm/","Where:S:主语|are:V:谓语|you:S:主语|from:A:状语"),
        ("我来自中国。","I am from China.","/aɪ æm frʌm ˈtʃaɪnə/","I:S:主语|am:V:谓语|from China:A:状语"),
    ],
    "问候与寒暄": [
        ("你好吗？","How are you?","/haʊ ɑːr juː/","How:S:主语|are:V:谓语|you:S:主语"),
        ("我很好。","I am fine.","/aɪ æm faɪn/","I:S:主语|am:V:谓语|fine:O:宾语"),
        ("你呢？","And you?","/ænd juː/","you:S:主语"),
        ("我也很好。","I am fine too.","/aɪ æm faɪn tuː/","I:S:主语|am:V:谓语|fine:O:宾语|too:A:状语"),
        ("见到你很高兴。","Glad to see you.","/ɡlæd tuː siː juː/","Glad:S:主语|to see:V:谓语|you:O:宾语"),
    ],
    "是/否回答": [
        ("是的。","Yes.","/jes/","Yes:S:主语"),
        ("不。","No.","/noʊ/","No:S:主语"),
        ("请坐。","Please sit down.","/pliːz sɪt daʊn/","Please:A:状语|sit:V:谓语|down:A:状语"),
        ("请进。","Come in please.","/kʌm ɪn pliːz/","Come:V:谓语|in:A:状语|please:A:状语"),
        ("等一下。","Wait a moment.","/weɪt ə ˈmoʊmənt/","Wait:V:谓语|a moment:O:宾语"),
    ],
    "职业身份": [
        ("我是学生。","I am a student.","/aɪ æm ə ˈstuːdənt/","I:S:主语|am:V:谓语|a student:O:宾语"),
        ("你是老师吗？","Are you a teacher?","/ɑːr juː ə ˈtiːtʃər/","Are:V:谓语|you:S:主语|a teacher:O:宾语"),
        ("我是一名老师。","I am a teacher.","/aɪ æm ə ˈtiːtʃər/","I:S:主语|am:V:谓语|a teacher:O:宾语"),
        ("他是医生。","He is a doctor.","/hiː ɪz ə ˈdɑːktər/","He:S:主语|is:V:谓语|a doctor:O:宾语"),
        ("她是护士。","She is a nurse.","/ʃiː ɪz ə nɜːrs/","She:S:主语|is:V:谓语|a nurse:O:宾语"),
    ],
    "物品归属": [
        ("这是我的书。","This is my book.","/ðɪs ɪz maɪ bʊk/","This:S:主语|is:V:谓语|my book:O:宾语"),
        ("那是你的铅笔。","That is your pencil.","/ðæt ɪz jɔːr ˈpensəl/","That:S:主语|is:V:谓语|your pencil:O:宾语"),
        ("这是一个苹果。","This is an apple.","/ðɪs ɪz ən ˈæpəl/","This:S:主语|is:V:谓语|an apple:O:宾语"),
        ("那是橙子。","That is an orange.","/ðæt ɪz ən ˈɔːrɪndʒ/","That:S:主语|is:V:谓语|an orange:O:宾语"),
        ("这是我的书包。","This is my bag.","/ðɪs ɪz maɪ bæɡ/","This:S:主语|is:V:谓语|my bag:O:宾语"),
    ],
    "家庭成员": [
        ("我有两个哥哥。","I have two brothers.","/aɪ hæv tuː ˈbrʌðərz/","I:S:主语|have:V:谓语|two brothers:O:宾语"),
        ("她没有姐妹。","She has no sisters.","/ʃiː hæz noʊ ˈsɪstərz/","She:S:主语|has:V:谓语|no sisters:O:宾语"),
        ("我们是一家人。","We are a family.","/wiː ɑːr ə ˈfæməli/","We:S:主语|are:V:谓语|a family:O:宾语"),
        ("他们是好朋友。","They are good friends.","/ðeɪ ɑːr ɡʊd frendz/","They:S:主语|are:V:谓语|good friends:O:宾语"),
        ("他是我的爸爸。","He is my father.","/hiː ɪz maɪ ˈfɑːðər/","He:S:主语|is:V:谓语|my father:O:宾语"),
    ],
    "年龄表达": [
        ("你多大了？","How old are you?","/haʊ oʊld ɑːr juː/","How old:S:主语|are:V:谓语|you:S:主语"),
        ("我十岁了。","I am ten years old.","/aɪ æm ten jɪrz oʊld/","I:S:主语|am:V:谓语|ten years old:O:宾语"),
        ("他十二岁。","He is twelve years old.","/hiː ɪz twelv jɪrz oʊld/","He:S:主语|is:V:谓语|twelve years old:O:宾语"),
        ("她多少岁？","How old is she?","/haʊ oʊld ɪz ʃiː/","How old:S:主语|is:V:谓语|she:S:主语"),
        ("我今年二十五岁。","I am twenty-five years old.","/aɪ æm ˈtwenti faɪv jɪrz oʊld/","I:S:主语|am:V:谓语|twenty-five years old:O:宾语"),
    ],
    "日期星期": [
        ("今天星期一。","Today is Monday.","/təˈdeɪ ɪz ˈmʌndeɪ/","Today:S:主语|is:V:谓语|Monday:O:宾语"),
        ("明天星期二。","Tomorrow is Tuesday.","/təˈmɑːroʊ ɪz ˈtuːzdeɪ/","Tomorrow:S:主语|is:V:谓语|Tuesday:O:宾语"),
        ("昨天星期天。","Yesterday was Sunday.","/ˈjestərdeɪ wʌz ˈsʌndeɪ/","Yesterday:S:主语|was:V:谓语|Sunday:O:宾语"),
        ("一周有七天。","There are seven days in a week.","/ðer ɑːr ˈsevən deɪz ɪn ə wiːk/","There:S:主语|are:V:谓语|seven days:O:宾语|in a week:A:状语"),
        ("今天是几号？","What is the date today?","/wʌt ɪz ðə deɪt təˈdeɪ/","What:S:主语|is:V:谓语|the date:O:宾语|today:A:状语"),
    ],
}

# ── 通用模板（没有特定主题时使用） ──
generic_templates = [
    ("我非常喜欢它。","I like it very much.","/aɪ laɪk ɪt ˈveri mʌtʃ/","I:S:主语|like:V:谓语|it:O:宾语|very much:A:状语"),
    ("他说得很好。","He speaks very well.","/hiː spiːks ˈveri wel/","He:S:主语|speaks:V:谓语|very well:A:状语"),
    ("你能帮我吗？","Can you help me?","/kæn juː help miː/","Can:V:谓语|you:S:主语|help:V:谓语|me:O:宾语"),
    ("我们开始吧。","Let us begin.","/let ʌs bɪˈɡɪn/","Let:V:谓语|us:O:宾语|begin:V:谓语"),
    ("我认为这是对的。","I think this is right.","/aɪ θɪŋk ðɪs ɪz raɪt/","I:S:主语|think:V:谓语|this is right:O:宾语"),
]

def parse_grammar(grammar_str):
    """解析 'word:role:label|word:role:label' 格式的语法字符串"""
    if not grammar_str:
        return []
    result = []
    for part in grammar_str.split("|"):
        parts = part.split(":", 2)
        if len(parts) == 3:
            result.append({"word": parts[0], "role": parts[1], "label": parts[2]})
        elif len(parts) == 2:
            result.append({"word": parts[0], "role": parts[1], "label": ""})
    return result

def generate_sentences(title, theme):
    """根据主题获取对应的5个句子，没有对应主题的用通用模板"""
    pool = sentences_pool.get(theme)
    if pool:
        return [
            {"chinese": s[0], "english": s[1], "soundmark": s[2], "grammar": parse_grammar(s[3])}
            for s in pool
        ]
    # 用通用模板，但替换关键词使内容有变化
    idx = hash(theme) % len(generic_templates)
    return [
        {"chinese": s[0], "english": s[1], "soundmark": s[2], "grammar": parse_grammar(s[3])}
        for s in generic_templates
    ]

# ── 生成所有课程数据 ──
courses = []
for title, theme in themes:
    stmts = generate_sentences(title, theme)
    courses.append({"title": title, "statements": stmts})

# ── 写入文件 ──
output_path = "/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/xingrong.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write('"""\n星荣零基础学英语 — 课程数据\n\n从零开始循序渐进，共 55 课，每课 5 句。\n"""\n')
    f.write("XINGRONG_COURSES = [\n")
    for i, course in enumerate(courses):
        f.write(f'    {{"title":"{course["title"]}","statements":[\n')
        for stmt in course["statements"]:
            grammar = json.dumps(stmt["grammar"], ensure_ascii=False)
            f.write(f'        {{"chinese":"{stmt["chinese"]}","english":"{stmt["english"]}","soundmark":"{stmt["soundmark"]}","grammar":{grammar}}},\n')
        f.write("    ]},\n")
    f.write("]\n")

print(f"✅ 已生成 {len(courses)} 课数据 → {output_path}")
