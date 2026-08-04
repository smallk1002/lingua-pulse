"""
批量生成新概念英语 1-4 册课程数据
用法：uv run python generate_nce.py
"""
import json

# ── 新概念一 (30课) ──
nce1_themes = [
    ("Lesson 1","Excuse me!"),("Lesson 2","Is this your...?"),("Lesson 3","Sorry, sir."),("Lesson 4","Are you...?"),("Lesson 5","Nice to meet you"),
    ("Lesson 6","What make is it?"),("Lesson 7","Nationality"),("Lesson 8","Jobs"),("Lesson 9","How are you today?"),("Lesson 10","Describing people"),
    ("Lesson 11","Whose is this?"),("Lesson 12","Family"),("Lesson 13","Colors"),("Lesson 14","Clothes"),("Lesson 15","Customs"),
    ("Lesson 16","Housework"),("Lesson 17","At the office"),("Lesson 18","Daily routine"),("Lesson 19","Shopping"),("Lesson 20","At the restaurant"),
    ("Lesson 21","Which book?"),("Lesson 22","At home"),("Lesson 23","Rooms"),("Lesson 24","Furniture"),("Lesson 25","In the kitchen"),
    ("Lesson 26","Food and drink"),("Lesson 27","Weather"),("Lesson 28","Seasons"),("Lesson 29","Transport"),("Lesson 30","Holidays"),
]
# ── 新概念二 (20课) ──
nce2_themes = [
    ("Lesson 1","A private conversation"),("Lesson 2","Breakfast or lunch?"),("Lesson 3","Please send me a card"),("Lesson 4","An exciting trip"),("Lesson 5","No wrong numbers"),
    ("Lesson 6","Percy Buttons"),("Lesson 7","Too late"),("Lesson 8","The best and the worst"),("Lesson 9","A cold welcome"),("Lesson 10","Not for jazz"),
    ("Lesson 11","One good turn deserves another"),("Lesson 12","Goodbye and good luck"),("Lesson 13","The Greenwood Boys"),("Lesson 14","Do you speak English?"),("Lesson 15","Good news"),
    ("Lesson 16","A polite request"),("Lesson 17","Always young"),("Lesson 18","He often does this!"),("Lesson 19","Sold out"),("Lesson 20","One man in a boat"),
]
# ── 新概念三 (15课) ──
nce3_themes = [
    ("Lesson 1","A puma at large"),("Lesson 2","Thirteen equals one"),("Lesson 3","An unknown goddess"),("Lesson 4","The double life"),("Lesson 5","The facts"),
    ("Lesson 6","Smash-and-grab"),("Lesson 7","Mutilated ladies"),("Lesson 8","A famous monastery"),("Lesson 9","Flying cats"),("Lesson 10","The loss of Titanic"),
    ("Lesson 11","Not guilty"),("Lesson 12","Life on a desert island"),("Lesson 13","It's only me"),("Lesson 14","A noble gangster"),("Lesson 15","Fifty pence worth of trouble"),
]
# ── 新概念四 (15课) ──
nce4_themes = [
    ("Lesson 1","Finding fossil man"),("Lesson 2","Spare that spider"),("Lesson 3","Matterhorn man"),("Lesson 4","Seeing hands"),("Lesson 5","Youth"),
    ("Lesson 6","The sporting spirit"),("Lesson 7","Bats"),("Lesson 8","Trading standards"),("Lesson 9","Royal espionage"),("Lesson 10","Silicon Valley"),
    ("Lesson 11","How to grow old"),("Lesson 12","Banks and their customers"),("Lesson 13","The search for oil"),("Lesson 14","The Butterfly Effect"),("Lesson 15","Secrecy in industry"),
]

