from enum import Enum

all = ['PersonIdentifierTypeEnum']
  
class PersonIdentifierTypeEnum(Enum):
  """
  The enumeration values associated with person identifier sources.
  """
  ARNU = "ARNU"
  """
  Alien Registration Number, number assigned by a social security agency to identify a non-resident person.
  """
  CCPT = "CCPT"
  """
  Passport Number, number assigned by an authority to identify the passport number of a person.
  """
  CUST = "CUST"
  """
  Customer Identification Number, number assigned by an issuer to identify a customer.
  """
  DRLC = "DRLC"
  """
  Drivers License Number, number assigned by an authority to identify a driver's license.
  """
  EMPL = "EMPL"
  """
  Employee Identification Number, number assigned by a registration authority to an employee.
  """
  NIDN = "NIDN"
  """
  National Identity Number, number assigned by an authority to identify the national identity number of a person..
  """
  NPID = "NPID"
  """
  Natural Person Identifier. To identify the person who is acting as private individual, not as business entity. Used for regulatory reporting.
  """
  PLID = "PLID"
  """
  Privacy Law Identifier. It refers to the DMO Letter No. 17-16, http://www.cftc.gov/idc/groups/public/@lrlettergeneral/documents/letter/17-16.pdf
  """
  SOSE = "SOSE"
  """
  Social Security Number, number assigned by an authority to identify the social security number of a person.
  """
  TXID = "TXID"
  """
  Tax Identification Number, number assigned by a tax authority to identify a person.
  """
