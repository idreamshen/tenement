### 项目说明
由于房子快到期了，为了便于自己找到合适的房源，写一个爬虫项目来爬取各个租房网站的房源信息，来便于自己筛选房源。

### 采集需求
* 房源网站：豆瓣，58，安居客，房天下，链家，我爱我家等等
* 房源筛选条件：限定西湖区与拱墅区两个范围
* 需要采集的信息：标题，图片，地理位置，户型，整租/合租，房源链接，所属小区
* 需要将采集到的数据持久化下来，保存到数据库中
* 定期去采集新数据与更新老数据
* 一次采集过程中如果中断了，下次重启程序后会从中断处开始采集
* 采集效率越高越好（可以后续优化）

### 功能列表
* 可以实时查询采集到的数据，需要有各种查询维度，例如价格区间，指定某一小区，指定户型等等。
* 展示查询结果（可简单可复杂，简单的话自己写数据库查询语句，然后导出为相关文件，复杂的话做一个web页面）
* 可以在地图上进行查询，某一地址周围 n 米内的所有指定条件的房源（可以后续作为一个进阶功能来做）

### 技术选型与架构
* 开发环境使用 Docker 运行以下各应用
* Python 版本选择 3
* 爬虫框架使用 Scrapy
* 数据库使用 Mongodb
* 爬虫任务队列系统使用 Redis
* Web 框架使用 Flask

### 数据库设计
* _id
* title: 字符串，房源标题
* images: 字符串数组，房源图片
* location: 地理位置，经纬度？
* ?
* ?
* origin_href: 源链接
* origin: 源
* origin_id: 源 id
* create_at: 创建日期
* update_at: 更新日期

需要的字段：房源标题，房源图片，房源地理位置，房源户型，整租/合租，房源链接，所属小区，房源来源网站，唯一表示 id 等 

### 任务
- [ ] requirements.txt 文件整理
- [ ] items.py 字段设计
- [ ] pipelines.py 将 item 导入数据库
