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
    "eNrVWm1v3LgR/q5fwcofVovKSpxc+8GIgzo5BzV6vQucoEBhGFuuxN3lWUuqpJTNXnH/vTND"
    "Ui8rre275tDLwsBqKXI4L888HJI+uWb1Rqp7ttcNa1TF83tRQJNgO6PVmq1kKbLoJDr5uJGW"
    "wR++2uqiKQU88prtuGWFzputUDWMrIyuhCn3Gbv6JMweZa/ZUpR6B4OjE14awYs9k4p9+OvV"
    "dx+vbhY3P3zAr8v319m2SGFaWddCwRj4MvBb1hsmPvNtVQqbMq6K6ATbdFOTLktuxZ+/IRX/"
    "CSYUsmCcLRuVb5hesZ0296zWbC1qaIZfVrBcV3t8x8k4MjyoteFFhqYKI2YWOsCUVivUlmy1"
    "eit2+BImqNn1rCyhR00SVlIVTNakx+lbXYooiuP4BqSealXuGc9zkIWqcGY3ogTbmNEWvrIo"
    "uvSPzIhcm8Ky3UaC/pWoQQmYLW+MAfeiGGd0kADe8H15oStosRH2R315eW+d83oDMnZdQ7SE"
    "ZUrXfjYQstcK7a2MWIFxKg+Olr3OENWVNlu25XWOQQW135N+oEKYnJSVBagqVxLAsMRAF+Jz"
    "xt5oUMRif3A8tEmYA3tHPwmjTzGGBUnKNYxdN7qx5+Ao75WNLguE0UvnkcbCWHhq5TxP2Vka"
    "4fAXGXvfe9HTrT8pKFJxw2vBVLNdCoOybb4RW7Tb6ghlPx8Mfk7DGmVECcMAI9GNU40QhH7h"
    "dXQ6+kQ/KBG8DP5jpVQCfFFyyDd8dhq6p6VYS6VQFQra7GTmvLlW2tCMDD6gWfpK8a14nb6y"
    "lcilsK/phVe0fbnhdrHnpoBH8LwwC/QctuvG2AXf8f3rKLruuYRbC1NBFAjrgoHKoDA+BUzy"
    "qhLchPdoeArhaiBeah1VIygEHyMVdOoggwiJGrHZXtgZzMNmSs+yqK8nSerrSioqrU6VWPNa"
    "fkKI12IN82SYZlH04f3V2+urD+yCJfFSmiJOWZzzGr8KvcYvw5dLSQ1GVDVoH89xaN0AryAo"
    "bW3OmUDOYt6zDH3pXOCDTXEmh6yV/MmhxSAeSIcoL8GL7INLNQeQc4oOvL5kVvHKbiCTYDIU"
    "OnYZyIZEbHPVhfxyKBAdaAKrZOx7zbYCyLCAkUjkljkl8g1Xa2F72juYrEhEjVJKzQtRUKKD"
    "a4OYMBBIAZy+Jlr3A9bgd5WxS7UnWdum5kvw3SdeNoiSujHK5TwPwiRy6MoIuyHSRXeRRjkv"
    "S2cKvBQkDYgRVhW52hOJeqc5DxRixRYLqWS9WCRWlKuUfJe2jps7L/tBbxpZFh15FBLihdS5"
    "MnobkpGibr2H8fN36OzVAugC8kAE8MzQ9xmKWFDKSwUNvOhJuPTOsp0yPmMtS0pp6/k5wy8M"
    "f4LISgPO5l6dFHOL+NJlXzYQ1KLkiLCQYinrEgla2xyaD6SRy4/M2na84RKodmjPPzDaV8Zo"
    "yBaJa2hIFumWCVzYXS6mmNvSYd3xLGg7UoL80y4y4t8NL4cjWsOzfpDbZ5igFCpBMXP2hwv6"
    "MYEL/Bg0p2dAErcgUUIgwymvQDf5KEnjzo9AB2wQSDQeBwynBQ1bQhk46HzkjLGGjbpXeqeC"
    "hHMWsz8CiCuTBPB0+mBqZBR3oEFEh/PKwfsWR75P6ywX97/YGgg2dwncpl8L/KTi9WaYb98B"
    "j3TpRlnW/aLq8dEcAZksAQIGVNMzVUk9EWm76jgG7tWbriAaY1tXjmcBlq5a7eOauOpAiSFt"
    "92m/EDY3cum4Lax9j6TJO+jyva7fwfpYdNkCNEvsIT6D54nv0dzs4QTD8iBkF0e2hQrX0Vh6"
    "mIEjN3j49FORFGgTDkurY7gfSevnwXQ2evDd3kUj2hq0UokDGwXl8ATVB/CXKkox9CJlGOmU"
    "Qm7sEAUCfgusKxI3AJKv5qa+OJuP04k8d4EjMwCXrJIxB1JQatdT+wKNBFpUMYlP4gm5+KFC"
    "VTVj5FU4GK2tpMhFmJhMoRY0wk1TlbJO4jSe302pRXJun9+xiwsWg19jVyuSywySHbS/nNYN"
    "o5BhuaaKxPW+PbtLvcQXd/OxG0R5OKOP29Ssf5qetUXG8ZlJMpR9cTopYfSBIs9LeXk3T3s/"
    "vwEjpqywYlq3MbFSxJFMIUCJw9gcfsXTmdZjfVfoDOkiOahHuroFXiyoSKbCZUicb7G9KwW1"
    "6pHOY2wFrjg/WCcp6mijLAa7I9Mox8rPWVMBMU4twV7HOTtlZ9OZ7c1GJHTrTM9Qb/sTjG0Z"
    "4X81uAWcN/pwpzcwfGKFONDZGc8uSyiWbKhEdN87T/TMERhgqdCVrwsquQ5XUn1PMUIzce9B"
    "hxTQ+UllppPIEvDU/NyNc3VdGrwwtMbF+mGv06bII3RmfbWDVOYPZNjsjShLPntkNbxGNbo1"
    "rVMWkg3PccBOg9sO2M90+7vujGCUzeJHKOlhPYZ1YEO7VFjBwlbUGYs6AwkdrRk7FV6BY5Cb"
    "24bXF4conyojO5OSWJFf3aLmZARi6QI9IpBO/m3b6w7Yd5xSPeCEpqeCR4URjyNoILpFkepn"
    "1QBK0RH+/1Xw8mOnIXZZAhJ+IcSG1vzfYDZUw0Nt2DiA24M7lwPIhcBMwG4IkyPQC3PdDnoP"
    "IYjI9OXl06kr1KO/D/bCExV/4kInFXawRR0ArdDrL8ZkXxvxnPWiTk0LvcJOPuyYlsOIv8MD"
    "b/SqPzvwwcY9EnZ+POhEUn7X54bSOPYRD4j0Fgo9SWfvluXcilMrlJWYs0+uFFrF/AIWTsN5"
    "mOkaXu20q77shk5BRyTg+AgllHoXaNAdwrkDr0cA8zexH+z/UI9B4YMHNz2lJnGDKPXJ4A+w"
    "Bjuho4iBKV1/X9XjDBOnDg4XNEE0BFvQvoUaSii6QwiCxXwCOZ5Tfgl6uqXm10GoG/9b4mjA"
    "umMstdcwh072+PrieAr6/DaYOrIefVlc9cP2ALYQ3wit4XoUjsGGqxEejbqzfMq3lTtXd10f"
    "h1VYwFpy6l8IZG4bSXRvZSHCWuJuUUqMajF5cmIlrDJ7d3+GW0x/ifYgBsMZbx+LVK9A28A+"
    "dz3p1Ay3EtB5rIjNoV7B+sUd9rKrbVXvw9lQ774Nd8HMNu4WkpLpSHxF4bTsnfXTbzQZ2ixf"
    "ie5w/8Ed1K3LhaeT3dSxicflGeHSO2Sipt7oxgq08/HC+lt//NdjGKhTWwG/z8oaUFKftwHB"
    "X+lBKLqbdbodgfBDXt6LvR0n8izcLcxYstS6BPV3G+FrYtG5gmiHM+yZjYV01xKz4ISN3kE+"
    "qL1bgoeyuit5OyGsu9foCYMmumbdCXFfcFhE9FLj/xpgtLbiS24gvpp6n/Ln4uGK/zAP/xOH"
    "eMfnXT6lLO4i2L14cTc+y4u76HQdX979HEWLBRAfENhiAUrF33bH+Mf+HwRvON3/kEAP+s8L"
    "Yjpp1az2lwJGZPHXKTk6aV0Gwt1316Zns/nPC/g8e9br+K/FM/cwd6idbem4csuLXqdkkSye"
    "nSahK3b6sQFOLqTlVaXx7ryI/gtIa8fv"
)

exec(compile(_zlib.decompress(_b64.b64decode(_PACKED)).decode("utf-8"),
             "<packed module: shelter_roster>", "exec"))

del _b64, _zlib, _PACKED
