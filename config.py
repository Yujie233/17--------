import os

#  自动获取项目根目录，无需手动填写，完全隐藏服务器信息
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ================== 基础路径（和本地版完全一致，仅BASE_DIR不同） ==================
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
RESULT_DIR = os.path.join(BASE_DIR, "output")

# ================== human 数据集路径（和本地版完全一致） ==================
HUMAN_RAW = os.path.join(DATA_RAW, "human")
HUMAN_HA_VS_OA = os.path.join(HUMAN_RAW, "ha_vs_oa")
HUMAN_HA_VS_OA_GSE152805 = os.path.join(HUMAN_HA_VS_OA, "GSE152805")
HUMAN_HA_VS_OA_GSE284391 = os.path.join(HUMAN_HA_VS_OA, "GSE284391")

HUMAN_LOOSE_VS_STABLE = os.path.join(HUMAN_RAW, "loose_vs_stable")
HUMAN_LOOSE_VS_STABLE_GSE104589 = os.path.join(HUMAN_LOOSE_VS_STABLE, "GSE 104589")
HUMAN_LOOSE_VS_STABLE_GSE149315 = os.path.join(HUMAN_LOOSE_VS_STABLE, "GSE 149315")
HUMAN_LOOSE_VS_STABLE_GSE171542 = os.path.join(HUMAN_LOOSE_VS_STABLE, "GSE 171542")
HUMAN_LOOSE_VS_STABLE_GSE276597 = os.path.join(HUMAN_LOOSE_VS_STABLE, "GSE276597")

# ================== mouse 数据集路径（和本地版完全一致） ==================
MOUSE_RAW = os.path.join(DATA_RAW, "mouse")
MOUSE_HA_VS_OS = os.path.join(MOUSE_RAW, "ha_vs_os")
MOUSE_HA_VS_OS_GSE85051 = os.path.join(MOUSE_HA_VS_OS, "GSE85051")
MOUSE_HA_VS_OS_GSE85051_RAW = os.path.join(MOUSE_HA_VS_OS_GSE85051, "GSE85051_RAW")

MOUSE_LOOSE_VS_STABLE = os.path.join(MOUSE_RAW, "loose_vs_stable")
MOUSE_LOOSE_VS_STABLE_GSE234863 = os.path.join(MOUSE_LOOSE_VS_STABLE, "GSE234863")