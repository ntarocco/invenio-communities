# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2021 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Community views."""

from .config import CommunityResourceConfig
from .resource import CommunityResource

__all__ = (
    'CommunityResource',
    'CommunityResourceConfig',
)
