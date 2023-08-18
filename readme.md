# 洛羽柒

这里是各种奇奇怪怪的Api合集，部署在Vercel

## HMCL启动器镜像下载源

基于[HMCL-Update](https://github.com/Glavo/HMCL-Update) 的一个复制版本

**使用方法**
```
https://api.yokinanya.icu/hmcl/<channel>/<version>/<options>
```
channel：更新通道 可输入值：`stable` 或 `dev`
version：版本号 可输入值：`latest` 或 具体的版本号
options：选项 可输入值：`exe` 或 `jar` 可以获取对应下载链接，`json` 返回对应版本的json文件

**设置为HMCL下载源**

您可以手动在环境变量 JAVA_TOOL_OPTIONS 中添加以下内容实现：

稳定版：
```java
-Dhmcl.update_source.override=https://api.yokinanya.icu/hmcl/stable/latest/json

```

测试版：
```java
-Dhmcl.update_source.override=https://api.yokinanya.icu/hmcl/dev/latest/json

```

## Minecraft UUID 转换

**使用方法**
```
https://api.yokinanya.icu/mcuuid/<nickname>
```

返回为一个json，这一个参考值：

访问 <https://api.yokinanya.icu/mcuuid/yokinanya>，得到结果
```json
{
    "nick": "yokinanya",
    "offlineuuid": "dd8f2a8d83de3a59ba30a348fe0c1843",
    "offlinesplitteduuid": "dd8f2a8d-83de-3a59-ba30-a348fe0c1843",
    "uuid": "916c251133e44dbabc99c3e5cffa41ef",
    "splitteduuid": "916c2511-33e4-4dba-bc99-c3e5cffa41ef"
}
```

## 尊嘟假嘟翻译器

**使用方法**
```
https://api.yokinanya.icu/zdjd/<mode>/<t>
```
mode支持输入：`zdjd2human`(尊嘟语转换人语) `human2zdjd`(人语转换尊嘟语) `auto`(自动)
