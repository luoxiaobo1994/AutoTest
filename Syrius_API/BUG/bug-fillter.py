# -*- coding:utf-8 -*-
# Author: luoxiaobo
# TIME: 2021/11/9 15:25

import requests, re
from lxml import etree
from collections import Counter
from multiprocessing.dummy import Pool
import pandas as pd
from base.common import dict_to_csv

base_url = 'https://jira.syriusrobotics.cn/browse/DIPLO-1026?jql=issuetype%20%3D%20Bug%20AND%20labels%20%3D%20'
issue_url = 'https://jira.syriusrobotics.cn/rest/api/latest/issue/{}?_=1636442915282'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Cookie": "jira.editor.user.mode=wysiwyg; seraph.rememberme.cookie=15036%3A6f5a1fab08980c8322c2d1cb2f779866499c01b8; JSESSIONID=7B56D6A629A1D6CBB325E14ED4F8D372; atlassian.xsrf.token=B7GL-1W9H-SNF9-JK4G_2f66c38e2ca600deef8efa56657e5304b600bcd7_lin"
}

label_ls = ['phenix-2021--8-14-sz-test-diplo', 'phenix-2021-08-09', 'phenix-2021-08-11-sz-test-diplo',
            'phenix-2021-08-14-sz-test-diplo',
            'phenix-2021-08-17-sz-test', 'phenix-2021-08-23-sz-test', 'phenix-2021-08-26-sz-test',
            'phenix-2021-08-28-sz-test',
            'phenix-2021-08-29-sg', 'phenix-2021-09--11-sz-test-cj', 'phenix-2021-09--26-sz-test-cj',
            'phenix-2021-09-01-sz-test',
            'phenix-2021-09-08-sz-test', 'phenix-2021-09-11-sz-test', 'phenix-2021-08-29-sz-test',
            'phenix-2021-09-11-sz-test-cj', 'phenix-2021-09-14-jp-prod', 'phenix-2021-09-15-sz-test',
            'phenix-2021-09-18-sz-test', 'phenix-2021-10--25-sz-test', 'phenix-2021-10-04-sz-test',
            'phenix-2021-10-08-sz-test',
            'phenix-2021-10-10-sz-test', 'phenix-2021-10-13-sz-test', 'phenix-2021-10-14-sz-test',
            'phenix-2021-10-14-sz-test-local', 'phenix-2021-10-16-sz-test',
            'phenix-2021-10-19sz-test', 'phenix-2021-10-21sz_test', 'phenix-2021-10-25-sz-test',
            'phenix-2021-10-27sz-tes',
            'phenix-2021-10-27-sz-test', 'phenix-2021-10-29cj_local', 'phenix-2021-11-05-sz-test',
            'phenix-2021-11-05-sz-test', 'phenix-2021-11-10sz-test'
            ]

no_count = 0


# df = pd.DataFrame(data={'??????':1,'Bug??????':0,'Bug????????????':0,'DI':0})

def get_issue_list(label):
    file = './buglist.csv'
    version = {'??????': label}
    global no_count
    response = requests.get(url=base_url + label, headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)
    issue_ls = html.xpath('//ol[@class="issue-list"]/li')
    # print(f"????????????:{label},???????????????:{len(issue_ls)}???.")
    all_level = []
    conetent = html.xpath('//span[@class="issue-link-key"]/text()')
    version['Bug??????'] = len(issue_ls)
    # print(conetent)  # ??????bug???key
    for bug in conetent:
        common = get_bug_level(bug) & {'??????', '??????', '??????', '??????'}
        if len(common) != 0:
            all_level.append(list(common)[0])
        else:
            # print(f'bug:{bug},???????????????')
            all_level.append('?????????')
            no_count += 1
    # print(all_level)
    info = dict(Counter(all_level))
    version['Bug????????????'] = info
    DI = get_key(info, '??????') * 10 + get_key(info, '??????') * 3 + get_key(info, '??????') * 1 + get_key(info, '??????') * 0.1
    version['DI'] = DI
    # print(f"??????:{label}???DI???:{DI}")
    # df.append(version)
    # dict_to_csv(version, file=file)
    print(version)


def get_bug_level(bug_key):
    response = requests.get(url=issue_url.format(bug_key), headers=headers)
    # print(response.text)
    bug_state = re.findall('"name":"??????"', response.text, re.DOTALL)
    bug_level = re.findall('"value":"(.*?)"', response.text, re.DOTALL)
    # print(bug_state,bug_level)
    if len(bug_state) != 0:
        # print(bug_level)
        return set(bug_level)
    else:
        return set()  # ?????????????????????,????????????????????????????????????,????????????.


def get_key(d, key):
    return d.get(key, 0)


if __name__ == '__main__':
    pool = Pool(10)
    pool.map(get_issue_list, label_ls)
    # print(no_count)
    # get_bug_level('DIPLO-2012')  # ?????????bug??????
