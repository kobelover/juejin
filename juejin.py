#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique
import urllib.request


@unique
class Category(Enum):
    Android = '5562b410e4b00c57d9b94a92'  # 安卓
    Frontend = '5562b415e4b00c57d9b94ac8'  # 前端
    IOS = '5562b405e4b00c57d9b94a41'  # iOS
    Backend = '5562b419e4b00c57d9b94ae2'  # 后端
    Design = '5562b41de4b00c57d9b94b0f'  # 设计
    Product = '569cbe0460b23e90721dff38'  # 产品
    Freebie = '5562b422e4b00c57d9b94b53'  # 工具资源
    Article = '5562b428e4b00c57d9b94b9d'  # 阅读
    AI = '57be7c18128fe1005fa902de'  # 人工智能
    All = 'all'


ARTICLETYPE = {
    'hot': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_rank',
    'new': 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline',
}


def get_juejin(limit=20, category=Category.All, article_type='hot', src='sixgold'):
    if article_type == 'hot':
        url = ARTICLETYPE['hot']
    else:
        url = ARTICLETYPE['new']

    req_url = '%s?src=%s&limit=%s&category=%s' % (url, src, limit, category.value)

    def make_request():
        with urllib.request.urlopen(req_url) as f:
            yield f.read()

    yield from make_request()

if __name__ == '__main__':
    for i in get_juejin(limit=5, category=Category.AI, article_type='new', src='sixgold'):
        print(i.decode('utf-8'))
        print("\n")