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
uvicorn app.main:app --reload
```

## Docker
- docker image作成
```
docker build -t $myimagename .
```
- コンテナ起動
```
docker run -d --name $mycontainername -p 80:80 $myimagename
```
- curlで確認
```
curl localhost:80
```

- イメージ名の変更
```
docker tag $myimagename $hub-user/$myimagename:tag
```

- imageをDocker HubにPush 

```
docker push $DockerHubname/$myimagename:tag 
```
- 起動中のコンテナをイメージ化
```
docker container commit $container-id or $container-name $hub-name/$myimagename:tag
```


