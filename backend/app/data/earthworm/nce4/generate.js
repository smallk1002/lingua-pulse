#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const outputDir = '/Users/smallk/www/vibecoding/LinguaPulse/backend/app/data/earthworm/nce4';

// Lesson 29: Hovercraft
const lesson29 = {
  title: "Hovercraft",
  theme: "气垫船/交通工具/科技",
  vocabulary: [
    {chinese: "气垫船", english: "hovercraft", soundmark: "/ˈhɒvəkrɑːft/"},
    {chinese: "悬浮", english: "hover", soundmark: "/ˈhɒvər/"},
    {chinese: "气垫", english: "cushion of air", soundmark: "/ˈkʊʃən əv eər/"},
    {chinese: "推进", english: "propel", soundmark: "/prəˈpel/"},
    {chinese: "两栖的", english: "amphibious", soundmark: "/æmˈfɪbiəs/"},
    {chinese: "底盘", english: "chassis", soundmark: "/ˈʃæsi/"},
    {chinese: "灵活的", english: "maneuverable", soundmark: "/məˈnuːvərəbl/"},
    {chinese: "引擎", english: "engine", soundmark: "/ˈendʒɪn/"},
    {chinese: "水面", english: "water surface", soundmark: "/ˈwɔːtər ˈsɜːfɪs/"},
    {chinese: "沼泽", english: "marsh", soundmark: "/mɑːrʃ/"},
    {chinese: "浅滩", english: "shoal", soundmark: "/ʃoʊl/"},
    {chinese: "革命性的", english: "revolutionary", soundmark: "/ˌrevəˈluːʃəneri/"},
    {chinese: "交通工具", english: "vehicle", soundmark: "/ˈviːɪkl/"},
    {chinese: "阻力", english: "friction", soundmark: "/ˈfrɪkʃn/"},
    {chinese: "漂浮", english: "float", soundmark: "/floʊt/"}
  ],
  sentences: [
    {
      chinese: "气垫船是一种能够在水面和陆地上行驶的革命性交通工具。",
      english: "The hovercraft is a revolutionary vehicle that can travel over both water and land.",
      soundmark: "/ðə ˈhɒvəkrɑːft ɪz ə ˌrevəˈluːʃəneri ˈviːɪkl ðæt kən ˈtrævəl ˈoʊvər boʊθ ˈwɔːtər ənd lænd/",
      grammar: [
        {text: "hovercraft", role: "S", phonetic: "/ˈhɒvəkrɑːft/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "revolutionary vehicle", role: "C", phonetic: "/ˌrevəˈluːʃəneri ˈviːɪkl/"},
        {text: "that", role: "S", phonetic: "/ðæt/"},
        {text: "can travel", role: "V", phonetic: "/kən ˈtrævəl/"},
        {text: "over both water and land", role: "Adv", phonetic: "/ˈoʊvər boʊθ ˈwɔːtər ənd lænd/"}
      ]
    },
    {
      chinese: "它通过向下喷射空气形成气垫来实现悬浮。",
      english: "It achieves levitation by directing air downward to form a cushion.",
      soundmark: "/ɪt əˈtʃiːvz ˌlevɪˈteɪʃn baɪ dɪˈrektɪŋ eər ˈdaʊnwərd tə fɔːrm ə ˈkʊʃən/",
      grammar: [
        {text: "It", role: "S", phonetic: "/ɪt/"},
        {text: "achieves", role: "V", phonetic: "/əˈtʃiːvz/"},
        {text: "levitation", role: "O", phonetic: "/ˌlevɪˈteɪʃn/"},
        {text: "by directing air downward", role: "Adv", phonetic: "/baɪ dɪˈrektɪŋ eər ˈdaʊnwərd/"},
        {text: "to form", role: "V", phonetic: "/tə fɔːrm/"},
        {text: "cushion", role: "O", phonetic: "/ˈkʊʃən/"}
      ]
    },
    {
      chinese: "这种交通工具消除了传统船只和车辆面临的摩擦阻力。",
      english: "This mode of transport eliminates the friction encountered by conventional ships and vehicles.",
      soundmark: "/ðɪs moʊd əv ˈtrænspɔːrt ɪˈlɪmɪneɪts ðə ˈfrɪkʃən ɪnˈkaʊntərd baɪ kənˈvenʃənl ʃɪps ənd ˈviːɪklz/",
      grammar: [
        {text: "mode of transport", role: "S", phonetic: "/moʊd əv ˈtrænspɔːrt/"},
        {text: "eliminates", role: "V", phonetic: "/ɪˈlɪmɪneɪts/"},
        {text: "friction", role: "O", phonetic: "/ˈfrɪkʃn/"},
        {text: "encountered", role: "V", phonetic: "/ɪnˈkaʊntərd/"},
        {text: "by conventional ships and vehicles", role: "P", phonetic: "/baɪ kənˈvenʃənl ʃɪps ənd ˈviːɪklz/"}
      ]
    },
    {
      chinese: "气垫船在沼泽和浅滩等难以到达的区域特别有用。",
      english: "Hovercraft are particularly useful in inaccessible areas such as marshes and shoals.",
      soundmark: "/ˈhɒvəkrɑːft ɑːr pɑːrˈtɪkjələrli ˈjuːsfəl ɪn ˌɪnækˈsesəbl ˈeəriəz sʌtʃ æz mɑːrʃɪz ənd ʃoʊlz/",
      grammar: [
        {text: "Hovercraft", role: "S", phonetic: "/ˈhɒvəkrɑːft/"},
        {text: "are", role: "V", phonetic: "/ɑːr/"},
        {text: "particularly useful", role: "C", phonetic: "/pɑːrˈtɪkjələrli ˈjuːsfəl/"},
        {text: "in inaccessible areas", role: "Adv", phonetic: "/ɪn ˌɪnækˈsesəbl ˈeəriəz/"},
        {text: "such as marshes and shoals", role: "P", phonetic: "/sʌtʃ æz mɑːrʃɪz ənd ʃoʊlz/"}
      ]
    },
    {
      chinese: "工程师们已经改进了设计，使现代气垫船更加灵活和节能。",
      english: "Engineers have refined the design to make modern hovercraft more maneuverable and fuel-efficient.",
      soundmark: "/ˌendʒɪˈnɪrz hæv rɪˈfaɪnd ðə dɪˈzaɪn tə meɪk ˈmɒdərn ˈhɒvəkrɑːft mɔːr məˈnuːvərəbl ənd ˈfjuːəl ɪˈfɪʃənt/",
      grammar: [
        {text: "Engineers", role: "S", phonetic: "/ˌendʒɪˈnɪrz/"},
        {text: "have refined", role: "V", phonetic: "/hæv rɪˈfaɪnd/"},
        {text: "design", role: "O", phonetic: "/dɪˈzaɪn/"},
        {text: "to make", role: "V", phonetic: "/tə meɪk/"},
        {text: "modern hovercraft", role: "O", phonetic: "/ˈmɒdərn ˈhɒvəkrɑːft/"},
        {text: "more maneuverable and fuel-efficient", role: "C", phonetic: "/mɔːr məˈnuːvərəbl ənd ˈfjuːəl ɪˈfɪʃənt/"}
      ]
    },
    {
      chinese: "这项发明展示了人类克服自然障碍的创造力。",
      english: "This invention demonstrates humanity's creativity in overcoming natural barriers.",
      soundmark: "/ðɪs ɪnˈvenʃən ˈdemənstreɪts hjuːˈmænɪtiz ˌkriːeɪˈtɪvɪti ɪn ˌoʊvərˈkʌmɪŋ ˈnætʃərəl ˈbæriərz/",
      grammar: [
        {text: "invention", role: "S", phonetic: "/ɪnˈvenʃən/"},
        {text: "demonstrates", role: "V", phonetic: "/ˈdemənstreɪts/"},
        {text: "creativity", role: "O", phonetic: "/ˌkriːeɪˈtɪvɪti/"},
        {text: "in overcoming natural barriers", role: "Adv", phonetic: "/ɪn ˌoʊvərˈkʌmɪŋ ˈnætʃərəl ˈbæriərz/"}
      ]
    },
    {
      chinese: "尽管有其优点，气垫船仍然受到高运营成本和噪音污染的限制。",
      english: "Despite its advantages, the hovercraft remains limited by high operating costs and noise pollution.",
      soundmark: "/dɪˈspaɪt ɪts ædˈvæntɪdʒɪz, ðə ˈhɒvəkrɑːft rɪˈmeɪnz ˈlɪmɪtɪd baɪ haɪ ˈɒpəreɪtɪŋ kɒsts ənd nɔɪz pəˈluːʃn/",
      grammar: [
        {text: "Despite its advantages", role: "Adv", phonetic: "/dɪˈspaɪt ɪts ædˈvæntɪdʒɪz/"},
        {text: "hovercraft", role: "S", phonetic: "/ˈhɒvəkrɑːft/"},
        {text: "remains", role: "V", phonetic: "/rɪˈmeɪnz/"},
        {text: "limited", role: "C", phonetic: "/ˈlɪmɪtɪd/"},
        {text: "by high operating costs and noise pollution", role: "P", phonetic: "/baɪ haɪ ˈɒpəreɪtɪŋ kɒsts ənd nɔɪz pəˈluːʃn/"}
      ]
    },
    {
      chinese: "气垫船的概念继续激励着工程师们探索新的交通解决方案。",
      english: "The concept of the hovercraft continues to inspire engineers to explore new transportation solutions.",
      soundmark: "/ðə ˈkɒnsept əv ðə ˈhɒvəkrɑːft kənˈtɪnjuːz tə ɪnˈspaɪər ˌendʒɪˈnɪrz tə ɪkˈsplɔːr njuː ˌtrænspɔːrˈteɪʃn səˈluːʃənz/",
      grammar: [
        {text: "concept", role: "S", phonetic: "/ˈkɒnsept/"},
        {text: "continues", role: "V", phonetic: "/kənˈtɪnjuːz/"},
        {text: "to inspire", role: "V", phonetic: "/tə ɪnˈspaɪər/"},
        {text: "engineers", role: "O", phonetic: "/ˌendʒɪˈnɪrz/"},
        {text: "to explore new transportation solutions", role: "C", phonetic: "/tə ɪkˈsplɔːr njuː ˌtrænspɔːrˈteɪʃn səˈluːʃənz/"}
      ]
    }
  ],
  review: [
    {chinese: "创新", english: "innovation", soundmark: "/ˌɪnəˈveɪʃn/"},
    {chinese: "运输", english: "transportation", soundmark: "/ˌtrænspɔːrˈteɪʃn/"},
    {chinese: "障碍", english: "barrier", soundmark: "/ˈbæriər/"},
    {chinese: "效率", english: "efficiency", soundmark: "/ɪˈfɪʃənsi/"},
    {chinese: "可持续的", english: "sustainable", soundmark: "/səˈsteɪnəbl/"},
    {chinese: "克服", english: "overcome", soundmark: "/ˌoʊvərˈkʌm/"},
    {chinese: "设计", english: "design", soundmark: "/dɪˈzaɪn/"}
  ]
};

// Lesson 30: The invisible scar
const lesson30 = {
  title: "The invisible scar",
  theme: "无形的伤痕/心理创伤",
  vocabulary: [
    {chinese: "创伤", english: "trauma", soundmark: "/ˈtraʊmə/"},
    {chinese: "心理的", english: "psychological", soundmark: "/ˌsaɪkəˈlɒdʒɪkl/"},
    {chinese: "伤痕", english: "scar", soundmark: "/skɑːr/"},
    {chinese: "隐形的", english: "invisible", soundmark: "/ɪnˈvɪzɪbl/"},
    {chinese: "康复", english: "recovery", soundmark: "/rɪˈkʌvəri/"},
    {chinese: "治愈", english: "heal", soundmark: "/hiːl/"},
    {chinese: "情感", english: "emotion", soundmark: "/ɪˈmoʊʃn/"},
    {chinese: "记忆", english: "memory", soundmark: "/ˈmeməri/"},
    {chinese: "痛苦的", english: "painful", soundmark: "/ˈpeɪnfəl/"},
    {chinese: "恢复", english: "restore", soundmark: "/rɪˈstɔːr/"},
    {chinese: "坚韧", english: "resilience", soundmark: "/rɪˈzɪliəns/"},
    {chinese: "治疗", english: "therapy", soundmark: "/ˈθerəpi/"},
    {chinese: "内心", english: "inner", soundmark: "/ˈɪnər/"},
    {chinese: "伤害", english: "wound", soundmark: "/wuːnd/"},
    {chinese: "持久", english: "enduring", soundmark: "/ɪnˈdjʊərɪŋ/"}
  ],
  sentences: [
    {
      chinese: "心理创伤往往在事件过去很久后仍然影响着人们的情感健康。",
      english: "Psychological trauma often affects people's emotional well-being long after the event has passed.",
      soundmark: "/ˌsaɪkəˈlɒdʒɪkl ˈtraʊmə ˈɒfn əˈfekts ˈpiːplz ɪˈmoʊʃənl ˈwiːl ˈbiːɪŋ lɒŋ ˈæftər ðə ɪˈvent hæz pɑːst/",
      grammar: [
        {text: "trauma", role: "S", phonetic: "/ˈtraʊmə/"},
        {text: "affects", role: "V", phonetic: "/əˈfekts/"},
        {text: "well-being", role: "O", phonetic: "/ˈwiːl ˈbiːɪŋ/"},
        {text: "long after the event has passed", role: "Adv", phonetic: "/lɒŋ ˈæftər ðə ɪˈvent hæz pɑːst/"}
      ]
    },
    {
      chinese: "看不见的伤痕比身体的伤疤更加持久。",
      english: "Invisible scars endure far longer than physical ones.",
      soundmark: "/ɪnˈvɪzɪbl skɑːrz ɪnˈdjʊr fɑːr ˈlɒŋgər ðæn ˈfɪzɪkl wʌnz/",
      grammar: [
        {text: "scars", role: "S", phonetic: "/skɑːrz/"},
        {text: "endure", role: "V", phonetic: "/ɪnˈdjʊr/"},
        {text: "far longer", role: "Adv", phonetic: "/fɑːr ˈlɒŋgər/"},
        {text: "than physical ones", role: "P", phonetic: "/ðæn ˈfɪzɪkl wʌnz/"}
      ]
    },
    {
      chinese: "治疗可以帮助人们治愈内心的痛苦并重建生活。",
      english: "Therapy can help people heal inner wounds and rebuild their lives.",
      soundmark: "/ˈθerəpi kən help ˈpiːpl hiːl ˈɪnər wuːndz ənd ˌriːˈbɪld ðer laɪvz/",
      grammar: [
        {text: "Therapy", role: "S", phonetic: "/ˈθerəpi/"},
        {text: "can help", role: "V", phonetic: "/kən help/"},
        {text: "people", role: "O", phonetic: "/ˈpiːpl/"},
        {text: "heal", role: "V", phonetic: "/hiːl/"},
        {text: "wounds", role: "O", phonetic: "/wuːndz/"},
        {text: "and rebuild", role: "V", phonetic: "/ənd ˌriːˈbɪld/"},
        {text: "lives", role: "O", phonetic: "/laɪvz/"}
      ]
    },
    {
      chinese: "情感上的伤痛需要时间来治愈，但人类的精神具有惊人的韧性。",
      english: "Emotional pain requires time to heal, yet the human spirit possesses remarkable resilience.",
      soundmark: "/ɪˈmoʊʃənl peɪn rɪˈkwaɪərz taɪm tə hiːl, jet ðə ˈhjuːmən ˈspɪrɪt pəˈzesɪz rɪˈmɑːrkəbl rɪˈzɪliəns/",
      grammar: [
        {text: "pain", role: "S", phonetic: "/peɪn/"},
        {text: "requires", role: "V", phonetic: "/rɪˈkwaɪərz/"},
        {text: "time", role: "O", phonetic: "/taɪm/"},
        {text: "to heal", role: "V", phonetic: "/tə hiːl/"},
        {text: "spirit", role: "S", phonetic: "/ˈspɪrɪt/"},
        {text: "possesses", role: "V", phonetic: "/pəˈzesɪz/"},
        {text: "resilience", role: "O", phonetic: "/rɪˈzɪliəns/"}
      ]
    },
    {
      chinese: "那些经历过创伤的人常常发展出更强的同理心和智慧。",
      english: "Those who have experienced trauma often develop greater empathy and wisdom.",
      soundmark: "/ðoʊz huː hæv ɪkˈspɪəriənst ˈtraʊmə ˈɒfn dɪˈveləp ˈgreɪtər ˈempəθi ənd ˈwɪzdəm/",
      grammar: [
        {text: "Those", role: "S", phonetic: "/ðoʊz/"},
        {text: "who", role: "S", phonetic: "/huː/"},
        {text: "have experienced", role: "V", phonetic: "/hæv ɪkˈspɪəriənst/"},
        {text: "trauma", role: "O", phonetic: "/ˈtraʊmə/"},
        {text: "develop", role: "V", phonetic: "/dɪˈveləp/"},
        {text: "empathy and wisdom", role: "O", phonetic: "/ˈempəθi ənd ˈwɪzdəm/"}
      ]
    },
    {
      chinese: "承认伤痛是康复过程的第一步。",
      english: "Acknowledging the wound is the first step in the recovery process.",
      soundmark: "/əkˈnɒlɪdʒɪŋ ðə wuːnd ɪz ðə fɜːrst step ɪn ðə rɪˈkʌvəri ˈprɒses/",
      grammar: [
        {text: "Acknowledging", role: "S", phonetic: "/əkˈnɒlɪdʒɪŋ/"},
        {text: "wound", role: "O", phonetic: "/wuːnd/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "step", role: "C", phonetic: "/step/"},
        {text: "in the recovery process", role: "Adv", phonetic: "/ɪn ðə rɪˈkʌvəri ˈprɒses/"}
      ]
    },
    {
      chinese: "每个人的内心都有一块需要被关怀和理解的角落。",
      english: "Everyone carries within them a corner of the heart that needs care and understanding.",
      soundmark: "/ˈevriwʌn ˈkæriz wɪˈðɪn ðəm ə ˈkɔːrnər əv ðə hɑːrt ðæt niːdz ker ənd ˌʌndərˈstændɪŋ/",
      grammar: [
        {text: "Everyone", role: "S", phonetic: "/ˈevriwʌn/"},
        {text: "carries", role: "V", phonetic: "/ˈkæriz/"},
        {text: "corner", role: "O", phonetic: "/ˈkɔːrnər/"},
        {text: "that", role: "S", phonetic: "/ðæt/"},
        {text: "needs", role: "V", phonetic: "/niːdz/"},
        {text: "care and understanding", role: "O", phonetic: "/ker ənd ˌʌndərˈstændɪŋ/"}
      ]
    },
    {
      chinese: "通过耐心和支持，人们可以学会与过去的伤痛和平共处。",
      english: "Through patience and support, people can learn to coexist peacefully with their past hurts.",
      soundmark: "/θruː ˈpeɪʃəns ənd səˈpɔːrt, ˈpiːpl kən lɜːrn tə ˌkəʊɪɡˈzɪst ˈpiːsfəli wɪð ðer pɑːst hɜːrts/",
      grammar: [
        {text: "Through patience and support", role: "Adv", phonetic: "/θruː ˈpeɪʃəns ənd səˈpɔːrt/"},
        {text: "people", role: "S", phonetic: "/ˈpiːpl/"},
        {text: "can learn", role: "V", phonetic: "/kən lɜːrn/"},
        {text: "to coexist", role: "V", phonetic: "/tə ˌkəʊɪɡˈzɪst/"},
        {text: "peacefully", role: "Adv", phonetic: "/ˈpiːsfəli/"},
        {text: "with their past hurts", role: "P", phonetic: "/wɪð ðer pɑːst hɜːrts/"}
      ]
    }
  ],
  review: [
    {chinese: "同情", english: "compassion", soundmark: "/kəmˈpæʃn/"},
    {chinese: "接受", english: "acceptance", soundmark: "/əkˈseptəns/"},
    {chinese: "成长", english: "growth", soundmark: "/ɡroʊθ/"},
    {chinese: "力量", english: "strength", soundmark: "/streŋθ/"},
    {chinese: "宽恕", english: "forgiveness", soundmark: "/fərˈɡɪvnəs/"},
    {chinese: "平静", english: "peace", soundmark: "/piːs/"},
    {chinese: "希望", english: "hope", soundmark: "/hoʊp/"}
  ]
};

// Lesson 31: The sculptor speaks
const lesson31 = {
  title: "The sculptor speaks",
  theme: "雕塑家谈创作/艺术",
  vocabulary: [
    {chinese: "雕塑家", english: "sculptor", soundmark: "/ˈskʌlptər/"},
    {chinese: "雕塑", english: "sculpture", soundmark: "/ˈskʌlptʃər/"},
    {chinese: "雕刻", english: "carve", soundmark: "/kɑːrv/"},
    {chinese: "石头", english: "stone", soundmark: "/stoʊn/"},
    {chinese: "大理石", english: "marble", soundmark: "/ˈmɑːrbl/"},
    {chinese: "形式", english: "form", soundmark: "/fɔːrm/"},
    {chinese: "创造", english: "create", soundmark: "/kriˈeɪt/"},
    {chinese: "艺术", english: "art", soundmark: "/ɑːrt/"},
    {chinese: "灵感", english: "inspiration", soundmark: "/ˌɪnspɪˈreɪʃn/"},
    {chinese: "愿景", english: "vision", soundmark: "/ˈvɪʒn/"},
    {chinese: "塑造", english: "shape", soundmark: "/ʃeɪp/"},
    {chinese: "凿子", english: "chisel", soundmark: "/ˈtʃɪzl/"},
    {chinese: "锤子", english: "mallet", soundmark: "/ˈmælɪt/"},
    {chinese: "美感", english: "aesthetic", soundmark: "/esˈθetɪk/"},
    {chinese: "杰作", english: "masterpiece", soundmark: "/ˈmɑːstərpiːs/"}
  ],
  sentences: [
    {
      chinese: "雕塑家说他能在每一块石头中看到隐藏的形式。",
      english: "The sculptor says he can see the hidden form within every stone.",
      soundmark: "/ðə ˈskʌlptər sez hi kən siː ðə ˈhɪdn fɔːrm wɪˈðɪn ˈevri stoʊn/",
      grammar: [
        {text: "sculptor", role: "S", phonetic: "/ˈskʌlptər/"},
        {text: "says", role: "V", phonetic: "/sez/"},
        {text: "he", role: "S", phonetic: "/hi/"},
        {text: "can see", role: "V", phonetic: "/kən siː/"},
        {text: "form", role: "O", phonetic: "/fɔːrm/"},
        {text: "within every stone", role: "P", phonetic: "/wɪˈðɪn ˈevri stoʊn/"}
      ]
    },
    {
      chinese: "他的作品不仅仅是切割大理石，而是赋予材料生命。",
      english: "His work is not merely cutting marble, but giving life to the material.",
      soundmark: "/hɪz wɜːrk ɪz nɒt ˈmɪəli ˈkʌtɪŋ ˈmɑːrbl, bʌt ˈɡɪvɪŋ laɪf tə ðə məˈtɪəriəl/",
      grammar: [
        {text: "work", role: "S", phonetic: "/wɜːrk/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "cutting", role: "C", phonetic: "/ˈkʌtɪŋ/"},
        {text: "marble", role: "O", phonetic: "/ˈmɑːrbl/"},
        {text: "but", role: "Int", phonetic: "/bʌt/"},
        {text: "giving", role: "C", phonetic: "/ˈɡɪvɪŋ/"},
        {text: "life", role: "O", phonetic: "/laɪf/"},
        {text: "to the material", role: "P", phonetic: "/tə ðə məˈtɪəriəl/"}
      ]
    },
    {
      chinese: "每一次凿击都揭示出已经存在于石头中的东西。",
      english: "Each strike of the chisel reveals what already exists within the stone.",
      soundmark: "/iːtʃ straɪk əv ðə ˈtʃɪzl rɪˈviːlz wɒt ɔːlˈredi ɪɡˈzɪsts wɪˈðɪn ðə stoʊn/",
      grammar: [
        {text: "strike", role: "S", phonetic: "/straɪk/"},
        {text: "reveals", role: "V", phonetic: "/rɪˈviːlz/"},
        {text: "what", role: "O", phonetic: "/wɒt/"},
        {text: "exists", role: "V", phonetic: "/ɪɡˈzɪsts/"},
        {text: "within the stone", role: "P", phonetic: "/wɪˈðɪn ðə stoʊn/"}
      ]
    },
    {
      chinese: "艺术创作需要耐心、技巧和对材料的深刻理解。",
      english: "Artistic creation demands patience, skill, and a profound understanding of the material.",
      soundmark: "/ɑːrˈtɪstɪk ˌkriˈeɪʃn dɪˈmɑːndz ˈpeɪʃəns, skɪl, ənd ə prəˈfaʊnd ˌʌndərˈstændɪŋ əv ðə məˈtɪəriəl/",
      grammar: [
        {text: "creation", role: "S", phonetic: "/ˌkriˈeɪʃn/"},
        {text: "demands", role: "V", phonetic: "/dɪˈmɑːndz/"},
        {text: "patience, skill, and understanding", role: "O", phonetic: "/ˈpeɪʃəns, skɪl, ənd ˌʌndərˈstændɪŋ/"},
        {text: "of the material", role: "P", phonetic: "/əv ðə məˈtɪəriəl/"}
      ]
    },
    {
      chinese: "他说真正的美感在于发现材料的内在本质。",
      english: "He says true aesthetic lies in discovering the inner essence of the material.",
      soundmark: "/hi sez truː esˈθetɪk laɪz ɪn dɪˈskʌvərɪŋ ðə ˈɪnər ˈesns əv ðə məˈtɪəriəl/",
      grammar: [
        {text: "He", role: "S", phonetic: "/hi/"},
        {text: "says", role: "V", phonetic: "/sez/"},
        {text: "aesthetic", role: "S", phonetic: "/esˈθetɪk/"},
        {text: "lies", role: "V", phonetic: "/laɪz/"},
        {text: "in discovering", role: "P", phonetic: "/ɪn dɪˈskʌvərɪŋ/"},
        {text: "essence", role: "O", phonetic: "/ˈesns/"},
        {text: "of the material", role: "P", phonetic: "/əv ðə məˈtɪəriəl/"}
      ]
    },
    {
      chinese: "伟大的雕塑能够超越时代和文化，触动所有人的心灵。",
      english: "Great sculpture transcends time and culture, touching hearts across all generations.",
      soundmark: "/ɡreɪt ˈskʌlptʃər trænˈsendz taɪm ənd ˈkʌltʃər, ˈtʌtʃɪŋ hɑːrts əˈkrɒs ɔːl ˌdʒenəˈreɪʃənz/",
      grammar: [
        {text: "sculpture", role: "S", phonetic: "/ˈskʌlptʃər/"},
        {text: "transcends", role: "V", phonetic: "/trænˈsendz/"},
        {text: "time and culture", role: "O", phonetic: "/taɪm ənd ˈkʌltʃər/"},
        {text: "touching", role: "V", phonetic: "/ˈtʌtʃɪŋ/"},
        {text: "hearts", role: "O", phonetic: "/hɑːrts/"},
        {text: "across all generations", role: "P", phonetic: "/əˈkrɒs ɔːl ˌdʒenəˈreɪʃənz/"}
      ]
    },
    {
      chinese: "工具很重要，但真正塑造作品的是艺术家的愿景。",
      english: "Tools matter, but what truly shapes the work is the artist's vision.",
      soundmark: "/tuːlz ˈmætər, bʌt wɒt ˈtruːli ʃeɪps ðə wɜːrk ɪz ðə ˈɑːrtɪsts ˈvɪʒn/",
      grammar: [
        {text: "Tools", role: "S", phonetic: "/tuːlz/"},
        {text: "matter", role: "V", phonetic: "/ˈmætər/"},
        {text: "what", role: "S", phonetic: "/wɒt/"},
        {text: "shapes", role: "V", phonetic: "/ʃeɪps/"},
        {text: "work", role: "O", phonetic: "/wɜːrk/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "vision", role: "C", phonetic: "/ˈvɪʒn/"}
      ]
    }
  ],
  review: [
    {chinese: "工艺", english: "craftsmanship", soundmark: "/ˈkrɑːftsmənʃɪp/"},
    {chinese: "表达", english: "expression", soundmark: "/ɪkˈspreʃn/"},
    {chinese: "美", english: "beauty", soundmark: "/ˈbjuːti/"},
    {chinese: "想象力", english: "imagination", soundmark: "/ɪˌmædʒɪˈneɪʃn/"},
    {chinese: "传统", english: "tradition", soundmark: "/trəˈdɪʃn/"},
    {chinese: "技巧", english: "technique", soundmark: "/tekˈniːk/"},
    {chinese: "永恒", english: "eternal", soundmark: "/ɪˈtɜːrnəl/"}
  ]
};

// Lesson 32: Galileo's telescope
const lesson32 = {
  title: "Galileo's telescope",
  theme: "伽利略望远镜/科学史",
  vocabulary: [
    {chinese: "望远镜", english: "telescope", soundmark: "/ˈtelɪskoʊp/"},
    {chinese: "天文学", english: "astronomy", soundmark: "/əˈstrɒnəmi/"},
    {chinese: "观察", english: "observe", soundmark: "/əbˈzɜːrv/"},
    {chinese: "宇宙", english: "universe", soundmark: "/ˈjuːnɪvɜːrs/"},
    {chinese: "行星", english: "planet", soundmark: "/ˈplænɪt/"},
    {chinese: "月球", english: "moon", soundmark: "/muːn/"},
    {chinese: "革命", english: "revolution", soundmark: "/ˌrevəˈluːʃn/"},
    {chinese: "科学的", english: "scientific", soundmark: "/ˌsaɪənˈtɪfɪk/"},
    {chinese: "发现", english: "discovery", soundmark: "/dɪˈskʌvəri/"},
    {chinese: "木星", english: "Jupiter", soundmark: "/ˈdʒuːpɪtər/"},
    {chinese: "轨道", english: "orbit", soundmark: "/ˈɔːrbɪt/"},
    {chinese: "挑战", english: "challenge", soundmark: "/ˈtʃælɪndʒ/"},
    {chinese: "理论", english: "theory", soundmark: "/ˈθɪəri/"},
    {chinese: "证明", english: "demonstrate", soundmark: "/ˈdemənstreɪt/"},
    {chinese: "仪器", english: "instrument", soundmark: "/ˈɪnstrəmənt/"}
  ],
  sentences: [
    {
      chinese: "伽利略在1609年改进了望远镜，永远改变了人类对宇宙的理解。",
      english: "Galileo improved the telescope in 1609, forever changing humanity's understanding of the universe.",
      soundmark: "/ɡæliˈleɪo ɪmˈpruːvd ðə ˈtelɪskoʊp ɪn ˈskoʊp, fərˈevər ˈtʃeɪndʒɪŋ hjuːˈmænɪtiz ˌʌndərˈstændɪŋ əv ðə ˈjuːnɪvɜːrs/",
      grammar: [
        {text: "Galileo", role: "S", phonetic: "/ɡæliˈleɪo/"},
        {text: "improved", role: "V", phonetic: "/ɪmˈpruːvd/"},
        {text: "telescope", role: "O", phonetic: "/ˈtelɪskoʊp/"},
        {text: "in 1609", role: "Adv", phonetic: "/ɪn ˈskoʊp/"},
        {text: "changing", role: "V", phonetic: "/ˈtʃeɪndʒɪŋ/"},
        {text: "understanding", role: "O", phonetic: "/ˌʌndərˈstændɪŋ/"},
        {text: "of the universe", role: "P", phonetic: "/əv ðə ˈjuːnɪvɜːrs/"}
      ]
    },
    {
      chinese: "通过他的仪器，他发现了围绕木星运行的四颗卫星。",
      english: "Through his instrument, he discovered four moons orbiting Jupiter.",
      soundmark: "/θruː hɪz ˈɪnstrəmənt, hi dɪˈskʌvərd fɔːr muːnz ˈɔːrbɪtɪŋ ˈdʒuːpɪtər/",
      grammar: [
        {text: "Through his instrument", role: "Adv", phonetic: "/θruː hɪz ˈɪnstrəmənt/"},
        {text: "he", role: "S", phonetic: "/hi/"},
        {text: "discovered", role: "V", phonetic: "/dɪˈskʌvərd/"},
        {text: "moons", role: "O", phonetic: "/muːnz/"},
        {text: "orbiting Jupiter", role: "V", phonetic: "/ˈɔːrbɪtɪŋ ˈdʒuːpɪtər/"}
      ]
    },
    {
      chinese: "这一发现挑战了当时被广泛接受的地心说。",
      english: "This discovery challenged the widely accepted geocentric theory of the time.",
      soundmark: "/ðɪs dɪˈskʌvəri ˈtʃælɪndʒd ðə ˈwaɪdli əkˈseptɪd ˌdʒiːoʊˈsentrɪk ˈθɪəri əv ðə taɪm/",
      grammar: [
        {text: "discovery", role: "S", phonetic: "/dɪˈskʌvəri/"},
        {text: "challenged", role: "V", phonetic: "/ˈtʃælɪndʒd/"},
        {text: "theory", role: "O", phonetic: "/ˈθɪəri/"},
        {text: "of the time", role: "P", phonetic: "/əv ðə taɪm/"}
      ]
    },
    {
      chinese: "他的观察证明了并非所有天体都围绕地球运转。",
      english: "His observations demonstrated that not all celestial bodies revolve around the Earth.",
      soundmark: "/hɪz ˌɒbzərˈveɪʃənz ˈdemənstreɪtɪd ðæt nɒt ɔːl sɪˈlestiəl ˈbɒdiz rɪˈvɒlv əˈraʊnd ðə ɜːrθ/",
      grammar: [
        {text: "observations", role: "S", phonetic: "/ˌɒbzərˈveɪʃənz/"},
        {text: "demonstrated", role: "V", phonetic: "/ˈdemənstreɪtɪd/"},
        {text: "that", role: "Int", phonetic: "/ðæt/"},
        {text: "bodies", role: "S", phonetic: "/ˈbɒdiz/"},
        {text: "revolve", role: "V", phonetic: "/rɪˈvɒlv/"},
        {text: "around the Earth", role: "P", phonetic: "/əˈraʊnd ðə ɜːrθ/"}
      ]
    },
    {
      chinese: "尽管遭到教会的反对，伽利略仍然坚持他的科学发现。",
      english: "Despite opposition from the Church, Galileo persisted in his scientific findings.",
      soundmark: "/dɪˈspaɪt ˌɒpəˈzɪʃn frɒm ðə tʃɜːrtʃ, ɡæliˈleɪo pərˈsɪstɪd ɪn hɪz ˌsaɪənˈtɪfɪk ˈfaɪndɪŋz/",
      grammar: [
        {text: "Despite opposition", role: "Adv", phonetic: "/dɪˈspaɪt ˌɒpəˈzɪʃn/"},
        {text: "Galileo", role: "S", phonetic: "/ɡæliˈleɪo/"},
        {text: "persisted", role: "V", phonetic: "/pərˈsɪstɪd/"},
        {text: "in his findings", role: "P", phonetic: "/ɪn hɪz ˈfaɪndɪŋz/"}
      ]
    },
    {
      chinese: "望远镜揭示了月球表面的山脉和陨石坑。",
      english: "The telescope revealed mountains and craters on the lunar surface.",
      soundmark: "/ðə ˈtelɪskoʊp rɪˈviːld ˈmaʊntnz ənd ˈkrætərz ɒn ðə ˈluːnər ˈsɜːrfɪs/",
      grammar: [
        {text: "telescope", role: "S", phonetic: "/ˈtelɪskoʊp/"},
        {text: "revealed", role: "V", phonetic: "/rɪˈviːld/"},
        {text: "mountains and craters", role: "O", phonetic: "/ˈmaʊntnz ənd ˈkrætərz/"},
        {text: "on the lunar surface", role: "P", phonetic: "/ɒn ðə ˈluːnər ˈsɜːrfɪs/"}
      ]
    },
    {
      chinese: "伽利略的工作为现代天文学奠定了基础，改变了科学的进程。",
      english: "Galileo's work laid the foundation for modern astronomy, transforming the course of science.",
      soundmark: "/ɡæliˈleɪoʊz wɜːrk leɪd ðə faʊnˈdeɪʃn fɔːr ˈmɒdən əˈstrɒnəmi, trænsˈfɔːrmɪŋ ðə kɔːrs əv ˈsaɪəns/",
      grammar: [
        {text: "work", role: "S", phonetic: "/wɜːrk/"},
        {text: "laid", role: "V", phonetic: "/leɪd/"},
        {text: "foundation", role: "O", phonetic: "/faʊnˈdeɪʃn/"},
        {text: "for modern astronomy", role: "P", phonetic: "/fɔːr ˈmɒdən əˈstrɒnəmi/"},
        {text: "transforming", role: "V", phonetic: "/trænsˈfɔːrmɪŋ/"},
        {text: "course", role: "O", phonetic: "/kɔːrs/"},
        {text: "of science", role: "P", phonetic: "/əv ˈsaɪəns/"}
      ]
    }
  ],
  review: [
    {chinese: "观察", english: "observation", soundmark: "/ˌɒbzərˈveɪʃn/"},
    {chinese: "证据", english: "evidence", soundmark: "/ˈevɪdəns/"},
    {chinese: "假设", english: "hypothesis", soundmark: "/haɪˈpɒθəsɪs/"},
    {chinese: "进步", english: "progress", soundmark: "/ˈprəʊɡres/"},
    {chinese: "创新", english: "invent", soundmark: "/ɪnˈvent/"},
    {chinese: "知识", english: "knowledge", soundmark: "/ˈnɒlɪdʒ/"},
    {chinese: "突破", english: "breakthrough", soundmark: "/ˈbreɪkθruː/"}
  ]
};

// Lesson 33: Education
const lesson33 = {
  title: "Education",
  theme: "教育/教育理念",
  vocabulary: [
    {chinese: "教育", english: "education", soundmark: "/ˌedʒuˈkeɪʃn/"},
    {chinese: "学习", english: "learning", soundmark: "/ˈlɜːrnɪŋ/"},
    {chinese: "知识", english: "knowledge", soundmark: "/ˈnɒlɪdʒ/"},
    {chinese: "技能", english: "skill", soundmark: "/skɪl/"},
    {chinese: "发展", english: "development", soundmark: "/dɪˈveləpmənt/"},
    {chinese: "批判性的", english: "critical", soundmark: "/ˈkrɪtɪkl/"},
    {chinese: "思考", english: "thinking", soundmark: "/ˈθɪŋkɪŋ/"},
    {chinese: "创造力", english: "creativity", soundmark: "/ˌkriːeɪˈtɪvɪti/"},
    {chinese: "潜能", english: "potential", soundmark: "/pəˈtenʃl/"},
    {chinese: "培养", english: "cultivate", soundmark: "/ˈkʌltɪveɪt/"},
    {chinese: "好奇心", english: "curiosity", soundmark: "/ˌkjʊəriˈɒsɪti/"},
    {chinese: "启发", english: "inspire", soundmark: "/ɪnˈspaɪər/"},
    {chinese: "终身", english: "lifelong", soundmark: "/ˈlaɪflɒŋ/"},
    {chinese: "探索", english: "explore", soundmark: "/ɪkˈsplɔːr/"},
    {chinese: "智慧", english: "wisdom", soundmark: "/ˈwɪzdəm/"}
  ],
  sentences: [
    {
      chinese: "教育的真正目的不是灌输知识，而是培养独立思考的能力。",
      english: "The true purpose of education is not to fill minds with knowledge, but to cultivate the ability to think independently.",
      soundmark: "/ðə truː ˈpɜːrpəs əv ˌedʒuˈkeɪʃn ɪz nɒt tə fɪl maɪndz wɪð ˈnɒlɪdʒ, bʌt tə ˈkʌltɪveɪt ðə əˈbɪlɪti tə θɪŋk ˌɪndɪˈpendəntli/",
      grammar: [
        {text: "purpose", role: "S", phonetic: "/ˈpɜːrpəs/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "to fill", role: "C", phonetic: "/tə fɪl/"},
        {text: "minds", role: "O", phonetic: "/maɪndz/"},
        {text: "with knowledge", role: "P", phonetic: "/wɪð ˈnɒlɪdʒ/"},
        {text: "but", role: "Int", phonetic: "/bʌt/"},
        {text: "to cultivate", role: "C", phonetic: "/tə ˈkʌltɪveɪt/"},
        {text: "ability", role: "O", phonetic: "/əˈbɪlɪti/"},
        {text: "to think independently", role: "V", phonetic: "/tə θɪŋk ˌɪndɪˈpendəntli/"}
      ]
    },
    {
      chinese: "好的教育应该激发学生的好奇心，而不是扑灭它。",
      english: "Good education should inspire curiosity in students, not extinguish it.",
      soundmark: "/ɡʊd ˌedʒuˈkeɪʃn ʃʊd ɪnˈspaɪər ˌkjʊəriˈɒsɪti ɪn ˈstjuːdənts, nɒt ɪkˈstɪŋɡwɪʃ ɪt/",
      grammar: [
        {text: "education", role: "S", phonetic: "/ˌedʒuˈkeɪʃn/"},
        {text: "should inspire", role: "V", phonetic: "/ʃʊd ɪnˈspaɪər/"},
        {text: "curiosity", role: "O", phonetic: "/ˌkjʊəriˈɒsɪti/"},
        {text: "in students", role: "P", phonetic: "/ɪn ˈstjuːdənts/"},
        {text: "not", role: "Neg", phonetic: "/nɒt/"},
        {text: "extinguish", role: "V", phonetic: "/ɪkˈstɪŋɡwɪʃ/"},
        {text: "it", role: "O", phonetic: "/ɪt/"}
      ]
    },
    {
      chinese: "学习不仅仅是为了考试，而是为了终身的成长和发展。",
      english: "Learning is not merely for examinations, but for lifelong growth and development.",
      soundmark: "/ˈlɜːrnɪŋ ɪz nɒt ˈmɪəli fɔːr ɪɡˈzæmɪˌneɪʃənz, bʌt fɔːr ˈlaɪflɒŋ ɡroʊθ ənd dɪˈveləpmənt/",
      grammar: [
        {text: "Learning", role: "S", phonetic: "/ˈlɜːrnɪŋ/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "for examinations", role: "P", phonetic: "/fɔːr ɪɡˈzæmɪˌneɪʃənz/"},
        {text: "but", role: "Int", phonetic: "/bʌt/"},
        {text: "for growth and development", role: "P", phonetic: "/fɔːr ˈɡroʊθ ənd dɪˈveləpmənt/"}
      ]
    },
    {
      chinese: "每位学生都有独特的潜能，等待着被教育者发现和培养。",
      english: "Every student possesses unique potential, waiting to be discovered and nurtured by educators.",
      soundmark: "/ˈevri ˈstjuːdənt pəˈzesɪz juˈniːk pəˈtenʃl, ˈweɪtɪŋ tə bi dɪˈskʌvərd ənd ˈnɜːrtʃəd baɪ ˈedʒukeɪtərz/",
      grammar: [
        {text: "student", role: "S", phonetic: "/ˈstjuːdənt/"},
        {text: "possesses", role: "V", phonetic: "/pəˈzesɪz/"},
        {text: "potential", role: "O", phonetic: "/pəˈtenʃl/"},
        {text: "waiting", role: "V", phonetic: "/ˈweɪtɪŋ/"},
        {text: "to be discovered", role: "V", phonetic: "/tə bi dɪˈskʌvərd/"},
        {text: "and nurtured", role: "V", phonetic: "/ənd ˈnɜːrtʃəd/"},
        {text: "by educators", role: "P", phonetic: "/baɪ ˈedʒukeɪtərz/"}
      ]
    },
    {
      chinese: "批判性思维能力比单纯记忆事实更为重要。",
      english: "The ability to think critically is more important than simply memorizing facts.",
      soundmark: "/ðə əˈbɪlɪti tə θɪŋk ˈkrɪtɪkli ɪz mɔːr ɪmˈpɔːrtənt ðæn ˈsɪmpli ˈmeməraɪzɪŋ fækts/",
      grammar: [
        {text: "ability", role: "S", phonetic: "/əˈbɪlɪti/"},
        {text: "to think critically", role: "V", phonetic: "/tə θɪŋk ˈkrɪtɪkli/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "more important", role: "C", phonetic: "/mɔːr ɪmˈpɔːrtənt/"},
        {text: "than", role: "Int", phonetic: "/ðæn/"},
        {text: "memorizing", role: "V", phonetic: "/ˈmeməraɪzɪŋ/"},
        {text: "facts", role: "O", phonetic: "/fækts/"}
      ]
    },
    {
      chinese: "一个理想的教育系统应该培养创造力和解决问题的能力。",
      english: "An ideal education system should foster creativity and problem-solving abilities.",
      soundmark: "/ən aɪˈdiːl ˌedʒuˈkeɪʃn ˈsɪstəm ʃʊd ˈfɒstər ˌkriːeɪˈtɪvɪti ənd ˈprɒbləm ˈsɒlvɪŋ əˈbɪlɪtiz/",
      grammar: [
        {text: "system", role: "S", phonetic: "/ˈsɪstəm/"},
        {text: "should foster", role: "V", phonetic: "/ʃʊd ˈfɒstər/"},
        {text: "creativity and abilities", role: "O", phonetic: "/ˌkriːeɪˈtɪvɪti ənd əˈbɪlɪtiz/"},
        {text: "problem-solving", role: "Det", phonetic: "/ˈprɒbləm ˈsɒlvɪŋ/"}
      ]
    },
    {
      chinese: "教育的最终目标是帮助学生成为有思想、有责任感的公民。",
      english: "The ultimate goal of education is to help students become thoughtful, responsible citizens.",
      soundmark: "/ðə ˈʌltɪmət ɡoʊl əv ˌedʒuˈkeɪʃn ɪz tə help ˈstjuːdənts bɪˈkʌm ˈθɔːtfəl, rɪˈspɒnsɪbl ˈsɪtɪzənz/",
      grammar: [
        {text: "goal", role: "S", phonetic: "/ɡoʊl/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "to help", role: "C", phonetic: "/tə help/"},
        {text: "students", role: "O", phonetic: "/ˈstjuːdənts/"},
        {text: "become", role: "V", phonetic: "/bɪˈkʌm/"},
        {text: "citizens", role: "C", phonetic: "/ˈsɪtɪzənz/"}
      ]
    }
  ],
  review: [
    {chinese: "导师", english: "mentor", soundmark: "/ˈmentɔːr/"},
    {chinese: "学科", english: "subject", soundmark: "/ˈsʌbdʒɪkt/"},
    {chinese: "课程", english: "curriculum", soundmark: "/kəˈrɪkjələm/"},
    {chinese: "理解", english: "comprehend", soundmark: "/ˌkɒmprɪˈhend/"},
    {chinese: "分析", english: "analyze", soundmark: "/ˈænəlaɪz/"},
    {chinese: "应用", english: "apply", soundmark: "/əˈplaɪ/"},
    {chinese: "成就", english: "achievement", soundmark: "/əˈtʃiːvmənt/"}
  ]
};

// Lesson 34: Ways of measuring time
const lesson34 = {
  title: "Ways of measuring time",
  theme: "计时方法/历史",
  vocabulary: [
    {chinese: "测量", english: "measure", soundmark: "/ˈmeʒər/"},
    {chinese: "时间", english: "time", soundmark: "/taɪm/"},
    {chinese: "日晷", english: "sundial", soundmark: "/ˈsʌndaɪəl/"},
    {chinese: "沙漏", english: "hourglass", soundmark: "/ˈaʊərɡlɑːs/"},
    {chinese: "时钟", english: "clock", soundmark: "/klɒk/"},
    {chinese: "日历", english: "calendar", soundmark: "/ˈkælɪndər/"},
    {chinese: "精确", english: "precise", soundmark: "/prɪˈsaɪs/"},
    {chinese: "发明", english: "invent", soundmark: "/ɪnˈvent/"},
    {chinese: "世纪", english: "century", soundmark: "/ˈsentʃəri/"},
    {chinese: "机械的", english: "mechanical", soundmark: "/mɪˈkænɪkl/"},
    {chinese: "原子钟", english: "atomic clock", soundmark: "/əˈtɒmɪk klɒk/"},
    {chinese: "准确", english: "accurate", soundmark: "/ˈækjərət/"},
    {chinese: "间隔", english: "interval", soundmark: "/ˈɪntərvl/"},
    {chinese: "日影", english: "shadow", soundmark: "/ˈʃædoʊ/"},
    {chinese: "进化", english: "evolution", soundmark: "/ˌiːvəˈluːʃn/"}
  ],
  sentences: [
    {
      chinese: "古代文明使用日晷通过太阳的位置来测量时间。",
      english: "Ancient civilizations used sundials to measure time by the position of the sun.",
      soundmark: "/ˈeɪnʃənt ˌsɪvɪlaɪˈzeɪʃənz juːzd ˈsʌndaɪəlz tə ˈmeʒər taɪm baɪ ðə pəˈzɪʃn əv ðə sʌn/",
      grammar: [
        {text: "civilizations", role: "S", phonetic: "/ˌsɪvɪlaɪˈzeɪʃənz/"},
        {text: "used", role: "V", phonetic: "/juːzd/"},
        {text: "sundials", role: "O", phonetic: "/ˈsʌndaɪəlz/"},
        {text: "to measure", role: "V", phonetic: "/tə ˈmeʒər/"},
        {text: "time", role: "O", phonetic: "/taɪm/"},
        {text: "by the position", role: "P", phonetic: "/baɪ ðə pəˈzɪʃn/"},
        {text: "of the sun", role: "P", phonetic: "/əv ðə sʌn/"}
      ]
    },
    {
      chinese: "沙漏通过沙子从一个容器流到另一个容器来计时。",
      english: "An hourglass measures time as sand flows from one container to another.",
      soundmark: "/ən ˈaʊərɡlɑːs ˈmeʒərz taɪm æz sænd floʊz frɒm wʌn kənˈteɪnər tə əˈnʌðər/",
      grammar: [
        {text: "hourglass", role: "S", phonetic: "/ˈaʊərɡlɑːs/"},
        {text: "measures", role: "V", phonetic: "/ˈmeʒərz/"},
        {text: "time", role: "O", phonetic: "/taɪm/"},
        {text: "as sand flows", role: "Adv", phonetic: "/æz sænd floʊz/"},
        {text: "from one container to another", role: "P", phonetic: "/frɒm wʌn kənˈteɪnər tə əˈnʌðər/"}
      ]
    },
    {
      chinese: "机械钟的发明在计时历史上是一个重大突破。",
      english: "The invention of the mechanical clock was a significant breakthrough in the history of timekeeping.",
      soundmark: "/ðə ɪnˈvenʃn əv ðə mɪˈkænɪkl klɒk wəz ə sɪɡˈnɪfɪkənt ˈbreɪkθruː ɪn ðə ˈhɪstri əv ˈtaɪmˌkiːpɪŋ/",
      grammar: [
        {text: "invention", role: "S", phonetic: "/ɪnˈvenʃn/"},
        {text: "was", role: "V", phonetic: "/wəz/"},
        {text: "breakthrough", role: "C", phonetic: "/ˈbreɪkθruː/"},
        {text: "in the history", role: "P", phonetic: "/ɪn ðə ˈhɪstri/"},
        {text: "of timekeeping", role: "P", phonetic: "/əv ˈtaɪmˌkiːpɪŋ/"}
      ]
    },
    {
      chinese: "现代原子钟极其精确，每百万年才会误差一秒。",
      english: "Modern atomic clocks are so precise that they lose only one second every million years.",
      soundmark: "/ˈmɒdən əˈtɒmɪk klɒks ɑːr soʊ prɪˈsaɪs ðæt ðeɪ luːz ˈoʊnli wʌn ˈseknd ˈevri ˈmɪljən jɪərz/",
      grammar: [
        {text: "clocks", role: "S", phonetic: "/klɒks/"},
        {text: "are", role: "V", phonetic: "/ɑːr/"},
        {text: "precise", role: "C", phonetic: "/prɪˈsaɪs/"},
        {text: "so...that", role: "Int", phonetic: "/soʊ...ðæt/"},
        {text: "they", role: "S", phonetic: "/ðeɪ/"},
        {text: "lose", role: "V", phonetic: "/luːz/"},
        {text: "one second", role: "O", phonetic: "/wʌn ˈseknd/"},
        {text: "every million years", role: "Adv", phonetic: "/ˈevri ˈmɪljən jɪərz/"}
      ]
    },
    {
      chinese: "几个世纪以来，计时方法已经从简单的日影观察发展到复杂的电子设备。",
      english: "Over the centuries, methods of measuring time have evolved from simple shadow observation to complex electronic devices.",
      soundmark: "/ˈoʊvər ðə ˈsentʃəriz, ˈmeθədz əv ˈmeʒərɪŋ taɪm hæv ɪˈvɒlvd frɒm ˈsɪmpl ˈʃædoʊ ˌɒbzərˈveɪʃn tə kəmˈpleks ɪlekˈtrɒnɪk dɪˈvaɪsɪz/",
      grammar: [
        {text: "Over the centuries", role: "Adv", phonetic: "/ˈoʊvər ðə ˈsentʃəriz/"},
        {text: "methods", role: "S", phonetic: "/ˈmeθədz/"},
        {text: "of measuring time", role: "P", phonetic: "/əv ˈmeʒərɪŋ taɪm/"},
        {text: "have evolved", role: "V", phonetic: "/hæv ɪˈvɒlvd/"},
        {text: "from simple observation", role: "P", phonetic: "/frɒm ˈsɪmpl ˌɒbzərˈveɪʃn/"},
        {text: "to complex devices", role: "P", phonetic: "/tə kəmˈpleks dɪˈvaɪsɪz/"}
      ]
    },
    {
      chinese: "精确计时的能力对于现代科学和导航至关重要。",
      english: "The ability to measure time precisely is essential for modern science and navigation.",
      soundmark: "/ðə əˈbɪlɪti tə ˈmeʒər taɪm prɪˈsaɪsli ɪz ɪˈsenʃl fɔːr ˈmɒdən ˈsaɪəns ənd ˌnævɪˈɡeɪʃn/",
      grammar: [
        {text: "ability", role: "S", phonetic: "/əˈbɪlɪti/"},
        {text: "to measure time precisely", role: "V", phonetic: "/tə ˈmeʒər taɪm prɪˈsaɪsli/"},
        {text: "is", role: "V", phonetic: "/ɪz/"},
        {text: "essential", role: "C", phonetic: "/ɪˈsenʃl/"},
        {text: "for science and navigation", role: "P", phonetic: "/fɔːr ˈsaɪəns ənd ˌnævɪˈɡeɪʃn/"}
      ]
    },
    {
      chinese: "从日晷到原子钟，人类始终追求更准确的时间测量方法。",
      english: "From sundials to atomic clocks, humans have always pursued more accurate ways to measure time.",
      soundmark: "/frɒm ˈsʌndaɪəlz tə əˈtɒmɪk klɒks, ˈhjuːmənz hɔːlˈweɪz pərˈsjuːd mɔːr ˈækjərət weɪz tə ˈmeʒər taɪm/",
      grammar: [
        {text: "From sundials to atomic clocks", role: "Adv", phonetic: "/frɒm ˈsʌndaɪəlz tə əˈtɒmɪk klɒks/"},
        {text: "humans", role: "S", phonetic: "/ˈhjuːmənz/"},
        {text: "have pursued", role: "V", phonetic: "/hæv pərˈsjuːd/"},
        {text: "ways", role: "O", phonetic: "/weɪz/"},
        {text: "to measure time", role: "V", phonetic: "/tə ˈmeʒər taɪm/"}
      ]
    }
  ],
  review: [
    {chinese: "同步", english: "synchronize", soundmark: "/ˈsɪŋkrənaɪz/"},
    {chinese: "频率", english: "frequency", soundmark: "/ˈfriːkwənsi/"},
    {chinese: "振荡", english: "oscillate", soundmark: "/ˈɒsɪleɪt/"},
    {chinese: "创新", english: "innovation", soundmark: "/ˌɪnəˈveɪʃn/"},
    {chinese: "进步", english: "advancement", soundmark: "/ədˈvɑːnsmənt/"},
    {chinese: "可靠", english: "reliable", soundmark: "/rɪˈlaɪəbl/"},
    {chinese: "标准", english: "standard", soundmark: "/ˈstændərd/"}
  ]
};

// Lesson 35: Space odyssey
const lesson35 = {
  title: "Space odyssey",
  theme: "太空探索/宇宙",
  vocabulary: [
    {chinese: "太空", english: "space", soundmark: "/speɪs/"},
    {chinese: "宇宙", english: "universe", soundmark: "/ˈjuːnɪvɜːrs/"},
    {chinese: "探索", english: "exploration", soundmark: "/ˌekspləˈreɪʃn/"},
    {chinese: "宇航员", english: "astronaut", soundmark: "/ˈæstrənɔːt/"},
    {chinese: "火箭", english: "rocket", soundmark: "/ˈrɒkɪt/"},
    {chinese: "卫星", english: "satellite", soundmark: "/ˈsætəlaɪt/"},
    {chinese: "轨道", english: "orbit", soundmark: "/ˈɔːrbɪt/"},
    {chinese: "银河", english: "galaxy", soundmark: "/ˈɡæləksi/"},
    {chinese: "行星", english: "planet", soundmark: "/ˈplænɪt/"},
    {chinese: "使命", english: "mission", soundmark: "/ˈmɪʃn/"},
    {chinese: "发射", english: "launch", soundmark: "/lɔːntʃ/"},
    {chinese: "着陆", english: "landing", soundmark: "/ˈlændɪŋ/"},
    {chinese: "失重", english: "weightlessness", soundmark: "/ˈweɪtləsnəs/"},
    {chinese: "殖民地", english: "colony", soundmark: "/ˈkɒləni/"},
    {chinese: "望远镜", english: "telescope", soundmark: "/ˈtelɪskoʊp/"}
  ],
  sentences: [
    {
      chinese: "太空探索代表了人类最伟大的成就之一。",
      english: "Space exploration represents one of humanity's greatest achievements.",
      soundmark: "/speɪs ˌekspləˈreɪʃn ˌreprɪˈzents wʌn əv hjuːˈmænɪtiz ˈɡreɪtɪst əˈtʃiːvmənts/",
      grammar: [
        {text: "exploration", role: "S", phonetic: "/ˌekspləˈreɪʃn/"},
        {text: "represents", role: "V", phonetic: "/ˌreprɪˈzents/"},
        {text: "one", role: "O", phonetic: "/wʌn/"},
        {text: "of humanity's achievements", role: "P", phonetic: "/əv hjuːˈmænɪtiz əˈtʃiːvmənts/"}
      ]
    },
    {
      chinese: "宇航员们冒着生命危险执行进入未知领域的任务。",
      english: "Astronauts risk their lives to carry out missions into the unknown.",
      soundmark: "/ˈæstrənɔːts rɪsk ðer laɪvz tə ˈkæri aʊt ˈmɪʃənz ˈɪntə ðə ʌnˈnoʊn/",
      grammar: [
        {text: "Astronauts", role: "S", phonetic: "/ˈæstrənɔːts/"},
        {text: "risk", role: "V", phonetic: "/rɪsk/"},
        {text: "lives", role: "O", phonetic: "/laɪvz/"},
        {text: "to carry out", role: "V", phonetic: "/tə ˈkæri aʊt/"},
        {text: "missions", role: "O", phonetic: "/ˈmɪʃənz/"},
        {text: "into the unknown", role: "P", phonetic: "/ˈɪntə ðə ʌnˈnoʊn/"}
      ]
    },
    {
      chinese: "火箭技术使得人类能够突破地球大气层的限制。",
      english: "Rocket technology has enabled humans to transcend the limitations of Earth's atmosphere.",
      soundmark: "/ˈrɒkɪk tekˈnɒlədʒi hæz ɪˈneɪbld ˈhjuːmənz tə trænˈsend ðə ˌlɪmɪˈteɪʃənz əv ɜːrθs ˈætməsfɪər/",
      grammar: [
        {text: "technology", role: "S", phonetic: "/tekˈnɒlədʒi/"},
        {text: "has enabled", role: "V", phonetic: "/hæz ɪˈneɪbld/"},
        {text: "humans", role: "O", phonetic: "/ˈhjuːmənz/"},
        {text: "to transcend", role: "V", phonetic: "/tə trænˈsend/"},
        {text: "limitations", role: "O", phonetic: "/ˌlɪmɪˈteɪʃənz/"},
        {text: "of atmosphere", role: "P", phonetic: "/əv ˈætməsfɪər/"}
      ]
    },
    {
      chinese: "1969年的登月任务仍然是人类历史上最具标志性的时刻之一。",
      english: "The 1969 moon landing mission remains one of the most iconic moments in human history.",
      soundmark: "/ðə ˈnaɪntiːn ˈsɪkstɪˈnaɪn muːn ˈlændɪŋ ˈmɪʃn rɪˈmeɪnz wʌn əv ðə məʊst aɪˈkɒnɪk ˈmoʊmənts ɪn ˈhjuːmən ˈhɪstri/",
      grammar: [
        {text: "mission", role: "S", phonetic: "/ˈmɪʃn/"},
        {text: "remains", role: "V", phonetic: "/rɪˈmeɪnz/"},
        {text: "one", role: "C", phonetic: "/wʌn/"},
        {text: "of the most iconic moments", role: "P", phonetic: "/əv ðə məʊst aɪˈkɒnɪk ˈmoʊmənts/"},
        {text: "in human history", role: "P", phonetic: "/ɪn ˈhjuːmən ˈhɪstri/"}
      ]
    },
    {
      chinese: "太空中的失重状态给宇航员带来了独特的挑战。",
      english: "Weightlessness in space presents unique challenges for astronauts.",
      soundmark: "/ˈweɪtləsnəs ɪn speɪs prɪˈzents juˈniːk ˈtʃælɪndʒɪz fɔːr ˈæstrənɔːts/",
      grammar: [
        {text: "Weightlessness", role: "S", phonetic: "/ˈweɪtləsnəs/"},
        {text: "in space", role: "P", phonetic: "/ɪn speɪs/"},
        {text: "presents", role: "V", phonetic: "/prɪˈzents/"},
        {text: "challenges", role: "O", phonetic: "/ˈtʃælɪndʒɪz/"},
        {text: "for astronauts", role: "P", phonetic: "/fɔːr ˈæstrənɔːts/"}
      ]
    },
    {
      chinese: "太空望远镜让我们得以窥见数十亿光年之外的星系。",
      english: "Space telescopes allow us to glimpse galaxies billions of light-years away.",
      soundmark: "/speɪs ˈtelɪskoʊps əˈlaʊ ʌs tə ɡlɪmps ˈɡæləksiz ˈbɪljənz əv laɪt-jɪərz əˈweɪ/",
      grammar: [
        {text: "telescopes", role: "S", phonetic: "/ˈtelɪskoʊps/"},
        {text: "allow", role: "V", phonetic: "/əˈlaʊ/"},
        {text: "us", role: "O", phonetic: "/ʌs/"},
        {text: "to glimpse", role: "V", phonetic: "/tə ɡlɪmps/"},
        {text: "galaxies", role: "O", phonetic: "/ˈɡæləksiz/"},
        {text: "billions of light-years away", role: "Adv", phonetic: "/ˈbɪljənz əv laɪt-jɪərz əˈweɪ/"}
      ]
    },
    {
      chinese: "建立太空殖民地的愿景推动着当代太空探索的前沿。",
      english: "The vision of establishing space colonies drives the frontier of contemporary space exploration.",
      soundmark: "/ðə ˈvɪʒn əv ɪˈstæblɪʃɪŋ speɪs ˈkɒləniːz draɪvz ðə ˈfrʌntɪər əv kənˈtempərəri speɪs ˌekspləˈreɪʃn/",
      grammar: [
        {text: "vision", role: "S", phonetic: "/ˈvɪʒn/"},
        {text: "of establishing colonies", role: "P", phonetic: "/əv ɪˈstæblɪʃɪŋ ˈkɒləniːz/"},
        {text: "drives", role: "V", phonetic: "/draɪvz/"},
        {text: "frontier", role: "O", phonetic: "/ˈfrʌntɪər/"},
        {text: "of exploration", role: "P", phonetic: "/əv ˌekspləˈreɪʃn/"}
      ]
    }
  ],
  review: [
    {chinese: "引力", english: "gravity", soundmark: "/ˈɡrævɪti/"},
    {chinese: "天文", english: "cosmic", soundmark: "/ˈkɒzmɪk/"},
    {chinese: "现象", english: "phenomenon", soundmark: "/fɪˈnɒmɪnən/"},
    {chinese: "研究", english: "research", soundmark: "/rɪˈsɜːtʃ/"},
    {chinese: "实验", english: "experiment", soundmark: "/ɪkˈsperɪmənt/"},
    {chinese: "观察", english: "observe", soundmark: "/əbˈzɜːrv/"},
    {chinese: "发现", english: "discover", soundmark: "/dɪˈskʌvər/"}
  ]
};

// Combine all lessons
const lessons = {
  29: lesson29,
  30: lesson30,
  31: lesson31,
  32: lesson32,
  33: lesson33,
  34: lesson34,
  35: lesson35
};

// Convert to the required format
function convertToFormat(lesson) {
  const result = [];
  
  // Add vocabulary
  lesson.vocabulary.forEach(item => {
    result.push({
      chinese: item.chinese,
      english: item.english,
      soundmark: item.soundmark
    });
  });
  
  // Add sentences with grammar
  lesson.sentences.forEach(item => {
    result.push({
      chinese: item.chinese,
      english: item.english,
      soundmark: item.soundmark,
      grammar: item.grammar
    });
  });
  
  // Add review vocabulary
  lesson.review.forEach(item => {
    result.push({
      chinese: item.chinese,
      english: item.english,
      soundmark: item.soundmark
    });
  });
  
  return result;
}

// Write all files
Object.keys(lessons).forEach(lessonNum => {
  const lesson = lessons[lessonNum];
  const data = convertToFormat(lesson);
  const filename = path.join(outputDir, `${lessonNum}.json`);
  fs.writeFileSync(filename, JSON.stringify(data, null, 2), 'utf8');
  console.log(`✓ Generated ${filename} with ${data.length} items`);
});

console.log('\n✅ All 7 files generated successfully!');
