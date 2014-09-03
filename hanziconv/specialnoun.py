# -*- coding: utf-8 -*-
#
# Copyright 2014 Bernard Yue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals

import textwrap
from collections import defaultdict

s2t_exceptions = defaultdict(list)

masterlist = (
    ('几',
     """
     """,
     """
        茶几
     """),
    ('只',
     """
        只有 只欠 只可 只說 只是 只要 只能 只好 只不 只得
        只怕 只恐 只顾 只管 只身 只限 只读 只争 只可
     """,
     """
     """),
    ('志',
     """
        志愿 志向 志同 志工 志气 志氣 志趣 志丹 志在 志士
        志留 志贺 志留 志不 志得 志高
     """,
     """
        立志 同志
     """),
    ('后',
     """天后 皇后 后里 太后 帝后
     """,
     """后羿
     """),
    ('面',
     """
        面积 面前 面对 面临 面试 面膜 面料 面向 面板 面子
        面部 面孔 面的 面貌 面霜 面具 面容 面世 面纱 面影
        面目 面色 面谈 面值 面相 面带 面罩 面皮 面颊 面市
        面授 面庞 面面 面目 面面 面额 面红 面壁 面熟 面巾
        面型 面儿 面镜 面黄 面临 面形 面首 面朝 面授 面对
        面貼
     """,
     """
        上面 下面 左面 右面 前面 後面 里面 外面 斜面 表面
        板面 镜面 水面 出面 对面 貼面
     """),
)
for key, data1, data2 in masterlist:
    for data in data1, data2:
        for d in textwrap.dedent(data).strip().split(' '):
            s2t_exceptions[key].append(d)

