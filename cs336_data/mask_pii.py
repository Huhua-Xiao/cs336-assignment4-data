import re

EMAIL_MASK = "|||EMAIL_ADDRESS|||"
PHONE_MASK = "|||PHONE_NUMBER|||"
IP_MASK = "|||IP_ADDRESS|||"

EMAIL_RE = re.compile(r'''(?ix)\b[A-Z0-9._%+-]+@(?:[A-Z0-9-]+\.)+[A-Z]{2,}\b''')
PHONE_RE = re.compile(
    r'''(?x)
    (?<!\d)                                
    (?:\+?1[\s.-]?)?                      
    (?:\(\s*\d{3}\s*\)|\d{3})              
    [\s.-]?                               
    \d{3}                                 
    [\s.-]?                               
    \d{4}                                 
    (?!\d)                               
   '''
)

OCTET = r'(?:25[0-5]|2[0-4]\d|1?\d?\d)'
IPV4_RE = re.compile(rf'\b{OCTET}\.{OCTET}\.{OCTET}\.{OCTET}\b')

def mask_emails(text: str):
    res = re.subn(EMAIL_RE, EMAIL_MASK, text)
    return res

def mask_phone(text: str):
    res = re.subn(PHONE_RE, PHONE_MASK, text)
    return res

def mask_ip(text: str):
    res = re.subn(IPV4_RE, IP_MASK, text)
    return res


