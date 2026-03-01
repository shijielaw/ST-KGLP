# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from modelscope import snapshot_download

# model download
model_dir = snapshot_download(model_id='Qwen/Qwen2.5-14B', cache_dir='./')

print(model_dir)
