
import torchtext.data as data
import os
import random


class MyDataset(data.Dataset):

    def __init__(self, text_field, label_field, path='data', examples=None, **kwargs):

        fields = [('text', text_field), ('label', label_field)]

        if examples is None:
            path = path
            examples = []
            with open(os.path.join(path, 'negtive'), errors='ignore') as f:
                examples += [
                    data.Example.fromlist([line, 'negative'], fields) for line in f]
            with open(os.path.join(path, 'negtive'), errors='ignore') as f:
                for line in f:
                    examples.append(data.Example.fromlist([line, 'neutral'], fields))
        super(MyDataset, self).__init__(examples, fields, **kwargs)

    @classmethod
    def splits(cls, text_field, label_field, dev_ratio=.1, shuffle=True, root='.', **kwargs):
        examples = cls(text_field, label_field, path='data', **kwargs).examples
        if shuffle: random.shuffle(examples)
        dev_index = -1 * int(dev_ratio*len(examples))

        return (cls(text_field, label_field, examples=examples[:dev_index]),
                cls(text_field, label_field, examples=examples[dev_index:]))
