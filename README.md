# MyPlaylistShareApi

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