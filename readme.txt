原来后台向前端传递消息
render_template('test.html',msg='hello world')
前端接收
{{ msg }}

一 利用消息闪现：
    1.在一个请求结束的时候添加flash
        flash('恭喜！验证成功啦！')
        flash('哈哈哈')
        flash(username)
    在当前请求中渲染获取或者仅下一个请求获取。获取闪现数据链接点击后无内容
    获取闪现内容：
        get_flash_messages()

    2.设置类型
        flash('恭喜！验证成功啦', 'info')
        flash('哈哈哈', 'error')
        flash(username, 'warning')
    获取闪现内容：
        get_flash_messages(with_categories=[True/False])
        get_flashed_messages(category_filter=["error"])  可有针对性的获取对应类型的闪现消息


二 日志记录：
    程序出错想要让其继续运行下去 只是记录错误
    1.使用app自带logger
        app.logger.info('')
        app.logger.debug('A value for debugging')
        app.logger.warning('A warning occurred (%d apples)', 42) # WARNING in app: A warning occurred (42 apples)
        app.logger.error('An error occurred')

    2.通过python的logging模块进行创建
      同时输出及保存
        import logging

        logger = logging.getLogger( )
        logger.setLevel('DEBUG')

        BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
        DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)

        # 输出到控制台的handler
        chlr = logging.StreamHandler( )
        chlr.setFormatter(formatter)
        chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level

        # 输出到文件的handler
        fhlr = logging.FileHandler('log/log.txt')
        fhlr.setFormatter(formatter)

        # 添加两个流
        logger.addHandler(chlr)
        logger.addHandler(fhlr)

        # 设置log内容
        logger.debug("Do something")
        logger.info("Start print log")
        logger.warning("Something maybe fail.")
        logger.info("Finish")


      保存到文件：
        # 输出日志的级别 level=logging.WARNING 高于的显示 输出到log/log.txt文件中
        logging.basicConfig(filename='log/log.txt', filemode='a', level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

      第二种
        logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler("log/log.txt")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

      只输出到终端
        logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

      logger = logging.getLogger('flask.app') # 为flask.app时 app.logger.* 所有都输出到terminal中
      logger = logging.getLogger('app') # app时 app.logger.* 级别高于WARNING时输出到文件中