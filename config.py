# config.py （唯一需要改路径的文件，上传GitHub）
# 🔥 纯相对路径，无任何服务器敏感信息
import os

# 项目根目录（自动获取，不用手写）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据路径（统一配置）
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")    # 原始数据
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")  # 处理后数据
RESULT_DIR = os.path.join(BASE_DIR, "output")  # 输出结果