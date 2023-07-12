import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

def get_language_id():
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2**16 - 1)
    lid_hex = hex(lid)
    
    # Mapping of language IDs to POSIX format
    posix_map = {
        '0x401': 'ar_SA',
        '0x402': 'bg_BG',
        '0x403': 'ca_ES',
        '0x404': 'zh_TW',
        '0x405': 'cs_CZ',
        '0x406': 'da_DK',
        '0x407': 'de_DE',
        '0x409': 'en_US',
        '0x40a': 'es_ES',
        '0x40b': 'fi_FI',
        '0x40c': 'fr_FR',
        '0x40d': 'he_IL',
        '0x40e': 'hu_HU',
        '0x40f': 'is_IS',
        '0x410': 'it_IT',
        '0x411': 'ja_JP',
        '0x412': 'ko_KR',
        '0x413': 'nl_NL',
        '0x414': 'no_NO',
        '0x415': 'pl_PL',
        '0x416': 'pt_BR',
        '0x417': 'rm_CH',
        '0x418': 'ro_RO',
        '0x419': 'ru_RU',
        '0x41a': 'hr_HR',
        '0x41b': 'sk_SK',
        '0x41c': 'sq_AL',
        '0x41d': 'sv_SE',
        '0x41e': 'th_TH',
        '0x41f': 'tr_TR',
        '0x420': 'ur_PK',
        '0x421': 'id_ID',
        '0x422': 'uk_UA',
        '0x423': 'be_BY',
        '0x424': 'sl_SI',
        '0x425': 'et_EE',
        '0x426': 'lv_LV',
        '0x427': 'lt_LT',
        '0x428': 'tg_TJ',
        '0x429': 'fa_IR',
        '0x42a': 'vi_VN',
        '0x42b': 'hy_AM',
        '0x42c': 'az_AZ',
        '0x42d': 'eu_ES',
        '0x42e': 'hsb_DE',
        '0x42f': 'mk_MK',
        '0x430': 'st_ZA',
        '0x431': 'ts_ZA',
        '0x432': 'tn_ZA',
        '0x433': 've_ZA',
        '0x434': 'xh_ZA',
        '0x435': 'zu_ZA',
        '0x436': 'af_ZA',
        '0x809': 'en_UK'
    }
    
    return posix_map.get(lid_hex, 'Unknown')
