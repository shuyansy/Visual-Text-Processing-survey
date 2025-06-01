import json
import re
import os


def extract_numbers(input_str):
    # 正则表达式匹配冒号后面的数字
    numbers = re.findall(r":\s*(\d+)", input_str)
    # 将提取的数字转换为整数
    return [int(num) for num in numbers]

folder="./evaluation_results/ctrnet"
json_list=os.listdir(folder)
all_vs,all_tf,all_total=0,0,0
num=0
for j in json_list:
    json_file=os.path.join(folder,j)
    with open(json_file) as f:
        data=json.load(f)
    
    print("#####",data)

    for i in data:
        # print(i)
        try:
            scores = extract_numbers(data[i])
        except:
            continue
        # print(scores)

        if len(scores) <3:
            continue

    
        vs=scores[0]
        tf=scores[1]
        total=scores[2]
        all_vs+=vs
        all_tf+=tf
        all_total+=total
        num+=1





print("#############evaluation results")
final_vs=all_vs/num
final_tf=all_tf/num
final_total=all_total/num

print(final_vs)
print(final_tf)
print(final_total)


