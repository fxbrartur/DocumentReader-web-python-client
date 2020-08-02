# coding: utf-8

"""
    Regula Document Reader Web API

    Regula Document Reader Web API  # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


class LCID(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    "Latin"
    LATIN = int("0")

    "Afrikaans"
    AFRIKAANS = int("1078")

    "Albanian"
    ALBANIAN = int("1052")

    "Arabic (Algeria)"
    ARABIC_ALGERIA = int("5121")

    "Arabic (Bahrain)"
    ARABIC_BAHRAIN = int("15361")

    "Arabic (Egypt)"
    ARABIC_EGYPT = int("3073")

    "Arabic (Iraq)"
    ARABIC_IRAQ = int("2049")

    "Arabic (Jordan)"
    ARABIC_JORDAN = int("11265")

    "Arabic (Kuwait)"
    ARABIC_KUWAIT = int("13313")

    "Arabic (Lebanon)"
    ARABIC_LEBANON = int("12289")

    "Arabic (Libya)"
    ARABIC_LIBYA = int("4097")

    "Arabic (Morocco)"
    ARABIC_MOROCCO = int("6145")

    "Arabic (Oman)"
    ARABIC_OMAN = int("8193")

    "Arabic (Qatar)"
    ARABIC_QATAR = int("16385")

    "Arabic (Saudi Arabia)"
    ARABIC_SAUDI_ARABIA = int("1025")

    "Arabic (Syria)"
    ARABIC_SYRIA = int("10241")

    "Arabic (Tunisia)"
    ARABIC_TUNISIA = int("7169")

    "Arabic (U.A.E.)"
    ARABIC_UAE = int("4337")

    "Arabic (Yemen)"
    ARABIC_YEMEN = int("9217")

    "Armenian"
    ARABIC_ARMENIAN = int("1067")

    "Azeri (Cyrillic)"
    AZERI_CYRILIC = int("2092")

    "Azeri (Latin)"
    AZERI_LATIN = int("1068")

    "Basque"
    BASQUE = int("1069")

    "Belarusian"
    BELARUSIAN = int("1059")

    "Bulgarian"
    BULGARIAN = int("1026")

    "Catalan"
    CATALAN = int("1027")

    "Chinese (HongKong S.A.R.)"
    CHINESE_HONGKONG_SAR = int("3076")

    "Chinese (Macao S.A.R.)"
    CHINESE_MACAO_SAR = int("5124")

    "Chinese"
    CHINESE = int("2052")

    "Chinese (Singapore)"
    CHINESE_SINGAPORE = int("4100")

    "Chinese (Taiwan)"
    CHINESE_TAIWAN = int("1028")

    "Croatian"
    CROATIAN = int("1050")

    "Czech"
    CZECH = int("1029")

    "Danish"
    DANISH = int("1030")

    "Divehi"
    DIVEHI = int("1125")

    "Dutch (Belgium)"
    DUTCH_BELGIUM = int("2067")

    "Dutch (Netherlands)"
    DUTCH_NETHERLANDS = int("1043")

    "English (Australia)"
    ENGLISH_AUSTRALIA = int("3081")

    "English (Belize)"
    ENGLISH_BELIZE = int("10249")

    "English (Canada)"
    ENGLISH_CANADA = int("4105")

    "English (Caribbean)"
    ENGLISH_CARRIBEAN = int("9225")

    "English (Ireland)"
    ENGLISH_IRELAND = int("6153")

    "English (Jamaica)"
    ENGLISH_JAMAICA = int("8201")

    "English (New Zealand)"
    ENGLISH_NEW_ZEALAND = int("5129")

    "English (Philippines)"
    ENGLISH_PHILIPPINES = int("13321")

    "English (South Africa)"
    ENGLISH_SOUTH_AFRICA = int("7177")

    "English (Trinidad)"
    ENGLISH_TRINIDAD = int("11273")

    "English (United Kingdom)"
    ENGLISH_UK = int("2057")

    "English (United States)"
    ENGLISH_US = int("1033")

    "English (Zimbabwe)"
    ENGLISH_ZIMBABWE = int("12297")

    "Estonian"
    ESTONIAN = int("1061")

    "Faeroese"
    FAEROESE = int("1080")

    "Farsi"
    FARSI = int("1065")

    "Finnish"
    FINNISH = int("1035")

    "French (Belgium)"
    FRENCH_BELGIUM = int("2060")

    "French (Canada)"
    FRENCH_CANADA = int("3084")

    "French (France)"
    FRENCH_FRANCE = int("1036")

    "French (Luxembourg)"
    FRENCH_LUXEMBOURG = int("5132")

    "French (Monaco)"
    FRENCH_MONACO = int("6156")

    "French (Switzerland)"
    FRENCH_SWITZERLAND = int("4108")

    "Galician"
    FYRO_MACEDONIAN = int("1071")

    "Georgian"
    GALICIAN = int("1110")

    "German (Austria)"
    GEORGIAN = int("1079")

    "German (Germany)"
    GERMAN_AUSTRIA = int("3079")

    "German (Liechtenstein)"
    GERMAN_GERMANY = int("1031")

    "German (Luxembourg)"
    GERMAN_LIECHTENSTEIN = int("5127")

    "German (Switzerland)"
    GERMAN_LUXEMBOURG = int("4103")

    "Greek"
    GERMAN_SWITZERLAND = int("2055")

    "Gujarati"
    GREEK = int("1032")

    "Hebrew"
    GUJARATI = int("1095")

    "Hindi (India)"
    HEBREW = int("1037")

    "Hungarian"
    HINDI_INDIA = int("1081")

    "Icelandic"
    HUNGARIAN = int("1038")

    "Indonesian"
    ICELANDIC = int("1039")

    "Italian (Italy)"
    INDONESIAN = int("1057")

    "Italian (Switzerland)"
    ITALIAN_ITALY = int("1040")

    "Japanese"
    ITALIAN_SWITZERLAND = int("2064")

    "Kannada"
    JAPANESE = int("1041")

    "Kazakh"
    KANNADA = int("1099")

    "Konkani"
    KAZAKH = int("1087")

    "Korean"
    KONKANI = int("1111")

    "Kyrgyz (Cyrillic)"
    KOREAN = int("1042")

    "Latvian"
    KYRGYZ_CYRILICK = int("1088")

    "Lithuanian"
    LATVIAN = int("1062")

    "FYRO Macedonian"
    LITHUANIAN = int("1063")

    "Malay (Malaysia)"
    MALAY_MALAYSIA = int("1086")

    "Malay (Brunei Darussalam)"
    MALAY_BRUNEI_DARUSSALAM = int("2110")

    "Marathi"
    MARATHI = int("1102")

    "Mongolian (Cyrillic)"
    MONGOLIAN_CYRILIC = int("1104")

    "Norwegian (Bokmal)"
    NORWEGIAN_BOKMAL = int("1044")

    "Norwegian (Nynorsk)"
    NORWEGIAN_NYORSK = int("2068")

    "Polish"
    POLISH = int("1045")

    "Portuguese (Brazil)"
    PORTUGUESE_BRAZIL = int("1046")

    "Portuguese (Portugal)"
    PORTUGUESE_PORTUGAL = int("2070")

    "Punjabi"
    PUNJABI = int("1094")

    "Rhaeto-Romanic"
    RHAETO_ROMANIC = int("1047")

    "Romanian"
    ROMANIAN = int("1048")

    "Russian"
    RUSSIAN = int("1049")

    "Sanskrit"
    SANSKRIT = int("1103")

    "Serbian (Cyrillic)"
    SERBIAN_CYRILIC = int("3098")

    "Serbian (Latin)"
    SERBIAN_LATIN = int("2074")

    "Slovak"
    SLOVAK = int("1051")

    "Slovenian"
    SLOVENIAN = int("1060")

    "Spanish (Argentina)"
    SPANISH_ARGENTINA = int("11274")

    "Spanish (Bolivia)"
    SPANISH_BOLIVIA = int("16394")

    "Spanish (Chile)"
    SPANISH_CHILE = int("13322")

    "Spanish (Colombia)"
    SPANICH_COLOMBIA = int("9226")

    "Spanish (Costa Rica)"
    SPANISH_COSTA_RICA = int("5130")

    "Spanish (Dominican Republic)"
    SPANISH_DOMINICAN_REPUBLIC = int("7178")

    "Spanish (Ecuador)"
    SPANISH_ECUADOR = int("12298")

    "Spanish (El Salvador)"
    SPANISH_EL_SALVADOR = int("17418")

    "Spanish (Guatemala)"
    SPANISH_GUATEMALA = int("4106")

    "Spanish (Honduras)"
    SPANISH_HONDURAS = int("18442")

    "Spanish (Mexico)"
    SPANISH_MEXICO = int("2058")

    "Spanish (Nicaragua)"
    SPANISH_NICARAGUA = int("19466")

    "Spanish (Panama)"
    SPANISH_PANAMA = int("6154")

    "Spanish (Paraguay)"
    SPANISH_PARAGUAY = int("15370")

    "Spanish (Peru)"
    SPANISH_PERU = int("10250")

    "Spanish (Puerto Rico)"
    SPANISH_PUERTO_RICO = int("20490")

    "Spanish (Traditional Sort)"
    SPANISH_TRADITIONAL_SORT = int("1034")

    "Spanish (International Sort)"
    SPANISH_INTERNATIONAL_SORT = int("3082")

    "Spanish (Uruguay)"
    SPANISH_URUGUAY = int("14346")

    "Spanish (Venezuela)"
    SPANISH_VENEZUELA = int("8202")

    "Swahili"
    SWAHILI = int("1089")

    "Swedish"
    SWEDISH = int("1053")

    "Swedish (Finland)"
    SWEDISH_FINLAND = int("2077")

    "Syriac"
    SYRIAC = int("1114")

    "Tamil"
    TAMIL = int("1097")

    "Tatar"
    TATAR = int("1092")

    "Telugu"
    TELUGU = int("1098")

    "Thai (Thailand)"
    THAI_THAILAND = int("1054")

    "Turkish"
    TURKISH = int("1055")

    "Tajik (Cyrillic)"
    TAJIK_CYRILLIC = int("1064")

    "Turkmen"
    TURKMEN = int("1090")

    "Ukrainian"
    UKRAINIAN = int("1058")

    "Urdu"
    URDU = int("1056")

    "Uzbek (Cyrillic)"
    UZBEK_CYRILIC = int("2115")

    "Uzbek (Latin)"
    UZBEK_LATIN = int("1091")

    "Vietnamese"
    VIETNAMESE = int("1066")

    "CTC Simplified"
    CTC_SIMPLIFIED = int("50001")

    "CTC Traditional"
    CTC_TRADITIONAL = int("50002")

    allowable_values = [LATIN, AFRIKAANS, ALBANIAN, ARABIC_ALGERIA, ARABIC_BAHRAIN, ARABIC_EGYPT, ARABIC_IRAQ, ARABIC_JORDAN, ARABIC_KUWAIT, ARABIC_LEBANON, ARABIC_LIBYA, ARABIC_MOROCCO, ARABIC_OMAN, ARABIC_QATAR, ARABIC_SAUDI_ARABIA, ARABIC_SYRIA, ARABIC_TUNISIA, ARABIC_UAE, ARABIC_YEMEN, ARABIC_ARMENIAN, AZERI_CYRILIC, AZERI_LATIN, BASQUE, BELARUSIAN, BULGARIAN, CATALAN, CHINESE_HONGKONG_SAR, CHINESE_MACAO_SAR, CHINESE, CHINESE_SINGAPORE, CHINESE_TAIWAN, CROATIAN, CZECH, DANISH, DIVEHI, DUTCH_BELGIUM, DUTCH_NETHERLANDS, ENGLISH_AUSTRALIA, ENGLISH_BELIZE, ENGLISH_CANADA, ENGLISH_CARRIBEAN, ENGLISH_IRELAND, ENGLISH_JAMAICA, ENGLISH_NEW_ZEALAND, ENGLISH_PHILIPPINES, ENGLISH_SOUTH_AFRICA, ENGLISH_TRINIDAD, ENGLISH_UK, ENGLISH_US, ENGLISH_ZIMBABWE, ESTONIAN, FAEROESE, FARSI, FINNISH, FRENCH_BELGIUM, FRENCH_CANADA, FRENCH_FRANCE, FRENCH_LUXEMBOURG, FRENCH_MONACO, FRENCH_SWITZERLAND, FYRO_MACEDONIAN, GALICIAN, GEORGIAN, GERMAN_AUSTRIA, GERMAN_GERMANY, GERMAN_LIECHTENSTEIN, GERMAN_LUXEMBOURG, GERMAN_SWITZERLAND, GREEK, GUJARATI, HEBREW, HINDI_INDIA, HUNGARIAN, ICELANDIC, INDONESIAN, ITALIAN_ITALY, ITALIAN_SWITZERLAND, JAPANESE, KANNADA, KAZAKH, KONKANI, KOREAN, KYRGYZ_CYRILICK, LATVIAN, LITHUANIAN, MALAY_MALAYSIA, MALAY_BRUNEI_DARUSSALAM, MARATHI, MONGOLIAN_CYRILIC, NORWEGIAN_BOKMAL, NORWEGIAN_NYORSK, POLISH, PORTUGUESE_BRAZIL, PORTUGUESE_PORTUGAL, PUNJABI, RHAETO_ROMANIC, ROMANIAN, RUSSIAN, SANSKRIT, SERBIAN_CYRILIC, SERBIAN_LATIN, SLOVAK, SLOVENIAN, SPANISH_ARGENTINA, SPANISH_BOLIVIA, SPANISH_CHILE, SPANICH_COLOMBIA, SPANISH_COSTA_RICA, SPANISH_DOMINICAN_REPUBLIC, SPANISH_ECUADOR, SPANISH_EL_SALVADOR, SPANISH_GUATEMALA, SPANISH_HONDURAS, SPANISH_MEXICO, SPANISH_NICARAGUA, SPANISH_PANAMA, SPANISH_PARAGUAY, SPANISH_PERU, SPANISH_PUERTO_RICO, SPANISH_TRADITIONAL_SORT, SPANISH_INTERNATIONAL_SORT, SPANISH_URUGUAY, SPANISH_VENEZUELA, SWAHILI, SWEDISH, SWEDISH_FINLAND, SYRIAC, TAMIL, TATAR, TELUGU, THAI_THAILAND, TURKISH, TAJIK_CYRILLIC, TURKMEN, UKRAINIAN, URDU, UZBEK_CYRILIC, UZBEK_LATIN, VIETNAMESE, CTC_SIMPLIFIED, CTC_TRADITIONAL]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """LCID - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LCID):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LCID):
            return True

        return self.to_dict() != other.to_dict()
