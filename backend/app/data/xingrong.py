"""
星荣零基础学英语 — 课程数据

从零开始循序渐进，涵盖基础词汇、简单句型、日常对话。
共 20 课，每课 5 句。
"""

XINGRONG_COURSES = [
    # ═══════ 第 1-5 课：基础词汇 ═══════
    {
        "title": "第一课",
        "statements": [
            {
                "chinese": "你好。",
                "english": "Hello.",
                "soundmark": "/həˈloʊ/",
                "grammar": [{"word": "Hello", "role": "S", "label": "主语"}],
            },
            {
                "chinese": "早上好。",
                "english": "Good morning.",
                "soundmark": "/ɡʊd ˈmɔːrnɪŋ/",
                "grammar": [
                    {"word": "Good", "role": "S", "label": "主语"},
                    {"word": "morning", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "再见。",
                "english": "Goodbye.",
                "soundmark": "/ɡʊdˈbaɪ/",
                "grammar": [{"word": "Goodbye", "role": "S", "label": "主语"}],
            },
            {
                "chinese": "谢谢。",
                "english": "Thank you.",
                "soundmark": "/θæŋk juː/",
                "grammar": [
                    {"word": "Thank", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "是的。",
                "english": "Yes.",
                "soundmark": "/jes/",
                "grammar": [{"word": "Yes", "role": "S", "label": "主语"}],
            },
        ],
    },
    {
        "title": "第二课",
        "statements": [
            {
                "chinese": "不。",
                "english": "No.",
                "soundmark": "/noʊ/",
                "grammar": [{"word": "No", "role": "S", "label": "主语"}],
            },
            {
                "chinese": "请问。",
                "english": "Excuse me.",
                "soundmark": "/ɪkˈskjuːz miː/",
                "grammar": [
                    {"word": "Excuse", "role": "V", "label": "谓语"},
                    {"word": "me", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "对不起。",
                "english": "I am sorry.",
                "soundmark": "/aɪ æm ˈsɑːri/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "sorry", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "请坐。",
                "english": "Please sit down.",
                "soundmark": "/pliːz sɪt daʊn/",
                "grammar": [
                    {"word": "Please", "role": "A", "label": "状语"},
                    {"word": "sit", "role": "V", "label": "谓语"},
                    {"word": "down", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "没关系。",
                "english": "That is all right.",
                "soundmark": "/ðæt ɪz ɔːl raɪt/",
                "grammar": [
                    {"word": "That", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "all right", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第三课",
        "statements": [
            {
                "chinese": "我很好。",
                "english": "I am fine.",
                "soundmark": "/aɪ æm faɪn/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "fine", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你叫什么名字？",
                "english": "What is your name?",
                "soundmark": "/wʌt ɪz jɔːr neɪm/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "your name", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我叫汤姆。",
                "english": "My name is Tom.",
                "soundmark": "/maɪ neɪm ɪz tɒm/",
                "grammar": [
                    {"word": "My name", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "Tom", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "很高兴认识你。",
                "english": "Nice to meet you.",
                "soundmark": "/naɪs tuː miːt juː/",
                "grammar": [
                    {"word": "Nice", "role": "S", "label": "主语"},
                    {"word": "to meet", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你是学生吗？",
                "english": "Are you a student?",
                "soundmark": "/ɑːr juː ə ˈstuːdənt/",
                "grammar": [
                    {"word": "Are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "a student", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第四课",
        "statements": [
            {
                "chinese": "我是一名老师。",
                "english": "I am a teacher.",
                "soundmark": "/aɪ æm ə ˈtiːtʃər/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "a teacher", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这是我的书。",
                "english": "This is my book.",
                "soundmark": "/ðɪs ɪz maɪ bʊk/",
                "grammar": [
                    {"word": "This", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "my book", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "那是什么？",
                "english": "What is that?",
                "soundmark": "/wʌt ɪz ðæt/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "that", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "那是一支笔。",
                "english": "That is a pen.",
                "soundmark": "/ðæt ɪz ə pen/",
                "grammar": [
                    {"word": "That", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a pen", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这是一个苹果。",
                "english": "This is an apple.",
                "soundmark": "/ðɪs ɪz ən ˈæpəl/",
                "grammar": [
                    {"word": "This", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "an apple", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第五课",
        "statements": [
            {
                "chinese": "他是我爸爸。",
                "english": "He is my father.",
                "soundmark": "/hiː ɪz maɪ ˈfɑːðər/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "my father", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她是我妈妈。",
                "english": "She is my mother.",
                "soundmark": "/ʃiː ɪz maɪ ˈmʌðər/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "my mother", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我们是一家人。",
                "english": "We are a family.",
                "soundmark": "/wiː ɑːr ə ˈfæməli/",
                "grammar": [
                    {"word": "We", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "a family", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他们是朋友。",
                "english": "They are friends.",
                "soundmark": "/ðeɪ ɑːr frendz/",
                "grammar": [
                    {"word": "They", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "friends", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "它是一只猫。",
                "english": "It is a cat.",
                "soundmark": "/ɪt ɪz ə kæt/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a cat", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },

    # ═══════ 第 6-10 课：简单句型 ═══════
    {
        "title": "第六课",
        "statements": [
            {
                "chinese": "我有一个新书包。",
                "english": "I have a new bag.",
                "soundmark": "/aɪ hæv ə nuː bæɡ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "a new bag", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她有一本词典。",
                "english": "She has a dictionary.",
                "soundmark": "/ʃiː hæz ə ˈdɪkʃəneri/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "has", "role": "V", "label": "谓语"},
                    {"word": "a dictionary", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我没有橡皮。",
                "english": "I do not have an eraser.",
                "soundmark": "/aɪ duː nɑːt hæv ən ɪˈreɪsər/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "do not have", "role": "V", "label": "谓语"},
                    {"word": "an eraser", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你有铅笔吗？",
                "english": "Do you have a pencil?",
                "soundmark": "/duː juː hæv ə ˈpensəl/",
                "grammar": [
                    {"word": "Do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "a pencil", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他有一辆自行车。",
                "english": "He has a bike.",
                "soundmark": "/hiː hæz ə baɪk/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "has", "role": "V", "label": "谓语"},
                    {"word": "a bike", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第七课",
        "statements": [
            {
                "chinese": "我会说英语。",
                "english": "I can speak English.",
                "soundmark": "/aɪ kæn spiːk ˈɪŋɡlɪʃ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "can speak", "role": "V", "label": "谓语"},
                    {"word": "English", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你会游泳吗？",
                "english": "Can you swim?",
                "soundmark": "/kæn juː swɪm/",
                "grammar": [
                    {"word": "Can", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "swim", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "我不会开车。",
                "english": "I cannot drive.",
                "soundmark": "/aɪ ˈkænɑːt draɪv/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "cannot", "role": "V", "label": "谓语"},
                    {"word": "drive", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "他会弹钢琴。",
                "english": "He can play the piano.",
                "soundmark": "/hiː kæn pleɪ ðə piˈænoʊ/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "can play", "role": "V", "label": "谓语"},
                    {"word": "the piano", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我们能帮你。",
                "english": "We can help you.",
                "soundmark": "/wiː kæn help juː/",
                "grammar": [
                    {"word": "We", "role": "S", "label": "主语"},
                    {"word": "can help", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第八课",
        "statements": [
            {
                "chinese": "我喜欢音乐。",
                "english": "I like music.",
                "soundmark": "/aɪ laɪk ˈmjuːzɪk/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "like", "role": "V", "label": "谓语"},
                    {"word": "music", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她喜欢跳舞。",
                "english": "She likes dancing.",
                "soundmark": "/ʃiː laɪks ˈdænsɪŋ/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "likes", "role": "V", "label": "谓语"},
                    {"word": "dancing", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我们不喜欢下雨天。",
                "english": "We do not like rainy days.",
                "soundmark": "/wiː duː nɑːt laɪk ˈreɪni deɪz/",
                "grammar": [
                    {"word": "We", "role": "S", "label": "主语"},
                    {"word": "do not like", "role": "V", "label": "谓语"},
                    {"word": "rainy days", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你喜欢看电影吗？",
                "english": "Do you like watching movies?",
                "soundmark": "/duː juː laɪk ˈwɑːtʃɪŋ ˈmuːviz/",
                "grammar": [
                    {"word": "Do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "like", "role": "V", "label": "谓语"},
                    {"word": "watching movies", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他最喜欢足球。",
                "english": "He loves football best.",
                "soundmark": "/hiː lʌvz ˈfʊtbɔːl best/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "loves", "role": "V", "label": "谓语"},
                    {"word": "football", "role": "O", "label": "宾语"},
                    {"word": "best", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第九课",
        "statements": [
            {
                "chinese": "我正在看书。",
                "english": "I am reading a book.",
                "soundmark": "/aɪ æm ˈriːdɪŋ ə bʊk/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am reading", "role": "V", "label": "谓语"},
                    {"word": "a book", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她在写作业。",
                "english": "She is doing homework.",
                "soundmark": "/ʃiː ɪz ˈduːɪŋ ˈhoʊmwɜːrk/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "is doing", "role": "V", "label": "谓语"},
                    {"word": "homework", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他们在踢足球。",
                "english": "They are playing football.",
                "soundmark": "/ðeɪ ɑːr ˈpleɪɪŋ ˈfʊtbɔːl/",
                "grammar": [
                    {"word": "They", "role": "S", "label": "主语"},
                    {"word": "are playing", "role": "V", "label": "谓语"},
                    {"word": "football", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你正在听什么？",
                "english": "What are you listening to?",
                "soundmark": "/wʌt ɑːr juː ˈlɪsənɪŋ tuː/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "listening to", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "爸爸正在看报纸。",
                "english": "Father is reading the newspaper.",
                "soundmark": "/ˈfɑːðər ɪz ˈriːdɪŋ ðə ˈnuːzpeɪpər/",
                "grammar": [
                    {"word": "Father", "role": "S", "label": "主语"},
                    {"word": "is reading", "role": "V", "label": "谓语"},
                    {"word": "the newspaper", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第十课",
        "statements": [
            {
                "chinese": "桌子上有一本书。",
                "english": "There is a book on the desk.",
                "soundmark": "/ðer ɪz ə bʊk ɒn ðə desk/",
                "grammar": [
                    {"word": "There", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a book", "role": "O", "label": "宾语"},
                    {"word": "on the desk", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "房间里有两把椅子。",
                "english": "There are two chairs in the room.",
                "soundmark": "/ðer ɑːr tuː tʃerz ɪn ðə ruːm/",
                "grammar": [
                    {"word": "There", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "two chairs", "role": "O", "label": "宾语"},
                    {"word": "in the room", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "书包里有什么？",
                "english": "What is in the bag?",
                "soundmark": "/wʌt ɪz ɪn ðə bæɡ/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "in the bag", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "墙上有张地图。",
                "english": "There is a map on the wall.",
                "soundmark": "/ðer ɪz ə mæp ɒn ðə wɔːl/",
                "grammar": [
                    {"word": "There", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a map", "role": "O", "label": "宾语"},
                    {"word": "on the wall", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "花园里有很多花。",
                "english": "There are many flowers in the garden.",
                "soundmark": "/ðer ɑːr ˈmeni ˈflaʊərz ɪn ðə ˈɡɑːrdən/",
                "grammar": [
                    {"word": "There", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "many flowers", "role": "O", "label": "宾语"},
                    {"word": "in the garden", "role": "A", "label": "状语"},
                ],
            },
        ],
    },

    # ═══════ 第 11-15 课：时间与地点 ═══════
    {
        "title": "第十一课",
        "statements": [
            {
                "chinese": "现在几点了？",
                "english": "What time is it?",
                "soundmark": "/wʌt taɪm ɪz ɪt/",
                "grammar": [
                    {"word": "What time", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "现在七点钟。",
                "english": "It is seven o'clock.",
                "soundmark": "/ɪt ɪz ˈsevən əˈklɑːk/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "seven o'clock", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我每天早上六点起床。",
                "english": "I get up at six every morning.",
                "soundmark": "/aɪ ɡet ʌp æt sɪks ˈevri ˈmɔːrnɪŋ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "get up", "role": "V", "label": "谓语"},
                    {"word": "at six", "role": "A", "label": "状语"},
                    {"word": "every morning", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我们八点半上课。",
                "english": "We have class at half past eight.",
                "soundmark": "/wiː hæv klæs æt hæf pæst eɪt/",
                "grammar": [
                    {"word": "We", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "class", "role": "O", "label": "宾语"},
                    {"word": "at half past eight", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "她通常晚上十点睡觉。",
                "english": "She usually goes to bed at ten at night.",
                "soundmark": "/ʃiː ˈjuːʒuəli ɡoʊz tuː bed æt ten æt naɪt/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "usually", "role": "A", "label": "状语"},
                    {"word": "goes to bed", "role": "V", "label": "谓语"},
                    {"word": "at ten at night", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第十二课",
        "statements": [
            {
                "chinese": "你的书包在哪里？",
                "english": "Where is your bag?",
                "soundmark": "/wer ɪz jɔːr bæɡ/",
                "grammar": [
                    {"word": "Where", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "your bag", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "它在椅子下面。",
                "english": "It is under the chair.",
                "soundmark": "/ɪt ɪz ˈʌndər ðə tʃer/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "under the chair", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "邮局在银行旁边。",
                "english": "The post office is next to the bank.",
                "soundmark": "/ðə poʊst ˈɑːfɪs ɪz nekst tuː ðə bæŋk/",
                "grammar": [
                    {"word": "The post office", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "next to the bank", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "图书馆在哪里？",
                "english": "Where is the library?",
                "soundmark": "/wer ɪz ðə ˈlaɪbreri/",
                "grammar": [
                    {"word": "Where", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "the library", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "医院在公园对面。",
                "english": "The hospital is opposite the park.",
                "soundmark": "/ðə ˈhɑːspɪtəl ɪz ˈɑːpəzɪt ðə pɑːrk/",
                "grammar": [
                    {"word": "The hospital", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "opposite the park", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第十三课",
        "statements": [
            {
                "chinese": "今天天气怎么样？",
                "english": "How is the weather today?",
                "soundmark": "/haʊ ɪz ðə ˈweðər təˈdeɪ/",
                "grammar": [
                    {"word": "How", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "the weather", "role": "O", "label": "宾语"},
                    {"word": "today", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "今天很暖和。",
                "english": "It is warm today.",
                "soundmark": "/ɪt ɪz wɔːrm təˈdeɪ/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "warm", "role": "O", "label": "宾语"},
                    {"word": "today", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "昨天天气很冷。",
                "english": "It was cold yesterday.",
                "soundmark": "/ɪt wʌz koʊld ˈjestərdeɪ/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "was", "role": "V", "label": "谓语"},
                    {"word": "cold", "role": "O", "label": "宾语"},
                    {"word": "yesterday", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "明天会下雨吗？",
                "english": "Will it rain tomorrow?",
                "soundmark": "/wɪl ɪt reɪn təˈmɑːroʊ/",
                "grammar": [
                    {"word": "Will", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "S", "label": "主语"},
                    {"word": "rain", "role": "V", "label": "谓语"},
                    {"word": "tomorrow", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "春天很美丽。",
                "english": "Spring is very beautiful.",
                "soundmark": "/sprɪŋ ɪz ˈveri ˈbjuːtɪfəl/",
                "grammar": [
                    {"word": "Spring", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "very beautiful", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第十四课",
        "statements": [
            {
                "chinese": "你每天怎么去上学？",
                "english": "How do you go to school every day?",
                "soundmark": "/haʊ duː juː ɡoʊ tuː skuːl ˈevri deɪ/",
                "grammar": [
                    {"word": "How", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "go to school", "role": "V", "label": "谓语"},
                    {"word": "every day", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我骑自行车去上学。",
                "english": "I go to school by bike.",
                "soundmark": "/aɪ ɡoʊ tuː skuːl baɪ baɪk/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "go to school", "role": "V", "label": "谓语"},
                    {"word": "by bike", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "她坐公共汽车去上班。",
                "english": "She goes to work by bus.",
                "soundmark": "/ʃiː ɡoʊz tuː wɜːrk baɪ bʌs/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "goes to work", "role": "V", "label": "谓语"},
                    {"word": "by bus", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "他走路去公园。",
                "english": "He walks to the park.",
                "soundmark": "/hiː wɔːks tuː ðə pɑːrk/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "walks", "role": "V", "label": "谓语"},
                    {"word": "to the park", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "从这里到学校有多远？",
                "english": "How far is it from here to the school?",
                "soundmark": "/haʊ fɑːr ɪz ɪt frʌm hɪr tuː ðə skuːl/",
                "grammar": [
                    {"word": "How far", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "O", "label": "宾语"},
                    {"word": "from here to the school", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第十五课",
        "statements": [
            {
                "chinese": "我想要一杯水。",
                "english": "I would like a glass of water.",
                "soundmark": "/aɪ wʊd laɪk ə ɡlæs ʌv ˈwɔːtər/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "would like", "role": "V", "label": "谓语"},
                    {"word": "a glass of water", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你想吃点什么？",
                "english": "What would you like to eat?",
                "soundmark": "/wʌt wʊd juː laɪk tuː iːt/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "would", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "like to eat", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "请给我一杯咖啡。",
                "english": "Please give me a cup of coffee.",
                "soundmark": "/pliːz ɡɪv miː ə kʌp ʌv ˈkɑːfi/",
                "grammar": [
                    {"word": "Please", "role": "A", "label": "状语"},
                    {"word": "give", "role": "V", "label": "谓语"},
                    {"word": "me", "role": "O", "label": "宾语"},
                    {"word": "a cup of coffee", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我可以点餐吗？",
                "english": "May I take your order?",
                "soundmark": "/meɪ aɪ teɪk jɔːr ˈɔːrdər/",
                "grammar": [
                    {"word": "May", "role": "V", "label": "谓语"},
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "take", "role": "V", "label": "谓语"},
                    {"word": "your order", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "一共多少钱？",
                "english": "How much is it altogether?",
                "soundmark": "/haʊ mʌtʃ ɪz ɪt ˌɔːltəˈɡeðər/",
                "grammar": [
                    {"word": "How much", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "O", "label": "宾语"},
                    {"word": "altogether", "role": "A", "label": "状语"},
                ],
            },
        ],
    },

    # ═══════ 第 16-20 课：日常对话 ═══════
    {
        "title": "第十六课",
        "statements": [
            {
                "chinese": "昨天你去哪里了？",
                "english": "Where did you go yesterday?",
                "soundmark": "/wer dɪd juː ɡoʊ ˈjestərdeɪ/",
                "grammar": [
                    {"word": "Where", "role": "S", "label": "主语"},
                    {"word": "did", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "go", "role": "V", "label": "谓语"},
                    {"word": "yesterday", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我去了超市。",
                "english": "I went to the supermarket.",
                "soundmark": "/aɪ went tuː ðə ˈsuːpərˌmɑːrkɪt/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "went", "role": "V", "label": "谓语"},
                    {"word": "to the supermarket", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "你买了什么？",
                "english": "What did you buy?",
                "soundmark": "/wʌt dɪd juː baɪ/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "did", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "buy", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "我买了一些水果。",
                "english": "I bought some fruit.",
                "soundmark": "/aɪ bɔːt sʌm fruːt/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "bought", "role": "V", "label": "谓语"},
                    {"word": "some fruit", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我昨天过得很开心。",
                "english": "I had a good time yesterday.",
                "soundmark": "/aɪ hæd ə ɡʊd taɪm ˈjestərdeɪ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "had", "role": "V", "label": "谓语"},
                    {"word": "a good time", "role": "O", "label": "宾语"},
                    {"word": "yesterday", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第十七课",
        "statements": [
            {
                "chinese": "你周末打算做什么？",
                "english": "What are you going to do this weekend?",
                "soundmark": "/wʌt ɑːr juː ˈɡoʊɪŋ tuː duː ðɪs ˈwiːkend/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "going to do", "role": "V", "label": "谓语"},
                    {"word": "this weekend", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我打算去看电影。",
                "english": "I am going to watch a movie.",
                "soundmark": "/aɪ æm ˈɡoʊɪŋ tuː wɑːtʃ ə ˈmuːvi/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am going to watch", "role": "V", "label": "谓语"},
                    {"word": "a movie", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我们明天会去爬山。",
                "english": "We will climb the mountain tomorrow.",
                "soundmark": "/wiː wɪl klaɪm ðə ˈmaʊntən təˈmɑːroʊ/",
                "grammar": [
                    {"word": "We", "role": "S", "label": "主语"},
                    {"word": "will climb", "role": "V", "label": "谓语"},
                    {"word": "the mountain", "role": "O", "label": "宾语"},
                    {"word": "tomorrow", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "你会来参加派对吗？",
                "english": "Will you come to the party?",
                "soundmark": "/wɪl juː kʌm tuː ðə ˈpɑːrti/",
                "grammar": [
                    {"word": "Will", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "come", "role": "V", "label": "谓语"},
                    {"word": "to the party", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我希望我能去。",
                "english": "I hope I can go.",
                "soundmark": "/aɪ hoʊp aɪ kæn ɡoʊ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "hope", "role": "V", "label": "谓语"},
                    {"word": "I can go", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第十八课",
        "statements": [
            {
                "chinese": "你感觉怎么样？",
                "english": "How are you feeling?",
                "soundmark": "/haʊ ɑːr juː ˈfiːlɪŋ/",
                "grammar": [
                    {"word": "How", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "feeling", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "我有点头疼。",
                "english": "I have a headache.",
                "soundmark": "/aɪ hæv ə ˈhedeɪk/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "a headache", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你应该去看医生。",
                "english": "You should see a doctor.",
                "soundmark": "/juː ʃʊd siː ə ˈdɑːktər/",
                "grammar": [
                    {"word": "You", "role": "S", "label": "主语"},
                    {"word": "should see", "role": "V", "label": "谓语"},
                    {"word": "a doctor", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "多喝水，好好休息。",
                "english": "Drink more water and rest well.",
                "soundmark": "/drɪŋk mɔːr ˈwɔːtər ænd rest wel/",
                "grammar": [
                    {"word": "Drink", "role": "V", "label": "谓语"},
                    {"word": "more water", "role": "O", "label": "宾语"},
                    {"word": "and", "role": "", "label": ""},
                    {"word": "rest", "role": "V", "label": "谓语"},
                    {"word": "well", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我希望你早日康复。",
                "english": "I hope you get well soon.",
                "soundmark": "/aɪ hoʊp juː ɡet wel suːn/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "hope", "role": "V", "label": "谓语"},
                    {"word": "you get well soon", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "第十九课",
        "statements": [
            {
                "chinese": "你能帮我一个忙吗？",
                "english": "Can you do me a favor?",
                "soundmark": "/kæn juː duː miː ə ˈfeɪvər/",
                "grammar": [
                    {"word": "Can", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                    {"word": "me", "role": "O", "label": "宾语"},
                    {"word": "a favor", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "当然可以。",
                "english": "Of course.",
                "soundmark": "/ʌv kɔːrs/",
                "grammar": [
                    {"word": "Of", "role": "", "label": ""},
                    {"word": "course", "role": "S", "label": "主语"},
                ],
            },
            {
                "chinese": "请把门打开。",
                "english": "Please open the door.",
                "soundmark": "/pliːz ˈoʊpən ðə dɔːr/",
                "grammar": [
                    {"word": "Please", "role": "A", "label": "状语"},
                    {"word": "open", "role": "V", "label": "谓语"},
                    {"word": "the door", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "能把盐递给我吗？",
                "english": "Could you pass me the salt?",
                "soundmark": "/kʊd juː pæs miː ðə sɔːlt/",
                "grammar": [
                    {"word": "Could", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "pass", "role": "V", "label": "谓语"},
                    {"word": "me", "role": "O", "label": "宾语"},
                    {"word": "the salt", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "非常感谢你的帮助。",
                "english": "Thank you very much for your help.",
                "soundmark": "/θæŋk juː ˈveri mʌtʃ fɔːr jɔːr help/",
                "grammar": [
                    {"word": "Thank", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "O", "label": "宾语"},
                    {"word": "very much", "role": "A", "label": "状语"},
                    {"word": "for your help", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "第二十课",
        "statements": [
            {
                "chinese": "你学英语多久了？",
                "english": "How long have you studied English?",
                "soundmark": "/haʊ lɔːŋ hæv juː ˈstʌdid ˈɪŋɡlɪʃ/",
                "grammar": [
                    {"word": "How long", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "studied", "role": "V", "label": "谓语"},
                    {"word": "English", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我已经学了三年了。",
                "english": "I have studied for three years.",
                "soundmark": "/aɪ hæv ˈstʌdid fɔːr θriː jɪrz/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "have studied", "role": "V", "label": "谓语"},
                    {"word": "for three years", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "你去过北京吗？",
                "english": "Have you ever been to Beijing?",
                "soundmark": "/hæv juː ˈevər bɪn tuː beɪˈdʒɪŋ/",
                "grammar": [
                    {"word": "Have", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "ever", "role": "A", "label": "状语"},
                    {"word": "been to", "role": "V", "label": "谓语"},
                    {"word": "Beijing", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我还没有完成作业。",
                "english": "I have not finished my homework yet.",
                "soundmark": "/aɪ hæv nɑːt ˈfɪnɪʃt maɪ ˈhoʊmwɜːrk jet/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "have not finished", "role": "V", "label": "谓语"},
                    {"word": "my homework", "role": "O", "label": "宾语"},
                    {"word": "yet", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "继续加油，你会越来越好的！",
                "english": "Keep going and you will get better!",
                "soundmark": "/kiːp ˈɡoʊɪŋ ænd juː wɪl ɡet ˈbetər/",
                "grammar": [
                    {"word": "Keep", "role": "V", "label": "谓语"},
                    {"word": "going", "role": "V", "label": "谓语"},
                    {"word": "and", "role": "", "label": ""},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "will get", "role": "V", "label": "谓语"},
                    {"word": "better", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
]
