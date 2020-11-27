# hot_invitation

支持PyCon China社区活动所做的小工具

![](docs/20201126130727.png)

## TODO

- [x] 基础功能可用
- [ ] 自主更换背景
- [ ] 修改文字的位置、大小、字体
- [ ] 支持批量导入、下载
- [ ] 优化交互体验

## 部署

测试环境：ubuntu + python3.9 

```bash
root@node_1:/opt# git clone https://github.com/zmf963/hot_invitation.git
root@node_1:/opt# cd hot_invitation
root@node_1:/opt/hot_invitation# pip install -r requirements.txt
root@node_1:/opt/hot_invitation# cd hot_invitation/
root@node_1:/opt/hot_invitation/hot_invitation# python main.py 
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [31686] using statreload
INFO:     Started server process [31688]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

使用浏览器访问 http://ip:8080 ，账号密码：hot/invitation

### 使用docker

`docker-compose build && docker-compose up　-d `


## Other

- 更改默认的背景图： 

    替换hot_invitation/data目录下的base.png 
- 更改默认字体：　  

    替换hot_invitation/data目录下的base.ttf
- 调整字体的位置:   

    修改draw_image(text,x=0,y=60)参数x, y的默认值

## 求star 

(狗头保命) 代码太烂，逃

后面会尽快完善相关功能
