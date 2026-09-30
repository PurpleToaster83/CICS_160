#NOTICE: This module is distributed in packed form. The source is
#compressed and embedded below, and is expanded at import time.
#
#Pets Unlimited Engineering ships packed modules so that consumers
#integrate against the published interface rather than against the
#implementation. Please refer to the documentation supplied with this
#package.
#
#This file is not intended to be read.
#
#Questions regarding this policy should be directed to your team lead.

import base64 as _b64
import zlib as _zlib

_PACKED = (
    "eNrdU8Fq3DAQvesrHvYlJRsHem4LgeRYCCHkFCoUa2yL1WpcjXaNIR8fybsOabv9gQzG1sw8"
    "vzdPsmtJPDaqVnUanCBfaSCYIBNFbGlGxxH3JiZ8bZZWy5ZgmQSBEwZzICTGxHGbn6ruKaHb"
    "e482knVpAw5+Xl78vSdJjgM898gwQR+NJbuBcAFEKuqZdHChV7XlKWCpZu40LBQysvMUT+NS"
    "Zgo9DhSl0HKH1YJJCzw7K9WWIzXj3ODq6Umpqqp2JrVDYvaSE6W6yDs0BQW3G7MY7iN1j+bF"
    "09obqN3K2qWsOHMgvfAUAy/Z2THboDMHji6RHlnEZY5NmUMHLSY56RzZE+k+Ob9SRjJWj1lV"
    "lNI674FrSWt8R2W5zX7KaAEPdze3P++anW0wDRQWj8d+sB/OxonpIxXdtTS5IA1cgvGTmeWU"
    "5+2oPrucqvEel1fn4/Ij6LXcrp/19TP+iNe/QRfghvElrywvv8I5EH7gF76VRTnh4/f5L+g9"
    "Zkrn5P4/+Bub1SH6"
)

exec(compile(_zlib.decompress(_b64.b64decode(_PACKED)).decode("utf-8"),
             "<packed module: matchtools>", "exec"))

del _b64, _zlib, _PACKED
