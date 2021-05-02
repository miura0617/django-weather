# 実行方法

## (1) git cloneする

git clone https://github.com/miura0617/django-weather.git

## (2) 仮想環境を作成する

python -m venv venv

## (3) 仮想環境に外部ライブラリをインストールし、開発環境を復元します

pip install -r django-weather\requirements.txt

## (4) インストールした外部ライブラリを確認

外部ライブラリにdjangoとdjangorestframeworkがあることを確認

pip freeze

## (5) manage.pyがあるフォルダ移動する

cd django-weather

## (6) SECRET_KEYを作成します

以下のURLを元にweatherproject\get_random_secret_key.pyを作成してSECRET_KEYを作成します
https://qiita.com/frosty/items/bb5bc1553f452e5bb8ff


python weatherproject\get_random_secret_key.py


## (7) weatherproject\local_settings.pyを作成し、先程作成したSECRET_KEYを定義します


## (8) モデルを生成

以下の2つのコマンドを実行し、モデルを生成します

python manage.py makemigrations
python manage.py migrate

## (9) スーパユーザを作成

以下のコマンドでスーパユーザを作成します。

python manage.py createsuperuser


## (10) サーバを起動します

python manage.py runserver


# 動作確認方法

## (1) 管理画面にログインする

管理画面「http://127.0.0.1:8000/admin/」にアクセスし、スーパーユーザでログインします

## (2) 動作確認のために天気情報を作成

管理画面から天気情報を2、3個作成します

## (3) 天気情報ページで表示を確認

天気情報ページ「http://127.0.0.1:8000/top/」へアクセスし、天気情報が表示されることを確認します。


## (4) Django Rest Frameworkで作成したAPIサーバのレスポンスを確認

(2)で作成した天気情報のJSONデータがレスポンスで取得できることを確認します。

「http://127.0.0.1:8000/api/1/」
「http://127.0.0.1:8000/api/2/」


