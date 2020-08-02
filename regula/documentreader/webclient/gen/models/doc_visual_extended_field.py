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


class DocVisualExtendedField(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'w_field_type': 'TextFieldType',
        'w_lcid': 'LCID',
        'strings_result': 'list[StringRecognitionResult]',
        'buf_text': 'str',
        'field_rect': 'RectangleCoordinates',
        'rfid_origin_dg': 'int',
        'rfid_origin_tag_entry': 'int'
    }

    attribute_map = {
        'w_field_type': 'wFieldType',
        'w_lcid': 'wLCID',
        'strings_result': 'StringsResult',
        'buf_text': 'Buf_Text',
        'field_rect': 'FieldRect',
        'rfid_origin_dg': 'RFID_OriginDG',
        'rfid_origin_tag_entry': 'RFID_OriginTagEntry'
    }

    def __init__(self, w_field_type=None, w_lcid=None, strings_result=None, buf_text=None, field_rect=None, rfid_origin_dg=None, rfid_origin_tag_entry=None, local_vars_configuration=None):  # noqa: E501
        """DocVisualExtendedField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._w_field_type = None
        self._w_lcid = None
        self._strings_result = None
        self._buf_text = None
        self._field_rect = None
        self._rfid_origin_dg = None
        self._rfid_origin_tag_entry = None
        self.discriminator = None

        self.w_field_type = w_field_type
        self.w_lcid = w_lcid
        if strings_result is not None:
            self.strings_result = strings_result
        self.buf_text = buf_text
        if field_rect is not None:
            self.field_rect = field_rect
        if rfid_origin_dg is not None:
            self.rfid_origin_dg = rfid_origin_dg
        if rfid_origin_tag_entry is not None:
            self.rfid_origin_tag_entry = rfid_origin_tag_entry

    @property
    def w_field_type(self):
        """Gets the w_field_type of this DocVisualExtendedField.  # noqa: E501


        :return: The w_field_type of this DocVisualExtendedField.  # noqa: E501
        :rtype: TextFieldType
        """
        return self._w_field_type

    @w_field_type.setter
    def w_field_type(self, w_field_type):
        """Sets the w_field_type of this DocVisualExtendedField.


        :param w_field_type: The w_field_type of this DocVisualExtendedField.  # noqa: E501
        :type w_field_type: TextFieldType
        """
        if self.local_vars_configuration.client_side_validation and w_field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `w_field_type`, must not be `None`")  # noqa: E501

        self._w_field_type = w_field_type

    @property
    def w_lcid(self):
        """Gets the w_lcid of this DocVisualExtendedField.  # noqa: E501


        :return: The w_lcid of this DocVisualExtendedField.  # noqa: E501
        :rtype: LCID
        """
        return self._w_lcid

    @w_lcid.setter
    def w_lcid(self, w_lcid):
        """Sets the w_lcid of this DocVisualExtendedField.


        :param w_lcid: The w_lcid of this DocVisualExtendedField.  # noqa: E501
        :type w_lcid: LCID
        """
        if self.local_vars_configuration.client_side_validation and w_lcid is None:  # noqa: E501
            raise ValueError("Invalid value for `w_lcid`, must not be `None`")  # noqa: E501

        self._w_lcid = w_lcid

    @property
    def strings_result(self):
        """Gets the strings_result of this DocVisualExtendedField.  # noqa: E501

        Array of recognizing probabilities for a each line of text field. Only for Result.VISUAL_TEXT and Result.MRZ_TEXT results.  # noqa: E501

        :return: The strings_result of this DocVisualExtendedField.  # noqa: E501
        :rtype: list[StringRecognitionResult]
        """
        return self._strings_result

    @strings_result.setter
    def strings_result(self, strings_result):
        """Sets the strings_result of this DocVisualExtendedField.

        Array of recognizing probabilities for a each line of text field. Only for Result.VISUAL_TEXT and Result.MRZ_TEXT results.  # noqa: E501

        :param strings_result: The strings_result of this DocVisualExtendedField.  # noqa: E501
        :type strings_result: list[StringRecognitionResult]
        """

        self._strings_result = strings_result

    @property
    def buf_text(self):
        """Gets the buf_text of this DocVisualExtendedField.  # noqa: E501

        Text field data in UTF8 format. Results of reading different lines of a multi-line field are separated by '^'  # noqa: E501

        :return: The buf_text of this DocVisualExtendedField.  # noqa: E501
        :rtype: str
        """
        return self._buf_text

    @buf_text.setter
    def buf_text(self, buf_text):
        """Sets the buf_text of this DocVisualExtendedField.

        Text field data in UTF8 format. Results of reading different lines of a multi-line field are separated by '^'  # noqa: E501

        :param buf_text: The buf_text of this DocVisualExtendedField.  # noqa: E501
        :type buf_text: str
        """
        if self.local_vars_configuration.client_side_validation and buf_text is None:  # noqa: E501
            raise ValueError("Invalid value for `buf_text`, must not be `None`")  # noqa: E501

        self._buf_text = buf_text

    @property
    def field_rect(self):
        """Gets the field_rect of this DocVisualExtendedField.  # noqa: E501


        :return: The field_rect of this DocVisualExtendedField.  # noqa: E501
        :rtype: RectangleCoordinates
        """
        return self._field_rect

    @field_rect.setter
    def field_rect(self, field_rect):
        """Sets the field_rect of this DocVisualExtendedField.


        :param field_rect: The field_rect of this DocVisualExtendedField.  # noqa: E501
        :type field_rect: RectangleCoordinates
        """

        self._field_rect = field_rect

    @property
    def rfid_origin_dg(self):
        """Gets the rfid_origin_dg of this DocVisualExtendedField.  # noqa: E501

        Origin data group information. Only for Result.RFID_TEXT results.  # noqa: E501

        :return: The rfid_origin_dg of this DocVisualExtendedField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_dg

    @rfid_origin_dg.setter
    def rfid_origin_dg(self, rfid_origin_dg):
        """Sets the rfid_origin_dg of this DocVisualExtendedField.

        Origin data group information. Only for Result.RFID_TEXT results.  # noqa: E501

        :param rfid_origin_dg: The rfid_origin_dg of this DocVisualExtendedField.  # noqa: E501
        :type rfid_origin_dg: int
        """

        self._rfid_origin_dg = rfid_origin_dg

    @property
    def rfid_origin_tag_entry(self):
        """Gets the rfid_origin_tag_entry of this DocVisualExtendedField.  # noqa: E501

        Index of the text field record in origin data group. Only for Result.RFID_TEXT results.  # noqa: E501

        :return: The rfid_origin_tag_entry of this DocVisualExtendedField.  # noqa: E501
        :rtype: int
        """
        return self._rfid_origin_tag_entry

    @rfid_origin_tag_entry.setter
    def rfid_origin_tag_entry(self, rfid_origin_tag_entry):
        """Sets the rfid_origin_tag_entry of this DocVisualExtendedField.

        Index of the text field record in origin data group. Only for Result.RFID_TEXT results.  # noqa: E501

        :param rfid_origin_tag_entry: The rfid_origin_tag_entry of this DocVisualExtendedField.  # noqa: E501
        :type rfid_origin_tag_entry: int
        """

        self._rfid_origin_tag_entry = rfid_origin_tag_entry

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
        if not isinstance(other, DocVisualExtendedField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocVisualExtendedField):
            return True

        return self.to_dict() != other.to_dict()
