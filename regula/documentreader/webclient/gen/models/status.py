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


class Status(object):
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
        'optical': 'CheckResult',
        'portrait': 'CheckResult',
        'rfid': 'CheckResult',
        'stop_list': 'CheckResult',
        'details_rfid': 'DetailsRFID',
        'details_optical': 'DetailsOptical'
    }

    attribute_map = {
        'overall_status': 'overallStatus',
        'optical': 'optical',
        'portrait': 'portrait',
        'rfid': 'rfid',
        'stop_list': 'stopList',
        'details_rfid': 'detailsRFID',
        'details_optical': 'detailsOptical'
    }

    def __init__(self, overall_status=None, optical=None, portrait=None, rfid=None, stop_list=None, details_rfid=None, details_optical=None, local_vars_configuration=None):  # noqa: E501
        """Status - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_status = None
        self._optical = None
        self._portrait = None
        self._rfid = None
        self._stop_list = None
        self._details_rfid = None
        self._details_optical = None
        self.discriminator = None

        self.overall_status = overall_status
        self.optical = optical
        if portrait is not None:
            self.portrait = portrait
        if rfid is not None:
            self.rfid = rfid
        if stop_list is not None:
            self.stop_list = stop_list
        if details_rfid is not None:
            self.details_rfid = details_rfid
        self.details_optical = details_optical

    @property
    def overall_status(self):
        """Gets the overall_status of this Status.  # noqa: E501


        :return: The overall_status of this Status.  # noqa: E501
        :rtype: CheckResult
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this Status.


        :param overall_status: The overall_status of this Status.  # noqa: E501
        :type overall_status: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and overall_status is None:  # noqa: E501
            raise ValueError("Invalid value for `overall_status`, must not be `None`")  # noqa: E501

        self._overall_status = overall_status

    @property
    def optical(self):
        """Gets the optical of this Status.  # noqa: E501


        :return: The optical of this Status.  # noqa: E501
        :rtype: CheckResult
        """
        return self._optical

    @optical.setter
    def optical(self, optical):
        """Sets the optical of this Status.


        :param optical: The optical of this Status.  # noqa: E501
        :type optical: CheckResult
        """
        if self.local_vars_configuration.client_side_validation and optical is None:  # noqa: E501
            raise ValueError("Invalid value for `optical`, must not be `None`")  # noqa: E501

        self._optical = optical

    @property
    def portrait(self):
        """Gets the portrait of this Status.  # noqa: E501


        :return: The portrait of this Status.  # noqa: E501
        :rtype: CheckResult
        """
        return self._portrait

    @portrait.setter
    def portrait(self, portrait):
        """Sets the portrait of this Status.


        :param portrait: The portrait of this Status.  # noqa: E501
        :type portrait: CheckResult
        """

        self._portrait = portrait

    @property
    def rfid(self):
        """Gets the rfid of this Status.  # noqa: E501


        :return: The rfid of this Status.  # noqa: E501
        :rtype: CheckResult
        """
        return self._rfid

    @rfid.setter
    def rfid(self, rfid):
        """Sets the rfid of this Status.


        :param rfid: The rfid of this Status.  # noqa: E501
        :type rfid: CheckResult
        """

        self._rfid = rfid

    @property
    def stop_list(self):
        """Gets the stop_list of this Status.  # noqa: E501


        :return: The stop_list of this Status.  # noqa: E501
        :rtype: CheckResult
        """
        return self._stop_list

    @stop_list.setter
    def stop_list(self, stop_list):
        """Sets the stop_list of this Status.


        :param stop_list: The stop_list of this Status.  # noqa: E501
        :type stop_list: CheckResult
        """

        self._stop_list = stop_list

    @property
    def details_rfid(self):
        """Gets the details_rfid of this Status.  # noqa: E501


        :return: The details_rfid of this Status.  # noqa: E501
        :rtype: DetailsRFID
        """
        return self._details_rfid

    @details_rfid.setter
    def details_rfid(self, details_rfid):
        """Sets the details_rfid of this Status.


        :param details_rfid: The details_rfid of this Status.  # noqa: E501
        :type details_rfid: DetailsRFID
        """

        self._details_rfid = details_rfid

    @property
    def details_optical(self):
        """Gets the details_optical of this Status.  # noqa: E501


        :return: The details_optical of this Status.  # noqa: E501
        :rtype: DetailsOptical
        """
        return self._details_optical

    @details_optical.setter
    def details_optical(self, details_optical):
        """Sets the details_optical of this Status.


        :param details_optical: The details_optical of this Status.  # noqa: E501
        :type details_optical: DetailsOptical
        """
        if self.local_vars_configuration.client_side_validation and details_optical is None:  # noqa: E501
            raise ValueError("Invalid value for `details_optical`, must not be `None`")  # noqa: E501

        self._details_optical = details_optical

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
        if not isinstance(other, Status):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Status):
            return True

        return self.to_dict() != other.to_dict()