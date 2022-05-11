import pytz
from datetime import timedelta
import requests,datetime, json



def coin_data_collect(symbol = 'MANA',market = 'USD',interval='5min'):
    api_key = 'VKYYBU3O19HP6199'

    url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={symbol}&market={market}&interval={interval}&apikey={api_key}'

    r = requests.get(url)
    data_collection = r.json()
    print('data_collection: ', data_collection)
    print('symbol: ', symbol)

    # print(data["Time Series Crypto (5min)"])
    #
    # print(data["Time Series Crypto (5min)"]['2022-04-05 08:05:00']["1. open"])

    with open('full_data.json', 'w') as outfile:
        json.dump(data_collection, outfile)

    data_col = {"open": [], "close": [], "low": [], "high": [], "volume": [], "date": []}

    for index, item in enumerate(data_collection[f"Time Series Crypto ({interval})"]):
        data_col["open"].append(float(data_collection[f"Time Series Crypto ({interval})"][item]["1. open"]))
        data_col["close"].append(float(data_collection[f"Time Series Crypto ({interval})"][item]["4. close"]))
        data_col["high"].append(float(data_collection[f"Time Series Crypto ({interval})"][item]["2. high"]))
        data_col["low"].append(float(data_collection[f"Time Series Crypto ({interval})"][item]["3. low"]))
        data_col["volume"].append(float(data_collection[f"Time Series Crypto ({interval})"][item]["5. volume"]))
        # data_col["date"].append(index * 5)
        data_col["date"].append(datetime.datetime.strptime(item.replace('-','/'),'%Y/%m/%d %H:%M:%S')+timedelta(hours=3))




    return (data_col)


da = coin_data_collect()
print(da)
print('da: ', da['date'])





