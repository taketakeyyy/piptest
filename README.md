# piptest
自作パッケージ（モジュール）を GitHub 経由で `pip install` するサンプルプログラム。

PyPi に公開したくない自作モジュールを作ることはよくあります。

この `piptest` をGitHub経由でインストールして、モジュール呼び出しするサンプルプログラムです。

# 使い方

適当な作業フォルダ `sandbox` を作成します。

この `sandbox` フォルダ直下で、以下のどれかのコマンドを実行してインストールします。

* `pip install git+https://github.com/taketakeyyy/piptest.git -t mylib`
    - `sandbox` 直下に `mylib` というフォルダが作成され、そこに `piptest` パッケージがインストールされます。

* `pip install git+https://github.com/taketakeyyy/piptest.git`
    - システムに `piptest` パッケージがインストールされます。

## piptestを使ってみる

`sandbox` 直下に、以下の`run.py`を作成します。

```py
# -*- coding: utf-8 -*-

# mylib フォルダにインストールした場合、パスを通す
import sys
sys.path.append('mylib')

# モジュール内の関数を import する
from piptest import call
from piptest import Dog
from piptest import __author__
from piptest import __url__
from piptest import __version__

if __name__ == "__main__":
    call()

    dog = Dog("Taro")
    dog.bark()

    print("===[piptest info]===")
    print(f"author:{__author__}")
    print(f"url:{__url__}")
    print(f"version:{__version__}")
```

これを実行してみます。

```sh
> python run.py
Hello, here is pip test.
Bow! Bow name is Taro!
===[piptest info]===
author:taketakeyyy
url:https://github.com/taketakeyyy/piptest
version:0.1.0
```

`piptest` の `call()`, `dog.bark()` のモジュールや、パッケージ情報が呼び出せました。


## piptestのアップデート
`piptest` に変更を加えてアップデートしたとします。

一般に、パッケージのアップデートは以下のコマンドで行います。

```sh
> pip install --upgrade [パッケージ名]
```

なので、 `piptest` をアップデートしたい場合は以下のコマンドを使います。

```sh
# mylib にインストールした場合
> pip install --upgrade git+https://github.com/taketakeyyy/piptest.git -t mylib
# システムにインストールした場合
> pip install --upgrade git+https://github.com/taketakeyyy/piptest.git
```

# 参考
* [python の pip でインストールできる自作モジュールを作ってみる](https://blog.chocolapod.net/momokan/entry/117)
* [navdeep-G/setup.py](https://github.com/navdeep-G/setup.py)