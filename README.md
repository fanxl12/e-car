# e-car
a python flask project!

sudo docker login --username=guijj12 registry.cn-shanghai.aliyuncs.com
sudo docker tag 10cc7d94dab8 registry.cn-shanghai.aliyuncs.com/guijj12/e-car:0.4
sudo docker push registry.cn-shanghai.aliyuncs.com/guijj12/e-car:0.4

sudo docker pull registry.cn-shanghai.aliyuncs.com/guijj12/e-car:0.4

docker run -d -p 8062:8062 --name e-car registry.cn-shanghai.aliyuncs.com/guijj12/e-car:0.4