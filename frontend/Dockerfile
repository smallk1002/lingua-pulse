# ── LinguaPulse Frontend ──
# Stage 1: 构建
FROM node:22-alpine AS builder

WORKDIR /app

# 使用国内 npm 镜像加速
RUN echo "registry=https://registry.npmmirror.com" > /root/.npmrc

# 先复制依赖文件（缓存层）
COPY package.json ./

# 安装全部依赖（构建需要 devDependencies）
RUN npm install --legacy-peer-deps

# 复制源码
COPY . .

# 生产环境 API 走相对路径（通过 Nginx 反代）
ENV NEXT_PUBLIC_API_URL=""
ENV NEXT_TELEMETRY_DISABLED=1
ENV CI=true

# 构建 Next.js
RUN npm run build

# Stage 2: 运行
FROM node:22-alpine AS runner

WORKDIR /app

# 使用国内 npm 镜像加速
RUN echo "registry=https://registry.npmmirror.com" > /root/.npmrc

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# 复制构建产物
COPY --from=builder /app/package.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/next.config.ts ./

# 只安装生产依赖
RUN npm install --legacy-peer-deps --omit=dev

EXPOSE 3000

CMD ["npm", "start", "--", "-H", "0.0.0.0", "-p", "3000"]