# ── 根据课程编号选择合适难度级别的句子 ──
def get_grammar_str(level, tag):
    """返回 'word:role:label|...' 格式"""
    basic = {
        "be": "I:S:主语|am:V:谓语|a student:O:宾语",
        "is_this": "Is:V:谓语|this:S:主语|your book:O:宾语",
        "where": "Where:S:主语|is:V:谓语|your pen:O:宾语",
        "like": "I:S:主语|like:V:谓语|this song:O:宾语",
        "have": "I:S:主语|have:V:谓语|an idea:O:宾语",
    }
    intermediate = {
        "went": "They:S:主语|went:V:谓语|to London:A:状语|last week:A:状语",
        "since": "I:S:主语|have lived:V:谓语|here:A:状语|since 2010:A:状语",
        "passive": "English:O:宾语|is spoken:V:谓语|worldwide:A:状语",
        "if": "I:S:主语|will go:V:谓语|if it is sunny:A:状语",
        "when": "I:S:主语|was reading:V:谓语|when she called:A:状语",
    }
    advanced = {
        "not_only": "Not only:S:主语|did he win:V:谓语|but also:",
        "hardly": "Hardly:S:主语|had I arrived:V:谓语|when it started:A:状语",
        "should": "Should:V:谓语|you need help:O:宾语|call me:A:状语",
        "were": "Were:S:主语|I you:O:宾语|I would accept:A:状语",
        "it_is": "It is:S:主语|the first time:O:宾语|I have visited:V:谓语",
    }
    if level == 1:
        return list(basic.values())[hash(tag) % len(basic)]
    elif level == 2:
        return list(intermediate.values())[hash(tag) % len(intermediate)]
    else:
        return list(advanced.values())[hash(tag) % len(advanced)]

def parse_grammar(s):
    if not s:
        return []
    result = []
    for part in s.split("|"):
        parts = part.split(":", 2)
        if len(parts) >= 3:
            result.append({"word": parts[0], "role": parts[1], "label": parts[2]})
        elif len(parts) >= 2:
            result.append({"word": parts[0], "role": parts[1], "label": ""})
        elif parts[0]:
            result.append({"word": parts[0], "role": "", "label": ""})
    return result

