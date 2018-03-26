
import torchtext.data as data
import os
import random

import newdatasets


if __name__ == '__main__':
    TEXT = data.Field(sequential=True, lower=True)
    LABEL = data.Field(sequential=False, use_vocab=False)

    # mydata = MyDataset(TEXT, LABEL)

    train_data, dev_data = newdatasets.MyDataset.splits(TEXT, LABEL)
    print(type(train_data))

    # TEXT.build_vocab(train_data, vectors="glove.6B.100d")
    TEXT.build_vocab(train_data)
    data.Iterator.splits((train_data, dev_data),batch_sizes=(64, len(dev_data)),**kargs)

    print(TEXT)
