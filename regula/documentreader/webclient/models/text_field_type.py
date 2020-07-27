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

from regula.documentreader.webclient.configuration import Configuration


class TextFieldType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DOCUMENT_CLASS_CODE = "0"
    ISSUING_STATE_CODE = "1"
    DOCUMENT_NUMBER = "2"
    DATE_OF_EXPIRY = "3"
    DATE_OF_ISSUE = "4"
    DATE_OF_BIRTH = "5"
    PLACE_OF_BIRTH = "6"
    PERSONAL_NUMBER = "7"
    SURNAME = "8"
    GIVEN_NAME = "9"
    MOTHERS_NAME = "10"
    NATIONALITY = "11"
    SEX = "12"
    HEIGHT = "13"
    WEIGHT = "14"
    EYES_COLOR = "15"
    HAIR_COLOR = "16"
    ADDRESS = "17"
    DONOR = "18"
    SOCIAL_SECURITY_NUMBER = "19"
    DL_CLASS = "20"
    DL_ENDORSED = "21"
    DL_RESTRICTION_CODE = "22"
    DL_UNDER_21_DATE = "23"
    AUTHORITY = "24"
    SURNAME_AND_GIVEN_NAMES = "25"
    NATIONALITY_CODE = "26"
    PASSPORT_NUMBER = "27"
    INVITATION_NUMBER = "28"
    VISA_ID = "29"
    VISA_CLASS = "30"
    VISA_SUBCLASS = "31"
    MRZ_TYPE = "35"
    DOCUMENT_CLASS_NAME = "37"
    ISSUING_STATE_NAME = "38"
    PLACE_OF_ISSUE = "39"
    DOCUMENT_NUMBER_CHECKSUM = "40"
    DATE_OF_BIRTH_CHECKSUM = "41"
    DATE_OF_EXPIRY_CHECKSUM = "42"
    PERSONAL_NUMBER_CHECKSUM = "43"
    FINAL_CHECKSUM = "44"
    PASSPORT_NUMBER_CHECKSUM = "45"
    INVITATION_NUMBER_CHECKSUM = "46"
    VISA_ID_CHECKSUM = "47"
    SURNAME_AND_GIVEN_NAME_CHECKSUM = "48"
    VISA_VALID_UNTIL_CHECKSUM = "49"
    OTHER = "50"
    MRZ_STRINGS = "51"
    NAME_SUFFIX = "52"
    NAME_PREFIX = "53"
    DATE_OF_ISSUE_CHECKSUM = "54"
    DATE_OF_ISSUE_CHECK_DIGIT = "55"
    DOCUMENT_SERIES = "56"
    REG_CERT_REG_NUMBER = "57"
    REG_CERT_CAR_MODEL = "58"
    REG_CERT_CAR_COLOR = "59"
    REG_CERT_BODY_NUMBER = "60"
    REG_CERT_CAR_TYPE = "61"
    REG_CERT_MAX_WEIGHT = "62"
    REG_CERT_WEIGHT = "63"
    ADDRESS_AREA = "64"
    ADDRESS_STATE = "65"
    ADDRESS_BUILDING = "66"
    ADDRESS_HOUSE = "67"
    ADDRESS_FLAT = "68"
    PLACE_OF_REGISTRATION = "69"
    DATE_OF_REGISTRATION = "70"
    RESIDENT_FROM = "71"
    RESIDENT_UNTIL = "72"
    AUTHORITY_CODE = "73"
    PLACE_OF_BIRTH_AREA = "74"
    PLACE_OF_BIRTH_STATE_CODE = "75"
    ADDRESS_STREET = "76"
    ADDRESS_CITY = "77"
    ADDRESS_JURISDICTION_CODE = "78"
    ADDRESS_POSTAL_CODE = "79"
    DOCUMENT_NUMBER_CHECK_DIGIT = "80"
    DATE_OF_BIRTH_CHECK_DIGIT = "81"
    DATE_OF_EXPIRY_CHECK_DIGIT = "82"
    PERSONAL_NUMBER_CHECK_DIGIT = "83"
    FINAL_CHECK_DIGIT = "84"
    PASSPORT_NUMBER_CHECK_DIGIT = "85"
    INVITATION_NUMBER_CHECK_DIGIT = "86"
    VISA_ID_CHECK_DIGIT = "87"
    SURNAME_AND_GIVEN_NAMES_CHECK_DIGIT = "88"
    VISA_VALID_UNTIL_CHECK_DIGIT = "89"
    PERMIT_DL_CLASS = "90"
    PERMIT_DATE_OF_EXPIRY = "91"
    PERMIT_IDENTIFIER = "92"
    PERMIT_DATE_OF_ISSUE = "93"
    PERMIT_RESTRICTION_CODE = "94"
    PERMIT_ENDORSED = "95"
    ISSUE_TIMESTAMP = "96"
    NUMBER_OF_DUPLICATES = "97"
    MEDICAL_INDICATOR_CODES = "98"
    NON_RESIDENT_INDICATOR = "99"
    VISA_TYPE = "100"
    VISA_VALID_FROM = "101"
    VISA_VALID_UNTIL = "102"
    DURATION_OF_STAY = "103"
    NUMBER_OF_ENTRIES = "104"
    DAY = "105"
    MONTH = "106"
    YEAR = "107"
    UNIQUE_CUSTOMER_IDENTIFIER = "108"
    COMMERCIAL_VEHICLE_CODES = "109"
    AKA_DATE_OF_BIRTH = "110"
    AKA_SOCIAL_SECURITY_NUMBER = "111"
    AKA_SURNAME = "112"
    AKA_GIVEN_NAMES = "113"
    AKA_NAME_SUFFIX = "114"
    AKA_NAME_PREFIX = "115"
    MAILING_ADDRESS_STREET = "116"
    MAILING_ADDRESS_CITY = "117"
    MAILING_ADDRESS_JURISDICTION_CODE = "118"
    MAILING_ADDRESS_POSTAL_CODE = "119"
    AUDIT_INFORMATION = "120"
    INVENTORY_NUMBER = "121"
    RACE_ETHNICITY = "122"
    JURISDICTION_VEHICLE_CLASS = "123"
    JURISDICTION_ENDORSEMENT_CODE = "124"
    JURISDICTION_RESTRICTION_CODE = "125"
    FAMILY_NAME = "126"
    GIVEN_NAMES_RUS = "127"
    VISA_ID_RUS = "128"
    FATHERS_NAME = "129"
    FATHERS_NAME_RUS = "130"
    SURNAME_AND_GIVEN_NAME_RUS = "131"
    PLACE_OF_BIRTH_RUS = "132"
    AUTHORITY_RUS = "133"
    ISSUING_STATE_CODE_NUMERIC = "134"
    NATIONALITY_CODE_NUMERIC = "135"
    ENGINE_POWER = "136"
    ENGINE_VOLUME = "137"
    CHASSIS_NUMBER = "138"
    ENGINE_NUMBER = "139"
    ENGINE_MODEL = "140"
    VEHICLE_CATEGORY = "141"
    IDENTITY_CARD_NUMBER = "142"
    CONTROL_NUMBER = "143"
    PARENTS_GIVEN_NAMES = "144"
    SECOND_SURNAME = "145"
    MIDDLE_NAME = "146"
    REG_CERT_VIN = "147"
    REG_CERT_VIN_CHECK_DIGIT = "148"
    REG_CERT_VIN_CHECKSUM = "149"
    LINE_1_CHECK_DIGIT = "150"
    LINE_2_CHECK_DIGIT = "151"
    LINE_3_CHECK_DIGIT = "152"
    LINE_1_CHECKSUM = "153"
    LINE_2_CHECKSUM = "154"
    LINE_3_CHECKSUM = "155"
    REG_CERT_REG_NUMBER_CHECK_DIGIT = "156"
    REG_CERT_REG_NUMBER_CHECKSUM = "157"
    REG_CERT_VEHICLE_ITS_CODE = "158"
    CARD_ACCESS_NUMBER = "159"
    MARITAL_STATUS = "160"
    COMPANY_NAME = "161"
    SPECIAL_NOTES = "162"
    SURNAME_OF_SPOUSE = "163"
    TRACKING_NUMBER = "164"
    BOOKLET_NUMBER = "165"
    CHILDREN = "166"
    COPY_NUMBER = "167"
    SERIAL_NUMBER = "168"
    DOSSIER_NUMBER = "169"
    AKA_SURNAME_AND_GIVEN_NAMES = "170"
    TERRITORIAL_VALIDITY = "171"
    MRZ_STRINGS_WITH_CORRECT_CHECK_SUMS = "172"
    DL_CDL_RESTRICTION_CODE = "173"
    DL_UNDER_18_DATE = "174"
    DL_RECORD_CREATED = "175"
    DL_DUPLICATE_DATE = "176"
    DL_ISSUE_TYPE = "177"
    MILITARY_BOOK_NUMBER = "178"
    DESTINATION = "179"
    BLOOD_GROUP = "180"
    SEQUENCE_NUMBER = "181"
    REG_CERT_BODY_TYPE = "182"
    REG_CERT_CAR_MARK = "183"
    TRANSACTION_NUMBER = "184"
    AGE = "185"
    FOLIO_NUMBER = "186"
    VOTER_KEY = "187"
    ADDRESS_MUNICIPALITY = "188"
    ADDRESS_LOCATION = "189"
    SECTION = "190"
    OCR_NUMBER = "191"
    FEDERAL_ELECTIONS = "192"
    REFERENCE_NUMBER = "193"
    OPTIONAL_DATA_CHECKSUM = "194"
    OPTIONAL_DATA_CHECK_DIGIT = "195"
    VISA_NUMBER = "196"
    VISA_NUMBER_CHECKSUM = "197"
    VISA_NUMBER_CHECK_DIGIT = "198"
    VOTER = "199"
    PREVIOUS_TYPE = "200"
    FIELD_FROM_MRZ = "220"
    CURRENT_DATE = "221"
    STATUS_DATE_OF_EXPIRY = "251"
    BANK_NOTE_NUMBER = "252"
    CSC_CODE = "253"
    ARTISTIC_NAME = "254"
    ACADEMIC_TITLE = "255"
    ADDRESS_COUNTRY = "256"
    ADDRESS_ZIP_CODE = "257"
    E_ID_RESIDENCE_PERMIT_1 = "258"
    E_ID_RESIDENCE_PERMIT_2 = "259"
    E_ID_PLACE_OF_BIRTH_STREET = "260"
    E_ID_PLACE_OF_BIRTH_CITY = "261"
    E_ID_PLACE_OF_BIRTH_STATE = "262"
    E_ID_PLACE_OF_BIRTH_COUNTRY = "263"
    E_ID_PLACE_OF_BIRTH_ZIP_CODE = "264"
    CDL_CLASS = "265"
    DL_UNDER_19_DATE = "266"
    WEIGHT_POUNDS = "267"
    LIMITED_DURATION_DOCUMENT_INDICATOR = "268"
    ENDORSEMENT_EXPIRATION_DATE = "269"
    REVISION_DATE = "270"
    COMPLIANCE_TYPE = "271"
    FAMILY_NAME_TRUNCATION = "272"
    FIRST_NAME_TRUNCATION = "273"
    MIDDLE_NAME_TRUNCATION = "274"
    EXAM_DATE = "275"
    ORGANIZATION = "276"
    DEPARTMENT = "277"
    PAY_GRADE = "278"
    RANK = "279"
    BENEFITS_NUMBER = "280"
    SPONSOR_SERVICE = "281"
    SPONSOR_STATUS = "282"
    SPONSOR = "283"
    RELATIONSHIP = "284"
    USCIS = "285"
    CATEGORY = "286"
    CONDITIONS = "287"
    IDENTIFIER = "288"
    CONFIGURATION = "289"
    DISCRETIONARY_DATA = "290"
    LINE_1_OPTIONAL_DATA = "291"
    LINE_2_OPTIONAL_DATA = "292"
    LINE_3_OPTIONAL_DATA = "293"
    EQV_CODE = "294"
    ALT_CODE = "295"
    BINARY_CODE = "296"
    PSEUDO_CODE = "297"
    FEE = "298"
    STAMP_NUMBER = "299"
    SBH_SECURITY_OPTIONS = "300"
    SBH_INTEGRITY_OPTIONS = "301"
    DATE_OF_CREATION = "302"
    VALIDITY_PERIOD = "303"
    PATRON_HEADER_VERSION = "304"
    BDB_TYPE = "305"
    BIOMETRIC_TYPE = "306"
    BIOMETRIC_SUBTYPE = "307"
    BIOMETRIC_PRODUCT_ID = "308"
    BIOMETRIC_FORMAT_OWNER = "309"
    BIOMETRIC_FORMAT_TYPE = "310"
    PHONE = "311"
    PROFESSION = "312"
    TITLE = "313"
    PERSONAL_SUMMARY = "314"
    OTHER_VALID_ID = "315"
    CUSTODY_INFO = "316"
    OTHER_NAME = "317"
    OBSERVATIONS = "318"
    TAX = "319"
    DATE_OF_PERSONALIZATION = "320"
    PERSONALIZATION_SN = "321"
    DATE_OF_RECORD = "322"
    PERSON_TO_NOTIFY_DATE_OF_RECORD = "323"
    PERSON_TO_NOTIFY_NAME = "324"
    PERSON_TO_NOTIFY_PHONE = "325"
    PERSON_TO_NOTIFY_ADDRESS = "326"
    DS_CERTIFICATE_ISSUER = "327"
    DS_CERTIFICATE_SUBJECT = "328"
    DS_CERTIFICATE_VALID_FROM = "329"
    DS_CERTIFICATE_VALID_TO = "330"
    VRC_DATA_OBJECT_ENTRY = "331"
    TYPE_APPROVAL_NUMBER = "332"
    ADMINISTRATIVE_NUMBER = "333"
    DOCUMENT_DISCRIMINATOR = "334"
    DATA_DISCRIMINATOR = "335"
    ISO_ISSUER_ID_NUMBER = "336"
    GNIB_NUMBER = "340"
    DEPT_NUMBER = "341"
    TELEX_CODE = "342"
    ALLERGIES = "343"
    SP_CODE = "344"
    COURT_CODE = "345"
    CTY = "346"
    SPONSOR_SSN = "347"
    DOD_NUMBER = "348"
    MC_NOVICE_DATE = "349"
    DUF_NUMBER = "350"
    AGY = "351"
    PNR_CODE = "352"
    FROM_AIRPORT_CODE = "353"
    TO_AIRPORT_CODE = "354"
    FLIGHT_NUMBER = "355"
    DATE_OF_FLIGHT = "356"
    SEAT_NUMBER = "357"
    DATE_OF_ISSUE_BOARDING_PASS = "358"
    CCW_UNTIL = "359"
    REFERENCE_NUMBER_CHECKSUM = "360"
    REFERENCE_NUMBER_CHECK_DIGIT = "361"
    ROOM_NUMBER = "362"
    RELIGION = "363"
    REMAINDER_TERM = "364"
    ELECTRONIC_TICKET_INDICATOR = "365"
    COMPARTMENT_CODE = "366"
    CHECK_IN_SEQUENCE_NUMBER = "367"
    AIRLINE_DESIGNATOR_OF_BOARDING_PASS_ISSUER = "368"
    AIRLINE_NUMERIC_CODE = "369"
    TICKET_NUMBER = "370"
    FREQUENT_FLYER_AIRLINE_DESIGNATOR = "371"
    FREQUENT_FLYER_NUMBER = "372"
    FREE_BAGGAGE_ALLOWANCE = "373"
    PDF_417_CODEC = "374"
    IDENTITY_CARD_NUMBER_CHECKSUM = "375"
    IDENTITY_CARD_NUMBER_CHECK_DIGIT = "376"
    VETERAN = "377"
    DL_CLASS_CODE_A1_FROM = "378"
    DL_CLASS_CODE_A1_TO = "379"
    DL_CLASS_CODE_A1_NOTES = "380"
    DL_CLASS_CODE_A_FROM = "381"
    DL_CLASS_CODE_A_TO = "382"
    DL_CLASS_CODE_A_NOTES = "383"
    DL_CLASS_CODE_B_FROM = "384"
    DL_CLASS_CODE_B_TO = "385"
    DL_CLASS_CODE_B_NOTES = "386"
    DL_CLASS_CODE_C1_FROM = "387"
    DL_CLASS_CODE_C1_TO = "388"
    DL_CLASS_CODE_C1_NOTES = "389"
    DL_CLASS_CODE_C_FROM = "390"
    DL_CLASS_CODE_C_TO = "391"
    DL_CLASS_CODE_C_NOTES = "392"
    DL_CLASS_CODE_D1_FROM = "393"
    DL_CLASS_CODE_D1_TO = "394"
    DL_CLASS_CODE_D1_NOTES = "395"
    DL_CLASS_CODE_D_FROM = "396"
    DL_CLASS_CODE_D_TO = "397"
    DL_CLASS_CODE_D_NOTES = "398"
    DL_CLASS_CODE_BE_FROM = "399"
    DL_CLASS_CODE_BE_TO = "400"
    DL_CLASS_CODE_BE_NOTES = "401"
    DL_CLASS_CODE_C1E_FROM = "402"
    DL_CLASS_CODE_C1E_TO = "403"
    DL_CLASS_CODE_C1E_NOTES = "404"
    DL_CLASS_CODE_CE_FROM = "405"
    DL_CLASS_CODE_CE_TO = "406"
    DL_CLASS_CODE_CE_NOTES = "407"
    DL_CLASS_CODE_D1E_FROM = "408"
    DL_CLASS_CODE_D1E_TO = "409"
    DL_CLASS_CODE_D1E_NOTES = "410"
    DL_CLASS_CODE_DE_FROM = "411"
    DL_CLASS_CODE_DE_TO = "412"
    DL_CLASS_CODE_DE_NOTES = "413"
    DL_CLASS_CODE_M_FROM = "414"
    DL_CLASS_CODE_M_TO = "415"
    DL_CLASS_CODE_M_NOTES = "416"
    DL_CLASS_CODE_L_FROM = "417"
    DL_CLASS_CODE_L_TO = "418"
    DL_CLASS_CODE_L_NOTES = "419"
    DL_CLASS_CODE_T_FROM = "420"
    DL_CLASS_CODE_T_TO = "421"
    DL_CLASS_CODE_T_NOTES = "422"
    DL_CLASS_CODE_AM_FROM = "423"
    DL_CLASS_CODE_AM_TO = "424"
    DL_CLASS_CODE_AM_NOTES = "425"
    DL_CLASS_CODE_A2_FROM = "426"
    DL_CLASS_CODE_A2_TO = "427"
    DL_CLASS_CODE_A2_NOTES = "428"
    DL_CLASS_CODE_B1_FROM = "429"
    DL_CLASS_CODE_B1_TO = "430"
    DL_CLASS_CODE_B1_NOTES = "431"
    SURNAME_AT_BIRTH = "432"
    CIVIL_STATUS = "433"
    NUMBER_OF_SEATS = "434"
    NUMBER_OF_STANDING_PLACES = "435"
    MAX_SPEED = "436"
    FUEL_TYPE = "437"
    EC_ENVIRONMENTAL_TYPE = "438"
    POWER_WEIGHT_RATIO = "439"
    MAX_MASS_OF_TRAILER_BRAKED = "440"
    MAX_MASS_OF_TRAILER_UNBRAKED = "441"
    TRANSMISSION_TYPE = "442"
    TRAILER_HITCH = "443"
    ACCOMPANIED_BY = "444"
    POLICE_DISTRICT = "445"
    FIRST_ISSUE_DATE = "446"
    PAYLOAD_CAPACITY = "447"
    NUMBER_OF_AXLES = "448"
    PERMISSIBLE_AXLE_LOAD = "449"
    PRECINCT = "450"
    INVITED_BY = "451"
    PURPOSE_OF_ENTRY = "452"
    SKIN_COLOR = "453"
    COMPLEXION = "454"
    AIRPORT_FROM = "455"
    AIRPORT_TO = "456"
    AIRLINE_NAME = "457"
    AIRLINE_NAME_FREQUENT_FLYER = "458"
    LICENSE_NUMBER = "459"
    IN_TANKS = "460"
    EXCEPT_IN_TANKS = "461"
    FAST_TRACK = "462"
    OWNER = "463"
    MRZ_STRINGS_ICAO_RFID = "464"
    NUMBER_OF_CARD_ISSUANCE = "465"
    NUMBER_OF_CARD_ISSUANCE_CHECKSUM = "466"
    NUMBER_OF_CARD_ISSUANCE_CHECK_DIGIT = "467"
    CENTURY_DATE_OF_BIRTH = "468"
    DL_CLASS_CODE_A3_FROM = "469"
    DL_CLASS_CODE_A3_TO = "470"
    DL_CLASS_CODE_A3_NOTES = "471"
    DL_CLASS_CODE_C2_FROM = "472"
    DL_CLASS_CODE_C2_TO = "473"
    DL_CLASS_CODE_C2_NOTES = "474"
    DL_CLASS_CODE_B2_FROM = "475"
    DL_CLASS_CODE_B2_TO = "476"
    DL_CLASS_CODE_B2_NOTES = "477"
    DL_CLASS_CODE_D2_FROM = "478"
    DL_CLASS_CODE_D2_TO = "479"
    DL_CLASS_CODE_D2_NOTES = "480"
    DL_CLASS_CODE_B2E_FROM = "481"
    DL_CLASS_CODE_B2E_TO = "482"
    DL_CLASS_CODE_B2E_NOTES = "483"
    DL_CLASS_CODE_G_FROM = "484"
    DL_CLASS_CODE_G_TO = "485"
    DL_CLASS_CODE_G_NOTES = "486"
    DL_CLASS_CODE_J_FROM = "487"
    DL_CLASS_CODE_J_TO = "488"
    DL_CLASS_CODE_J_NOTES = "489"
    DL_CLASS_CODE_LC_FROM = "490"
    DL_CLASS_CODE_LC_TO = "491"
    DL_CLASS_CODE_LC_NOTES = "492"
    BANK_CARD_NUMBER = "493"
    BANK_CARD_VALID_THRU = "494"
    TAX_NUMBER = "495"
    HEALTH_NUMBER = "496"
    GRANDFATHER_NAME = "497"
    SELECTEE_INDICATOR = "498"
    MOTHER_SURNAME = "499"
    MOTHER_GIVEN_NAME = "500"
    FATHER_SURNAME = "501"
    FATHER_GIVEN_NAME = "502"
    MOTHER_DATE_OF_BIRTH = "503"
    FATHER_DATE_OF_BIRTH = "504"
    MOTHER_PERSONAL_NUMBER = "505"
    FATHER_PERSONAL_NUMBER = "506"
    MOTHER_PLACE_OF_BIRTH = "507"
    FATHER_PLACE_OF_BIRTH = "508"
    MOTHER_COUNTRY_OF_BIRTH = "509"
    FATHER_COUNTRY_OF_BIRTH = "510"
    DATE_FIRST_RENEWAL = "511"
    DATE_SECOND_RENEWAL = "512"
    PLACE_OF_EXAMINATION = "513"
    APPLICATION_NUMBER = "514"
    VOUCHER_NUMBER = "515"
    AUTHORIZATION_NUMBER = "516"
    FACULTY = "517"
    FORM_OF_EDUCATION = "518"
    DNI_NUMBER = "519"
    RETIREMENT_NUMBER = "520"
    PROFESSIONAL_ID_NUMBER = "521"
    AGE_AT_ISSUE = "522"
    YEARS_SINCE_ISSUE = "523"
    DL_CLASS_CODE_BTP_FROM = "524"
    DL_CLASS_CODE_BTP_NOTES = "525"
    DL_CLASS_CODE_BTP_TO = "526"
    DL_CLASS_CODE_C3_FROM = "527"
    DL_CLASS_CODE_C3_NOTES = "528"
    DL_CLASS_CODE_C3_TO = "529"
    DL_CLASS_CODE_E_FROM = "530"
    DL_CLASS_CODE_E_NOTES = "531"
    DL_CLASS_CODE_E_TO = "532"
    DL_CLASS_CODE_F_FROM = "533"
    DL_CLASS_CODE_F_NOTES = "534"
    DL_CLASS_CODE_F_TO = "535"
    DL_CLASS_CODE_FA_FROM = "536"
    DL_CLASS_CODE_FA_NOTES = "537"
    DL_CLASS_CODE_FA_TO = "538"
    DL_CLASS_CODE_FA1_FROM = "539"
    DL_CLASS_CODE_FA1_NOTES = "540"
    DL_CLASS_CODE_FA1_TO = "541"
    DL_CLASS_CODE_FB_FROM = "542"
    DL_CLASS_CODE_FB_NOTES = "543"
    DL_CLASS_CODE_FB_TO = "544"
    DL_CLASS_CODE_G1_FROM = "545"
    DL_CLASS_CODE_G1_NOTES = "546"
    DL_CLASS_CODE_G1_TO = "547"
    DL_CLASS_CODE_H_FROM = "548"
    DL_CLASS_CODE_H_NOTES = "549"
    DL_CLASS_CODE_H_TO = "550"
    DL_CLASS_CODE_I_FROM = "551"
    DL_CLASS_CODE_I_NOTES = "552"
    DL_CLASS_CODE_I_TO = "553"
    DL_CLASS_CODE_K_FROM = "554"
    DL_CLASS_CODE_K_NOTES = "555"
    DL_CLASS_CODE_K_TO = "556"
    DL_CLASS_CODE_LK_FROM = "557"
    DL_CLASS_CODE_LK_NOTES = "558"
    DL_CLASS_CODE_LK_TO = "559"
    DL_CLASS_CODE_N_FROM = "560"
    DL_CLASS_CODE_N_NOTES = "561"
    DL_CLASS_CODE_N_TO = "562"
    DL_CLASS_CODE_S_FROM = "563"
    DL_CLASS_CODE_S_NOTES = "564"
    DL_CLASS_CODE_S_TO = "565"
    DL_CLASS_CODE_TB_FROM = "566"
    DL_CLASS_CODE_TB_NOTES = "567"
    DL_CLASS_CODE_TB_TO = "568"
    DL_CLASS_CODE_TM_FROM = "569"
    DL_CLASS_CODE_TM_NOTES = "570"
    DL_CLASS_CODE_TM_TO = "571"
    DL_CLASS_CODE_TR_FROM = "572"
    DL_CLASS_CODE_TR_NOTES = "573"
    DL_CLASS_CODE_TR_TO = "574"
    DL_CLASS_CODE_TV_FROM = "575"
    DL_CLASS_CODE_TV_NOTES = "576"
    DL_CLASS_CODE_TV_TO = "577"
    DL_CLASS_CODE_V_FROM = "578"
    DL_CLASS_CODE_V_NOTES = "579"
    DL_CLASS_CODE_V_TO = "580"
    DL_CLASS_CODE_W_FROM = "581"
    DL_CLASS_CODE_W_NOTES = "582"
    DL_CLASS_CODE_W_TO = "583"
    URL = "584"
    CALIBER = "585"
    MODEL = "586"
    MAKE = "587"
    NUMBER_OF_CYLINDERS = "588"
    SURNAME_OF_HUSBAND_AFTER_REGISTRATION = "589"
    SURNAME_OF_WIFE_AFTER_REGISTRATION = "590"
    DATE_OF_BIRTH_OF_WIFE = "591"
    DATE_OF_BIRTH_OF_HUSBAND = "592"
    CITIZENSHIP_OF_FIRST_PERSON = "593"
    CITIZENSHIP_OF_SECOND_PERSON = "594"
    CVV = "595"

    allowable_values = [DOCUMENT_CLASS_CODE, ISSUING_STATE_CODE, DOCUMENT_NUMBER, DATE_OF_EXPIRY, DATE_OF_ISSUE, DATE_OF_BIRTH, PLACE_OF_BIRTH, PERSONAL_NUMBER, SURNAME, GIVEN_NAME, MOTHERS_NAME, NATIONALITY, SEX, HEIGHT, WEIGHT, EYES_COLOR, HAIR_COLOR, ADDRESS, DONOR, SOCIAL_SECURITY_NUMBER, DL_CLASS, DL_ENDORSED, DL_RESTRICTION_CODE, DL_UNDER_21_DATE, AUTHORITY, SURNAME_AND_GIVEN_NAMES, NATIONALITY_CODE, PASSPORT_NUMBER, INVITATION_NUMBER, VISA_ID, VISA_CLASS, VISA_SUBCLASS, MRZ_TYPE, DOCUMENT_CLASS_NAME, ISSUING_STATE_NAME, PLACE_OF_ISSUE, DOCUMENT_NUMBER_CHECKSUM, DATE_OF_BIRTH_CHECKSUM, DATE_OF_EXPIRY_CHECKSUM, PERSONAL_NUMBER_CHECKSUM, FINAL_CHECKSUM, PASSPORT_NUMBER_CHECKSUM, INVITATION_NUMBER_CHECKSUM, VISA_ID_CHECKSUM, SURNAME_AND_GIVEN_NAME_CHECKSUM, VISA_VALID_UNTIL_CHECKSUM, OTHER, MRZ_STRINGS, NAME_SUFFIX, NAME_PREFIX, DATE_OF_ISSUE_CHECKSUM, DATE_OF_ISSUE_CHECK_DIGIT, DOCUMENT_SERIES, REG_CERT_REG_NUMBER, REG_CERT_CAR_MODEL, REG_CERT_CAR_COLOR, REG_CERT_BODY_NUMBER, REG_CERT_CAR_TYPE, REG_CERT_MAX_WEIGHT, REG_CERT_WEIGHT, ADDRESS_AREA, ADDRESS_STATE, ADDRESS_BUILDING, ADDRESS_HOUSE, ADDRESS_FLAT, PLACE_OF_REGISTRATION, DATE_OF_REGISTRATION, RESIDENT_FROM, RESIDENT_UNTIL, AUTHORITY_CODE, PLACE_OF_BIRTH_AREA, PLACE_OF_BIRTH_STATE_CODE, ADDRESS_STREET, ADDRESS_CITY, ADDRESS_JURISDICTION_CODE, ADDRESS_POSTAL_CODE, DOCUMENT_NUMBER_CHECK_DIGIT, DATE_OF_BIRTH_CHECK_DIGIT, DATE_OF_EXPIRY_CHECK_DIGIT, PERSONAL_NUMBER_CHECK_DIGIT, FINAL_CHECK_DIGIT, PASSPORT_NUMBER_CHECK_DIGIT, INVITATION_NUMBER_CHECK_DIGIT, VISA_ID_CHECK_DIGIT, SURNAME_AND_GIVEN_NAMES_CHECK_DIGIT, VISA_VALID_UNTIL_CHECK_DIGIT, PERMIT_DL_CLASS, PERMIT_DATE_OF_EXPIRY, PERMIT_IDENTIFIER, PERMIT_DATE_OF_ISSUE, PERMIT_RESTRICTION_CODE, PERMIT_ENDORSED, ISSUE_TIMESTAMP, NUMBER_OF_DUPLICATES, MEDICAL_INDICATOR_CODES, NON_RESIDENT_INDICATOR, VISA_TYPE, VISA_VALID_FROM, VISA_VALID_UNTIL, DURATION_OF_STAY, NUMBER_OF_ENTRIES, DAY, MONTH, YEAR, UNIQUE_CUSTOMER_IDENTIFIER, COMMERCIAL_VEHICLE_CODES, AKA_DATE_OF_BIRTH, AKA_SOCIAL_SECURITY_NUMBER, AKA_SURNAME, AKA_GIVEN_NAMES, AKA_NAME_SUFFIX, AKA_NAME_PREFIX, MAILING_ADDRESS_STREET, MAILING_ADDRESS_CITY, MAILING_ADDRESS_JURISDICTION_CODE, MAILING_ADDRESS_POSTAL_CODE, AUDIT_INFORMATION, INVENTORY_NUMBER, RACE_ETHNICITY, JURISDICTION_VEHICLE_CLASS, JURISDICTION_ENDORSEMENT_CODE, JURISDICTION_RESTRICTION_CODE, FAMILY_NAME, GIVEN_NAMES_RUS, VISA_ID_RUS, FATHERS_NAME, FATHERS_NAME_RUS, SURNAME_AND_GIVEN_NAME_RUS, PLACE_OF_BIRTH_RUS, AUTHORITY_RUS, ISSUING_STATE_CODE_NUMERIC, NATIONALITY_CODE_NUMERIC, ENGINE_POWER, ENGINE_VOLUME, CHASSIS_NUMBER, ENGINE_NUMBER, ENGINE_MODEL, VEHICLE_CATEGORY, IDENTITY_CARD_NUMBER, CONTROL_NUMBER, PARENTS_GIVEN_NAMES, SECOND_SURNAME, MIDDLE_NAME, REG_CERT_VIN, REG_CERT_VIN_CHECK_DIGIT, REG_CERT_VIN_CHECKSUM, LINE_1_CHECK_DIGIT, LINE_2_CHECK_DIGIT, LINE_3_CHECK_DIGIT, LINE_1_CHECKSUM, LINE_2_CHECKSUM, LINE_3_CHECKSUM, REG_CERT_REG_NUMBER_CHECK_DIGIT, REG_CERT_REG_NUMBER_CHECKSUM, REG_CERT_VEHICLE_ITS_CODE, CARD_ACCESS_NUMBER, MARITAL_STATUS, COMPANY_NAME, SPECIAL_NOTES, SURNAME_OF_SPOUSE, TRACKING_NUMBER, BOOKLET_NUMBER, CHILDREN, COPY_NUMBER, SERIAL_NUMBER, DOSSIER_NUMBER, AKA_SURNAME_AND_GIVEN_NAMES, TERRITORIAL_VALIDITY, MRZ_STRINGS_WITH_CORRECT_CHECK_SUMS, DL_CDL_RESTRICTION_CODE, DL_UNDER_18_DATE, DL_RECORD_CREATED, DL_DUPLICATE_DATE, DL_ISSUE_TYPE, MILITARY_BOOK_NUMBER, DESTINATION, BLOOD_GROUP, SEQUENCE_NUMBER, REG_CERT_BODY_TYPE, REG_CERT_CAR_MARK, TRANSACTION_NUMBER, AGE, FOLIO_NUMBER, VOTER_KEY, ADDRESS_MUNICIPALITY, ADDRESS_LOCATION, SECTION, OCR_NUMBER, FEDERAL_ELECTIONS, REFERENCE_NUMBER, OPTIONAL_DATA_CHECKSUM, OPTIONAL_DATA_CHECK_DIGIT, VISA_NUMBER, VISA_NUMBER_CHECKSUM, VISA_NUMBER_CHECK_DIGIT, VOTER, PREVIOUS_TYPE, FIELD_FROM_MRZ, CURRENT_DATE, STATUS_DATE_OF_EXPIRY, BANK_NOTE_NUMBER, CSC_CODE, ARTISTIC_NAME, ACADEMIC_TITLE, ADDRESS_COUNTRY, ADDRESS_ZIP_CODE, E_ID_RESIDENCE_PERMIT_1, E_ID_RESIDENCE_PERMIT_2, E_ID_PLACE_OF_BIRTH_STREET, E_ID_PLACE_OF_BIRTH_CITY, E_ID_PLACE_OF_BIRTH_STATE, E_ID_PLACE_OF_BIRTH_COUNTRY, E_ID_PLACE_OF_BIRTH_ZIP_CODE, CDL_CLASS, DL_UNDER_19_DATE, WEIGHT_POUNDS, LIMITED_DURATION_DOCUMENT_INDICATOR, ENDORSEMENT_EXPIRATION_DATE, REVISION_DATE, COMPLIANCE_TYPE, FAMILY_NAME_TRUNCATION, FIRST_NAME_TRUNCATION, MIDDLE_NAME_TRUNCATION, EXAM_DATE, ORGANIZATION, DEPARTMENT, PAY_GRADE, RANK, BENEFITS_NUMBER, SPONSOR_SERVICE, SPONSOR_STATUS, SPONSOR, RELATIONSHIP, USCIS, CATEGORY, CONDITIONS, IDENTIFIER, CONFIGURATION, DISCRETIONARY_DATA, LINE_1_OPTIONAL_DATA, LINE_2_OPTIONAL_DATA, LINE_3_OPTIONAL_DATA, EQV_CODE, ALT_CODE, BINARY_CODE, PSEUDO_CODE, FEE, STAMP_NUMBER, SBH_SECURITY_OPTIONS, SBH_INTEGRITY_OPTIONS, DATE_OF_CREATION, VALIDITY_PERIOD, PATRON_HEADER_VERSION, BDB_TYPE, BIOMETRIC_TYPE, BIOMETRIC_SUBTYPE, BIOMETRIC_PRODUCT_ID, BIOMETRIC_FORMAT_OWNER, BIOMETRIC_FORMAT_TYPE, PHONE, PROFESSION, TITLE, PERSONAL_SUMMARY, OTHER_VALID_ID, CUSTODY_INFO, OTHER_NAME, OBSERVATIONS, TAX, DATE_OF_PERSONALIZATION, PERSONALIZATION_SN, DATE_OF_RECORD, PERSON_TO_NOTIFY_DATE_OF_RECORD, PERSON_TO_NOTIFY_NAME, PERSON_TO_NOTIFY_PHONE, PERSON_TO_NOTIFY_ADDRESS, DS_CERTIFICATE_ISSUER, DS_CERTIFICATE_SUBJECT, DS_CERTIFICATE_VALID_FROM, DS_CERTIFICATE_VALID_TO, VRC_DATA_OBJECT_ENTRY, TYPE_APPROVAL_NUMBER, ADMINISTRATIVE_NUMBER, DOCUMENT_DISCRIMINATOR, DATA_DISCRIMINATOR, ISO_ISSUER_ID_NUMBER, GNIB_NUMBER, DEPT_NUMBER, TELEX_CODE, ALLERGIES, SP_CODE, COURT_CODE, CTY, SPONSOR_SSN, DOD_NUMBER, MC_NOVICE_DATE, DUF_NUMBER, AGY, PNR_CODE, FROM_AIRPORT_CODE, TO_AIRPORT_CODE, FLIGHT_NUMBER, DATE_OF_FLIGHT, SEAT_NUMBER, DATE_OF_ISSUE_BOARDING_PASS, CCW_UNTIL, REFERENCE_NUMBER_CHECKSUM, REFERENCE_NUMBER_CHECK_DIGIT, ROOM_NUMBER, RELIGION, REMAINDER_TERM, ELECTRONIC_TICKET_INDICATOR, COMPARTMENT_CODE, CHECK_IN_SEQUENCE_NUMBER, AIRLINE_DESIGNATOR_OF_BOARDING_PASS_ISSUER, AIRLINE_NUMERIC_CODE, TICKET_NUMBER, FREQUENT_FLYER_AIRLINE_DESIGNATOR, FREQUENT_FLYER_NUMBER, FREE_BAGGAGE_ALLOWANCE, PDF_417_CODEC, IDENTITY_CARD_NUMBER_CHECKSUM, IDENTITY_CARD_NUMBER_CHECK_DIGIT, VETERAN, DL_CLASS_CODE_A1_FROM, DL_CLASS_CODE_A1_TO, DL_CLASS_CODE_A1_NOTES, DL_CLASS_CODE_A_FROM, DL_CLASS_CODE_A_TO, DL_CLASS_CODE_A_NOTES, DL_CLASS_CODE_B_FROM, DL_CLASS_CODE_B_TO, DL_CLASS_CODE_B_NOTES, DL_CLASS_CODE_C1_FROM, DL_CLASS_CODE_C1_TO, DL_CLASS_CODE_C1_NOTES, DL_CLASS_CODE_C_FROM, DL_CLASS_CODE_C_TO, DL_CLASS_CODE_C_NOTES, DL_CLASS_CODE_D1_FROM, DL_CLASS_CODE_D1_TO, DL_CLASS_CODE_D1_NOTES, DL_CLASS_CODE_D_FROM, DL_CLASS_CODE_D_TO, DL_CLASS_CODE_D_NOTES, DL_CLASS_CODE_BE_FROM, DL_CLASS_CODE_BE_TO, DL_CLASS_CODE_BE_NOTES, DL_CLASS_CODE_C1E_FROM, DL_CLASS_CODE_C1E_TO, DL_CLASS_CODE_C1E_NOTES, DL_CLASS_CODE_CE_FROM, DL_CLASS_CODE_CE_TO, DL_CLASS_CODE_CE_NOTES, DL_CLASS_CODE_D1E_FROM, DL_CLASS_CODE_D1E_TO, DL_CLASS_CODE_D1E_NOTES, DL_CLASS_CODE_DE_FROM, DL_CLASS_CODE_DE_TO, DL_CLASS_CODE_DE_NOTES, DL_CLASS_CODE_M_FROM, DL_CLASS_CODE_M_TO, DL_CLASS_CODE_M_NOTES, DL_CLASS_CODE_L_FROM, DL_CLASS_CODE_L_TO, DL_CLASS_CODE_L_NOTES, DL_CLASS_CODE_T_FROM, DL_CLASS_CODE_T_TO, DL_CLASS_CODE_T_NOTES, DL_CLASS_CODE_AM_FROM, DL_CLASS_CODE_AM_TO, DL_CLASS_CODE_AM_NOTES, DL_CLASS_CODE_A2_FROM, DL_CLASS_CODE_A2_TO, DL_CLASS_CODE_A2_NOTES, DL_CLASS_CODE_B1_FROM, DL_CLASS_CODE_B1_TO, DL_CLASS_CODE_B1_NOTES, SURNAME_AT_BIRTH, CIVIL_STATUS, NUMBER_OF_SEATS, NUMBER_OF_STANDING_PLACES, MAX_SPEED, FUEL_TYPE, EC_ENVIRONMENTAL_TYPE, POWER_WEIGHT_RATIO, MAX_MASS_OF_TRAILER_BRAKED, MAX_MASS_OF_TRAILER_UNBRAKED, TRANSMISSION_TYPE, TRAILER_HITCH, ACCOMPANIED_BY, POLICE_DISTRICT, FIRST_ISSUE_DATE, PAYLOAD_CAPACITY, NUMBER_OF_AXLES, PERMISSIBLE_AXLE_LOAD, PRECINCT, INVITED_BY, PURPOSE_OF_ENTRY, SKIN_COLOR, COMPLEXION, AIRPORT_FROM, AIRPORT_TO, AIRLINE_NAME, AIRLINE_NAME_FREQUENT_FLYER, LICENSE_NUMBER, IN_TANKS, EXCEPT_IN_TANKS, FAST_TRACK, OWNER, MRZ_STRINGS_ICAO_RFID, NUMBER_OF_CARD_ISSUANCE, NUMBER_OF_CARD_ISSUANCE_CHECKSUM, NUMBER_OF_CARD_ISSUANCE_CHECK_DIGIT, CENTURY_DATE_OF_BIRTH, DL_CLASS_CODE_A3_FROM, DL_CLASS_CODE_A3_TO, DL_CLASS_CODE_A3_NOTES, DL_CLASS_CODE_C2_FROM, DL_CLASS_CODE_C2_TO, DL_CLASS_CODE_C2_NOTES, DL_CLASS_CODE_B2_FROM, DL_CLASS_CODE_B2_TO, DL_CLASS_CODE_B2_NOTES, DL_CLASS_CODE_D2_FROM, DL_CLASS_CODE_D2_TO, DL_CLASS_CODE_D2_NOTES, DL_CLASS_CODE_B2E_FROM, DL_CLASS_CODE_B2E_TO, DL_CLASS_CODE_B2E_NOTES, DL_CLASS_CODE_G_FROM, DL_CLASS_CODE_G_TO, DL_CLASS_CODE_G_NOTES, DL_CLASS_CODE_J_FROM, DL_CLASS_CODE_J_TO, DL_CLASS_CODE_J_NOTES, DL_CLASS_CODE_LC_FROM, DL_CLASS_CODE_LC_TO, DL_CLASS_CODE_LC_NOTES, BANK_CARD_NUMBER, BANK_CARD_VALID_THRU, TAX_NUMBER, HEALTH_NUMBER, GRANDFATHER_NAME, SELECTEE_INDICATOR, MOTHER_SURNAME, MOTHER_GIVEN_NAME, FATHER_SURNAME, FATHER_GIVEN_NAME, MOTHER_DATE_OF_BIRTH, FATHER_DATE_OF_BIRTH, MOTHER_PERSONAL_NUMBER, FATHER_PERSONAL_NUMBER, MOTHER_PLACE_OF_BIRTH, FATHER_PLACE_OF_BIRTH, MOTHER_COUNTRY_OF_BIRTH, FATHER_COUNTRY_OF_BIRTH, DATE_FIRST_RENEWAL, DATE_SECOND_RENEWAL, PLACE_OF_EXAMINATION, APPLICATION_NUMBER, VOUCHER_NUMBER, AUTHORIZATION_NUMBER, FACULTY, FORM_OF_EDUCATION, DNI_NUMBER, RETIREMENT_NUMBER, PROFESSIONAL_ID_NUMBER, AGE_AT_ISSUE, YEARS_SINCE_ISSUE, DL_CLASS_CODE_BTP_FROM, DL_CLASS_CODE_BTP_NOTES, DL_CLASS_CODE_BTP_TO, DL_CLASS_CODE_C3_FROM, DL_CLASS_CODE_C3_NOTES, DL_CLASS_CODE_C3_TO, DL_CLASS_CODE_E_FROM, DL_CLASS_CODE_E_NOTES, DL_CLASS_CODE_E_TO, DL_CLASS_CODE_F_FROM, DL_CLASS_CODE_F_NOTES, DL_CLASS_CODE_F_TO, DL_CLASS_CODE_FA_FROM, DL_CLASS_CODE_FA_NOTES, DL_CLASS_CODE_FA_TO, DL_CLASS_CODE_FA1_FROM, DL_CLASS_CODE_FA1_NOTES, DL_CLASS_CODE_FA1_TO, DL_CLASS_CODE_FB_FROM, DL_CLASS_CODE_FB_NOTES, DL_CLASS_CODE_FB_TO, DL_CLASS_CODE_G1_FROM, DL_CLASS_CODE_G1_NOTES, DL_CLASS_CODE_G1_TO, DL_CLASS_CODE_H_FROM, DL_CLASS_CODE_H_NOTES, DL_CLASS_CODE_H_TO, DL_CLASS_CODE_I_FROM, DL_CLASS_CODE_I_NOTES, DL_CLASS_CODE_I_TO, DL_CLASS_CODE_K_FROM, DL_CLASS_CODE_K_NOTES, DL_CLASS_CODE_K_TO, DL_CLASS_CODE_LK_FROM, DL_CLASS_CODE_LK_NOTES, DL_CLASS_CODE_LK_TO, DL_CLASS_CODE_N_FROM, DL_CLASS_CODE_N_NOTES, DL_CLASS_CODE_N_TO, DL_CLASS_CODE_S_FROM, DL_CLASS_CODE_S_NOTES, DL_CLASS_CODE_S_TO, DL_CLASS_CODE_TB_FROM, DL_CLASS_CODE_TB_NOTES, DL_CLASS_CODE_TB_TO, DL_CLASS_CODE_TM_FROM, DL_CLASS_CODE_TM_NOTES, DL_CLASS_CODE_TM_TO, DL_CLASS_CODE_TR_FROM, DL_CLASS_CODE_TR_NOTES, DL_CLASS_CODE_TR_TO, DL_CLASS_CODE_TV_FROM, DL_CLASS_CODE_TV_NOTES, DL_CLASS_CODE_TV_TO, DL_CLASS_CODE_V_FROM, DL_CLASS_CODE_V_NOTES, DL_CLASS_CODE_V_TO, DL_CLASS_CODE_W_FROM, DL_CLASS_CODE_W_NOTES, DL_CLASS_CODE_W_TO, URL, CALIBER, MODEL, MAKE, NUMBER_OF_CYLINDERS, SURNAME_OF_HUSBAND_AFTER_REGISTRATION, SURNAME_OF_WIFE_AFTER_REGISTRATION, DATE_OF_BIRTH_OF_WIFE, DATE_OF_BIRTH_OF_HUSBAND, CITIZENSHIP_OF_FIRST_PERSON, CITIZENSHIP_OF_SECOND_PERSON, CVV]  # noqa: E501

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
        """TextFieldType - a model defined in OpenAPI"""  # noqa: E501
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
        if not isinstance(other, TextFieldType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextFieldType):
            return True

        return self.to_dict() != other.to_dict()