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


class DetailsRFID(object):
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
        'overall_status': 'CheckResult',
        'aa': 'CheckResult',
        'bac': 'CheckResult',
        'ca': 'CheckResult',
        'pa': 'CheckResult',
        'pace': 'CheckResult',
        'ta': 'CheckResult'
    }

    attribute_map = {
        'overall_status': 'overallStatus',
        'aa': 'AA',
        'bac': 'BAC',
        'ca': 'CA',
        'pa': 'PA',
        'pace': 'PACE',
        'ta': 'TA'
    }

    def __init__(self, overall_status=None, aa=None, bac=None, ca=None, pa=None, pace=None, ta=None, local_vars_configuration=None):  # noqa: E501
        """DetailsRFID - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_status = None
        self._aa = None
        self._bac = None
        self._ca = None
        self._pa = None
        self._pace = None
        self._ta = None
        self.discriminator = None

        self.overall_status = overall_status
        self.aa = aa
        self.bac = bac
        self.ca = ca
        self.pa = pa
        self.pace = pace
        self.ta = ta

    @property
    def overall_status(self):
        """Gets the overall_status of this DetailsRFID.  # noqa: E501


        :return: The overall_status of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this DetailsRFID.


        :param overall_status: The overall_status of this DetailsRFID.  # noqa: E501
        :type overall_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and overall_status is None:  # noqa: E501
            raise ValueError("Invalid value for `overall_status`, must not be `None`")  # noqa: E501

        self._overall_status = overall_status

    @property
    def aa(self):
        """Gets the aa of this DetailsRFID.  # noqa: E501


        :return: The aa of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._aa

    @aa.setter
    def aa(self, aa):
        """Sets the aa of this DetailsRFID.


        :param aa: The aa of this DetailsRFID.  # noqa: E501
        :type aa: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and aa is None:  # noqa: E501
            raise ValueError("Invalid value for `aa`, must not be `None`")  # noqa: E501

        self._aa = aa

    @property
    def bac(self):
        """Gets the bac of this DetailsRFID.  # noqa: E501


        :return: The bac of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._bac

    @bac.setter
    def bac(self, bac):
        """Sets the bac of this DetailsRFID.


        :param bac: The bac of this DetailsRFID.  # noqa: E501
        :type bac: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and bac is None:  # noqa: E501
            raise ValueError("Invalid value for `bac`, must not be `None`")  # noqa: E501

        self._bac = bac

    @property
    def ca(self):
        """Gets the ca of this DetailsRFID.  # noqa: E501


        :return: The ca of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this DetailsRFID.


        :param ca: The ca of this DetailsRFID.  # noqa: E501
        :type ca: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and ca is None:  # noqa: E501
            raise ValueError("Invalid value for `ca`, must not be `None`")  # noqa: E501

        self._ca = ca

    @property
    def pa(self):
        """Gets the pa of this DetailsRFID.  # noqa: E501


        :return: The pa of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._pa

    @pa.setter
    def pa(self, pa):
        """Sets the pa of this DetailsRFID.


        :param pa: The pa of this DetailsRFID.  # noqa: E501
        :type pa: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and pa is None:  # noqa: E501
            raise ValueError("Invalid value for `pa`, must not be `None`")  # noqa: E501

        self._pa = pa

    @property
    def pace(self):
        """Gets the pace of this DetailsRFID.  # noqa: E501


        :return: The pace of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._pace

    @pace.setter
    def pace(self, pace):
        """Sets the pace of this DetailsRFID.


        :param pace: The pace of this DetailsRFID.  # noqa: E501
        :type pace: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and pace is None:  # noqa: E501
            raise ValueError("Invalid value for `pace`, must not be `None`")  # noqa: E501

        self._pace = pace

    @property
    def ta(self):
        """Gets the ta of this DetailsRFID.  # noqa: E501


        :return: The ta of this DetailsRFID.  # noqa: E501
        :rtype: CheckResult
        """
        return self._ta

    @ta.setter
    def ta(self, ta):
        """Sets the ta of this DetailsRFID.


        :param ta: The ta of this DetailsRFID.  # noqa: E501
        :type ta: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and ta is None:  # noqa: E501
            raise ValueError("Invalid value for `ta`, must not be `None`")  # noqa: E501

        self._ta = ta

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
        if not isinstance(other, DetailsRFID):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailsRFID):
            return True

        return self.to_dict() != other.to_dict()