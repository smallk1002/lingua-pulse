# ── LinguaPulse Frontend ──
# Stage 1: 构建
FROM node:22-alpine AS builder

WORKDIR /app

# 使用国内 npm 镜像加速（pnpm 会继承该配置）
RUN npm config set registry https://registry.npmmirror.com

# 启用 pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# 禁用 side-effects-cache，避免 Docker overlay2 上 SQLite 磁盘 I/O 错误
RUN pnpm config set side-effects-cache false

# 先复制依赖文件（缓存层）
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./

# 安装全部依赖（构建需要 devDependencies）
RUN pnpm install --frozen-lockfile

# 复制源码
COPY . .

# 生产环境 API 走相对路径（通过 Nginx 反代）
ENV NEXT_PUBLIC_API_URL=""

# 构建 Next.js
RUN pnpm build

# Stage 2: 运行
FROM node:22-alpine AS runner

WORKDIR /app

# 使用国内 npm 镜像加速
RUN npm config set registry https://registry.npmmirror.com

RUN corepack enable && corepack prepare pnpm@latest --activate

# 禁用 side-effects-cache，避免 Docker overlay2 上 SQLite 磁盘 I/O 错误
RUN pnpm config set side-effects-cache false

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# 复制构建产物
COPY --from=builder /app/package.json ./
COPY --from=builder /app/pnpm-lock.yaml ./
COPY --from=builder /app/pnpm-workspace.yaml ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/next.config.ts ./

# 只安装生产依赖
RUN pnpm install --frozen-lockfile --prod

EXPOSE 3000

CMD ["pnpm", "start", "-H", "0.0.0.0", "-p", "3000"]