def generate_nce_sentences(level, idx):
    """根据级别和编号生成5句话"""
    templates = {
        1: [  # NCE1: 简单句型
            [("请把门打开。","Open the door, please.","/ˈoʊpən ðə dɔːr pliːz/", "Open:V:谓语|the door:O:宾语|please:A:状语"),
             ("你能等一下吗？","Can you wait a moment?","/kæn juː weɪt ə ˈmoʊmənt/", "Can:V:谓语|you:S:主语|wait:V:谓语|a moment:O:宾语"),
             ("我有一些消息给你。","I have some news for you.","/aɪ hæv sʌm nuːz fɔːr juː/", "I:S:主语|have:V:谓语|some news:O:宾语|for you:A:状语"),
             ("他正在花园里工作。","He is working in the garden.","/hiː ɪz ˈwɜːrkɪŋ ɪn ðə ˈɡɑːrdən/", "He:S:主语|is working:V:谓语|in the garden:A:状语"),
             ("你看起来很开心。","You look very happy.","/juː lʊk ˈveri ˈhæpi/", "You:S:主语|look:V:谓语|very happy:O:宾语")],
            [("请把书给我。","Give me the book, please.","/ɡɪv miː ðə bʊk pliːz/", "Give:V:谓语|me:O:宾语|the book:O:宾语|please:A:状语"),
             ("这是谁的书包？","Whose bag is this?","/huːz bæɡ ɪz ðɪs/", "Whose bag:S:主语|is:V:谓语|this:O:宾语"),
             ("你能拼写一下吗？","Can you spell it?","/kæn juː spel ɪt/", "Can:V:谓语|you:S:主语|spell:V:谓语|it:O:宾语"),
             ("他来自加拿大。","He comes from Canada.","/hiː kʌmz frʌm ˈkænədə/", "He:S:主语|comes from:V:谓语|Canada:O:宾语"),
             ("我想买一件新外套。","I want to buy a new coat.","/aɪ wɑːnt tuː baɪ ə nuː koʊt/", "I:S:主语|want to buy:V:谓语|a new coat:O:宾语")],
            [("请把灯关掉。","Turn off the light, please.","/tɜːrn ɔːf ðə laɪt pliːz/", "Turn off:V:谓语|the light:O:宾语|please:A:状语"),
             ("你能帮我拿一下包吗？","Can you carry my bag?","/kæn juː ˈkæri maɪ bæɡ/", "Can:V:谓语|you:S:主语|carry:V:谓语|my bag:O:宾语"),
             ("今天天气真好！","What a lovely day!","/wʌt ə ˈlʌvli deɪ/", "What:S:主语|a lovely day:O:宾语"),
             ("我姐姐比我高。","My sister is taller than me.","/maɪ ˈsɪstər ɪz ˈtɔːlər ðæn miː/", "My sister:S:主语|is:V:谓语|taller:O:宾语|than me:A:状语"),
             ("我们去公园散步吧。","Let us go for a walk in the park.","/let ʌs ɡoʊ fɔːr ə wɔːk ɪn ðə pɑːrk/", "Let us:V:谓语|go for a walk:V:谓语|in the park:A:状语")],
        ],
        2: [  # NCE2: 段落和过去时
            [("他迅速离开了房间。","He left the room quickly.","/hiː left ðə ruːm ˈkwɪkli/", "He:S:主语|left:V:谓语|the room:O:宾语|quickly:A:状语"),
             ("他们已经在路上了。","They are already on their way.","/ðeɪ ɑːr ɔːlˈredi ɒn ðer weɪ/", "They:S:主语|are:V:谓语|already:A:状语|on their way:A:状语"),
             ("当时我正在看一本书。","I was reading a book at that time.","/aɪ wʌz ˈriːdɪŋ ə bʊk æt ðæt taɪm/", "I:S:主语|was reading:V:谓语|a book:O:宾语|at that time:A:状语"),
             ("直到今天我才明白。","I did not understand until today.","/aɪ dɪd nɑːt ˌʌndərˈstænd ənˈtɪl təˈdeɪ/", "I:S:主语|did not understand:V:谓语|until today:A:状语"),
             ("她转身看向窗外。","She turned and looked out of the window.","/ʃiː tɜːrnd ænd lʊkt aʊt ʌv ðə ˈwɪndoʊ/", "She:S:主语|turned:V:谓语|and looked:V:谓语|out of the window:A:状语")],
            [("他决定改变他的计划。","He decided to change his plan.","/hiː dɪˈsaɪdɪd tuː tʃeɪndʒ hɪz plæn/", "He:S:主语|decided:V:谓语|to change his plan:O:宾语"),
             ("消息很快传遍了整个镇子。","The news spread quickly through the town.","/ðə nuːz spred ˈkwɪkli θruː ðə taʊn/", "The news:S:主语|spread:V:谓语|quickly:A:状语|through the town:A:状语"),
             ("我从未见过如此美丽的景色。","I have never seen such a beautiful view.","/aɪ hæv ˈnevər siːn sʌtʃ ə ˈbjuːtɪfəl vjuː/", "I:S:主语|have never seen:V:谓语|such a beautiful view:O:宾语"),
             ("那栋楼是去年建的。","That building was built last year.","/ðæt ˈbɪldɪŋ wʌz bɪlt læst jɪr/", "That building:S:主语|was built:V:谓语|last year:A:状语"),
             ("如果我有时间，我会帮你。","If I have time, I will help you.","/ɪf aɪ hæv taɪm aɪ wɪl help juː/", "If I have time:A:状语|I:S:主语|will help:V:谓语|you:O:宾语")],
            [("这个问题很难回答。","This question is difficult to answer.","/ðɪs ˈkwestʃən ɪz ˈdɪfɪkəlt tuː ˈænsər/", "This question:S:主语|is:V:谓语|difficult to answer:O:宾语"),
             ("他们最终到达了目的地。","They finally reached the destination.","/ðeɪ ˈfaɪnəli riːtʃt ðə ˌdestɪˈneɪʃən/", "They:S:主语|finally:A:状语|reached:V:谓语|the destination:O:宾语"),
             ("我确认一切都安排好了。","I made sure everything was arranged.","/aɪ meɪd ʃʊr ˈevriθɪŋ wʌz əˈreɪndʒd/", "I:S:主语|made sure:V:谓语|everything was arranged:O:宾语"),
             ("他拒绝接受这个条件。","He refused to accept the condition.","/hiː rɪˈfjuːzd tuː əkˈsept ðə kənˈdɪʃən/", "He:S:主语|refused:V:谓语|to accept the condition:O:宾语"),
             ("随着时间推移，情况改善了。","As time went by, things improved.","/æz taɪm went baɪ θɪŋz ɪmˈpruːvd/", "As time went by:A:状语|things:S:主语|improved:V:谓语")],
        ],
        3: [  # NCE3-4: 复杂句型
            [("不可否认，技术改变了我们的生活。","There is no denying that technology has changed our lives.","","There:S:主语|is no denying:V:谓语|that technology has changed our lives:O:宾语"),
             ("事实是，很少有人能真正做到。","The fact is that very few people can truly do it.","","The fact:S:主语|is:V:谓语|that very few people can truly do it:O:宾语"),
             ("尽管困难重重，他最终还是成功了。","Despite all the difficulties, he finally succeeded.","","Despite all the difficulties:A:状语|he:S:主语|finally:A:状语|succeeded:V:谓语"),
             ("据估计，全球人口已超过八十亿。","It is estimated that the global population has exceeded eight billion.","","It:S:主语|is estimated:V:谓语|that the global population has exceeded eight billion:O:宾语"),
             ("越来越多的人意识到环境保护的重要性。","More and more people are realizing the importance of environmental protection.","","More and more people:S:主语|are realizing:V:谓语|the importance of environmental protection:O:宾语")],
            [("这个问题值得深入探讨。","This issue is worth discussing in depth.","","This issue:S:主语|is:V:谓语|worth discussing:O:宾语|in depth:A:状语"),
             ("没有人能否认教育的重要性。","No one can deny the importance of education.","","No one:S:主语|can deny:V:谓语|the importance of education:O:宾语"),
             ("随着科技的发展，我们的生活发生了巨大的变化。","With the development of technology, our lives have changed dramatically.","","With the development of technology:A:状语|our lives:S:主语|have changed:V:谓语|dramatically:A:状语"),
             ("我们不仅要关注现在，还要关注未来。","We should focus not only on the present but also on the future.","","We:S:主语|should focus:V:谓语|not only on the present:A:状语|but also on the future:A:状语"),
             ("这种现象背后的原因很复杂。","The reasons behind this phenomenon are complex.","","The reasons behind this phenomenon:S:主语|are:V:谓语|complex:O:宾语")],
            [("只有在极端情况下，才会采取这种措施。","Only in extreme cases will such measures be taken.","","Only in extreme cases:A:状语|will:V:谓语|such measures:S:主语|be taken:V:谓语"),
             ("时至今日，人们仍对这一发现争论不休。","To this day, people still debate this discovery.","","To this day:A:状语|people:S:主语|still:A:状语|debate:V:谓语|this discovery:O:宾语"),
             ("毫无疑问，这将是一个巨大的挑战。","There is no doubt that this will be a huge challenge.","","There is no doubt:S:主语|that this will be a huge challenge:O:宾语"),
             ("尽管科技进步了，但一些基本问题仍然存在。","Despite technological advances, some basic problems remain.","","Despite technological advances:A:状语|some basic problems:S:主语|remain:V:谓语"),
             ("我们面对的挑战前所未有。","The challenges we face are unprecedented.","","The challenges:S:主语|we face:V:谓语|are unprecedented:V:谓语")],
        ],
    }
    bucket = templates[level]
    return bucket[idx % len(bucket)]

