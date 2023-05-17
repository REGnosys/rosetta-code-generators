'''PEP 396 module version attribute in PEP 440 version format'''

version = (1, 0, 0, 0)

version_str = f"{'.'.join(str(i) for i in version[:3])}-{version[3]}"  # pylint: disable=invalid-name

__version__ = '.'.join(str(i) for i in version[:3])

# EOF
