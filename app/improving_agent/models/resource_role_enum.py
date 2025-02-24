# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent import util


class ResourceRoleEnum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PRIMARY_KNOWLEDGE_SOURCE = "primary_knowledge_source"
    AGGREGATOR_KNOWLEDGE_SOURCE = "aggregator_knowledge_source"
    SUPPORTING_DATA_SOURCE = "supporting_data_source"
    def __init__(self):  # noqa: E501
        """ResourceRoleEnum - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceRoleEnum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceRoleEnum of this ResourceRoleEnum.  # noqa: E501
        :rtype: ResourceRoleEnum
        """
        return util.deserialize_model(dikt, cls)
