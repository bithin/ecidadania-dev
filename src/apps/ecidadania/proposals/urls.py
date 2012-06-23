# -*- coding: utf-8 -*-
#
# Copyright (c) 2010-2012 Cidadania S. Coop. Galega
#
# This file is part of e-cidadania.
#
# e-cidadania is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# e-cidadania is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with e-cidadania. If not, see <http://www.gnu.org/licenses/>.

"""
Proposal module URLs.
"""

from django.conf.urls import *
from django.utils.translation import ugettext_lazy as _
from apps.ecidadania.proposals.views import ListProposalSet, AddProposalSet, \
    ViewProposalSet, EditProposalSet, DeleteProposalSet, ListProposals, \
    ViewProposal, DeleteProposal, EditProposal, AddProposal

from apps.thirdparty.userroles.decorators import role_required
from apps.thirdparty.userroles import roles

urlpatterns = patterns('apps.ecidadania.proposals.views',

    url(_(r'^$'), ListProposals.as_view(), name='list-proposals'),
    
    url(_(r'^psets/(?P<set_id>\w+)/edit/'), EditProposalSet.as_view(), name='edit-proposalset'),
       
    url(_(r'^psets/(?P<set_id>\w+)/delete/'), DeleteProposalSet.as_view(), name='delete-proposalset'),
    
    url(_(r'^psets/(?P<set_id>\w+)/'), ViewProposalSet.as_view(), name='view-proposalset'),

    url(_(r'^psets/'), ListProposalSet.as_view(), name='list-proposalset'),

    url(_(r'^addset/'), role_required(roles.space_admin)(AddProposalSet.as_view()), name='add-proposalset'),

    url(_(r'^add/'), AddProposal.as_view(), name='add-proposal'),

    url(_(r'^add_support_vote/'),'vote_proposal'),

    url(_(r'^(?P<prop_id>\w+)/$'), ViewProposal.as_view(), name='view-proposal'),
  
    url(_(r'^(?P<prop_id>\w+)/edit/$'), EditProposal.as_view(), name='edit-proposal'),   
    
    url(_(r'^(?P<prop_id>\w+)/delete/$'), DeleteProposal.as_view(), name='delete-proposal'),

)

