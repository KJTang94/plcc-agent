import json
import os
from pathlib import Path

_CONFIG_DIR = Path(__file__).parent
_CONFIG_FILE = _CONFIG_DIR / "config.json"
_CONFIG_FILES_DIR = _CONFIG_DIR / "config_files"

# excel_path 各键对应的默认文件名：config.json 未配置或路径无效时，
# 自动回退到 config_files 目录下的同名文件
_DEFAULT_FILE_NAMES = {
    "prop_def": "prop_def_test.xlsx",
    "cns": "cns_test.xlsx",
    "rsr_def": "rsr_def_test.xlsx",
    "resources": "resources_test.xlsx",
    "meas_def": "meas_def_test.xlsx",
    "points": "point.xlsx",
    "flows_models": "dff.xlsx",
    "aoe_model": "aoe.xlsx",
}

_ENV_MAP = {
    "llm.api_key": "LLM_API_KEY",
    "llm.base_url": "LLM_BASE_URL",
    "llm.model": "LLM_MODEL",
    "mems_api.base_url": "MEMS_API_BASE_URL",
    "mems_api.username": "MEMS_API_USERNAME",
    "mems_api.password": "MEMS_API_PASSWORD",
    "mems_api.secret_key": "MEMS_API_SECRET_KEY",
}

_config_cache = None


def _get_by_dot_key(data: dict, dot_key: str, default=None):
    keys = dot_key.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def load_config(force_reload: bool = False) -> dict:
    global _config_cache
    if _config_cache is not None and not force_reload:
        return _config_cache

    if not _CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"配置文件未找到: {_CONFIG_FILE}\n"
        )

    with open(_CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    for dot_key, env_var in _ENV_MAP.items():
        env_value = os.environ.get(env_var)
        if env_value is not None:
            keys = dot_key.split(".")
            current = config
            for key in keys[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            current[keys[-1]] = env_value

    _config_cache = config
    return config


def get_llm_config() -> dict:
    return load_config().get("llm", {})


def get_mems_api_config() -> dict:
    return load_config().get("mems_api", {})


def _resolve_excel_path(key: str) -> str:
    """解析 excel_path 中某个键对应的文件路径。
    优先使用 config.json 中配置且真实存在的路径；
    若未配置或路径无效，则回退到 config_files 目录下的约定默认文件。
    两者都不可用时返回空字符串。"""
    try:
        configured = load_config().get("excel_path", {}).get(key, "")
    except FileNotFoundError:
        # config.json 不存在时不阻断文件解析，直接走 config_files 回退
        configured = ""
    if configured and os.path.isfile(configured):
        return configured

    default_name = _DEFAULT_FILE_NAMES.get(key)
    if default_name:
        fallback = _CONFIG_FILES_DIR / default_name
        if fallback.is_file():
            return str(fallback)

    return configured


def get_prop_def_file_path() -> str:
    """
    获取设备属性定义文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("prop_def")

def get_cns_file_path() -> str:
    """
    获取拓扑配置Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("cns")

def get_rsr_def_file_path() -> str:
    """
    获取设备定义Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("rsr_def")

def get_resources_file_path() -> str:
    return _resolve_excel_path("resources")


def get_meas_def_file_path() -> str:
    """
    获取设备测点配置Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("meas_def")

def get_points_models_file_path() -> str:
    """
    获取测点模型配置Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("points")


def get_flows_models_file_path() -> str:
    """
    获取报表配置Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("flows_models")


def get_aoes_models_file_path() -> str:
    """
    获取AOE配置Excel文件的路径，从配置文件中读取
    """
    return _resolve_excel_path("aoe_model")