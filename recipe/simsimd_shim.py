"""Install simsimd.py, a compatibility shim for the NumKong rename, into site-packages."""
import os
import shutil

shutil.copy(os.path.join(os.environ["RECIPE_DIR"], "simsimd.py"), os.environ["SP_DIR"])
