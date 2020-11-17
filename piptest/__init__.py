import piptest._constants as consts

__author__ = consts.__author__
__url__ = consts.__url__
__version__ = consts.__version__


# 明示的に公開したいモジュールを以下のように書いておけば、使う側は使いやすい
from piptest.call import call
from piptest.dog import Dog