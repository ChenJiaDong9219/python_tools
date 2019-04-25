import os
from random import randint
from urllib import request

from mitmproxy import ctx


class Dump_Videos:
    def __init__(self, dst_path, target_urls):
        self.dst_path = dst_path
        self.target_urls =  target_urls

    def request(self, flow):
        url = str(flow.request.url)
        ctx.log.info('{0}\ncurrent url: {1}\n{0}'.format('='*80, url))
        for t in target_urls:
            if t in url:
                filename = os.path.join(dst_path, str(randint(0, 9999999999999999))+'.mp4')
                rsp = request.urlopen(url)
                with open(filename, 'wb') as f:
                    f.write(rsp.read())


target_urls = ['v1-dy', 'v3-dy', 'v9-dy']
dst_path = '/storage/datasets/douyin/drunk'
addons = [Dump_Videos(dst_path = dst_path, target_urls = target_urls)]