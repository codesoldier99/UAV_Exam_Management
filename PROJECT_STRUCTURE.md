# 无人机考点管理系统 - 项目结构说明

## 📁 完整文件结构

```
/home/user/webapp/uav-exam-complete/
│
├── 📂 backend/                    # FastAPI后端服务
│   ├── 📂 app/
│   │   ├── 📂 api/               # API接口
│   │   │   ├── 📂 v1/            # API版本1
│   │   │   │   ├── auth.py      # 认证接口
│   │   │   │   ├── candidates.py # 考生管理接口
│   │   │   │   └── schedules.py  # 排期管理接口
│   │   │   └── deps.py          # 依赖注入
│   │   │
│   │   ├── 📂 core/              # 核心配置
│   │   │   ├── config.py        # 系统配置
│   │   │   └── security.py      # 安全/加密
│   │   │
│   │   ├── 📂 db/                # 数据库
│   │   │   ├── base.py          # 数据库基类
│   │   │   ├── session.py       # 数据库会话
│   │   │   └── init_db.py       # 初始化数据
│   │   │
│   │   ├── 📂 models/            # 数据模型
│   │   │   ├── user.py          # 用户模型
│   │   │   ├── institution.py   # 机构模型
│   │   │   ├── exam.py          # 考试产品模型
│   │   │   ├── candidate.py     # 考生模型
│   │   │   └── schedule.py      # 排期模型
│   │   │
│   │   ├── 📂 schemas/           # Pydantic模式
│   │   │   ├── user.py          # 用户模式
│   │   │   ├── candidate.py     # 考生模式
│   │   │   └── schedule.py      # 排期模式
│   │   │
│   │   └── main.py               # 主应用入口
│   │
│   ├── requirements.txt          # Python依赖
│   ├── Dockerfile               # Docker配置
│   ├── .env.example             # 环境变量示例
│   └── .env                     # 实际环境配置
│
├── 📂 admin-frontend/            # Vue 3 PC管理后台
│   ├── 📂 src/
│   │   ├── 📂 api/              # API调用
│   │   │   ├── config.js        # API配置
│   │   │   ├── auth.js          # 认证API
│   │   │   └── candidates.js    # 考生API
│   │   │
│   │   ├── 📂 views/            # 页面组件
│   │   │   ├── Login.vue        # 登录页
│   │   │   ├── Dashboard.vue    # 仪表板
│   │   │   └── Candidates.vue   # 考生管理
│   │   │
│   │   ├── 📂 layouts/          # 布局组件
│   │   │   └── MainLayout.vue   # 主布局
│   │   │
│   │   ├── 📂 router/           # 路由配置
│   │   │   └── index.js
│   │   │
│   │   ├── 📂 stores/           # Pinia状态管理
│   │   │   └── auth.js          # 认证状态
│   │   │
│   │   ├── App.vue              # 根组件
│   │   └── main.js              # 入口文件
│   │
│   ├── package.json             # 项目依赖
│   ├── vite.config.js           # Vite配置
│   ├── Dockerfile               # Docker配置
│   └── nginx.conf               # Nginx配置
│
├── 📂 miniprogram/              # 微信小程序
│   ├── 📂 pages/                # 页面
│   │   ├── 📂 login/            # 登录页
│   │   ├── 📂 candidate/        # 考生功能
│   │   │   ├── 📂 home/         # 首页
│   │   │   ├── 📂 qrcode/       # 二维码
│   │   │   └── 📂 schedule/     # 日程
│   │   ├── 📂 staff/            # 考务人员
│   │   │   └── 📂 scan/         # 扫码
│   │   └── 📂 public/           # 公共页面
│   │       └── 📂 board/        # 考场看板
│   │
│   ├── app.js                   # 小程序入口
│   ├── app.json                 # 小程序配置
│   └── app.wxss                 # 全局样式
│
├── 📄 docker-compose.yml        # Docker编排
├── 📄 ecosystem.config.js       # PM2配置
├── 📄 deploy.sh                 # 部署脚本
├── 📄 start-dev.sh              # 开发启动脚本
├── 📄 README.md                 # 项目说明
├── 📄 DEPLOYMENT.md             # 部署指南
└── 📄 PROJECT_STRUCTURE.md      # 本文件

```

## 🔧 技术栈详情

### 后端技术
- **框架**: FastAPI (Python 3.10+)
- **数据库**: MySQL 8.0 / SQLite (测试)
- **ORM**: SQLAlchemy 2.0
- **认证**: JWT (python-jose)
- **异步**: asyncio + aiofiles
- **缓存**: Redis (可选)

### 前端技术
- **框架**: Vue 3 + Vite
- **UI库**: Element Plus
- **状态管理**: Pinia
- **路由**: Vue Router 4
- **HTTP客户端**: Axios

### 小程序技术
- **框架**: 原生微信小程序
- **UI**: 自定义组件
- **数据请求**: wx.request API

### 部署技术
- **容器化**: Docker + Docker Compose
- **进程管理**: PM2
- **反向代理**: Nginx
- **数据库**: MySQL 8.0 + Redis

## 📦 核心模块说明

### 1. 用户权限系统 (RBAC)
- 超级管理员：系统所有权限
- 考务管理员：考务排期、场地管理
- 培训机构：考生报名、查看本机构数据
- 考务人员：扫码签到
- 考生：查看日程、显示二维码

### 2. 考生管理模块
- 单个录入/批量导入
- 状态跟踪（待排期→已排期→考试中→完成）
- 数据隔离（机构只能看自己的考生）

### 3. 考务排期模块
- 批量排期功能
- 按机构分组安排
- 自动计算时间段
- 实时队列管理

### 4. 移动端功能
- 考生二维码生成与展示
- 考务人员扫码签到
- 实时排队状态
- 公共考场看板

## 🚀 快速开始

### 开发环境启动
```bash
cd /home/user/webapp/uav-exam-complete
./start-dev.sh
```

### 生产环境部署
```bash
cd /home/user/webapp/uav-exam-complete
./deploy.sh
```

### 访问地址
- PC管理后台: http://localhost:3000
- API文档: http://localhost:8000/docs
- 小程序: 使用微信开发者工具打开miniprogram目录

## 📝 默认账号
- 超级管理员: admin / admin123
- 考务管理员: examadmin / exam123
- 培训机构: institution / inst123