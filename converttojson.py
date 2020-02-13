import json
import pandas as pd
import sys
import os


CSV_ENCODING = 'cp949'

'sme_string'.encode('utf-8')

# with open('clips_db.csv', 'r',encoding = CSV_ENCODING ) as f:
if True:
    reader = pd.read_csv(os.path.join('u_clips_db.csv'), encoding = 'UTF-8', dtype=str)
    data_list1 = list()
    data_list2 = list()
    data_list3 = list()
    a = dict()
    count = 0
    count2 = 0
    count3 =0
   # '{}'.format(5252)
    for i3 in range(len(reader)):
        c =list()
        row = reader.iloc[i3]
        row = dict(row)
        for j in a.keys():
            if (j == row['ori_word']):
                count2 = count2 + 1
                break
        if ((0 == count2)):
            if(count3 ==0):
                count3=count3+1
                for i4 in range(len(reader)):
                    row1 = reader.iloc[i4]
                    row1 = dict(row1)
                    del row1['Unnamed: 0']
                    del row1['word_ind']
              #      del row1['word_mean']
                    if (row['ori_word'] == row1['ori_word']):
                        del row1['ori_word']
                        c.append(row1)
                b = dict()
                b["meaning"] = "22"
                    #row['word_mean']
                b["tracks"] = c
                a[row['ori_word']] = b
            else:
                for j in a.keys():
                    for i4 in range(len(reader)):
                        row1 = reader.iloc[i4]
                        row1 = dict(row1)
                        del row1['Unnamed: 0']
                        del row1['word_ind']
                    #    del row1['word_mean']
                        if (j != row1['ori_word']):
                            del row1['ori_word']
                            c.append(row1)
                    break
                b = dict()
                b["meaning"] = "22"
                    #row['word_mean']
                b["tracks"] = c
                a[row['ori_word']] = b

        else:
            count2 = count2 - 1

    print(a)
    json_val = json.dumps(a)

    with open('clips_db.json','w',encoding='utf-8') as make_file:
        json.dump(a, make_file, indent="\t")



with open('clips_db.json', 'r') as f:
    json_data = json.load(f)

print(json.dumps(json_data, indent="\t") )
