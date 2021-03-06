from pyrevit import PYREVIT_ADDON_NAME
from pyrevit import HOME_DIR, VERSION_MAJOR, VERSION_MINOR, EXEC_PARAMS
from pyrevit.coreutils.logger import get_logger
from pyrevit.coreutils.envvars import set_pyrevit_env_var
import pyrevit.coreutils.git as git


logger = get_logger(__name__)


class PyRevitVersion(object):
    """Contains current pyrevit version"""
    major = VERSION_MAJOR
    minor = VERSION_MINOR
    patch = ''

    def __init__(self, patch_number):
        self.patch = unicode(patch_number)[:7]

    def as_int_tuple(self):
        """Returns version as an int tuple (major, minor, patch)"""
        try:
            patch_number = int(self.patch, 16)
        except:
            patch_number = 0
        ver_tuple = (PyRevitVersion.major, PyRevitVersion.minor, patch_number)
        return ver_tuple

    def as_str_tuple(self):
        """Returns version as an string tuple ('major', 'minor', 'patch')"""
        ver_tuple = (unicode(PyRevitVersion.major),
                     unicode(PyRevitVersion.minor), self.patch)
        return ver_tuple

    def get_formatted(self):
        """Returns 'major.minor:patch' in string"""
        return '{}.{}:{}'.format(PyRevitVersion.major,
                                 PyRevitVersion.minor,
                                 self.patch)


def get_pyrevit_repo():
    try:
        return git.get_repo(HOME_DIR)
    except Exception as repo_err:
        logger.error('Can not create repo from directory: {} | {}'
                     .format(HOME_DIR, repo_err))

if not EXEC_PARAMS.doc_mode:
    try:
        PYREVIT_REPO = get_pyrevit_repo()
        PYREVIT_VERSION = PyRevitVersion(PYREVIT_REPO.last_commit_hash)
    except Exception as ver_err:
        logger.error('Can not get pyRevit patch number. | {}'.format(ver_err))
        PYREVIT_VERSION = PyRevitVersion('?')

    set_pyrevit_env_var(PYREVIT_ADDON_NAME + '_versionISC',
                        PYREVIT_VERSION.get_formatted())

else:
    PYREVIT_REPO = None
    PYREVIT_VERSION = None
