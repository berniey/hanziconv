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
import textwrap
from collections import defaultdict

s2t_exceptions = defaultdict(list)

masterlist = (
    ('后',
     """天后 皇后 后里 太后 帝后 后羿"""),
    ('面',
     """
    面对面 面貼面
    面积 面前 面对 面临 面试 面膜 面料 面向 面板 面子
    面部 面孔 面的 面貌 面霜 面具 面容 面世 面纱 面影
    面目 面色 面谈 面值 面相 面带 面罩 面皮 面颊 面市
    面授 面庞 面面 面目 面面 面额 面红 面壁 面熟 面巾
    面型 面儿 面镜 面黄 面临 面形 面首 面朝 面授
    上面 下面 左面 右面 前面 後面 里面 外面 斜面 表面
    板面 镜面 水面 出面
     """),
)
for key, data in masterlist:
    for d in textwrap.dedent(data).strip().split(' '):
        s2t_exceptions[key].append(d)

"""
0    1    2    3    4    5    6    7    8    9
"""
