# 🚀 无人机考点管理系统 - 快速使用指南

## 一、系统概述

本系统是一个完整的无人机考点运营管理解决方案，包含：
- **后端API服务**：基于FastAPI的RESTful API
- **PC管理后台**：Vue 3开发的Web管理界面
- **微信小程序**：考生和考务人员使用的移动端

## 二、快速启动（5分钟上手）

### 方法1：使用Docker一键部署（推荐）

```bash
# 1. 克隆项目
git clone https://github.com/codesoldier99/UAV_Exam_Management.git
cd UAV_Exam_Management

# 2. 复制环境配置
cp backend/.env.example backend/.env

# 3. 启动所有服务
docker-compose up -d

# 4. 等待服务启动完成（约30秒）
docker-compose ps
```

### 方法2：本地开发环境

```bash
# 1. 克隆项目
git clone https://github.com/codesoldier99/UAV_Exam_Management.git
cd UAV_Exam_Management

# 2. 安装后端依赖
cd backend
pip install -r requirements.txt

# 3. 安装前端依赖
cd ../admin-frontend
npm install

# 4. 启动服务（使用PM2）
cd ..
npx pm2 start ecosystem.config.js

# 5. 查看服务状态
npx pm2 status
```

## 三、访问系统

### 1. PC管理后台
- **地址**: http://localhost:3000
- **账号**: 
  - 超级管理员: `admin` / `admin123`
  - 考务管理员: `examadmin` / `exam123`
  - 培训机构: `institution` / `inst123`

### 2. API文档
- **地址**: http://localhost:8000/docs
- **说明**: FastAPI自动生成的交互式API文档

### 3. 微信小程序
- 使用微信开发者工具打开 `miniprogram` 目录
- 配置AppID（在小程序管理后台获取）
- 修改 `app.js` 中的 `baseUrl` 为实际服务器地址

## 四、核心功能使用流程

### 1. 管理员初始设置
1. 使用admin账号登录PC后台
2. 进入【考务管理】→【考场管理】添加考场
3. 进入【考务管理】→【考试产品】添加考试类型
4. 进入【用户管理】→【培训机构】添加机构

### 2. 培训机构报名流程
1. 机构用户登录PC后台
2. 进入【考生管理】→【考生列表】
3. 点击【添加考生】单个录入 或
4. 点击【批量导入】上传Excel文件

### 3. 考务排期流程
1. 考务管理员登录PC后台
2. 进入【考务管理】→【排期管理】
3. 选择日期和考生批次
4. 批量生成考试安排

### 4. 考生使用流程
1. 打开微信小程序
2. 输入身份证号登录
3. 查看【我的日程】了解考试安排
4. 在【我的二维码】页面向考务人员展示二维码

### 5. 考务人员签到流程
1. 考务人员登录小程序
2. 进入扫码页面
3. 扫描考生二维码完成签到

## 五、腾讯云部署步骤

### 1. 服务器准备
```bash
# SSH登录服务器
ssh root@your-server-ip

# 克隆项目
git clone https://github.com/codesoldier99/UAV_Exam_Management.git
cd UAV_Exam_Management
```

### 2. 配置环境变量
```bash
# 编辑配置文件
vim backend/.env

# 修改以下配置：
DATABASE_URL=mysql+aiomysql://user:password@localhost:3306/uav_exam
SECRET_KEY=your-production-secret-key
BACKEND_CORS_ORIGINS=["https://your-domain.com"]
```

### 3. 启动服务
```bash
# 使用部署脚本
chmod +x deploy.sh
./deploy.sh
```

### 4. 配置域名
- 在腾讯云控制台配置域名解析
- 配置SSL证书（推荐使用Let's Encrypt）
- 更新Nginx配置指向您的域名

## 六、常见问题解决

### Q1: 数据库连接失败
**解决方案**：
1. 检查MySQL服务是否启动
2. 验证数据库连接字符串
3. 确认用户权限

### Q2: 前端无法访问后端API
**解决方案**：
1. 检查CORS配置
2. 确认API地址配置正确
3. 查看浏览器控制台错误

### Q3: 小程序无法登录
**解决方案**：
1. 检查AppID配置
2. 验证服务器域名白名单
3. 确认后端服务正常运行

### Q4: PM2服务启动失败
**解决方案**：
```bash
# 查看详细日志
npx pm2 logs

# 重启服务
npx pm2 restart all

# 清除日志
npx pm2 flush
```

## 七、数据管理

### 备份数据库
```bash
# MySQL备份
docker exec uav_exam_mysql mysqldump -u root -p uav_exam > backup.sql

# 恢复数据
docker exec -i uav_exam_mysql mysql -u root -p uav_exam < backup.sql
```

### 清理测试数据
```bash
# 进入数据库
docker exec -it uav_exam_mysql mysql -u root -p

# 清理考生数据
DELETE FROM schedules WHERE exam_date < CURDATE();
DELETE FROM candidates WHERE status = 'completed';
```

## 八、性能优化建议

1. **数据库优化**
   - 为常用查询字段添加索引
   - 定期清理过期数据
   - 使用读写分离（大规模部署）

2. **前端优化**
   - 启用Gzip压缩
   - 配置CDN加速
   - 实现懒加载

3. **后端优化**
   - 使用Redis缓存热点数据
   - 实现接口限流
   - 配置负载均衡

## 九、安全建议

1. 修改所有默认密码
2. 配置HTTPS
3. 定期更新依赖包
4. 启用防火墙
5. 定期备份数据
6. 监控系统日志

## 十、技术支持

- **GitHub仓库**: https://github.com/codesoldier99/UAV_Exam_Management
- 查看详细文档：README.md
- 部署指南：DEPLOYMENT.md
- 项目结构：PROJECT_STRUCTURE.md
- API文档：http://localhost:8000/docs

如有问题，请提交Issue或联系技术支持团队。