# UAV Exam Management System - Backend API

## 概述

无人机考点运营与流程管理系统后端API，基于FastAPI构建，提供完整的考试管理、用户认证、考生签到等功能。

## 技术栈

- **框架**: FastAPI
- **数据库**: PostgreSQL / MySQL
- **缓存**: Redis
- **认证**: JWT
- **ORM**: SQLAlchemy
- **任务队列**: Celery (可选)

## 功能特性

- 🔐 **完整的RBAC权限管理**
  - 超级管理员
  - 考点管理员
  - 培训机构管理员
  - 考务人员
  - 考生

- 📝 **考试管理**
  - 考试产品配置
  - 考试场次管理
  - 考生报名
  - 日程安排

- ✅ **签到管理**
  - 动态二维码生成
  - 多节点签到
  - 实时状态更新

- 📊 **数据看板**
  - 实时考场状态
  - 排队信息
  - 统计分析

## 快速开始

### 1. 环境要求

- Python 3.11+
- PostgreSQL 14+ 或 MySQL 8+
- Redis 6+

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 到 `.env` 并修改配置：

```bash
cp .env.example .env
```

### 4. 初始化数据库

```bash
python -m app.db.init_db
```

### 5. 运行服务

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 6. 使用Docker

```bash
docker-compose up -d
```

## API文档

启动服务后访问：
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## 项目结构

```
app/
├── api/           # API路由
│   ├── v1/       # API版本1
│   └── deps.py   # 依赖注入
├── core/         # 核心配置
├── db/           # 数据库
├── models/       # 数据模型
├── schemas/      # Pydantic模型
├── services/     # 业务逻辑
└── utils/        # 工具函数
```

## 默认账号

- **超级管理员**
  - 邮箱: admin@example.com
  - 密码: admin123456

## 部署说明

### 腾讯云部署

1. 准备服务器（推荐配置）
   - CPU: 2核+
   - 内存: 4GB+
   - 硬盘: 40GB+

2. 安装Docker和Docker Compose

3. 配置Nginx反向代理

4. 配置SSL证书

5. 设置防火墙规则

## License

MIT