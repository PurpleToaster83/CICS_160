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
    "eNq1Uk2P0zAQvftXDM0lkboJcEQqF6Q9Ig5oOWxXkTeeJFaDHWy3pag/nhnno9myy8eBtHIm"
    "4+c373km8cH2uUhEElrtgf6hRZDGH9HBDk9QWwefpAvwNo9blVUIyqIHYwO08oAQLByt29Fb"
    "JA0GqPddB5VDpcMarOlO8eC3PfqgrYHONkAwD42TCtUavGWAQ65OpK02jUiUPRqIWeIObaTw"
    "vdUdulEuEpNp4IDOM62tYbIgQ4STM85W1mHen3K4ubsTYrVaVS1WO0+BEEJhDUgUJ2uw/CoD"
    "7ak0vknFGoJ87DB7J4AeOvDZ7UlPiybyTzCqwCJmnpyp+cQEyD1ZSLOY80inN/SaEnzBvdQO"
    "tJkPDAUneC6VShly//phOOMw7J0ZuQYyJ02DadSbe/0D0yzLRn+PdPGDt5ed3Wqjht4zehAy"
    "+2CJUtk+oFtDTx1+VqqzRzI2KCA1O9pMx1PZDNJ1xFGTPtJNARHTJ/mCVxtmvrAtbN7KzuPS"
    "N7dh9FbLg3U6YNlb7zWVTq+MfWmRhwt0gEoackfDu2hRrZ2nUdzA/ZXwjEVF4+z2mdt9WCrq"
    "0KTchYEuy7grnBu/R7E0kKUpvQza1/rXOVuDuej+EId0nmMzK672wdY1KTZwA2/+T39ymgb8"
    "nhJVBu/Hiv/UmqSMT4RewimaV5FsOQ28FpwBDueI01v6OosEzuPvpWVbnP8KF5cBV3AlLsI1"
    "iqfRAhczA3AMF9ESV4x3sy3L4jqCC66A3z/bAfcnGBcXPwHoL6X9"
)

exec(compile(_zlib.decompress(_b64.b64decode(_PACKED)).decode("utf-8"),
             "<packed module: matchtools.checks>", "exec"))

del _b64, _zlib, _PACKED
