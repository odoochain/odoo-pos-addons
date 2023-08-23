{
    "name": """POS: Longpolling support""",
    "summary": """Technical module to implement instant updates in POS""",
    "category": "Point of Sale",
    "images": [],
    'version': '1.0.1',
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov, OdooChain",
    "support": "help@itpp.dev",
    "website": "https://github.com/itpp-labs/pos-addons",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["bus", "point_of_sale"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/pos_longpolling_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "/pos_longpolling/static/src/js/LongpollingBus.js",
            "/pos_longpolling/static/src/js/LongpollingModel.js",
            "/pos_longpolling/static/src/js/SyncBusService.js",
            "/pos_longpolling/static/src/js/SyncNotification.js",
            "/pos_longpolling/static/src/js/PosConnection.js",
            "/pos_longpolling/static/src/js/pos.js",
        ],
        "web.assets_backend": [
            "pos_longpolling/static/src/js/test_longpoll_pos.js",
        ],
        "web.assets_qweb": ["pos_longpolling/static/src/xml/SyncNotification.xml"],
    },
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
