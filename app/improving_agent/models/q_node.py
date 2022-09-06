# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from improving_agent.models.base_model_ import Model
from improving_agent.models.attribute_constraint import AttributeConstraint
from improving_agent import util

from improving_agent.models.attribute_constraint import AttributeConstraint  # noqa: E501

class QNode(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids=None, categories=None, is_set=False, constraints=[]):  # noqa: E501
        """QNode - a model defined in OpenAPI

        :param ids: The ids of this QNode.  # noqa: E501
        :type ids: List[str]
        :param categories: The categories of this QNode.  # noqa: E501
        :type categories: List[str]
        :param is_set: The is_set of this QNode.  # noqa: E501
        :type is_set: bool
        :param constraints: The constraints of this QNode.  # noqa: E501
        :type constraints: List[AttributeConstraint]
        """
        self.openapi_types = {
            'ids': List[str],
            'categories': List[str],
            'is_set': bool,
            'constraints': List[AttributeConstraint]
        }

        self.attribute_map = {
            'ids': 'ids',
            'categories': 'categories',
            'is_set': 'is_set',
            'constraints': 'constraints'
        }

        self._ids = ids
        self._categories = categories
        self._is_set = is_set
        self._constraints = constraints

    @classmethod
    def from_dict(cls, dikt) -> 'QNode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QNode of this QNode.  # noqa: E501
        :rtype: QNode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this QNode.

        CURIE identifier for this node  # noqa: E501

        :return: The ids of this QNode.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this QNode.

        CURIE identifier for this node  # noqa: E501

        :param ids: The ids of this QNode.
        :type ids: List[str]
        """
        if ids is not None and len(ids) < 1:
            raise ValueError("Invalid value for `ids`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ids = ids

    @property
    def categories(self):
        """Gets the categories of this QNode.


        :return: The categories of this QNode.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this QNode.


        :param categories: The categories of this QNode.
        :type categories: List[str]
        """
        if categories is not None and len(categories) < 1:
            raise ValueError("Invalid value for `categories`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._categories = categories

    @property
    def is_set(self):
        """Gets the is_set of this QNode.

        Boolean that if set to true, indicates that this QNode MAY have multiple KnowledgeGraph Nodes bound to it within each Result. The nodes in a set should be considered as a set of independent nodes, rather than a set of dependent nodes, i.e., the answer would still be valid if the nodes in the set were instead returned individually. Multiple QNodes may have is_set=True. If a QNode (n1) with is_set=True is connected to a QNode (n2) with is_set=False, each n1 must be connected to n2. If a QNode (n1) with is_set=True is connected to a QNode (n2) with is_set=True, each n1 must be connected to at least one n2.  # noqa: E501

        :return: The is_set of this QNode.
        :rtype: bool
        """
        return self._is_set

    @is_set.setter
    def is_set(self, is_set):
        """Sets the is_set of this QNode.

        Boolean that if set to true, indicates that this QNode MAY have multiple KnowledgeGraph Nodes bound to it within each Result. The nodes in a set should be considered as a set of independent nodes, rather than a set of dependent nodes, i.e., the answer would still be valid if the nodes in the set were instead returned individually. Multiple QNodes may have is_set=True. If a QNode (n1) with is_set=True is connected to a QNode (n2) with is_set=False, each n1 must be connected to n2. If a QNode (n1) with is_set=True is connected to a QNode (n2) with is_set=True, each n1 must be connected to at least one n2.  # noqa: E501

        :param is_set: The is_set of this QNode.
        :type is_set: bool
        """

        self._is_set = is_set

    @property
    def constraints(self):
        """Gets the constraints of this QNode.

        A list of contraints applied to a query node. If there are multiple items, they must all be true (equivalent to AND)  # noqa: E501

        :return: The constraints of this QNode.
        :rtype: List[AttributeConstraint]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this QNode.

        A list of contraints applied to a query node. If there are multiple items, they must all be true (equivalent to AND)  # noqa: E501

        :param constraints: The constraints of this QNode.
        :type constraints: List[AttributeConstraint]
        """

        self._constraints = constraints
