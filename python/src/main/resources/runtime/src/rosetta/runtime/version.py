'''PEP 396 module version attribute in PEP 440 version format'''
version = (2, 1, 0, 0)

# pylint: disable=invalid-name
version_str = f"{'.'.join(str(i) for i in version[:3])}-{version[3]}"

__version__ = '.'.join(str(i) for i in version[:3])

# EOF
