#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mebook_spider - download.py
# Created by JT on 04-Sep-18 20:54.

import time
from selenium import webdriver
from ast import literal_eval
import json


def baidu_login(name, passwd):
    url = 'https://pan.baidu.com/'
    driver.get(url)
    print('开始登录')
    time.sleep(2)
    chg_field = driver.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn')
    chg_field.click()

    name_field = driver.find_element_by_id('TANGRAM__PSP_4__userName')
    passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')

    name_field.send_keys(name)
    passwd_field.send_keys(passwd)
    login_button.click()
    time.sleep(2)
    try:
        driver.find_element_by_id('TANGRAM__37__button_send_mobile')
        get_code_button = driver.find_element_by_id('TANGRAM__37__button_send_mobile')
        code_field = driver.find_element_by_id('TANGRAM__37__input_vcode')
        code_submit_button = driver.find_element_by_id('TANGRAM__37__button_submit')

        get_code_button.click()
        code = input("输入手机验证码:\n")
        code_field.send_keys(code)
        code_submit_button.click()
        time.sleep(2)
    except Exception as e:
        print('不需要手机登录验证或验证错误', e)
    return driver.get_cookies()


def baidupan_resave():
    with open("dl_baidupan.txt", "r", encoding="utf-8") as f:
        for i in f.readlines():
            data = i.strip().split(" ")
            share_link = data[1]
            if len(data) == 3:
                key = data[2]
            else:
                key = ""
            driver.get(share_link)
            time.sleep(1)
            try:
                if '不存在' in driver.title:
                    print("ID", data[0], '链接失效')
                    continue
            except Exception as e:
                print("Error:", e)
                continue
            if key != "":
                pw_field = driver.find_element_by_id('xfspgN3b')
                pw_field.send_keys(key)
                submit_button = driver.find_element_by_xpath('//*[@id="fufc62wg"]/a')
                submit_button.click()
                time.sleep(2)
                # 开始转存操作
                file_title = driver.find_element_by_xpath('//*[@id="bd-main"]/div/div[1]/div/div[1]/h2').text
                print("ID", data[0], "转存", file_title, end=" -> ")
                select_all_button = driver.find_element_by_xpath('//*[@id="shareqr"]/div[2]/div[2]/div/ul[1]/li[1]/div/span[1]')
                select_all_button.click()
                time.sleep(0.5)
                resave_button = driver.find_element_by_xpath('//*[@id="shareqr"]/div[2]/div[2]/div/div/div/div[2]/a[1]')
                resave_button.click()
                time.sleep(1.5)
                if '最近保存路径' in driver.find_element_by_xpath('//*[@id="fileTreeDialog"]/div[3]').text:
                    driver.find_element_by_xpath('//*[@id="fileTreeDialog"]/div[3]/span').click()
                    save_confirm_button = driver.find_element_by_xpath('//*[@id="fileTreeDialog"]/div[4]/a[2]')
                else:
                    save_confirm_button = driver.find_element_by_xpath('//*[@id="fileTreeDialog"]/div[3]/a[2]')
                save_confirm_button.click()
                time.sleep(2)
                try:
                    if "成功" in driver.find_element_by_xpath('/html/body/div[5]/div/span[2]').text:
                        print("成功")
                    else:
                        print('失败')
                except Exception as e:
                    print("失败或未知错误", e)


if __name__ == '__main__':
    try:
        options = webdriver.ChromeOptions()
        # options.binary_location = '/Applications/Google Chrome'
        # options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()

        driver.get("https://pan.baidu.com/")
        # cookies = literal_eval(input("输入现有的百度网盘 cookies:\n") or "[0]")
        cookies = [{'domain': '.pan.baidu.com', 'expiry': 1567779220, 'httpOnly': False, 'name': 'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1536212067'}, {'domain': '.baidu.com', 'expiry': 1567748044.311379, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': True, 'value': 'AAEB9E494C663DF7809919A066B10010:FG=1'}, {'domain': '.pan.baidu.com', 'expiry': 1538835001.961357, 'httpOnly': False, 'name': 'BDCLND', 'path': '/', 'secure': False, 'value': 'SvIY56yBxhZbYv6Be7o2u9XnSryqB8V6t1dTSq5qyYM%3D'}, {'domain': '.baidu.com', 'expiry': 1795412064.801408, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': True, 'value': '1pdW5yeWZEVURVUy1KaWM0V0N-bVBHS1hvbEoxdFZ6VkJBcVowWnIteGdTYmhiQVFBQUFBJCQAAAAAAAAAAAEAAAAnc8amvMXM~UNOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGC8kFtgvJBbVC'}, {'domain': '.pan.baidu.com', 'expiry': 1538804066.095932, 'httpOnly': True, 'name': 'SCRC', 'path': '/', 'secure': True, 'value': '3762581b6ee064091095b955aa6e6b32'}, {'domain': 'pan.baidu.com', 'expiry': 4128212065.878977, 'httpOnly': False, 'name': 'pan_login_way', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.baidu.com', 'expiry': 1537107222, 'httpOnly': False, 'name': 'cflag', 'path': '/', 'secure': False, 'value': '15%3A3'}, {'domain': '.pan.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'path': '/', 'secure': False, 'value': '1536243220'}, {'domain': '.pan.baidu.com', 'expiry': 1567748065.966557, 'httpOnly': False, 'name': 'PANWEB', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.pan.baidu.com', 'expiry': 1538804066.095976, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': True, 'value': '1471b7e5eca709a0b4bfd0eb946eb03b4f359ef35320278cdb7e38979e23d852'}, {'domain': '.pan.baidu.com', 'expiry': 1536329622.173922, 'httpOnly': True, 'name': 'PANPSC', 'path': '/', 'secure': False, 'value': '13843120556196238077%3Au2C8FyuEb6irUYYZF9XxLen90oj%2BY%2FIs2NEnrqrLiykD2mOuWxR6GvFMne%2FXPWb6eJst8Txon9PCCcggVYLDBIB1mPC8kVmTlANdbjVx0gaCzr5I%2F7Ky%2BF5zx1fkxHzFOmqbmeevRtYDzLGxCF9yjchTKu%2BdwTb%2Fnr9yQoCeHI88g1PcRcrciMZ09rQO2Yg1vdvDG1Aevkc%3D'}]

        if len(cookies) < 2:
            login_name = input('请输入你的登录账号:\n')
            login_passwd = input('请输入你的登录密码:\n')
            cookies = baidu_login(login_name, login_passwd)
        for c in cookies:
            driver.add_cookie(c)
        driver.refresh()
        # 完成登录操作
        baidupan_resave()
        driver.close()
    except Exception as err:
        print('主程序错误:', err)
