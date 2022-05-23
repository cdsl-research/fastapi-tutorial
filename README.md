## FastAPI tutorial
B3勉強会で行ったFast APIを使ったアプリケーション

- 仮想環境の作成
```
python3 -m venv .venv
```
- 仮想環境起動
```
source .venv/bin/activate
```
- fastapi, uvicorn, Jinja2をインストール
```
pip install -r requirements.txt
```
- アプリケーション起動
```
uvicorn main:app --reload
```