{
    "name": "FECR",
    "version": "17.0",
    "category": "Accounting",
    "summary": "Factura electrónica para Costa Rica",
    "author": "BIG CLOUD CR SRL",
    "website": "https://github.com/lfelipecr/fecrsh",
    "license": "LGPL-3",
    "price": 500,
    "currency": "USD",
    "depends": [
        "account",
        "base_iban",
        "l10n_cr",
        "l10n_cr_accounting",
        "l10n_cr_cabys",
        "l10n_cr_currency_exchange",
        "l10n_cr_territories",
        "uom",
        "sale",
        "l10n_cr_identification_type"
        #"fetchmail",
    ],
    "data": [
        # security
        "security/ir.model.access.csv",
        "security/groups.xml",
    ],
    "external_dependencies": {
        "python": [
            "cryptography",
            "jsonschema",
            "OpenSSL",
            "phonenumbers",
            "PyPDF2",
            "suds",
            "xades",
            "xmlsig",
            "xmltodict"
        ],
    }, 
}