def make_sentences(level, idx):
    raw = generate_nce_sentences(level, idx)
    return [{"chinese":s[0],"english":s[1],"soundmark":s[2],"grammar":parse_grammar(s[3])} for s in raw]

# ── 生成所有文件 ──
base = "/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data"

configs = [
    ("nce1", "新概念英语第一册", "经典教材，涵盖基础对话与语法。共30课。", nce1_themes, 1),
    ("nce2", "新概念英语第二册", "实践与进步，短文阅读与过去时态。共20课。", nce2_themes, 2),
    ("nce3", "新概念英语第三册", "培养技能，复杂句型与段落理解。共15课。", nce3_themes, 3),
    ("nce4", "新概念英语第四册", "流利英语，学术与思辨表达。共15课。", nce4_themes, 3),
]

for filename, _, desc, themes, level in configs:
    courses = []
    for i, (title, theme) in enumerate(themes):
        stmts = make_sentences(level, i)
        courses.append({"title": title, "statements": stmts})

    varname = f"NCE{level}_COURSES" if level == 1 else f"NCE{level}_COURSES"
    if filename == "nce2": varname = "NCE2_COURSES"
    if filename == "nce3": varname = "NCE3_COURSES"
    if filename == "nce4": varname = "NCE4_COURSES"

    path = f"{base}/{filename}.py"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'"""\n{desc}\n"""\n')
        f.write(f"{varname} = [\n")
        for course in courses:
            f.write(f'    {{"title":"{course["title"]}","statements":[\n')
            for stmt in course["statements"]:
                grammar = json.dumps(stmt["grammar"], ensure_ascii=False)
                f.write(f'        {{"chinese":"{stmt["chinese"]}","english":"{stmt["english"]}","soundmark":"{stmt["soundmark"]}","grammar":{grammar}}},\n')
            f.write("    ]},\n")
        f.write("]\n")
    print(f"✅ {filename}: {len(courses)} 课")

print("\n全部生成完成！")
