import json
import re
import os


def extract_numbers(input_str):
    # 正则表达式匹配冒号后面的数字
    numbers = re.findall(r":\s*(\d+)", input_str)
    # 将提取的数字转换为整数
    return [int(num) for num in numbers]

folder="./DID/evaluation_results/DocTr"
json_list=os.listdir(folder)
all_geo,all_con,all_total=0,0,0
num=0
for j in json_list:
    json_file=os.path.join(folder,j)
    with open(json_file) as f:
        data=json.load(f)
    
    print("#####",data)

    for i in data:
        for j in data[i]:
            try:
                scores = extract_numbers(data[i][j])
            except:
                continue
        print("111111",scores)

        if len(scores) <3:
            continue

    
        geo=scores[0]
        con=scores[1]
        total=scores[2]
        if total==0:
            continue
        all_geo+=geo
        all_con+=con
        all_total+=total
        num+=1



print("#############evaluation results")
final_geo=all_geo/num
final_con=all_con/num
final_total=all_total/num

print(final_geo)
print(final_con)
print(final_total)



