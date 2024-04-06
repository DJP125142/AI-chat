# AI-chat

支持自定义上传知识文档，调用chatGPT模型api接口进行AI智能解答问题

## 体验地址

## 环境要求
Python >= 3.12

## 部署服务
1. 拉取代码
```
git clone https://github.com/DJP125142/AI-chat.git
```
2. 修改配置文件
复制.env.example文件，命名为.env，然后填写配置文件内容。
配置文件内 openApiKey 获取地址：[获取openApiKey](https://3.5.996444.icu/register?aff=BLIT "获取密钥地址")  
  

3. 安装依赖包
```
pip install -r requirements.txt
```
4. 启动服务
```
// 在根目录下启动，生产环境可以去掉参数--reload 
uvicorn main:app --host 0.0.0.0 --reload 
```
5. 验证服务  
GET请求127.0.0.1:8000 返回Hello World说明服务启动成功。
```
{
    "message": "Hello World"
}
```

## 接口文档
| 接口名称  | 接口api | 请求方式  | 请求参数     | 参数说明                                            |
|-------|:------|-------|-------------------|-------------------------------------------------|
| 发起提问	 | /ask  | 	POST	 | filename，question | filename：知识库文档地址，支持本地文档或者在线文档<br/>question：提问内容 |

## 接下来开始上传你的知识文档开始体验吧！  
