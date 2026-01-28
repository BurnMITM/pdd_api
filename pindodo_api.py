'''📥 Dictionary:
{
    "app_version" = "7.92.0";
    "battery_level" = "1.000000";
    "battery_status" = 3;
    blue = 1;
    "bundle_id" = "com.xunmeng.pinduoduo";
    "connect_type" = 1;
    "cpu_core" = 2;
    "cpu_type" = "ARM 64";
    "device_name" = "iPhone8,1";
    "gps_enable" = 1;
    idfa = "00000000-0000-0000-0000-000000000000";
    idfv = "490CE7EA-E04C-4521-81F6-B7FB03E29B75";
    "kernel_version" = "Darwin Kernel Version 20.5.0: Sat May  8 02:21:41 PDT 2021; root:xnu-7195.122.1~4/RELEASE_ARM64_S8000";
    "localized_model" = iPhone;
    "mcc_v2" = 250;
    "mnc_v2" = 01;
    "network_type_v2" = Wifi;
    "operate_time" = "242962.3534335417";
    os = iOS;
    "os_version" = "14.6";
    "random_number" = 1098961396846308781;
    sc = "667,375";
    "server_time" = 1769402481241;
    "user_phone_name" = iPhone;
    uuid = "8C616E49-E777-4FEB-92B3-078001966D9A";
}
📤 Token object: NSConcreteMutableData
📤 Token NSData length: 360
            0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
13f049020  03 02 7b 00 62 01 04 00 01 13 01 32 18 00 01 05  ..{.b......2....
13f049030  15 63 6f 6d 2e 78 75 6e 6d 65 6e 67 2e 70 69 6e  .com.xunmeng.pin
13f049040  64 75 6f 64 75 6f 04 00 01 08 01 31 06 00 01 1a  duoduo.....1....
13f049050  03 32 35 30 04 00 01 14 01 33 0b 00 01 07 08 f7  .250.....3......
13f049060  f6 d4 d3 92 a8 0d 41 09 00 01 0a 06 37 2e 39 32  ......A.....7.92
13f049070  2e 30 04 00 01 0d 01 31 09 00 01 11 06 69 50 68  .0.....1.....iPh
13f049080  6f 6e 65 0c 00 01 0f 09 69 50 68 6f 6e 65 38 2c  one.....iPhone8,
13f049090  31 23 00 01 04 20 38 43 36 31 36 45 34 39 45 37  1#... 8C616E49E7
13f0490a0  37 37 34 46 45 42 39 32 42 33 30 37 38 30 30 31  774FEB92B3078001
13f0490b0  39 36 36 44 39 41 09 00 01 10 06 69 50 68 6f 6e  966D9A.....iPhon
13f0490c0  65 09 00 01 16 06 41 52 4d 20 36 34 07 00 01 1c  e.....ARM 64....
13f0490d0  04 57 69 66 69 06 00 01 09 03 69 4f 53 0b 00 01  .Wifi.....iOS...
13f0490e0  19 08 ff ff ff ff ff ff ff 7f 0b 00 01 15 08 31  ...............1
13f0490f0  2e 30 30 30 30 30 30 04 00 01 0b 01 31 0b 00 01  .000000.....1...
13f049100  18 08 59 3a 9b f8 9b 01 00 00 23 00 01 02 20 34  ..Y:......#... 4
13f049110  39 30 43 45 37 45 41 45 30 34 43 34 35 32 31 38  90CE7EAE04C45218
13f049120  31 46 36 42 37 46 42 30 33 45 32 39 42 37 35 05  1F6B7FB03E29B75.
13f049130  00 01 1b 02 30 31 07 00 01 0e 04 31 34 2e 36 0a  ....01.....14.6.
13f049140  00 01 12 07 36 36 37 2c 33 37 35 16 00 01 01 13  ....667,375.....
13f049150  32 30 2e 35 2e 30 2d 37 31 39 35 2e 31 32 32 2e  20.5.0-7195.122.
13f049160  31 7e 34 23 00 01 03 20 30 30 30 30 30 30 30 30  1~4#... 00000000
13f049170  30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30  0000000000000000
13f049180  30 30 30 30 30 30 30 30                          00000000

'''