physical_currency_list={'currency code':['AED',	'AFN',	'ALL',	'AMD',	'ANG',	'AOA',	'ARS',	'AUD',	'AWG',	'AZN',	'BAM',	'BBD',	'BDT',	'BGN',	'BHD',	'BIF',	'BMD',	'BND',	'BOB',	'BRL',	'BSD',	'BTN',	'BWP',	'BZD',	'CAD',	'CDF',	'CHF',	'CLF',	'CLP',	'CNH',	'CNY',	'COP',	'CUP',	'CVE',	'CZK',	'DJF',	'DKK',	'DOP',	'DZD',	'EGP',	'ERN',	'ETB',	'EUR',	'FJD',	'FKP',	'GBP',	'GEL',	'GHS',	'GIP',	'GMD',	'GNF',	'GTQ',	'GYD',	'HKD',	'HNL',	'HRK',	'HTG',	'HUF',	'ICP',	'IDR',	'ILS',	'INR',	'IQD',	'IRR',	'ISK',	'JEP',	'JMD',	'JOD',	'JPY',	'KES',	'KGS',	'KHR',	'KMF',	'KPW',	'KRW',	'KWD',	'KYD',	'KZT',	'LAK',	'LBP',	'LKR',	'LRD',	'LSL',	'LYD',	'MAD',	'MDL',	'MGA',	'MKD',	'MMK',	'MNT',	'MOP',	'MRO',	'MRU',	'MUR',	'MVR',	'MWK',	'MXN',	'MYR',	'MZN',	'NAD',	'NGN',	'NOK',	'NPR',	'NZD',	'OMR',	'PAB',	'PEN',	'PGK',	'PHP',	'PKR',	'PLN',	'PYG',	'QAR',	'RON',	'RSD',	'RUB',	'RUR',	'RWF',	'SAR',	'SBDf',	'SCR',	'SDG',	'SDR',	'SEK',	'SGD',	'SHP',	'SLL',	'SOS',	'SRD',	'SYP',	'SZL',	'THB',	'TJS',	'TMT',	'TND',	'TOP',	'TRY',	'TTD',	'TWD',	'TZS',	'UAH',	'UGX',	'USD',	'UYU',	'UZS',	'VND',	'VUV',	'WST',	'XAF',	'XCD',	'XDR',	'XOF',	'XPF',	'YER',	'ZAR',	'ZMW',	'ZWL'],
'currency name':['United Arab Emirates Dirham',	'Afghan Afghani',	'Albanian Lek',	'Armenian Dram',	'Netherlands Antillean Guilder',	'Angolan Kwanza',	'Argentine Peso',	'Australian Dollar',	'Aruban Florin',	'Azerbaijani Manat',	'Bosnia-Herzegovina Convertible Mark',	'Barbadian Dollar',	'Bangladeshi Taka',	'Bulgarian Lev',	'Bahraini Dinar',	'Burundian Franc',	'Bermudan Dollar',	'Brunei Dollar',	'Bolivian Boliviano',	'Brazilian Real',	'Bahamian Dollar',	'Bhutanese Ngultrum',	'Botswanan Pula',	'Belize Dollar',	'Canadian Dollar',	'Congolese Franc',	'Swiss Franc',	'Chilean Unit of Account UF',	'Chilean Peso',	'Chinese Yuan Offshore',	'Chinese Yuan',	'Colombian Peso',	'Cuban Peso',	'Cape Verdean Escudo',	'Czech Republic Koruna',	'Djiboutian Franc',	'Danish Krone',	'Dominican Peso',	'Algerian Dinar',	'Egyptian Pound',	'Eritrean Nakfa',	'Ethiopian Birr',	'Euro',	'Fijian Dollar',	'Falkland Islands Pound',	'British Pound Sterling',	'Georgian Lari',	'Ghanaian Cedi',	'Gibraltar Pound',	'Gambian Dalasi',	'Guinean Franc',	'Guatemalan Quetzal',	'Guyanaese Dollar',	'Hong Kong Dollar',	'Honduran Lempira',	'Croatian Kuna',	'Haitian Gourde',	'Hungarian Forint',	'Internet Computer',	'Indonesian Rupiah',	'Israeli New Sheqel',	'Indian Rupee',	'Iraqi Dinar',	'Iranian Rial',	'Icelandic Krona',	'Jersey Pound',	'Jamaican Dollar',	'Jordanian Dinar',	'Japanese Yen',	'Kenyan Shilling',	'Kyrgystani Som',	'Cambodian Riel',	'Comorian Franc',	'North Korean Won',	'South Korean Won',	'Kuwaiti Dinar',	'Cayman Islands Dollar',	'Kazakhstani Tenge',	'Laotian Kip',	'Lebanese Pound',	'Sri Lankan Rupee',	'Liberian Dollar',	'Lesotho Loti',	'Libyan Dinar',	'Moroccan Dirham',	'Moldovan Leu',	'Malagasy Ariary',	'Macedonian Denar',	'Myanma Kyat',	'Mongolian Tugrik',	'Macanese Pataca',	'Mauritanian Ouguiya (pre-2018)',	'Mauritanian Ouguiya',	'Mauritian Rupee',	'Maldivian Rufiyaa',	'Malawian Kwacha',	'Mexican Peso',	'Malaysian Ringgit',	'Mozambican Metical',	'Namibian Dollar',	'Nigerian Naira',	'Norwegian Krone',	'Nepalese Rupee',	'New Zealand Dollar',	'Omani Rial',	'Panamanian Balboa',	'Peruvian Nuevo Sol',	'Papua New Guinean Kina',	'Philippine Peso',	'Pakistani Rupee',	'Polish Zloty',	'Paraguayan Guarani',	'Qatari Rial',	'Romanian Leu',	'Serbian Dinar',	'Russian Ruble',	'Old Russian Ruble',	'Rwandan Franc',	'Saudi Riyal',	'Solomon Islands Dollar',	'Seychellois Rupee',	'Sudanese Pound',	'Special Drawing Rights',	'Swedish Krona',	'Singapore Dollar',	'Saint Helena Pound',	'Sierra Leonean Leone',	'Somali Shilling',	'Surinamese Dollar',	'Syrian Pound',	'Swazi Lilangeni',	'Thai Baht',	'Tajikistani Somoni',	'Turkmenistani Manat',	'Tunisian Dinar',	'Tongan Pa\'anga',	'Turkish Lira',	'Trinidad and Tobago Dollar',	'New Taiwan Dollar',	'Tanzanian Shilling',	'Ukrainian Hryvnia',	'Ugandan Shilling',	'United States Dollar',	'Uruguayan Peso',	'Uzbekistan Som',	'Vietnamese Dong',	'Vanuatu Vatu',	'Samoan Tala',	'CFA Franc BEAC',	'East Caribbean Dollar',	'Special Drawing Rights',	'CFA Franc BCEAO',	'CFP Franc',	'Yemeni Rial',	'South African Rand',	'Zambian Kwacha',	'Zimbabwean Dollar']
}
cyropto_currency_list={ 'currency code':['1ST',	'2GIVE',	'808',	'AAVE',	'ABT',	'ABY',	'AC',	'ACT',	'ADA',	'ADT',	'ADX',	'AE',	'AEON',	'AGI',	'AGRS',	'AI',	'AID',	'AION',	'AIR',	'AKY',	'ALGO',	'ALIS',	'AMBER',	'AMP',	'AMPL',	'ANC',	'ANT',	'APPC',	'APX',	'ARDR',	'ARK',	'ARN',	'AST',	'ATB',	'ATM',	'ATOM',	'ATS',	'AUR',	'AVAX',	'AVT',	'B3',	'BAND',	'BAT',	'BAY',	'BBR',	'BCAP',	'BCC',	'BCD',	'BCH',	'BCN',	'BCPT',	'BCX',	'BCY',	'BDL',	'BEE',	'BELA',	'BET',	'BFT',	'BIS',	'BITB',	'BITBTC',	'BITCNY',	'BITEUR',	'BITGOLD',	'BITSILVER',	'BITUSD',	'BIX',	'BLITZ',	'BLK',	'BLN',	'BLOCK',	'BLZ',	'BMC',	'BNB',	'BNT',	'BNTY',	'BOST',	'BOT',	'BQ',	'BRD',	'BRK',	'BRX',	'BSV',	'BTA',	'BTC',	'BTCB',	'BTCD',	'BTCP',	'BTG',	'BTM',	'BTS',	'BTSR',	'BTT',	'BTX',	'BURST',	'BUSD',	'BUZZ',	'BYC',	'BYTOM',	'C20',	'CAKE',	'CANN',	'CAT',	'CCRB',	'CDT',	'CFI',	'CHAT',	'CHIPS',	'CLAM',	'CLOAK',	'CMP',	'CMT',	'CND',	'CNX',	'COFI',	'COMP',	'COSS',	'COVAL',	'CRBIT',	'CREA',	'CREDO',	'CRO',	'CRW',	'CSNO',	'CTR',	'CTXC',	'CURE',	'CVC',	'DAI',	'DAR',	'DASH',	'DATA',	'DAY',	'DBC',	'DBIX',	'DCN',	'DCR',	'DCT',	'DDF',	'DENT',	'DFS',	'DGB',	'DGC',	'DGD',	'DICE',	'DLT',	'DMD',	'DMT',	'DNT',	'DOGE',	'DOPE',	'DOT',	'DRGN',	'DTA',	'DTB',	'DYN',	'EAC',	'EBST',	'EBTC',	'ECC',	'ECN',	'EDG',	'EDO',	'EFL',	'EGC',	'EGLD',	'EKT',	'ELA',	'ELEC',	'ELF',	'ELIX',	'EMB',	'EMC',	'EMC2',	'ENG',	'ENJ',	'ENRG',	'EOS',	'EOT',	'EQT',	'ERC',	'ETC',	'ETH',	'ETHD',	'ETHOS',	'ETN',	'ETP',	'ETT',	'EVE',	'EVX',	'EXCL',	'EXP',	'FCT',	'FIL',	'FLDC',	'FLO',	'FLT',	'FRST',	'FTC',	'FTT',	'FUEL',	'FUN',	'GAM',	'GAME',	'GAS',	'GBG',	'GBX',	'GBYTE',	'GCR',	'GEO',	'GLD',	'GNO',	'GNT',	'GOLOS',	'GRC',	'GRT',	'GRS',	'GRWI',	'GTC',	'GTO',	'GUP',	'GVT',	'GXS',	'HBAR',	'HBN',	'HEAT',	'HMQ',	'HPB',	'HSR',	'HT',	'HUSH',	'HVN',	'HXX',	'ICN',	'ICX',	'IFC',	'IFT',	'IGNIS',	'INCNT',	'IND',	'INF',	'INK',	'INS',	'INSTAR',	'INT',	'INXT',	'IOC',	'ION',	'IOP',	'IOST',	'IOTA',	'IOTX',	'IQT',	'ITC',	'IXC',	'IXT',	'J8T',	'JNT',	'KCS',	'KICK',	'KIN',	'KLAY',	'KMD',	'KNC',	'KORE',	'KSM',	'LBC',	'LCC',	'LEND',	'LEO',	'LEV',	'LGD',	'LINDA',	'LINK',	'LKK',	'LMC',	'LOCI',	'LOOM',	'LRC',	'LSK',	'LTC',	'LUN',	'LUNA',	'MAID',	'MANA',	'MATIC',	'MAX',	'MBRS',	'MCAP',	'MCO',	'MDA',	'MEC',	'MED',	'MEME',	'MER',	'MGC',	'MGO',	'MINEX',	'MINT',	'MIOTA',	'MITH',	'MKR',	'MLN',	'MNE',	'MNX',	'MOD',	'MONA',	'MRT',	'MSP',	'MTH',	'MTN',	'MUE',	'MUSIC',	'MYB',	'MYST',	'MZC',	'NAMO',	'NANO',	'NAS',	'NAV',	'NBT',	'NCASH',	'NDC',	'NEBL',	'NEO',	'NEOS',	'NET',	'NLC2',	'NLG',	'NMC',	'NMR',	'NOBL',	'NOTE',	'NPXS',	'NSR',	'NTO',	'NULS',	'NVC',	'NXC',	'NXS',	'NXT',	'OAX',	'OBITS',	'OCL',	'OCN',	'ODEM',	'ODN',	'OF',	'OK',	'OMG',	'OMNI',	'ONION',	'ONT',	'OPT',	'ORN',	'OST',	'PART',	'PASC',	'PAY',	'PBL',	'PBT',	'PFR',	'PING',	'PINK',	'PIVX',	'PIX',	'PLBT',	'PLR',	'PLU',	'POA',	'POE',	'POLY',	'POSW',	'POT',	'POWR',	'PPC',	'PPT',	'PPY',	'PRG',	'PRL',	'PRO',	'PST',	'PTC',	'PTOY',	'PURA',	'QASH',	'QAU',	'QLC',	'QRK',	'QRL',	'QSP',	'QTL',	'QTUM',	'QUICK',	'QWARK',	'R',	'RADS',	'RAIN',	'RBIES',	'RBX',	'RBY',	'RCN',	'RDD',	'RDN',	'REC',	'RED',	'REP',	'REQ',	'RHOC',	'RIC',	'RISE',	'RLC',	'RLT',	'RPX',	'RRT',	'RUFF',	'RUNE',	'RUP',	'RVT',	'SAFEX',	'SALT',	'SAN',	'SBD',	'SBTC',	'SC',	'SEELE',	'SEQ',	'SHIB',	'SHIFT',	'SIB',	'SIGMA',	'SIGT',	'SJCX',	'SKIN',	'SKY',	'SLR',	'SLS',	'SMART',	'SMT',	'SNC',	'SNGLS',	'SNM',	'SNRG',	'SNT',	'SOC',	'SOL',	'SOUL',	'SPANK',	'SPC',	'SPHR',	'SPR',	'SNX',	'SRN',	'START',	'STEEM',	'STK',	'STORJ',	'STORM',	'STQ',	'STRAT',	'STX',	'SUB',	'SWFTC',	'SWIFT',	'SWT',	'SYNX',	'SYS',	'TAAS',	'TAU',	'TCC',	'TFL',	'THC',	'THETA',	'TIME',	'TIX',	'TKN',	'TKR',	'TKS',	'TNB',	'TNT',	'TOA',	'TRAC',	'TRC',	'TRCT',	'TRIBE',	'TRIG',	'TRST',	'TRUE',	'TRUST',	'TRX',	'TUSD',	'TX',	'UBQ',	'UKG',	'ULA',	'UNB',	'UNI',	'UNITY',	'UNO',	'UNY',	'UP',	'URO',	'USDT',	'UST',	'UTK',	'VEE',	'VEN',	'VERI',	'VET',	'VIA',	'VIB',	'VIBE',	'VIVO',	'VOISE',	'VOX',	'VPN',	'VRC',	'VRM',	'VRS',	'VSL',	'VTC',	'VTR',	'WABI',	'WAN',	'WAVES',	'WAX',	'WBTC',	'WCT',	'WDC',	'WGO',	'WGR',	'WINGS',	'WPR',	'WTC',	'WTT',	'XAS',	'XAUR',	'XBC',	'XBY',	'XCN',	'XCP',	'XDN',	'XEL',	'XEM',	'NEM',	'XHV',	'XID',	'XLM',	'XMG',	'XMR',	'XMT',	'XMY',	'XPM',	'XRL',	'XRP',	'XSPEC',	'XST',	'XTZ',	'XUC',	'XVC',	'XVG',	'XWC',	'XZC',	'XZR',	'YEE',	'YOYOW',	'ZCC',	'ZCL',	'ZCO',	'ZEC',	'ZEN',	'ZET',	'ZIL',	'ZLA',	'ZRX'],
'currency name':	['FirstBlood',	'GiveCoin',	'808Coin',	'Aave',	'ArcBlock',	'ArtByte',	'AsiaCoin',	'Achain',	'Cardano',	'adToken',	'AdEx',	'Aeternity',	'Aeon',	'SingularityNET',	'IDNI-Agoras',	'POLY-AI',	'AidCoin',	'Aion',	'AirToken',	'Akuya-Coin',	'Algorand',	'ALIS',	'AmberCoin',	'Synereo',	'Ampleforth',	'Anoncoin',	'Aragon',	'AppCoins',	'APX-Ventures',	'Ardor',	'Ark',	'Aeron',	'AirSwap',	'ATBCoin',	'ATMChain',	'Cosmos',	'Authorship',	'Auroracoin',	'Avalanche',	'Aventus',	'B3Coin',	'Band Protocol',	'Basic-Attention-Token',	'BitBay',	'Boolberry',	'BCAP',	'BitConnect',	'Bitcoin-Diamond',	'Bitcoin-Cash',	'Bytecoin',	'BlockMason-Credit-Protocol-Token',	'BitcoinX',	'BitCrystals',	'Bitdeal',	'Bee-Token',	'BelaCoin',	'DAO-Casino',	'BF-Token',	'Bismuth',	'BitBean',	'BitBTC',	'BitCNY',	'BitEUR',	'BitGOLD',	'BitSILVER',	'BitUSD',	'Bibox-Token',	'Blitzcash',	'Blackcoin',	'Bolenum',	'Blocknet',	'Bluzelle',	'Blackmoon-Crypto',	'Binance-Coin',	'Bancor-Network-Token',	'Bounty0x',	'BoostCoin',	'Bodhi',	'bitqy',	'Bread',	'Breakout-Coin',	'Breakout-Stake',	'Bitcoin SV',	'Bata',	'Bitcoin',	'Bitcoin BEP2',	'BitcoinDark',	'Bitcoin-Private',	'Bitcoin-Gold',	'Bitmark',	'BitShares',	'BTSR',	'BitTorrent',	'Bitcore',	'Burstcoin',	'Binance-USD',	'BuzzCoin',	'Bytecent',	'Bytom',	'Crypto20',	'PancakeSwap',	'CannabisCoin',	'BlockCAT',	'CryptoCarbon',	'Blox',	'Cofound-it',	'ChatCoin',	'Chips',	'Clams',	'CloakCoin',	'Compcoin',	'CyberMiles',	'Cindicator',	'Cryptonex',	'CoinFi',	'Compound',	'COSS',	'Circuits-Of-Value',	'CreditBIT',	'CreativeCoin',	'Credo',	'Crypto.com Coin',	'Crown',	'BitDice',	'Centra',	'Cortex',	'CureCoin',	'Civic',	'Dai',	'Darcrus',	'Dash',	'DATAcoin',	'Chronologic',	'DeepBrain-Chain',	'DubaiCoin',	'Dentacoin',	'Decred',	'DECENT',	'Digital-Developers-Fund',	'Dent',	'DFSCoin',	'DigiByte',	'Digitalcoin',	'DigixDAO',	'Etheroll',	'Agrello-Delta',	'Diamond',	'DMarket',	'district0x',	'DogeCoin',	'DopeCoin',	'Polkadot',	'Dragonchain',	'Data',	'Databits',	'Dynamic',	'EarthCoin',	'eBoost',	'eBTC',	'ECC',	'E-coin',	'Edgeless',	'Eidoo',	'Electronic-Gulden',	'EverGreenCoin',	'Elrond',	'EDUCare',	'Elastos',	'Electrify.Asia',	'aelf',	'Elixir',	'Embercoin',	'Emercoin',	'Einsteinium',	'Enigma',	'Enjin-Coin',	'EnergyCoin',	'EOS',	'EOT-Token',	'EquiTrader',	'EuropeCoin',	'Ethereum-Classic',	'Ethereum',	'Ethereum-Dark',	'Ethos',	'Electroneum',	'Metaverse-Entropy',	'EncryptoTel',	'Devery',	'Everex',	'ExclusiveCoin',	'Expanse',	'Factom',	'Filecoin',	'FoldingCoin',	'FlorinCoin',	'FlutterCoin',	'FirstCoin',	'Feathercoin',	'FTX Token',	'Etherparty',	'FunFair',	'Gambit',	'GameCredits',	'Gas',	'Golos Gold',	'GoByte',	'Byteball',	'GCRCoin',	'GeoCoin',	'GoldCoin',	'Gnosis-Token',	'Golem-Tokens',	'Golos',	'Gridcoin',	'Graph',	'Groestlcoin',	'Growers-International',	'Game',	'Gifto',	'Guppy',	'Genesis-Vision',	'GXShares',	'Hedera',	'HoboNickels',	'HEAT',	'Humaniq',	'High-Performance-Blockchain',	'Hshare',	'Huobi Token',	'Hush',	'Hive',	'HexxCoin',	'ICONOMI',	'ICON',	'Infinitecoin',	'investFeed',	'Ignis',	'Incent',	'Indorse-Token',	'InfChain',	'Ink',	'INS-Ecosystem',	'Insights-Network',	'Internet-Node-Token',	'Internxt',	'IOCoin',	'ION',	'Internet-of-People',	'IOStoken',	'IOTA',	'IoTeX',	'Iquant-Chain',	'IoT-Chain',	'iXcoin',	'InsureX',	'JET8',	'Jibrel-Network',	'KuCoin',	'KickCoin',	'KIN',	'Klaytn',	'Komodo',	'Kyber-Network',	'KoreCoin',	'Kusama',	'LBRY-Credits',	'Litecoin-Cash',	'EthLend',	'UNUS SED LEO',	'Leverj',	'Legends-Room',	'Linda',	'ChainLink',	'Lykke',	'LoMoCoin',	'LOCIcoin',	'Loom-Token',	'Loopring',	'Lisk',	'Litecoin',	'Lunyr',	'Terra',	'MaidSafeCoin',	'Decentraland',	'Polygon',	'Maxcoin',	'Embers',	'MCAP',	'Monaco',	'Moeda-Loyalty-Points',	'Megacoin',	'MediBlock',	'Memetic',	'Mercury',	'MergeCoin',	'MobileGo',	'Minex',	'Mintcoin',	'IOTA',	'Mithril',	'Maker',	'Melon',	'Minereum',	'MinexCoin',	'Modum',	'MonaCoin',	'Miners-Reward-Token',	'Mothership',	'Monetha',	'MedToken',	'MonetaryUnit',	'Musicoin',	'MyBit-Token',	'Mysterium',	'Mazacoin',	'Namocoin',	'Nano',	'Nebulas-Token',	'Nav-Coin',	'NuBits',	'Nucleus-Vision',	'NeverDie-Coin',	'Neblio',	'NEO',	'NeosCoin',	'Nimiq',	'NoLimitCoin',	'Gulden',	'Namecoin',	'Numeraire',	'NobleCoin',	'DNotes',	'Pundi-X-Token',	'NuShares',	'Fujinto',	'Nuls',	'Novacoin',	'Nexium',	'Nexus',	'Nxt',	'openANX',	'Obits',	'Oceanlab',	'Odyssey',	'ODEM',	'Obsidian',	'OFCOIN',	'OKCash',	'OmiseGo',	'Omni',	'DeepOnion',	'Ontology',	'Opus',	'Orion-Protocol',	'Simple-Token',	'Particl',	'PascalCoin',	'TenX',	'Pebbles',	'Primalbase-Token',	'Payfair',	'CryptoPing',	'Pinkcoin',	'PIVX',	'Lampix',	'Polybius',	'Pillar',	'Pluton',	'POA-Network',	'Poet',	'Polymath',	'PoSW-Coin',	'PotCoin',	'Power-Ledger',	'Peercoin',	'Populous',	'Peerplays',	'Paragon-Coin',	'Oyster-Pearl',	'Propy',	'Primas',	'Pesetacoin',	'Patientory',	'Pura',	'QASH',	'Quantum',	'Qlink',	'Quark',	'Quantum-Resistant-Ledger',	'Quantstamp',	'Quatloo',	'Qtum',	'Quickswap',	'Qwark',	'Revain',	'Radium',	'Condensate',	'Rubies',	'Ripto-Bux',	'RubyCoin',	'Ripio-Credit-Network',	'ReddCoin',	'Raiden-Network-Token',	'Regalcoin',	'Redcoin',	'Augur',	'Request-Network',	'RChain',	'Riecoin',	'Rise',	'RLC-Token',	'RouletteToken',	'Red-Pulse',	'Recovery-Right-Tokens',	'Ruff',	'THORChain',	'Rupee',	'Rivetz',	'SafeExchangeCoin',	'Salt',	'Santiment-Network-Token',	'Steem-Dollars',	'Super-Bitcoin',	'Siacoin',	'Seele',	'Sequence',	'SHIBA-INU',	'SHIFT',	'SIBCoin',	'SIGMAcoin',	'Signatum',	'Storjcoin-X',	'SkinCoin',	'Skycoin',	'SolarCoin',	'SaluS',	'SmartCash',	'SmartMesh',	'SunContract',	'SingularDTV',	'SONM',	'Synergy',	'Status-Network-Token',	'All-Sports',	'Solana',	'Phantasma',	'SpankChain',	'SpaceChain',	'Sphere',	'SpreadCoin',	'Synthetix-Network-Token',	'Sirin-Labs-Token',	'Startcoin',	'Steem',	'STK-Token',	'Storj',	'Storm',	'Storiqa',	'Stratis',	'Stox',	'Substratum',	'SwftCoin',	'Bitswift',	'Swarm-City',	'Syndicate',	'SysCoin',	'Taas',	'Lamden',	'The-ChampCoin',	'True-Flip',	'HempCoin',	'Theta-Token',	'Time',	'Blocktix',	'TokenCard',	'Trackr',	'Tokes',	'Time-New-Bank',	'Tierion',	'ToaCoin',	'OriginTrail',	'Terracoin',	'Tracto',	'Tribe',	'Triggers',	'Trustcoin',	'TrueChain',	'TrustPlus',	'Tronix',	'TrueUSD',	'TransferCoin',	'Ubiq',	'UnikoinGold',	'Ulatech',	'UnbreakableCoin',	'Uniswap',	'SuperNET',	'Unobtanium',	'Unity-Ingot',	'UpToken',	'Uro',	'Tether',	'TerraUSD',	'UTrust',	'BLOCKv',	'VeChain',	'Veritaseum',	'VeChain',	'Viacoin',	'Viberate',	'Vibe',	'VIVO',	'Voise',	'Voxels',	'VPNCoin',	'Vericoin',	'Verium',	'Veros',	'vSlice',	'Vertcoin',	'vTorrent',	'WaBi',	'Wanchain',	'Waves',	'Wax-Token',	'Wrapped Bitcoin',	'Waves-Community',	'WorldCoin',	'WavesGo',	'Wagerr',	'Wings',	'WePower',	'Walton',	'Giga-Watt-Token',	'Asch',	'Xaurum',	'Bitcoin-Plus',	'XtraBYtes',	'Cryptonite',	'Counterparty',	'DigitalNote',	'Elastic',	'NEM',	'NEM',	'Haven-Protocol',	'Sphere-Identity',	'Stellar',	'Magi',	'Monero',	'Metal',	'Myriadcoin',	'Primecoin',	'Rialto',	'Ripple',	'Spectrecoin',	'Stealthcoin',	'Tezos',	'Exchange-Union',	'Vcash',	'Verge',	'WhiteCoin',	'ZCoin',	'ZrCoin',	'Yee',	'YOYOW',	'ZcCoin',	'Zclassic',	'Zebi',	'Zcash',	'ZenCash',	'Zetacoin',	'Zilliqa',	'Zilla',	'0x']
}



