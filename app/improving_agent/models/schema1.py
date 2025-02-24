# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent.models.operation_lookup import OperationLookup
from improving_agent import util

from improving_agent.models.operation_lookup import OperationLookup  # noqa: E501


class Schema1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, parameters=None):  # noqa: E501
        """Schema1 - a model defined in OpenAPI

        :param id: The id of this Schema1.  # noqa: E501
        :type id: str
        :param parameters: The parameters of this Schema1.  # noqa: E501
        :type parameters: dict
        """
        self.openapi_types = {
            'id': str,
            'parameters': dict
        }

        self.attribute_map = {
            'id': 'id',
            'parameters': 'parameters'
        }

        self._id = id
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'Schema1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The schema_1 of this Schema1.  # noqa: E501
        :rtype: Schema1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Schema1.


        :return: The id of this Schema1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schema1.


        :param id: The id of this Schema1.
        :type id: str
        """
        allowed_values = ["sort_results_score"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this Schema1.


        :return: The parameters of this Schema1.
        :rtype: dict
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Schema1.


        :param parameters: The parameters of this Schema1.
        :type parameters: dict
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
