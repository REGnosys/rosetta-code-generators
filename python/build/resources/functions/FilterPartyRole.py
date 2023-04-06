
def FilterPartyRole(partyRoles, partyRoleEnum):
    filteredPartyRoles = filter(lambda x: x.role==partyRoleEnum, partyRoles)

    return filteredPartyRoles