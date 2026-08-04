# LinguaPulse 课程数据生成规范

## 数据格式

每课一个 JSON 文件，文件名 `NN.json`（两位数字，如 `01.json`）。文件内容是一个 JSON 数组，每项为一个语句对象：

```json
{
  "chinese": "中文（可以加括号注释，如：喜欢(过去)）",
  "english": "English text（绝对不加句号/问号等标点）",
  "soundmark": "/aɪ/ /laɪk/ （每个词空格分隔）",
  "grammar": [
    {"text": "I", "role": "S", "phonetic": "/aɪ/"},
    {"text": "like", "role": "V", "phonetic": "/laɪk/"},
    {"text": "the food", "role": "O", "phonetic": "/ðə/ /fud/"}
  ]
}
```

- 简单的词/短语不需要 grammar 字段
- 完整句子才需要 grammar 标注
- 纯单词复习（课末尾）不加 grammar

## 核心原则：渐进式搭建

每课按照「积木搭建」的方式，从零开始逐层构建：

```
单词 → 词组 → 简单句 → 否定/疑问变体 → 时态变化 → 复合句
```

示例（第1课片段）：
```json
{"chinese":"我","english":"I","soundmark":"/aɪ/"}
{"chinese":"喜欢","english":"like","soundmark":"/laɪk/"}
{"chinese":"我喜欢","english":"I like","soundmark":"/aɪ/ /laɪk/"}
{"chinese":"这个食物","english":"the food","soundmark":"/ðə/ /fud/"}
{"chinese":"我喜欢这个食物","english":"I like the food","soundmark":"/aɪ/ /laɪk/ /ðə/ /fud/","grammar":[...]}
{"chinese":"不","english":"don't","soundmark":"/dont/"}
{"chinese":"不喜欢","english":"don't like","soundmark":"/dont/ /laɪk/"}
{"chinese":"我不喜欢这个食物","english":"I don't like the food","soundmark":"/aɪ/ /dont/ /laɪk/ /ðə/ /fud/","grammar":[...]}
```

关键：**每个新词汇/语法点，都先单独引入，再逐步组合**。学习者始终在已有知识基础上扩展。

## 语法角色标签

| 标签 | 含义 | 示例 |
|------|------|------|
| S | 主语 | I, he, the car |
| V | 谓语动词 | like, eat, run |
| O | 宾语 | the food, him |
| A | 状语 | in the morning, quickly |
| Lv | 系动词 | is, am, are, was, been |
| C | 补语 | my handbag, a teacher |
| Art | 冠词 | the, a, an |
| Det | 限定词 | my, your, this, that |
| P | 介词/小品词 | in, on, to, out, up |
| Neg | 否定词 | not, don't, never |
| Adv | 副词 | very, always, sometimes |
| Int | 感叹词 | excuse, hello, yes |

## 课程结构规范

每课包含以下阶段：

### 阶段1：新词汇引入（约10-15条）
逐个引入本课核心单词，每个单词独立一条语句。单词附带音标，不需要 grammar。

### 阶段2：词组组合（约10-15条）
将新词汇逐步组合成短语。如：冠词+名词、形容词+名词、动词+副词等。

### 阶段3：简单句构建（约10-15条）
开始构建完整句子。每句加入 grammar 标注。先做肯定句，再做否定句、疑问句。

### 阶段4：变化与扩展（约10-15条）
在已有句型基础上引入时态变化（过去/将来/进行/完成）、被动语态、从句等。

### 阶段5：复合句（约5-10条）
将已学的句子组合成更复杂的表达。使用连接词、状语从句等。

### 阶段6：词汇复习（约5-10条）
课末尾用纯单词（无 grammar）回顾本课核心词汇。

## 各课程包规范

### 星荣零基础学英语（60课）
- 难度级别：beginner（第1-20课） → intermediate（第21-40课） → advanced（第41-60课）
- 每课 60-80 条语句
- 前20课：基础词汇、问候、自我介绍、简单动词、现在时
- 中20课：过去时、将来时、比较级、情态动词、场景对话
- 后20课：完成时、被动语态、条件句、从句、综合应用

### 新概念英语第一册（70课）
- 难度级别：beginner → intermediate
- 每课 50-70 条语句
- 基于经典 NCE1 课文内容：日常对话、基础语法、物品归属、家庭、时间、天气等

### 新概念英语第二册（90课）
- 难度级别：intermediate
- 每课 50-70 条语句
- 短文阅读、过去时态、被动语态、间接引语、条件句

### 新概念英语第三册（60课）
- 难度级别：advanced
- 每课 50-60 条语句
- 复杂句型、虚拟语气、倒装句、段落理解

### 新概念英语第四册（50课）
- 难度级别：advanced
- 每课 50-60 条语句
- 学术英语、论说文结构、高阶语法、修辞手法

## 输出要求

1. 每课一个独立 JSON 文件
2. 文件名 `NN.json`（01-99 范围）
3. 保存到对应目录：
   - 星荣 → `app/data/earthworm/courses/`
   - NCE1 → `app/data/earthworm/nce1/`
   - NCE2 → `app/data/earthworm/nce2/`
   - NCE3 → `app/data/earthworm/nce3/`
   - NCE4 → `app/data/earthworm/nce4/`
4. JSON 格式正确，可直接 parse
5. **英文文本不加任何标点符号**
6. 音标使用标准 IPA 格式，单词间空格分隔
