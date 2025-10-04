# 1. 基础配置 / Basic Configuration

import logging

logging.basicConfig(
    level=logging.DEBUG,                # 设置最低日志等级 / Set minimum log level
    filename="app.log",                 # 保存到文件 / Save logs to file
    filemode="w",                       # "w" 覆盖写入 / overwrite; "a" 追加写入 / append
    format="%(asctime)s - %(levelname)s - %(message)s"  
    # 日志格式 / Log format:
    # %(asctime)s   时间 / timestamp
    # %(levelname)s 日志等级 / log level
    # %(message)s   日志内容 / log message
)

"""
2. 日志等级 / Log Levels

从低到高（越高越严重）：

Level	中文	使用场景 / Use case
DEBUG	调试	记录详细调试信息，例如循环中间值 / Detailed debugging info
INFO	信息	程序运行的关键步骤，例如开始/结束 / General program flow info
WARNING	警告	潜在问题，例如值过大 / Potential issues, unexpected behavior
ERROR	错误	程序错误，但未崩溃 / Errors that affect functionality
CRITICAL	严重	程序可能崩溃 / Severe errors, program might stop
"""

#3. 基本用法 / Basic Usage
logging.debug("This is debug info")     # 调试信息 / Debugging info
logging.info("Program started")         # 程序运行信息 / Program started
logging.warning("Low memory")           # 警告 / Warning
logging.error("File not found")         # 错误 / Error
logging.critical("System crash!")       # 严重错误 / Critical issue

"""
4. 文件 vs 控制台 / File vs Console

默认情况下，basicConfig 只输出到文件。
如果你想同时输出到 控制台 和 文件，可以这样：
"""
# 同时保存到文件和控制台 / Save logs to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="w", encoding="utf-8"),
        logging.StreamHandler()  # 输出到终端 / print to console
    ]
)


