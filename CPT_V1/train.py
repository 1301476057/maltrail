#! coding=utf8
import torch
import read_data
import warnings
import first_clustering
import cal_smilar
from sklearn.externals import joblib
import match
import Sentiment_RNN_Solution


if __name__ == "__main__":
    output_size = 1
    embedding_dim = 400
    hidden_dim = 256
    n_layers = 2
    net = Sentiment_RNN_Solution.SentimentRNN(output_size, embedding_dim, hidden_dim, n_layers)
    net.fit()

    # 保存模型
    torch.save(net, 'model/LSTM_model.pkl')
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
    CPT.to_csv("model/CPT.csv", sep='\a', index=False)
    # # 保存模型
    # joblib.dump(gs, 'model/gs.m')
    joblib.dump(gs, 'model/gs.m',protocol=2)
