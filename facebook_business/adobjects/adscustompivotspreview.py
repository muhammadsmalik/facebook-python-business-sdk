# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsCustomPivotsPreview(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdsCustomPivotsPreview, self).__init__()
        self._isAdsCustomPivotsPreview = True
        self._api = api

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        account_name = 'account_name'
        ad_id = 'ad_id'
        ad_name = 'ad_name'
        adset_id = 'adset_id'
        adset_name = 'adset_name'
        campaign_id = 'campaign_id'
        campaign_name = 'campaign_name'
        custom_breakdown = 'custom_breakdown'

    _field_types = {
        'account_id': 'string',
        'account_name': 'string',
        'ad_id': 'string',
        'ad_name': 'string',
        'adset_id': 'string',
        'adset_name': 'string',
        'campaign_id': 'string',
        'campaign_name': 'string',
        'custom_breakdown': 'list<string>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


