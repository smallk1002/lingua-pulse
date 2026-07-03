# ── LinguaPulse Backend ──
FROM python:3.12-slim

WORKDIR /app

# 系统依赖（asyncpg 需要 libpq），APT 使用阿里云镜像加速
RUN sed -i 's|http://deb.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装 uv 包管理器（使用国内 PyPI 镜像，避免拉取 ghcr.io）
RUN pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置 PyPI 国内镜像（后续 uv sync 使用）
ENV UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple

# 先复制依赖文件（利用 Docker 缓存层）
COPY pyproject.toml uv.lock ./

# 安装依赖（生产模式，跳过开发依赖）
RUN uv sync --frozen --no-dev

# 复制源码
COPY . .

# 暴露端口（仅内网，由 Nginx 反向代理）
EXPOSE 8000

# 启动服务
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
