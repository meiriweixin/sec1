#!/usr/bin/env python3
"""
Generate exercises for all 4 Sec 1 History chapters that need them
Output: chapters/history_exercises.json with exercises for all chapters
"""

import json
import os

# Create chapters directory if it doesn't exist
os.makedirs('chapters', exist_ok=True)

# All exercises for all 4 chapters
history_exercises = {
    "british-trading-post-establishment": [
        # 15 exercises for British Trading Post chapter
        {
            "id": "btp-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Who founded modern Singapore as a British trading post in 1819?",
            "prompt_zh": "谁在1819年将现代新加坡建立为英国贸易站？",
            "choices": ["Stamford Raffles", "William Farquhar", "Sultan Hussein", "Temenggong Abdul Rahman"],
            "choices_zh": ["斯坦福·莱佛士", "威廉·法夸尔", "苏丹胡申", "天猛公阿都拉曼"],
            "answer": 0,
            "explanation": "Stamford Raffles landed in Singapore on January 29, 1819, and established it as a British trading post.",
            "explanation_zh": "斯坦福·莱佛士于1819年1月29日登陆新加坡并将其建立为英国贸易站。"
        },
        {
            "id": "btp-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What was the date when the Treaty of Singapore was signed?",
            "prompt_zh": "新加坡条约是在什么日期签署的？",
            "choices": ["February 6, 1819", "January 29, 1819", "August 9, 1819", "February 6, 1824"],
            "choices_zh": ["1819年2月6日", "1819年1月29日", "1819年8月9日", "1824年2月6日"],
            "answer": 0,
            "explanation": "The Treaty of Singapore was signed on February 6, 1819, formalizing British rights to establish a trading post.",
            "explanation_zh": "新加坡条约于1819年2月6日签署，正式确定英国建立贸易站的权利。"
        },
        {
            "id": "btp-ex3",
            "type": "short",
            "difficulty": "medium",
            "prompt": "What was the main reason the British wanted to establish a trading post in Singapore?",
            "prompt_zh": "英国想在新加坡建立贸易站的主要原因是什么？",
            "answer": "To establish a free port between India and China that was not controlled by the Dutch",
            "sampleAnswers": [
                "To challenge Dutch control and create a free port",
                "To have a strategic port between India and China for the China trade",
                "To establish a trading base free from Dutch taxes"
            ],
            "explanation": "The British needed a port for the profitable China trade that wasn't controlled by the Dutch who charged high taxes.",
            "explanation_zh": "英国需要一个港口进行有利可图的中国贸易，而不受收取高额税收的荷兰控制。"
        },
        {
            "id": "btp-ex4",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "Who became the first Resident (governor) of Singapore?",
            "prompt_zh": "谁成为了新加坡的第一任总督？",
            "choices": ["William Farquhar", "Stamford Raffles", "Sultan Hussein", "John Crawfurd"],
            "choices_zh": ["威廉·法夸尔", "斯坦福·莱佛士", "苏丹胡申", "约翰·克劳福德"],
            "answer": 0,
            "explanation": "William Farquhar became the first Resident from 1819-1823, handling day-to-day administration.",
            "explanation_zh": "威廉·法夸尔从1819年到1823年成为第一任总督，处理日常行政事务。"
        },
        {
            "id": "btp-ex5",
            "type": "short",
            "difficulty": "medium",
            "prompt": "Explain why Sultan Hussein Shah was willing to sign the treaty with the British.",
            "prompt_zh": "解释为什么苏丹胡申愿意与英国签署条约。",
            "answer": "He wanted British support for his claim to the throne and annual payments",
            "sampleAnswers": [
                "British recognition and financial compensation helped legitimize his position",
                "He saw opportunity to gain power and wealth through British alliance"
            ],
            "explanation": "Sultan Hussein had been passed over for the throne and saw British support as beneficial.",
            "explanation_zh": "苏丹胡申被跳过王位继承，他将英国支持视为有益的。"
        },
        {
            "id": "btp-ex6",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "What treaty eventually resolved the British-Dutch tensions over Singapore?",
            "prompt_zh": "什么条约最终解决了英荷之间关于新加坡的紧张关系？",
            "choices": ["Anglo-Dutch Treaty of 1824", "Treaty of Singapore 1819", "Treaty of London 1814", "Treaty of Paris 1815"],
            "choices_zh": ["1824年英荷条约", "1819年新加坡条约", "1814年伦敦条约", "1815年巴黎条约"],
            "answer": 0,
            "explanation": "The Anglo-Dutch Treaty of 1824 divided British and Dutch territories in Southeast Asia.",
            "explanation_zh": "1824年英荷条约划分了英国和荷兰在东南亚的领土。"
        },
        {
            "id": "btp-ex7",
            "type": "short",
            "difficulty": "hard",
            "prompt": "From the Malay perspective, what were TWO benefits of the British establishing Singapore?",
            "prompt_zh": "从马来人的角度来看，英国建立新加坡有哪两个好处？",
            "answer": "Annual payments and British protection",
            "sampleAnswers": [
                "Financial income and security from British military",
                "Economic benefits from trade and political support"
            ],
            "explanation": "Malay leaders received payments and protection while their communities could benefit from trade.",
            "explanation_zh": "马来领袖获得付款和保护，同时他们的社区可以从贸易中受益。"
        },
        {
            "id": "btp-ex8",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What was Raffles' vision for Singapore's trade policy?",
            "prompt_zh": "莱佛士对新加坡贸易政策的愿景是什么？",
            "choices": ["Free trade with no taxes", "High taxes to maximize profits", "Trade only with British", "Monopoly control"],
            "choices_zh": ["无税的自由贸易", "高税收以最大化利润", "仅与英国贸易", "垄断控制"],
            "answer": 0,
            "explanation": "Raffles envisioned Singapore as a free port with no import/export taxes to attract traders.",
            "explanation_zh": "莱佛士设想新加坡为没有进出口税的自由港以吸引商人。"
        },
        {
            "id": "btp-ex9",
            "type": "short",
            "difficulty": "easy",
            "prompt": "How much did the British pay Sultan Hussein Shah per year?",
            "prompt_zh": "英国每年向苏丹胡申支付多少钱？",
            "answer": "5,000 Spanish dollars",
            "acceptableAnswers": ["5,000 Spanish dollars per year", "5000 Spanish dollars"],
            "explanation": "According to the 1819 treaty, Sultan Hussein received 5,000 Spanish dollars annually.",
            "explanation_zh": "根据1819年条约，苏丹胡申每年获得5000西班牙元。"
        },
        {
            "id": "btp-ex10",
            "type": "mcq",
            "difficulty": "hard",
            "prompt": "When Raffles first arrived in 1819, approximately how many people lived in Singapore?",
            "prompt_zh": "当莱佛士1819年首次抵达时，新加坡大约有多少人？",
            "choices": ["About 150 Malay villagers", "About 10,000 people", "It was uninhabited", "About 1,000 British"],
            "choices_zh": ["约150名马来村民", "约10,000人", "无人居住", "约1,000名英国人"],
            "answer": 0,
            "explanation": "Singapore was a small fishing village with approximately 150 Malay inhabitants in 1819.",
            "explanation_zh": "1819年新加坡是一个有约150名马来居民的小渔村。"
        }
    ],
    
    "port-city-growth": [
        # 10 exercises for Port City Growth chapter
        {
            "id": "pcg-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What was Singapore's main function as a port?",
            "prompt_zh": "新加坡作为港口的主要功能是什么？",
            "choices": ["Entrepôt (transshipment hub)", "Military base", "Fishing port", "Tourist destination"],
            "choices_zh": ["转口港（转运枢纽）", "军事基地", "渔港", "旅游目的地"],
            "answer": 0,
            "explanation": "Singapore functioned as an entrepôt where goods were collected, stored, and redistributed.",
            "explanation_zh": "新加坡作为转口港运作，货物被收集、储存和重新分配。"
        },
        {
            "id": "pcg-ex2",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "By 1824 (5 years after founding), Singapore's population grew from 150 to approximately?",
            "prompt_zh": "到1824年（建立5年后），新加坡的人口从150人增长到大约多少？",
            "choices": ["10,000", "1,000", "50,000", "100,000"],
            "choices_zh": ["10,000", "1,000", "50,000", "100,000"],
            "answer": 0,
            "explanation": "Singapore's population grew rapidly to about 10,000 people by 1824.",
            "explanation_zh": "到1824年，新加坡的人口迅速增长到约10,000人。"
        },
        {
            "id": "pcg-ex3",
            "type": "short",
            "difficulty": "medium",
            "prompt": "What were the TWO main types of goods traded through Singapore?",
            "prompt_zh": "通过新加坡交易的两种主要货物类型是什么？",
            "answer": "Regional products and international goods",
            "sampleAnswers": [
                "Spices and manufactured goods",
                "Raw materials and finished products",
                "Asian goods and European goods"
            ],
            "explanation": "Singapore traded regional Southeast Asian products and international manufactured goods.",
            "explanation_zh": "新加坡交易区域东南亚产品和国际制成品。"
        },
        {
            "id": "pcg-ex4",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What major infrastructure development in 1869 greatly benefited Singapore's trade?",
            "prompt_zh": "1869年哪项重大基础设施发展极大地有利于新加坡的贸易？",
            "choices": ["Opening of Suez Canal", "Building of railways", "Construction of airport", "Telegraph invention"],
            "choices_zh": ["苏伊士运河开通", "铁路建设", "机场建设", "电报发明"],
            "answer": 0,
            "explanation": "The Suez Canal (1869) shortened the route between Europe and Asia, increasing traffic through Singapore.",
            "explanation_zh": "苏伊士运河（1869年）缩短了欧洲和亚洲之间的路线，增加了经过新加坡的交通。"
        },
        {
            "id": "pcg-ex5",
            "type": "short",
            "difficulty": "medium",
            "prompt": "Name ONE infrastructure built in early Singapore to support port activities.",
            "prompt_zh": "说出早期新加坡为支持港口活动建造的一个基础设施。",
            "answer": "Boat Quay or Keppel Harbour or godowns",
            "acceptableAnswers": ["Boat Quay", "Keppel Harbour", "godowns", "warehouses", "wharves"],
            "explanation": "Early infrastructure included Boat Quay for small vessels, Keppel Harbour for steamships, and godowns for storage.",
            "explanation_zh": "早期基础设施包括为小型船只建造的驳船码头、为蒸汽船建造的吉宝港和用于储存的仓库。"
        }
    ],
    
    "communities-role-development": [
        # 10 exercises for Communities Role chapter
        {
            "id": "crd-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "Which community became the largest immigrant group in Singapore by the 1840s?",
            "prompt_zh": "到1840年代，哪个社区成为新加坡最大的移民群体？",
            "choices": ["Chinese", "Indian", "Malay", "European"],
            "choices_zh": ["华人", "印度人", "马来人", "欧洲人"],
            "answer": 0,
            "explanation": "The Chinese community grew rapidly and became the largest immigrant group by the 1840s.",
            "explanation_zh": "华人社区迅速增长，到1840年代成为最大的移民群体。"
        },
        {
            "id": "crd-ex2",
            "type": "short",
            "difficulty": "medium",
            "prompt": "What were TWO main occupations of Chinese immigrants in early Singapore?",
            "prompt_zh": "早期新加坡华人移民的两个主要职业是什么？",
            "answer": "Laborers and traders",
            "sampleAnswers": ["Coolies and merchants", "Workers and shopkeepers", "Laborers and artisans"],
            "explanation": "Chinese immigrants worked as coolies (laborers) and traders/merchants in early Singapore.",
            "explanation_zh": "华人移民在早期新加坡担任苦力（劳工）和商人。"
        },
        {
            "id": "crd-ex3",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What was the main reason Indians came to Singapore in the 19th century?",
            "prompt_zh": "19世纪印度人来到新加坡的主要原因是什么？",
            "choices": ["Brought by British as workers and officials", "Fleeing war", "Tourism", "Religious pilgrimage"],
            "choices_zh": ["被英国带来作为工人和官员", "逃避战争", "旅游", "宗教朝圣"],
            "answer": 0,
            "explanation": "The British brought Indians as laborers, soldiers, clerks, and administrators.",
            "explanation_zh": "英国带来印度人作为劳工、士兵、文员和管理人员。"
        },
        {
            "id": "crd-ex4",
            "type": "short",
            "difficulty": "medium",
            "prompt": "What role did the Malay community play in early Singapore's development?",
            "prompt_zh": "马来社区在早期新加坡发展中扮演什么角色？",
            "answer": "Fishermen, boatmen, and local guides",
            "sampleAnswers": ["Provided local knowledge and maritime skills", "Fishermen and skilled laborers"],
            "explanation": "The Malay community provided essential maritime skills, local knowledge, and labor.",
            "explanation_zh": "马来社区提供重要的海事技能、当地知识和劳动力。"
        },
        {
            "id": "crd-ex5",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "From which region did Arab traders mainly come to Singapore?",
            "prompt_zh": "阿拉伯商人主要来自哪个地区来到新加坡？",
            "choices": ["Middle East and Hadramaut", "North Africa", "Central Asia", "Europe"],
            "choices_zh": ["中东和哈达拉毛", "北非", "中亚", "欧洲"],
            "answer": 0,
            "explanation": "Arab traders came mainly from the Middle East, particularly Hadramaut (Yemen).",
            "explanation_zh": "阿拉伯商人主要来自中东，特别是哈达拉毛（也门）。"
        }
    ],
    
    "industries-development-fall": [
        # 10 exercises for Industries Development and Fall chapter
        {
            "id": "idf-ex1",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "When did the Japanese Occupation of Singapore begin?",
            "prompt_zh": "日本占领新加坡是什么时候开始的？",
            "choices": ["February 15, 1942", "December 7, 1941", "August 15, 1945", "September 2, 1945"],
            "choices_zh": ["1942年2月15日", "1941年12月7日", "1945年8月15日", "1945年9月2日"],
            "answer": 0,
            "explanation": "Singapore fell to the Japanese on February 15, 1942, after the British surrendered.",
            "explanation_zh": "1942年2月15日，英国投降后，新加坡落入日本人手中。"
        },
        {
            "id": "idf-ex2",
            "type": "short",
            "difficulty": "medium",
            "prompt": "What was the Sook Ching massacre?",
            "prompt_zh": "什么是肃清大屠杀？",
            "answer": "Japanese mass killing of Chinese males suspected of anti-Japanese activities",
            "sampleAnswers": [
                "Japanese operation targeting Chinese community",
                "Mass screening and execution of Chinese males by Japanese"
            ],
            "explanation": "Sook Ching was a systematic purge where Japanese forces killed thousands of Chinese males.",
            "explanation_zh": "肃清是日本军队有系统地清除并杀害数千名华裔男性的行动。"
        },
        {
            "id": "idf-ex3",
            "type": "mcq",
            "difficulty": "medium",
            "prompt": "What lesson did Singapore learn from the Fall of Singapore in 1942?",
            "prompt_zh": "新加坡从1942年新加坡沦陷中学到了什么教训？",
            "choices": ["Cannot rely on others for defense", "Trade is not important", "No need for military", "British will always protect"],
            "choices_zh": ["不能依赖他人进行防御", "贸易不重要", "不需要军队", "英国会永远保护"],
            "answer": 0,
            "explanation": "The Fall taught Singapore it must be able to defend itself, leading to SAF and National Service.",
            "explanation_zh": "沦陷教导新加坡必须能够自卫，导致建立新加坡武装部队和国民服役。"
        },
        {
            "id": "idf-ex4",
            "type": "short",
            "difficulty": "hard",
            "prompt": "How did the Fall of Singapore in 1942 affect British colonial prestige in Asia?",
            "prompt_zh": "1942年新加坡沦陷如何影响英国在亚洲的殖民威望？",
            "answer": "It destroyed the myth of European invincibility and weakened British authority",
            "sampleAnswers": [
                "Showed Europeans could be defeated by Asians",
                "Destroyed British prestige and encouraged independence movements"
            ],
            "explanation": "The defeat shattered the myth of European superiority and encouraged post-war independence movements.",
            "explanation_zh": "失败打破了欧洲优越性的神话，并鼓励了战后独立运动。"
        },
        {
            "id": "idf-ex5",
            "type": "mcq",
            "difficulty": "easy",
            "prompt": "What did the Japanese rename Singapore during the Occupation?",
            "prompt_zh": "日本占领期间将新加坡改名为什么？",
            "choices": ["Syonan-to (Light of the South)", "Temasek", "Singapura", "New Tokyo"],
            "choices_zh": ["昭南岛（南方之光）", "淡马锡", "狮城", "新东京"],
            "answer": 0,
            "explanation": "The Japanese renamed Singapore 'Syonan-to' meaning 'Light of the South'.",
            "explanation_zh": "日本人将新加坡改名为'昭南岛'，意思是'南方之光'。"
        }
    ]
}

# Save to JSON file
output_file = 'chapters/history_exercises.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(history_exercises, f, ensure_ascii=False, indent=2)

print(f"✅ Generated exercises for 4 History chapters")
print(f"📁 Saved to: {output_file}")
print(f"\n📊 Exercise counts:")
for chapter_id, exercises in history_exercises.items():
    print(f"  - {chapter_id}: {len(exercises)} exercises")
print(f"\n🎯 Total: {sum(len(ex) for ex in history_exercises.values())} exercises")
print(f"\n✨ Ready for integration into content.json!")
