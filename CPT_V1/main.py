#! coding=utf8
import read_data
import warnings
import first_clustering
import cal_smilar
import match
warnings.filterwarnings('ignore')


if __name__ == "__main__":
    data = read_data.read('data/test.csv')
    data1 = read_data.read('data/data.csv')
    # print(data.columns)
    # del data['ip_24_count']
    # data = data[data['ip_24'] == '23.62.6']
    data = cal_smilar.group_feature(data, 'user_agent')
    data = cal_smilar.group_feature(data, 'host')
    data = cal_smilar.group_feature(data, 'accept_language')
    data = cal_smilar.group_feature(data, 'accept_encoding')
    data = cal_smilar.group_feature(data, 'ip_dst')
    # data = data.head(10000)
    gs = first_clustering.get_gs(data1[['path', 'original_host', 'ip_dst']])
    CPT = cal_smilar.get_all_CPT(data, gs)
    print("模板生成成功")
    CPT.to_csv("CPT.csv", sep='\a', index=False)
    # df 为后续获取的http请求
    df = data.tail(1)
    cpt, _ = match.get_dis(df, CPT, gs)
    print(cpt)
    print(data.columns.values)

