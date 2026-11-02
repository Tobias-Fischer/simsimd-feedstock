"""simsimd was renamed NumKong (https://github.com/ashvardanian/NumKong); this keeps
``import simsimd`` working for packages such as albucore, which call simsimd.wsum
(now numkong.blend)."""
from numkong import *  # noqa: F401,F403
from numkong import blend as wsum  # noqa: F401
