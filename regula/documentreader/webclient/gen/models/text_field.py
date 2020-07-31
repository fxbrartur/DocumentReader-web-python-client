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


class TextField(object):
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
        'field_type': 'TextFieldType',
        'lcid': 'LCID',
        'status': 'CheckResult',
        'validity_status': 'CheckResult',
        'comparison_status': 'CheckResult',
        'value': 'str',
        'value_list': 'list[TextFieldValue]',
        'validity_list': 'list[SourceValidity]',
        'comparison_list': 'list[CrossSourceValueComparison]'
    }

    attribute_map = {
        'field_type': 'fieldType',
        'lcid': 'lcid',
        'status': 'status',
        'validity_status': 'validityStatus',
        'comparison_status': 'comparisonStatus',
        'value': 'value',
        'value_list': 'valueList',
        'validity_list': 'validityList',
        'comparison_list': 'comparisonList'
    }

    def __init__(self, field_type=None, lcid=None, status=None, validity_status=None, comparison_status=None, value=None, value_list=None, validity_list=None, comparison_list=None, local_vars_configuration=None):  # noqa: E501
        """TextField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field_type = None
        self._lcid = None
        self._status = None
        self._validity_status = None
        self._comparison_status = None
        self._value = None
        self._value_list = None
        self._validity_list = None
        self._comparison_list = None
        self.discriminator = None

        self.field_type = field_type
        if lcid is not None:
            self.lcid = lcid
        self.status = status
        self.validity_status = validity_status
        self.comparison_status = comparison_status
        self.value = value
        self.value_list = value_list
        self.validity_list = validity_list
        self.comparison_list = comparison_list

    @property
    def field_type(self):
        """Gets the field_type of this TextField.  # noqa: E501


        :return: The field_type of this TextField.  # noqa: E501
        :rtype: TextFieldType
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this TextField.


        :param field_type: The field_type of this TextField.  # noqa: E501
        :type field_type: TextFieldType
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def lcid(self):
        """Gets the lcid of this TextField.  # noqa: E501


        :return: The lcid of this TextField.  # noqa: E501
        :rtype: LCID
        """
        return self._lcid

    @lcid.setter
    def lcid(self, lcid):
        """Sets the lcid of this TextField.


        :param lcid: The lcid of this TextField.  # noqa: E501
        :type lcid: LCID
        """

        self._lcid = lcid

    @property
    def status(self):
        """Gets the status of this TextField.  # noqa: E501


        :return: The status of this TextField.  # noqa: E501
        :rtype: CheckResult
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TextField.


        :param status: The status of this TextField.  # noqa: E501
        :type status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def validity_status(self):
        """Gets the validity_status of this TextField.  # noqa: E501


        :return: The validity_status of this TextField.  # noqa: E501
        :rtype: CheckResult
        """
        return self._validity_status

    @validity_status.setter
    def validity_status(self, validity_status):
        """Sets the validity_status of this TextField.


        :param validity_status: The validity_status of this TextField.  # noqa: E501
        :type validity_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and validity_status is None:  # noqa: E501
            raise ValueError("Invalid value for `validity_status`, must not be `None`")  # noqa: E501

        self._validity_status = validity_status

    @property
    def comparison_status(self):
        """Gets the comparison_status of this TextField.  # noqa: E501


        :return: The comparison_status of this TextField.  # noqa: E501
        :rtype: CheckResult
        """
        return self._comparison_status

    @comparison_status.setter
    def comparison_status(self, comparison_status):
        """Sets the comparison_status of this TextField.


        :param comparison_status: The comparison_status of this TextField.  # noqa: E501
        :type comparison_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and comparison_status is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_status`, must not be `None`")  # noqa: E501

        self._comparison_status = comparison_status

    @property
    def value(self):
        """Gets the value of this TextField.  # noqa: E501

        The most confidence value, selected from valueList  # noqa: E501

        :return: The value of this TextField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TextField.

        The most confidence value, selected from valueList  # noqa: E501

        :param value: The value of this TextField.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def value_list(self):
        """Gets the value_list of this TextField.  # noqa: E501


        :return: The value_list of this TextField.  # noqa: E501
        :rtype: list[TextFieldValue]
        """
        return self._value_list

    @value_list.setter
    def value_list(self, value_list):
        """Sets the value_list of this TextField.


        :param value_list: The value_list of this TextField.  # noqa: E501
        :type value_list: list[TextFieldValue]
        """
        if self.local_vars_configuration.client_side_validation and value_list is None:  # noqa: E501
            raise ValueError("Invalid value for `value_list`, must not be `None`")  # noqa: E501

        self._value_list = value_list

    @property
    def validity_list(self):
        """Gets the validity_list of this TextField.  # noqa: E501

        Validity of all field values for given source. If there are two values on different pages for one field-source pair, then validity also will include logical match checking. If such values do not match, validity will return error.  # noqa: E501

        :return: The validity_list of this TextField.  # noqa: E501
        :rtype: list[SourceValidity]
        """
        return self._validity_list

    @validity_list.setter
    def validity_list(self, validity_list):
        """Sets the validity_list of this TextField.

        Validity of all field values for given source. If there are two values on different pages for one field-source pair, then validity also will include logical match checking. If such values do not match, validity will return error.  # noqa: E501

        :param validity_list: The validity_list of this TextField.  # noqa: E501
        :type validity_list: list[SourceValidity]
        """
        if self.local_vars_configuration.client_side_validation and validity_list is None:  # noqa: E501
            raise ValueError("Invalid value for `validity_list`, must not be `None`")  # noqa: E501

        self._validity_list = validity_list

    @property
    def comparison_list(self):
        """Gets the comparison_list of this TextField.  # noqa: E501


        :return: The comparison_list of this TextField.  # noqa: E501
        :rtype: list[CrossSourceValueComparison]
        """
        return self._comparison_list

    @comparison_list.setter
    def comparison_list(self, comparison_list):
        """Sets the comparison_list of this TextField.


        :param comparison_list: The comparison_list of this TextField.  # noqa: E501
        :type comparison_list: list[CrossSourceValueComparison]
        """
        if self.local_vars_configuration.client_side_validation and comparison_list is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_list`, must not be `None`")  # noqa: E501

        self._comparison_list = comparison_list

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
        if not isinstance(other, TextField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextField):
            return True

        return self.to_dict() != other.to_dict()
