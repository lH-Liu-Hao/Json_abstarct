from JSON_ABSTRACT.abstract import Clean_json_text,GetContent,GetTitle,GetTime

class Json_abstract():
    def __init__(self):
        self.clean_json = Clean_json_text()

    def get_key_exp(self,key_exp_dict):
        tit_key_exp = key_exp_dict.get('tit_key_exp','')
        con_key_exp = key_exp_dict.get('con_key_exp','')
        time_key_exp = key_exp_dict.get('time_key_exp','')
        return tit_key_exp,con_key_exp,time_key_exp

    def all_abstract(self,JSON_TEXT,key_exp_dict=None,**kwargs):
        tit_key_exp, con_key_exp, time_key_exp = self.get_key_exp(key_exp_dict)
        text = self.clean_json.clean_json_text(JSON_TEXT)
        content = GetContent(con_key_exp=con_key_exp,**kwargs).abstract(text)
        title = GetTitle(tit_key_exp=tit_key_exp,**kwargs).abstract(text)
        time = GetTime(time_key_exp=time_key_exp,**kwargs).abstract(text)
        result = {
            'title':title,
            'time':time,
            'content':content,
        }
        return result