import requests
import json

POE_LEAGUE = 'Harvest'
POENINJA_URL_LIST = {
    'Currency': {
        'url': 'https://poe.ninja/api/data/currencyoverview',
        'type': 'Currency'
    },
    'Fragments': {
        'url': 'https://poe.ninja/api/data/currencyoverview',
        'type': 'Fragment'
    },
    'Incubators': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Incubator'
    },
    'Scarabs': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Scarab'
    },
    'Fossils': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Fossil'
    },
    'Resonators': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Resonator'
    },
    'Essences': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Essence'
    },
    'DivinationCards': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'DivinationCard'
    },
    'Prophecies': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Prophecy'
    },
    'SkillGems': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'SkillGem'
    },
    # Takes EXTREMELY long to download!
    # 'BaseTypes': {
    # 'url': 'https://poe.ninja/api/data/itemoverview',
    # 'type': 'BaseType'
    # },
    'HelmetEnchants': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'HelmetEnchant'
    },
    'UniqueMaps': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueMap'
    },
    'Maps': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Map'
    },
    'UniqueJewels': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueJewel'
    },
    'UniqueFlasks': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueFlask'
    },
    'UniqueWeapons': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueWeapon'
    },
    'UniqueArmour': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueArmour'
    },
    'UniqueAccesories': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'UniqueAccessory'
    },
    'Beasts': {
        'url': 'https://poe.ninja/api/data/itemoverview',
        'type': 'Beast'
    }
}


def get_item_name(item_json):
    try:
        return item_json['name']
    except KeyError:
        return item_json['currencyTypeName']


def get_item_chaos_value(item_json):
    try:
        return item_json['chaosValue']
    except KeyError:
        return item_json['chaosEquivalent']


def parse_category(json_data):
    category_data = {}
    for item in json_data['lines']:
        itemname = get_item_name(item)
        category_data[itemname] = {}
        # Add stuff you want to have parsed HERE!
        category_data[itemname]['value'] = get_item_chaos_value(item)

    return category_data


def load_category(category_name):
    request_arguments = {'league': POE_LEAGUE,
                         'type': POENINJA_URL_LIST[category_name]['type'],
                         'language': 'en'}
    data_request = requests.get(
        POENINJA_URL_LIST[category_name]['url'], params=request_arguments)

    return parse_category(json.loads(data_request.text))


def load_all_categories():
    category_data = {}

    for category_name in get_category_list():
        print('Downloading and parsing {0}'.format(category_name))
        category_data[category_name] = load_category(category_name)

    return category_data


def get_category_list():
    return [name for name in POENINJA_URL_LIST]


def get_league():
    return POE_LEAGUE
