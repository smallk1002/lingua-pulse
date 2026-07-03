"""
新概念英语第一册 — 课程数据

经典教材，涵盖基础语法与日常对话。
共 10 课，每课 5 句。
"""

NCE_COURSES = [
    {
        "title": "Lesson 1",
        "statements": [
            {
                "chinese": "对不起！",
                "english": "Excuse me!",
                "soundmark": "/ɪkˈskjuːz miː/",
                "grammar": [
                    {"word": "Excuse", "role": "V", "label": "谓语"},
                    {"word": "me", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这是您的手提包吗？",
                "english": "Is this your handbag?",
                "soundmark": "/ɪz ðɪs jɔːr ˈhændbæɡ/",
                "grammar": [
                    {"word": "Is", "role": "V", "label": "谓语"},
                    {"word": "this", "role": "S", "label": "主语"},
                    {"word": "your handbag", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "对不起，请再说一遍。",
                "english": "Pardon?",
                "soundmark": "/ˈpɑːrdən/",
                "grammar": [{"word": "Pardon", "role": "S", "label": "主语"}],
            },
            {
                "chinese": "是的，是我的。",
                "english": "Yes, it is.",
                "soundmark": "/jes ɪt ɪz/",
                "grammar": [
                    {"word": "Yes", "role": "S", "label": "主语"},
                    {"word": "it is", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "非常感谢。",
                "english": "Thank you very much.",
                "soundmark": "/θæŋk juː ˈveri mʌtʃ/",
                "grammar": [
                    {"word": "Thank", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "O", "label": "宾语"},
                    {"word": "very much", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 2",
        "statements": [
            {
                "chinese": "这是你的钢笔吗？",
                "english": "Is this your pen?",
                "soundmark": "/ɪz ðɪs jɔːr pen/",
                "grammar": [
                    {"word": "Is", "role": "V", "label": "谓语"},
                    {"word": "this", "role": "S", "label": "主语"},
                    {"word": "your pen", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这是我的铅笔。",
                "english": "This is my pencil.",
                "soundmark": "/ðɪs ɪz maɪ ˈpensəl/",
                "grammar": [
                    {"word": "This", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "my pencil", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这不是我的书。",
                "english": "This is not my book.",
                "soundmark": "/ðɪs ɪz nɑːt maɪ bʊk/",
                "grammar": [
                    {"word": "This", "role": "S", "label": "主语"},
                    {"word": "is not", "role": "V", "label": "谓语"},
                    {"word": "my book", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这是你的手表吗？",
                "english": "Is this your watch?",
                "soundmark": "/ɪz ðɪs jɔːr wɑːtʃ/",
                "grammar": [
                    {"word": "Is", "role": "V", "label": "谓语"},
                    {"word": "this", "role": "S", "label": "主语"},
                    {"word": "your watch", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "它是我的外套。",
                "english": "It is my coat.",
                "soundmark": "/ɪt ɪz maɪ koʊt/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "my coat", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 3",
        "statements": [
            {
                "chinese": "请把我的外套给我。",
                "english": "My coat and my umbrella please.",
                "soundmark": "/maɪ koʊt ænd maɪ ʌmˈbrelə pliːz/",
                "grammar": [
                    {"word": "My coat", "role": "S", "label": "主语"},
                    {"word": "and", "role": "", "label": ""},
                    {"word": "my umbrella", "role": "S", "label": "主语"},
                    {"word": "please", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "这是您的雨伞。",
                "english": "Here is your umbrella.",
                "soundmark": "/hɪr ɪz jɔːr ʌmˈbrelə/",
                "grammar": [
                    {"word": "Here", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "your umbrella", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这不是我的雨伞。",
                "english": "This is not my umbrella.",
                "soundmark": "/ðɪs ɪz nɑːt maɪ ʌmˈbrelə/",
                "grammar": [
                    {"word": "This", "role": "S", "label": "主语"},
                    {"word": "is not", "role": "V", "label": "谓语"},
                    {"word": "my umbrella", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这个号码对吗？",
                "english": "Is this number right?",
                "soundmark": "/ɪz ðɪs ˈnʌmbər raɪt/",
                "grammar": [
                    {"word": "Is", "role": "V", "label": "谓语"},
                    {"word": "this number", "role": "S", "label": "主语"},
                    {"word": "right", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "对不起，先生。",
                "english": "I am sorry, sir.",
                "soundmark": "/aɪ æm ˈsɑːri sɜːr/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "sorry", "role": "O", "label": "宾语"},
                    {"word": "sir", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 4",
        "statements": [
            {
                "chinese": "你是法国人吗？",
                "english": "Are you French?",
                "soundmark": "/ɑːr juː frentʃ/",
                "grammar": [
                    {"word": "Are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "French", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我是中国人。",
                "english": "I am Chinese.",
                "soundmark": "/aɪ æm tʃaɪˈniːz/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "Chinese", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他是德国人。",
                "english": "He is German.",
                "soundmark": "/hiː ɪz ˈdʒɜːrmən/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "German", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她来自日本。",
                "english": "She comes from Japan.",
                "soundmark": "/ʃiː kʌmz frʌm dʒəˈpæn/",
                "grammar": [
                    {"word": "She", "role": "S", "label": "主语"},
                    {"word": "comes from", "role": "V", "label": "谓语"},
                    {"word": "Japan", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你会说英语吗？",
                "english": "Can you speak English?",
                "soundmark": "/kæn juː spiːk ˈɪŋɡlɪʃ/",
                "grammar": [
                    {"word": "Can", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "speak", "role": "V", "label": "谓语"},
                    {"word": "English", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 5",
        "statements": [
            {
                "chinese": "你是做什么工作的？",
                "english": "What is your job?",
                "soundmark": "/wʌt ɪz jɔːr dʒɑːb/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "your job", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我是一名工程师。",
                "english": "I am an engineer.",
                "soundmark": "/aɪ æm ən ˌendʒɪˈnɪr/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "an engineer", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "他是护士。",
                "english": "He is a nurse.",
                "soundmark": "/hiː ɪz ə nɜːrs/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a nurse", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她是家庭主妇吗？",
                "english": "Is she a housewife?",
                "soundmark": "/ɪz ʃiː ə ˈhaʊswaɪf/",
                "grammar": [
                    {"word": "Is", "role": "V", "label": "谓语"},
                    {"word": "she", "role": "S", "label": "主语"},
                    {"word": "a housewife", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我在一家银行工作。",
                "english": "I work in a bank.",
                "soundmark": "/aɪ wɜːrk ɪn ə bæŋk/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "work", "role": "V", "label": "谓语"},
                    {"word": "in a bank", "role": "A", "label": "状语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 6",
        "statements": [
            {
                "chinese": "它是什么牌子的？",
                "english": "What make is it?",
                "soundmark": "/wʌt meɪk ɪz ɪt/",
                "grammar": [
                    {"word": "What make", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "它是沃尔沃。",
                "english": "It is a Volvo.",
                "soundmark": "/ɪt ɪz ə ˈvɒlvoʊ/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a Volvo", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "这不是日本车。",
                "english": "It is not a Japanese car.",
                "soundmark": "/ɪt ɪz nɑːt ə ˌdʒæpəˈniːz kɑːr/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is not", "role": "V", "label": "谓语"},
                    {"word": "a Japanese car", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "它是德国车。",
                "english": "It is a German car.",
                "soundmark": "/ɪt ɪz ə ˈdʒɜːrmən kɑːr/",
                "grammar": [
                    {"word": "It", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "a German car", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你的车是什么颜色的？",
                "english": "What color is your car?",
                "soundmark": "/wʌt ˈkʌlər ɪz jɔːr kɑːr/",
                "grammar": [
                    {"word": "What color", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "your car", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 7",
        "statements": [
            {
                "chinese": "你多大岁数了？",
                "english": "How old are you?",
                "soundmark": "/haʊ oʊld ɑːr juː/",
                "grammar": [
                    {"word": "How old", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                ],
            },
            {
                "chinese": "我二十五岁。",
                "english": "I am twenty-five years old.",
                "soundmark": "/aɪ æm ˈtwenti faɪv jɪrz oʊld/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "twenty-five years old", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "她多大了？",
                "english": "How old is she?",
                "soundmark": "/haʊ oʊld ɪz ʃiː/",
                "grammar": [
                    {"word": "How old", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "she", "role": "S", "label": "主语"},
                ],
            },
            {
                "chinese": "他三十岁了。",
                "english": "He is thirty years old.",
                "soundmark": "/hiː ɪz ˈθɜːrti jɪrz oʊld/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "thirty years old", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "我的名字叫索菲。",
                "english": "My name is Sophie.",
                "soundmark": "/maɪ neɪm ɪz ˈsoʊfi/",
                "grammar": [
                    {"word": "My name", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "Sophie", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 8",
        "statements": [
            {
                "chinese": "你今天好吗？",
                "english": "How are you today?",
                "soundmark": "/haʊ ɑːr juː təˈdeɪ/",
                "grammar": [
                    {"word": "How", "role": "S", "label": "主语"},
                    {"word": "are", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "today", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我很好，谢谢。",
                "english": "I am very well, thank you.",
                "soundmark": "/aɪ æm ˈveri wel θæŋk juː/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "am", "role": "V", "label": "谓语"},
                    {"word": "very well", "role": "O", "label": "宾语"},
                    {"word": "thank you", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "他身体好吗？",
                "english": "How is he?",
                "soundmark": "/haʊ ɪz hiː/",
                "grammar": [
                    {"word": "How", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "he", "role": "S", "label": "主语"},
                ],
            },
            {
                "chinese": "看那个男人。",
                "english": "Look at that man.",
                "soundmark": "/lʊk æt ðæt mæn/",
                "grammar": [
                    {"word": "Look", "role": "V", "label": "谓语"},
                    {"word": "at that man", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "他又高又瘦。",
                "english": "He is tall and thin.",
                "soundmark": "/hiː ɪz tɔːl ænd θɪn/",
                "grammar": [
                    {"word": "He", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "tall", "role": "O", "label": "宾语"},
                    {"word": "and", "role": "", "label": ""},
                    {"word": "thin", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 9",
        "statements": [
            {
                "chinese": "请进来吧。",
                "english": "Come in, please.",
                "soundmark": "/kʌm ɪn pliːz/",
                "grammar": [
                    {"word": "Come", "role": "V", "label": "谓语"},
                    {"word": "in", "role": "A", "label": "状语"},
                    {"word": "please", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "请把门关上。",
                "english": "Shut the door, please.",
                "soundmark": "/ʃʌt ðə dɔːr pliːz/",
                "grammar": [
                    {"word": "Shut", "role": "V", "label": "谓语"},
                    {"word": "the door", "role": "O", "label": "宾语"},
                    {"word": "please", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "这卧室太乱了。",
                "english": "This bedroom is very untidy.",
                "soundmark": "/ðɪs ˈbedruːm ɪz ˈveri ʌnˈtaɪdi/",
                "grammar": [
                    {"word": "This bedroom", "role": "S", "label": "主语"},
                    {"word": "is", "role": "V", "label": "谓语"},
                    {"word": "very untidy", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "请把衣服放进衣柜。",
                "english": "Put these clothes in the wardrobe.",
                "soundmark": "/pʊt ðiːz kloʊðz ɪn ðə ˈwɔːrdroʊb/",
                "grammar": [
                    {"word": "Put", "role": "V", "label": "谓语"},
                    {"word": "these clothes", "role": "O", "label": "宾语"},
                    {"word": "in the wardrobe", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "把它弄干净。",
                "english": "Make it clean.",
                "soundmark": "/meɪk ɪt kliːn/",
                "grammar": [
                    {"word": "Make", "role": "V", "label": "谓语"},
                    {"word": "it", "role": "O", "label": "宾语"},
                    {"word": "clean", "role": "O", "label": "宾语"},
                ],
            },
        ],
    },
    {
        "title": "Lesson 10",
        "statements": [
            {
                "chinese": "你通常几点起床？",
                "english": "When do you usually get up?",
                "soundmark": "/wen duː juː ˈjuːʒuəli ɡet ʌp/",
                "grammar": [
                    {"word": "When", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "usually", "role": "A", "label": "状语"},
                    {"word": "get up", "role": "V", "label": "谓语"},
                ],
            },
            {
                "chinese": "我每天七点起床。",
                "english": "I get up at seven every day.",
                "soundmark": "/aɪ ɡet ʌp æt ˈsevən ˈevri deɪ/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "get up", "role": "V", "label": "谓语"},
                    {"word": "at seven", "role": "A", "label": "状语"},
                    {"word": "every day", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "你早饭吃什么？",
                "english": "What do you have for breakfast?",
                "soundmark": "/wʌt duː juː hæv fɔːr ˈbrekfəst/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "for breakfast", "role": "A", "label": "状语"},
                ],
            },
            {
                "chinese": "我吃面包喝咖啡。",
                "english": "I have bread and coffee.",
                "soundmark": "/aɪ hæv bred ænd ˈkɑːfi/",
                "grammar": [
                    {"word": "I", "role": "S", "label": "主语"},
                    {"word": "have", "role": "V", "label": "谓语"},
                    {"word": "bread", "role": "O", "label": "宾语"},
                    {"word": "and", "role": "", "label": ""},
                    {"word": "coffee", "role": "O", "label": "宾语"},
                ],
            },
            {
                "chinese": "你的工作是什么？",
                "english": "What do you do?",
                "soundmark": "/wʌt duː juː duː/",
                "grammar": [
                    {"word": "What", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                    {"word": "you", "role": "S", "label": "主语"},
                    {"word": "do", "role": "V", "label": "谓语"},
                ],
            },
        ],
    },
]
