
import json
import os
from pathlib import Path

_CONFIG_DIR = Path(__file__).parent
_CONFIG_FILE = _CONFIG_DIR / "config.json"

_ENV_MAP = {
    "llm.api_key": "LLM_API_KEY",
    "llm.base_url": "LLM_BASE_URL",
    "llm.model": "LLM_MODEL",
    "plcc_api.base_url": "PLCC_API_BASE_URL",
    "plcc_api.username": "PLCC_API_USERNAME",
    "plcc_api.password": "PLCC_API_PASSWORD",
    "plcc_api.secret_key": "PLCC_API_SECRET_KEY",
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
            f"请复制 config.example.json 为 config.json 并填入实际配置值"
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


def get_plcc_api_config() -> dict:
    return load_config().get("plcc_api", {})

