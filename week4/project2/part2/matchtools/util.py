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
    "eNpVUM1qwzAMvvspRHJJoAvbjoW+w+ihl1KGGyuJqbE8W2koY+8+2VlhEQERfT/+pDoxhU7V"
    "qubJJpCPJwTt04IRbviAgSJ86Mjw3hWoJ4NgCBN4Ypj0HYEJFoo36aoekWGYnYM+orG8A/Lu"
    "UYRfMya25MHRCEJLMEZt0OwgUSZEzK+L6WT9qGpDi4cyFW+eikUKZB3Gv7goTn6EO8aUbWmA"
    "5wqaC102y9OeInbh0cHL6aRUVVUzWydNKWVwgIjafIaIQ2qC5qndK5AS/CjAeo6CwiBvd1mX"
    "cZoZDvD9U34WKwEpoF8dQAt5tcmVL+isl/X8/3GuMj6U1iWONjTtBrdDuXLGt8JcPXm2fsYN"
    "cLVy2KdjcJabaldtTSX62XpuMvX8emkvwuc5OGzKtC2BrzltYbztL6s+Is/RZ7n6BXBXqUw="
)

exec(compile(_zlib.decompress(_b64.b64decode(_PACKED)).decode("utf-8"),
             "<packed module: matchtools.util>", "exec"))

del _b64, _zlib, _PACKED
