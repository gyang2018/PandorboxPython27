
def Normalize(string):                    #格式化查询词
    #result = RemoveAccents(string)
    result = string.replace(".", " ")
    result = result.replace("-", " ")
    # trim extra blank
    result = " ".join(result.split())
    # upper chars to lower
    result = result.lower()               #字符串变成小写
   
    return result                         #0726上一句改：没有被nickname 中的词替换



from xml2dict import XML2Dict
xml = XML2Dict()
r = xml.parse("tac_2011_kbp_english_evaluation_entity_linking_queries.xml")
f = open("query_info_0727", 'w')
f.write('#id\tname\tdocid\tname(格式化）\n')
        
for q in r.kbpentlink.query:
    progress = Normalize(q.name)
    f.write(q.id+'\t'+q.name + '\t'+q.docid + '\t'+progress+'\n')
f.close()
    
