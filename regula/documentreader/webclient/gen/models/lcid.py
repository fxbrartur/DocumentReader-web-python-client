# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


"""
Locale id. Used to tag same typed fields declared in several languages.
For example: name can be provided in both native and latin variants.
Based on Microsoft locale id (https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f).

"""
class LCID(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    LATIN = int("0")

    AFRIKAANS = int("1078")

    ALBANIAN = int("1052")

    ARABIC_ALGERIA = int("5121")

    ARABIC_BAHRAIN = int("15361")

    ARABIC_EGYPT = int("3073")

    ARABIC_IRAQ = int("2049")

    ARABIC_JORDAN = int("11265")

    ARABIC_KUWAIT = int("13313")

    ARABIC_LEBANON = int("12289")

    ARABIC_LIBYA = int("4097")

    ARABIC_MOROCCO = int("6145")

    ARABIC_OMAN = int("8193")

    ARABIC_QATAR = int("16385")

    ARABIC_SAUDI_ARABIA = int("1025")

    ARABIC_SYRIA = int("10241")

    ARABIC_TUNISIA = int("7169")

    ARABIC_UAE = int("14337")

    ARABIC_YEMEN = int("9217")

    ARABIC_ARMENIAN = int("1067")

    AZERI_CYRILIC = int("2092")

    AZERI_LATIN = int("1068")

    BASQUE = int("1069")

    BELARUSIAN = int("1059")

    BULGARIAN = int("1026")

    CATALAN = int("1027")

    CHINESE_HONGKONG_SAR = int("3076")

    CHINESE_MACAO_SAR = int("5124")

    CHINESE = int("2052")

    CHINESE_SINGAPORE = int("4100")

    CHINESE_TAIWAN = int("1028")

    CROATIAN = int("1050")

    CZECH = int("1029")

    DANISH = int("1030")

    DIVEHI = int("1125")

    DUTCH_BELGIUM = int("2067")

    DUTCH_NETHERLANDS = int("1043")

    ENGLISH_AUSTRALIA = int("3081")

    ENGLISH_BELIZE = int("10249")

    ENGLISH_CANADA = int("4105")

    ENGLISH_CARRIBEAN = int("9225")

    ENGLISH_IRELAND = int("6153")

    ENGLISH_JAMAICA = int("8201")

    ENGLISH_NEW_ZEALAND = int("5129")

    ENGLISH_PHILIPPINES = int("13321")

    ENGLISH_SOUTH_AFRICA = int("7177")

    ENGLISH_TRINIDAD = int("11273")

    ENGLISH_UK = int("2057")

    ENGLISH_US = int("1033")

    ENGLISH_ZIMBABWE = int("12297")

    ESTONIAN = int("1061")

    FAEROESE = int("1080")

    FARSI = int("1065")

    FINNISH = int("1035")

    FRENCH_BELGIUM = int("2060")

    FRENCH_CANADA = int("3084")

    FRENCH_FRANCE = int("1036")

    FRENCH_LUXEMBOURG = int("5132")

    FRENCH_MONACO = int("6156")

    FRENCH_SWITZERLAND = int("4108")

    FYRO_MACEDONIAN = int("1071")

    GALICIAN = int("1110")

    GEORGIAN = int("1079")

    GERMAN_AUSTRIA = int("3079")

    GERMAN_GERMANY = int("1031")

    GERMAN_LIECHTENSTEIN = int("5127")

    GERMAN_LUXEMBOURG = int("4103")

    GERMAN_SWITZERLAND = int("2055")

    GREEK = int("1032")

    GUJARATI = int("1095")

    HEBREW = int("1037")

    HINDI_INDIA = int("1081")

    HUNGARIAN = int("1038")

    ICELANDIC = int("1039")

    INDONESIAN = int("1057")

    ITALIAN_ITALY = int("1040")

    ITALIAN_SWITZERLAND = int("2064")

    JAPANESE = int("1041")

    KANNADA = int("1099")

    KAZAKH = int("1087")

    KONKANI = int("1111")

    KOREAN = int("1042")

    KYRGYZ_CYRILICK = int("1088")

    LATVIAN = int("1062")

    LITHUANIAN = int("1063")

    MALAY_MALAYSIA = int("1086")

    MALAY_BRUNEI_DARUSSALAM = int("2110")

    MARATHI = int("1102")

    MONGOLIAN_CYRILIC = int("1104")

    NORWEGIAN_BOKMAL = int("1044")

    NORWEGIAN_NYORSK = int("2068")

    POLISH = int("1045")

    PORTUGUESE_BRAZIL = int("1046")

    PORTUGUESE_PORTUGAL = int("2070")

    PUNJABI = int("1094")

    RHAETO_ROMANIC = int("1047")

    ROMANIAN = int("1048")

    RUSSIAN = int("1049")

    SANSKRIT = int("1103")

    SERBIAN_CYRILIC = int("3098")

    SERBIAN_LATIN = int("2074")

    SLOVAK = int("1051")

    SLOVENIAN = int("1060")

    SPANISH_ARGENTINA = int("11274")

    SPANISH_BOLIVIA = int("16394")

    SPANISH_CHILE = int("13322")

    SPANICH_COLOMBIA = int("9226")

    SPANISH_COSTA_RICA = int("5130")

    SPANISH_DOMINICAN_REPUBLIC = int("7178")

    SPANISH_ECUADOR = int("12298")

    SPANISH_EL_SALVADOR = int("17418")

    SPANISH_GUATEMALA = int("4106")

    SPANISH_HONDURAS = int("18442")

    SPANISH_MEXICO = int("2058")

    SPANISH_NICARAGUA = int("19466")

    SPANISH_PANAMA = int("6154")

    SPANISH_PARAGUAY = int("15370")

    SPANISH_PERU = int("10250")

    SPANISH_PUERTO_RICO = int("20490")

    SPANISH_TRADITIONAL_SORT = int("1034")

    SPANISH_INTERNATIONAL_SORT = int("3082")

    SPANISH_URUGUAY = int("14346")

    SPANISH_VENEZUELA = int("8202")

    SWAHILI = int("1089")

    SWEDISH = int("1053")

    SWEDISH_FINLAND = int("2077")

    SYRIAC = int("1114")

    TAMIL = int("1097")

    TATAR = int("1092")

    TELUGU = int("1098")

    THAI_THAILAND = int("1054")

    TURKISH = int("1055")

    TAJIK_CYRILLIC = int("1064")

    TURKMEN = int("1090")

    UKRAINIAN = int("1058")

    URDU = int("1056")

    UZBEK_CYRILIC = int("2115")

    UZBEK_LATIN = int("1091")

    VIETNAMESE = int("1066")

    CTC_SIMPLIFIED = int("50001")

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
