路由功能由\think\Route类完成。
由于ThinkPHP5.0默认采用的URL规则是：
```
http://server/module/controller/action/param/value/...
```
路由的作用是简化URL访问地址，并根据定义的路由类型做出正确的解析。

新版的路由功能做了大量的增强，包括：
支持路由到模块的控制器/操作、控制器类的方法、闭包函数和重定向地址，甚至是任何类库的方法；
闭包路由的增强；
规则路由支持全局和局部变量规则定义（正则）；
支持路由到任意层次的控制器；
子域名路由功能改进；
支持路由分组并支持分组参数定义；
增加资源路由和嵌套支持；
支持使用行为或者自定义函数检测路由规则；

ThinkPHP5.0的路由支持三种方式的URL解析规则。
5.0的路由是针对应用而不是针对模块，因此路由的设置也是针对应用下面的所有模块，如果希望不同的模块区分不同的设置（例如某些模块需要关闭路由，某些模块需要强制路由等），需要给该模块增加单独的入口文件，并作如下修改：
```
// 定义项目路径
define('APP_PATH', __DIR__ . '/../application/');
// 加载框架基础文件
require __DIR__ . '/../thinkphp/base.php';
// 绑定当前入口文件到admin模块
\think\Route::bind('admin');
// 关闭admin模块的路由
\think\App::route(false);
// 执行应用
\think\App::run()->send();
```
V5.0.21+版本开始，支持了路由解析缓存。
在配置文件中 设置开启
```
 // 开启路由解析缓存
    'route_check_cache'      => true,
```

官方文档讲的很细致，我就不赘述了
```
路由模式：https://www.kancloud.cn/manual/thinkphp5/118019
路由定义：https://www.kancloud.cn/manual/thinkphp5/118030
批量注册：https://www.kancloud.cn/manual/thinkphp5/118031
变量规则：https://www.kancloud.cn/manual/thinkphp5/118033
组合变量：https://www.kancloud.cn/manual/thinkphp5/131398
路由参数：https://www.kancloud.cn/manual/thinkphp5/118034
路由地址：https://www.kancloud.cn/manual/thinkphp5/118037
```
如下暂时没看
```
资源路由
快捷路由
路由别名
路由分组
MISS路由
闭包支持
路由绑定
绑定模型
域名路由
URL生成
```