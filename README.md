# piptest
自作モジュールを GitHub 経由で `pip install` するサンプルプログラム。

PyPi に公開したくない自作モジュールを作ることはよくあります。

この`piptest`をGitHub経由でインストールして、モジュール呼び出するサンプルプログラムです。

# 使い方

適当な作業フォルダ `sandbox` を作成します。

この `sandbox` フォルダ直下で、以下のどれかのコマンドを実行してインストールします。

* `pip install git+https://github.com/taketakeyyy/piptest.git -t mylib`
    - `sandbox` 直下に `mylib` というフォルダが作成され、そこに `piptest` モジュールがインストールされます。

* `pip install git+https://github.com/taketakeyyy/piptest.git`
    - システムに `piptest` がインストールされます。

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

if __name__ == "__main__":
    call()

    dog = Dog("Taro")
    dog.bark()
```

これを実行してみます。

```sh
>
```

## piptestのアップデート
パッケージのアップデートは以下のコマンドで行います。

```sh
> pip install --upgrade [パッケージ名]
```

なので、 `piptest` をアップデートしたい場合は以下のコマンドを使います。

```sh
> pip install --upgrade piptest
```