import json
import os
import random
import secrets
import string
import struct
import subprocess
import time
import uuid

import requests
from Crypto.PublicKey import RSA
from curl_cffi import Session
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import gzip
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import get_random_bytes
from rnet import Client, Emulation


proxies = {
    'https': f'http://vLdevPAxEa:jCI75hGHnv@65.108.12.231:5002',
}


class CountryCodes:
    RU = 191000000


class PddApi:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ===  iOS/14.6 Model/iPhone8,1 BundleID/com.xunmeng.pinduoduo AppVersion/7.93.0 AppBuild/202601251202 pversion/2917'
        self.rctk_plat = "com.xunmeng.pinduoduo.ios"
        self.rctk_ver = "7.93.0"
        self.pdd_config = "V4:002.079300"
        self.ses = Session(proxies=proxies, timeout=10, ja3="771,4865-4866-4867-49196-49195-52393-49200-49199-52392-49188-49187-49162-49161-49192-49191-49172-49171-157-156-61-60-53-47-49160-49170-10,0-23-65281-10-11-16-5-13-18-51-45-43-21,29-23-24-25,0")
        self.app_version = "7.93.0"
        self.os_version = "14.6"
        self.bundle_id = "com.xunmeng.pinduoduo"
        self.total_capacity = "31978983424"
        self.uuid = str(uuid.uuid4()).upper() # device_id
        self.user_phone_name = "iPhone"
        self.idfa = "00000000-0000-0000-0000-000000000000"
        self.idfv = str(uuid.uuid4()).upper() # Меняется после переустановки
        self.etag = self.generate_random_string(8)
        self.etag = "HnfIQMVP"

        self.x_pdd_info = "tz%3DAsia%2FKrasnoyarsk%26pzvonm%3D0" # tz%3DAsia%2FKrasnoyarsk%26pzvonm%3D8 tz%3DAsia%2FBangkok%26pzvonm%3D8
        self.lat = "NLDEIQLNYEKTKGOHXDM7QDMHUHBBQQ34KOWFARYKS2EDOJW2S46A12042a1"  # Нужно понять алгоритм
        self.p_appname = "pinduoduo"
        self.build_no = '202601181454'

    @staticmethod
    def generate_random_string(len) -> str:
        alphabet = string.ascii_letters
        return''.join(secrets.choice(alphabet) for _ in range(len))

    def generate_public_key(self):
        n_hex = 'c21da1b2c66236e7cadcf82c04b3dd18a41fa9fe99e23388de4ab46636e4dd0296725d0a699e58544fddddcf251986230d03d7451a25eb5c6232c904cdc7bb6e4cb9f18126fb6e83f1a59b5da14917838e82938e71088c68356ea062a73d83ee44db698fa6cab356e0881d68b13aa8f87543f0d721cdd9b687a0175ee030479b'

        n = int(n_hex, 16)
        e = 65537

        key = RSA.construct((n, e))
        print(key.export_key().decode())
        return key.export_key().decode()

    def get_finger_print(self):
        '''key - Random 16 bytes -> RSA(AES-key).to_base64
           data(type-gzip) - AES(data_gzip).mode(CBC).IV(16*0x0)
        '''
        aes_key = get_random_bytes(16)  # AES-128
        print(aes_key.hex())
        n_hex = "c21da1b2c66236e7cadcf82c04b3dd18a41fa9fe99e23388de4ab46636e4dd0296725d0a699e58544fddddcf251986230d03d7451a25eb5c6232c904cdc7bb6e4cb9f18126fb6e83f1a59b5da14917838e82938e71088c68356ea062a73d83ee44db698fa6cab356e0881d68b13aa8f87543f0d721cdd9b687a0175ee030479b"
        n = int(n_hex, 16)
        e = 65537
        pub = RSA.construct((n, e))
        rsa_pub = pub.public_key()
        rsa_cipher = PKCS1_v1_5.new(rsa_pub)
        encrypted_key = rsa_cipher.encrypt(aes_key)

        key_b64 = base64.b64encode(encrypted_key).decode()

        plaintext = '{"app_version":"'+self.app_version+'","os_version":"'+self.os_version+'","bundle_id":"'+self.bundle_id+'","mcc":"","operate_time":"242970.5807253334","location":{},"total_capacity":"'+self.total_capacity+'","network_type":"","mcc_v2":"250","gps_enable":"1","cpu_usage":0.14981653168797493,"kernel_version":"Darwin Kernel Version 20.5.0: Sat May  8 02:21:41 PDT 2021; root:xnu-7195.122.1~4\/RELEASE_ARM64_S8000","uuid":"'+self.uuid+'","total_memory":"2107686912","user_phone_name":"'+self.user_phone_name+'","boot_time":"1769158146.280894","available_memory":"63422464","cpu_type":"ARM 64","mnc":"","per_cpu_usage":[0.088067561388015747,0.061748970299959183],"idfa":"'+self.idfa+'","current_time":"'+f"{time.time():.6f}"+'","idfv":"'+self.idfv+'","wifi":{"name":"","ip":"192.168.1.10","netmask":"255.255.255.0"},"connect_type":"1","mnc_v2":"01","os":"iOS","available_capacity":"17293484032","network_type_v2":"Wifi","localized_model":"iPhone","blue":"1","screen_brightness":"'+str(random.uniform(0.2, 0.8))[:18]+'","battery_level":"1.000000","cpu_core":2,"battery_status":"3","device_name":"iPhone8,1","sc":"667,375"}'

        gzipped = gzip.compress(plaintext.encode())
        iv = b"\x00" * 16

        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(gzipped, 16))

        data_b64 = base64.b64encode(ciphertext).decode()

        return key_b64, data_b64

    def get_short_anti_token(self):
        '''id __cdecl -[PDDRiskTokenManager getShortRiskToken](PDDRiskTokenManager *self, SEL a2)
        ========== [parametersWithParams:] ==========
📦 Params NSDictionary:
  pdd_id = HnfIQMVP
  device_id = 8C616E49-E777-4FEB-92B3-078001966D9A
  random_number = 65481310359585575
  keychain_id = 261F4AFE-564A-4585-8BA1-CFE93492D894
  server_time = 1769573816485
🧬 Risk NSData length: 66
🧬 Risk NSData HEX:
00000000  08 fc 48 6e 66 49 51 4d 56 50 a5 98 d1 02 9c 01  ..HnfIQMVP......
00000010  00 00 27 03 69 a3 e7 a2 e8 00 00 d8 3f c3 ef 8b  ..'.i.......?...
00000020  aa cc 26 1f 4a fe 56 4a 45 85 8b a1 cf e9 34 92  ..&.J.VJE.....4.
00000030  d8 94 39 09 5d 24 ec 4b 4e 2b bf 4c 76 89 b3 49  ..9.]$.KN+.Lv..I
00000040  f2 1c                                            ..
============================================
        '''
        n = int(time.time() * 1000)

        server_time = n.to_bytes(8, "little")

        n = random.randint(10481310359585575, 95481310359585575)
        random_number = n.to_bytes(8, "little")

        hex_dump = f"""08fc{self.etag.encode().hex()}{server_time.hex()}{random_number.hex()}00d83fc3ef8baacc261f4afe564a45858ba1cfe93492d8948f20b16a91d14719bc38ea2ba3107bad"""
        # print(hex_dump)
        # hex_dump = f'08fc486e6649514d5650{server_time.hex()}ffffffffffffff7f00d83fc3ef8baacc261f4afe564a45858ba1cfe93492d89439095d24ec4b4e2bbf4c7689b349f21c'
        raw = bytes.fromhex(hex_dump)

        # === CONFIG ===
        KEY = b"_pdd_anti_token_"  # 16 bytes
        IV = b"\x00" * 16  # zero IV (CBC)
        BLOCK_SIZE = 16

        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted = cipher.encrypt(pad(raw, BLOCK_SIZE))

        # === STEP 4: base64 ===
        token = base64.b64encode(encrypted).decode()

        print(token)
        return token

    def get_anti_token(self):
        '''0b        -> field id
            00 01     -> length = 1
            07        -> value = 7  (тип / версия / subtype)
            08        -> NEXT field id
            f7 f6 d4 d3 92 a8 0d 41  (8 байт)
'''
        struct.unpack("<d", bytes.fromhex("f7 f6 d4 d3 92 a8 0d 41")) # "operate_time"
        value = 242962.3534335420
        operate_time = struct.pack("<d", value)

        # b = bytes.fromhex("59 3a 9b f8 9b 01 00 00") #server_time
        # int.from_bytes(b, "little")

        n = int(time.time() * 1000)

        server_time = n.to_bytes(8, "little")

        # === CONFIG ===
        KEY = b"_pdd_anti_token_"  # 16 bytes
        IV = b"\x00" * 16  # zero IV (CBC)
        BLOCK_SIZE = 16

        # === RAW HEX DUMP ===
        hex_dump = f"""03027b0062010400011301321800010515636f6d2e78756e6d656e672e70696e64756f64756f0400010801310600011a033235300400011401330b00010708{operate_time.hex()}0900010a06372e39322e300400010d013109000111066950686f6e650c00010f096950686f6e65382c312300010420{self.uuid.replace('-', '').encode().hex()}09000110066950686f6e65090001160641524d2036340700011c04576966690600010903694f530b00011908{get_random_bytes(8).hex()}0b00011508312e3030303030300400010b01310b00011808{server_time.hex()}2300010220{self.idfv.replace('-', '').encode().hex()}0500011b0230310700010e0431342e360a000112073636372c333735160001011332302e352e302d373139352e3132322e317e3423000103203030303030303030303030303030303030303030303030303030303030303030"""
        print(hex_dump)
        # === STEP 1: hex → bytes ===
        raw = bytes.fromhex(hex_dump)

        # === STEP 2: gzip ===
        gzipped = gzip.compress(raw)

        # === STEP 3: AES-128-CBC ===
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        encrypted = cipher.encrypt(pad(gzipped, BLOCK_SIZE))

        # === STEP 4: base64 ===
        token = base64.b64encode(encrypted).decode()

        print(token)
        return token

    def get_pdd_queries(self):
        return 'width=750.000000&height=1334.000000&brand=apple&model=iPhone 6s&osv=14.6&appv=7.93.0&pl=iOS&net=-1&dpr=2.000000'
        # v2(с vpn включённым) return f'width=750.000000&height=1334.000000&brand=apple&model=iPhone 6s&osv=14.6&appv={self.app_version}&pl=iOS&net=1&dpr=2.000000'

    def get_rctk_sign(self, input_string):
        """Hash input string using custom_sha256 binary."""
        b64_input = base64.b64encode(input_string.strip().encode()).decode()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        binary_path = os.path.join(script_dir, 'custom_sha256')

        result = subprocess.run(
            [binary_path, b64_input],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"custom_sha256 failed: {result.stderr}")

        return result.stdout.strip()

    def send_sms(self, phone: str, country_id: CountryCodes, tel_code: int):
        key, data = self.get_finger_print()
        rctk = f'rctk_plat={self.rctk_plat}&rctk_ver={self.rctk_ver}&rctk_ts={int(time.time() * 1000)}&rctk_nonce={str(uuid.uuid4()).upper().replace("-", "")}&rctk_rpkg=0'
        data_sign = '&rctk_ak=logout&rctk_path=/api/sigerus/mobile/code/request&rctk_post={"mobile":"'+phone+'","tel_code":'+str(tel_code)+',"country_id":'+str(country_id)+',"fingerprint":"{\"key\":\"'+key+'\",\"data\":\"'+data+'\"}"}'
        headers = {
            'Host': 'api.pinduoduo.com',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU;q=1',
            'Content-Type': 'application/json',
            'Etag': self.etag,
            'Pdd-Config': self.pdd_config,
            'User-Agent': self.user_agent,
            'X-Pdd-Queries': self.get_pdd_queries(),
            'Anti-Token': f'1ab{self.get_anti_token()}',
            'Lat': self.lat,
            'Multi-Set': '1,1,100000107',
            'P-Appname': self.p_appname,
            'P-Proc-Time': '65614',
            'Rctk': rctk,
            'Rctk-Sign': self.get_rctk_sign(f'{rctk}{data_sign}'),
            'X-App-Lang': 'en',
            'X-App-Ui': 'zm%3D0%26dm%3D0',
            'X-B3-Ptracer': str(os.urandom(16).hex().upper()),
            'X-P-T': 't=1&x-p1-t=1',
            'X-P1': 'MDQwMTAyc2lNemlTenUtWDNWYS0zdkJRLTY4M2UtOWw5UXlBb1hJRTVEKRUSr5UmM8DCBafqHwGSEShtTkA9BdE8goimGKArXowjrVd9nCcIXIVaX/B+qQyGWaRzCWQBKdpCH7F9u+GJUX5+pskyFuCZQV0=',
            'X-Pdd-Info': self.x_pdd_info,
        }

        data = '{"mobile":"'+str(phone)+'","tel_code":'+str(tel_code)+',"country_id":'+str(country_id)+',"fingerprint":"{\\"key\\":\\"'+key+'\\",\\"data\\":\\"'+data+'\\"}"}'
        print(data)
        response = self.ses.post(
            'https://api.pinduoduo.com/api/sigerus/mobile/code/request',
            headers=headers,
            data=data,
        )
        print(response.text)

    def render(self):
        cookies = {
            'acid': '15f10b0145309c20630607bbf7aab04b',
            'api_uid': 'ChB6PmlrL8QYMQBoo0oeAg==',
        }

        headers = {
            'Host': 'api.pinduoduo.com',
            'Etag': 'PwBVTdGn',
            'Accesstoken': '4HYFODWFDLAFGGKJY37STRPUWZBMRIJYULZ7ARRETQW66CY57TQA122e86e',
            'Referer': 'Android',
            # 'Verifyauthtoken': '4IRJiueP0zZbb6aVeS0C_g8b7cf7979675ea538',
            'P-Appname': 'pinduoduo',
            'P-Proc-Time': '310379',
            'X-Pdd-Info': 'bold_free%3Dfalse%26bold_product%3D%26front%3D1%26tz%3DAsia%2FDhaka',
            'X-Pdd-Queries': 'width=1080&height=2131&net=1&brand=xiaomi&model=Redmi+Note+5a&osv=9&appv=7.89.0&pl=2',
            'X-Yak-Llt': '1768633208167',
            'Accept-Language': 'ru-RU',
            'X-App-Lang': 'en',
            'X-App-Ui': 'dm%3D0%26zm%3D0',
            'P-Proc': 'main',
            'P-Mediainfo': 'player=2.1.0&rtc=1.0.0',
            'X-B3-Ptracer': 'hctrue88eb46fd647242a4824161035c',
            'User-Agent': 'android Mozilla/5.0 (Linux; Android 11; Redmi Note 5A Build/RSR1.210722.013.A6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36  phh_android_version/7.89.0 phh_android_build/0f3ab7e3622f0058ae9ee34638bc907fa61379a4 phh_android_channel/sx pversion/0',
            'Pdd-Config': 'V4:001.078900',
            'Multi-Set': '1,1,100000824',
            'Content-Type': 'application/json;charset=UTF-8',
            # 'Content-Length': '1004',
            # 'Accept-Encoding': 'gzip, deflate',
            'Anti-Token': '2agvAxuty/ksTYJPge5/OxFMrsjaYCfTfPUJFa5o1oJjJARHE39S8aczesOE6lNwOTppvmBCT6nEoeT5ZppOzBOZg==',
            'Vip': '49.51.130.105',
            # 'Cookie': 'acid=15f10b0145309c20630607bbf7aab04b; api_uid=ChB6PmlrL8QYMQBoo0oeAg==',
        }

        params = {
            'pdduid': '5561402267548',
        }

        json_data = {"address_list":[],"page_sn":"10014","page_id":"10014_1769065576310_1893332732","goods_id":"890703028231","phone_model":"Redmi Note 5A","page_from":"35","page_version":"7","client_time":"1769065576409","refer_page_sn":"10002","refer_page_el_sn":"99862","pic_w":0,"pic_h":0,"has_pic_url":1,"extend_map":{},"_oak_gallery_token":"98f1e2b06a84a8247e6f4d1d2fd264a1","_oak_gallery":"https:\/\/img.pddpic.com\/mms-material-img\/2025-01-14\/0096d875-3c4f-402f-b15a-588bbcc51284.jpeg","_oak_rcto":"YWI68amo1gR3Kc7cnqF2ACqTzeNB3yJjQWb3iSrTsNPiwhsm4BjYhSTE","union_pay_installed":False,"client_lab":{"mall_h5_url_preload_enable":"1"},"is_sys_minor":0,"system_language":"en","cached_templates":["8b15b1bcedb124632496c7410ffc2f23","22cec5f5d74cdd847a1f16d583344546","879fe7129789509ef022725b24721377","014f83c57174bbc87bd3d1c3eedc79af","c6601a67445f298e62a16bb4073a1c98","5c958222f753308d54596431e4881ccf"],"impr_tips":[],"screen_height":866,"screen_width":411,"goods_detail_support_zoom":"true","pdd_goods_detail_dark_color_enable":True}

        response = self.ses.post(
            'https://api.pinduoduo.com/api/oak/integration/render',
            params=params,
            # cookies=cookies,
            headers=headers,
            json=json_data,

        )
        print(response.text)

    def get_user_info(self, token):
        headers = {
            'Host': 'api.pinduoduo.com',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU;q=1',
            'Accesstoken': 'UFU3VUD3OPSDBIWDYGTBIZWC3JZNGNWOYUPGQM3SYVI2RWJMWXOQ120ac59',
            'Etag': 'HnfIQMVP',
            'Pdd-Config': 'V4:002.079200',
            'User-Agent': self.user_agent,
            'X-Pdd-Queries': 'width=750.000000&height=1334.000000&brand=apple&model=iPhone 6s&osv=14.6&appv=7.92.0&pl=iOS&net=1&dpr=2.000000',
            # 'Accept-Encoding': 'gzip, deflate',
            'Anti-Token': f'1ab{token}',
            'Lat': 'UFU3VUD3OPSDBIWDYGTBIZWC3JZNGNWOYUPGQM3SYVI2RWJMWXOQ120ac59',
            'Multi-Set': '1,1,100000107',
            'P-Appname': 'pinduoduo',
            'P-Proc-Time': '790628',
            'Rctk': f'rctk_plat={self.rctk_plat}&rctk_ver={self.rctk_ver}&rctk_ts={self.rctk_ts}&rctk_nonce=3AEF6DBB55304B6E95358F8780B4082D&rctk_rpkg=0',
            # 'Rctk-Sign': '7lj0ZaUkG3PWPITgRt0ULvQnG1Ui5hmHYaTWynp73Iw=',
            'X-App-Lang': 'en',
            'X-App-Ui': 'zm%3D0%26dm%3D0',
            'X-B3-Ptracer': str(os.urandom(16).hex().upper()),
            'X-Pdd-Info': 'tz%3DAsia%2FKrasnoyarsk%26pzvonm%3D8%266cpi%3DMmEwMDoxZmEyOjg0MTI6ZjVmZDo1MTo4Yzg6MmJiZDo3ZmI4',
            'X-Yak-Llt': '1769159501000',
            # 'Cookie': 'api_uid=CiPgl2lzOK1zhQDSMAO2Ag==',
        }

        params = {
            'config_mode': '1',
            'pdduid': '3731002441900',
        }

        response = self.ses.get(
            'https://api.pinduoduo.com/api/apollo/user/personal/profile',
            params=params,
            headers=headers,
        )
        print(response.text)

    def bd_query(self):
        headers = {
            'Host': 'meta.pinduoduo.com',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'User-Agent': self.user_agent,
            'Accept-Language': 'ru',
        }

        json_data = {
            'appid': 'com.xunmeng.pinduoduo',
            'network': 'unknow',
            'internal_no': int(time.time() * 1000),
            'version': self.app_version,
            'sub_type': 'main',
            'channel': 'app store',
            'screen': '375x667',
            'brand': 'apple',
            'arch_type': 'ARM64',
            'patch_version': 0,
            'platform': 'iOS',
            'device_id': self.etag,
            'build_no': self.build_no,
            'model': 'iPhone8,1',
            'os_version': '14.6',
            'env': 'prod',
        }
        count = 0
        while count < 3:
            try:
                response = self.ses.post('https://meta.pinduoduo.com/api/app/v1/bd/query', headers=headers, json=json_data)
                print(response.text)
                return
            except Exception as e:
                count += 1
                print(f"Error bd_query {e}")

    def query_personal(self):
        rctk = f'rctk_plat={self.rctk_plat}&rctk_ver={self.rctk_ver}&rctk_ts={int(time.time() * 1000)}&rctk_nonce={str(uuid.uuid4()).upper().replace("-", "")}&rctk_rpkg=0'
        data_sign = '&rctk_ak=logout&rctk_path=/api/caterham/v3/query/personal&rctk_post=&count=20&dark_mode=0&engine_version=2.0&is_pull_down=1&list_id=1430957161&offset=0&page_el_sn=99084&page_id=personal.html&page_sn=10001&req_action_type=6&req_list_action_type=6'
        headers = {
            'Host': 'api.pinduoduo.com',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU;q=1',
            'Etag': self.etag,
            'Pdd-Config': self.pdd_config,
            'User-Agent': self.user_agent,
            'X-Pdd-Queries': self.get_pdd_queries(),
            'Anti-Token': f'1ac{self.get_short_anti_token()}',
            'Lat': self.lat,
            'Multi-Set': '1,1,100000176',
            'P-Appname': self.p_appname,
            'P-Proc-Time': '39975',
            'Rctk': rctk,
            'Rctk-Sign': self.get_rctk_sign(f'{rctk}{data_sign}'),
            'X-App-Lang': 'en',
            'X-App-Ui': 'zm%3D0%26dm%3D0',
            'X-B3-Ptracer': str(os.urandom(16).hex().upper()),
            'X-Pdd-Info': self.x_pdd_info,
        }

        count = 0
        while count < 3:
            try:
                response = self.ses.get(
                    'https://api.pinduoduo.com/api/caterham/v3/query/personal?offset=0&dark_mode=0&req_action_type=6&is_pull_down=1&list_id=1430957161&page_id=personal.html&count=20&req_list_action_type=6&page_sn=10001&engine_version=2.0&page_el_sn=99084',
                    headers=headers,
                )
                print(response.text)
                return
            except Exception as e:
                count += 1
                print(f"Error query personal {e}")

    def ip_galen(self):
        """Если возвращает "result":true, то нас не детектят, возвращает информацию об стране по ip для авторизации"""
        rctk = f'rctk_plat={self.rctk_plat}&rctk_ver={self.rctk_ver}&rctk_ts={int(time.time() * 1000)}&rctk_nonce={str(uuid.uuid4()).upper().replace("-", "")}&rctk_rpkg=0'
        data_sign = '&rctk_ak=logout&rctk_path=/api/galen/grayscale&rctk_post={"scene":"LOGIN","gray_type":2,"ip_type":1}'
        headers = {
            'Host': 'api.pinduoduo.com',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU;q=1',
            'Content-Type': 'application/json',
            'Etag': self.etag,
            'Pdd-Config': self.pdd_config,
            'User-Agent': self.user_agent,
            'X-Pdd-Queries': self.get_pdd_queries(),
            'Anti-Token': f'1ac{self.get_short_anti_token()}',
            'Lat': self.lat,
            'Multi-Set': '1,1,100000824',
            'P-Appname': self.p_appname,
            'P-Proc-Time': '2159135',
            'Rctk': rctk,
            'Rctk-Sign': self.get_rctk_sign(f'{rctk}{data_sign}'),
            'X-App-Lang': 'en',
            'X-App-Ui': 'zm%3D0%26dm%3D0',
            'X-B3-Ptracer': str(uuid.uuid4()).upper().replace("-", ""),
            'X-Pdd-Info': self.x_pdd_info,
        }

        json_data = {
            'scene': 'LOGIN',
            'gray_type': 2,
            'ip_type': 1,
        }

        response = self.ses.post(
            'https://api.pinduoduo.com/api/galen/grayscale',
            headers=headers,
            json=json_data,
        )
        print(response.text)

    def polemon_gbdbpdc(self):
        """Этот запрос показывает, детектят ли нас
        Детектят - {"access_array":"1","extra_array":"4,5","tip1":"","tip2":"","text":"dwfca","history":false,"degrade":false,"extra_array_style":1}
        Не детектят - {"access_array":"8,9,3,1","extra_array":"4,7","tip1":"","tip2":"","text":"wkdkb","history":false,"degrade":false,"extra_array_style":1}

        Этот запрос возвращает какие авторизации нам доступны
        """

        rctk = f'rctk_plat={self.rctk_plat}&rctk_ver={self.rctk_ver}&rctk_ts={int(time.time() * 1000)}&rctk_nonce={str(uuid.uuid4()).upper().replace("-", "")}&rctk_rpkg=0'
        data_sign = '&rctk_ak=logout&rctk_path=/api/polemon/gbdbpdc&rctk_post={"extra_info":0}'
        headers = {
            'Host': 'api.pinduoduo.com',
            'Accept': '*/*',
            'Accept-Language': 'ru-RU;q=1',
            'Content-Type': 'application/json',
            'Etag': self.etag,
            'Pdd-Config': self.pdd_config,
            'User-Agent': self.user_agent,
            'X-Pdd-Queries': self.get_pdd_queries(),
            'Anti-Token': f'1ac{self.get_short_anti_token()}',
            'Lat': self.lat,
            'Multi-Set': '1,1,100000107',
            'P-Appname': self.p_appname,
            'P-Proc-Time': '10775',
            'Rctk': rctk,
            'Rctk-Sign': self.get_rctk_sign(f'{rctk}{data_sign}'),
            'X-App-Lang': 'en',
            'X-App-Ui': 'zm%3D0%26dm%3D0',
            'X-B3-Ptracer': str(uuid.uuid4()).upper().replace("-", ""),
            'X-Pdd-Info': self.x_pdd_info,
        }
        data = '{"extra_info":0}'
        response = self.ses.post(
            'https://api.pinduoduo.com/api/polemon/gbdbpdc',
            headers=headers,
            data=data,
        )
        print(response.text)