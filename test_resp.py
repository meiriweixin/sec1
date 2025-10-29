import json
d=json.load(open("src/data/content.json","r",encoding="utf-8"))
for s in d["subjects"]:
 if s["id"]=="science":
  for c in s["chapters"]:
   if c["id"]=="respiratory-system":
    c["exercises"].extend([{"id":"resp-ex2","type":"mcq","difficulty":"easy","prompt":"What is the main function of the respiratory system?","prompt_zh":"呼吸系统的主要功能是什么？","choices":["To exchange oxygen and carbon dioxide","To pump blood","To digest food","To remove solid waste"],"choices_zh":["交换氧气和二氧化碳","泵血","消化食物","去除固体废物"],"answer":0,"explanation":"The respiratory system allows oxygen to enter the blood.","explanation_zh":"呼吸系统使氧气进入血液。"}])
json.dump(d,open("src/data/content.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("Added 1 exercise to test")