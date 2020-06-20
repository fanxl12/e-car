# e-car
a python flask project!

### 镜像推送到阿里云镜像仓库
```
sudo docker login --username=guijj12 registry.cn-shanghai.aliyuncs.com
sudo docker tag [镜像id] registry.cn-shanghai.aliyuncs.com/guijj12/e-car:[镜像版本号]
sudo docker push registry.cn-shanghai.aliyuncs.com/guijj12/e-car:[镜像版本号]
```

### 服务器拉取镜像
```
sudo docker pull registry.cn-shanghai.aliyuncs.com/guijj12/e-car:[镜像版本号]
```
### 服务器部署镜像
```
docker run -d -p 8062:8062 --name e-car registry.cn-shanghai.aliyuncs.com/guijj12/e-car:[镜像版本号]
```
