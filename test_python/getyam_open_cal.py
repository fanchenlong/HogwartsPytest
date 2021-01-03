
import yaml
def get_datas():
    with open("cal.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        ##加
        add_datas = datas["add_datas"]
        add_ids = datas["add_ids"]
        ##减
        sub_datas = datas["sub_datas"]
        sub_ids = datas["sub_ids"]
        ##乘
        mul_datas = datas["mul_datas"]
        mul_ids = datas["mul_ids"]
        ##除
        div_datas = datas["div_datas"]
        div_ids = datas["div_ids"]
        return [add_datas,add_ids,sub_datas,sub_ids,mul_datas,mul_ids,div_datas,div_ids]