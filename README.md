# MyPlaylistShareApi

* データベースはlocalで確認するので、初回起動時にマイグレーションを実行する

* 構成の参考：https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/f1b6fc

## 初回起動時
```sh
# イメージをビルド
docker compose build

# pyproject.toml(パッケージ管理ファイル)を作成する
# フレームワーク(FastAPI)とASGI(uvicorn)を依存先に設定する
docker-compose run \
  --entrypoint "poetry init \
    --name my-playlist-share-api \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  my-playlist-share-api

# パッケージをインストールする(lockファイル=poetry.lockが同時に作成される)
docker-compose run --entrypoint "poetry install --no-root" my-playlist-share-api

# データベース関連のパッケージを追加
docker-compose run --entrypoint "poetry add sqlalchemy aiomysql python-ulid bcrypt pyjwt" my-playlist-share-api
```
## パッケージを追加する時
* コンテナ内に入って`poetry add xxx`する
* dev-dependencies の場合、`--dev(-D)`オプションをつける
　`poetry add xxx -D`
```sh
# 下記コマンドで再ビルドする
docker-compose build --no-cache
```

## マイグレーション実行(テーブル作成)
```sh
# コンテナ内で下記コマンドを実行
poetry run python -m api.migrate_db
```

##  DB確認コマンド
```sh
# DB起動
docker compose exec db mysql my_playlist_share
# テーブル確認
select * from playlist
# 終了
\q
```
