<template>
  <div class="dashboard-container">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="12" :lg="6">
        <el-card class="stat-card">
          <el-statistic :value="stats.totalCandidates">
            <template #title>
              <div class="stat-title">
                <el-icon><User /></el-icon>
                <span>总考生数</span>
              </div>
            </template>
          </el-statistic>
        </el-card>
      </el-col>
      
      <el-col :xs="24" :sm="12" :lg="6">
        <el-card class="stat-card">
          <el-statistic :value="stats.todayExams">
            <template #title>
              <div class="stat-title">
                <el-icon><Calendar /></el-icon>
                <span>今日考试</span>
              </div>
            </template>
          </el-statistic>
        </el-card>
      </el-col>
      
      <el-col :xs="24" :sm="12" :lg="6">
        <el-card class="stat-card">
          <el-statistic :value="stats.passRate" suffix="%">
            <template #title>
              <div class="stat-title">
                <el-icon><TrophyBase /></el-icon>
                <span>通过率</span>
              </div>
            </template>
          </el-statistic>
        </el-card>
      </el-col>
      
      <el-col :xs="24" :sm="12" :lg="6">
        <el-card class="stat-card">
          <el-statistic :value="stats.activeOrgs">
            <template #title>
              <div class="stat-title">
                <el-icon><OfficeBuilding /></el-icon>
                <span>活跃机构</span>
              </div>
            </template>
          </el-statistic>
        </el-card>
      </el-col>
    </el-row>
    
    <el-row :gutter="20" style="margin-top: 20px;">
      <el-col :span="16">
        <el-card>
          <template #header>
            <div class="card-header">
              <span>近期考试安排</span>
              <el-button type="primary" size="small" @click="goToSchedules">
                查看全部
              </el-button>
            </div>
          </template>
          
          <el-table :data="recentExams" stripe>
            <el-table-column prop="date" label="日期" width="120" />
            <el-table-column prop="time" label="时间" width="100" />
            <el-table-column prop="type" label="考试类型">
              <template #default="{ row }">
                <el-tag :type="getExamTypeTag(row.type)">
                  {{ row.type }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="candidates" label="考生数" width="80" />
            <el-table-column prop="status" label="状态" width="80">
              <template #default="{ row }">
                <el-tag :type="getStatusTag(row.status)" size="small">
                  {{ row.status }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column label="操作" width="120">
              <template #default="{ row }">
                <el-button type="text" size="small" @click="viewExam(row)">
                  查看
                </el-button>
                <el-button type="text" size="small" @click="manageExam(row)">
                  管理
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </el-col>
      
      <el-col :span="8">
        <el-card>
          <template #header>
            <span>快捷操作</span>
          </template>
          
          <div class="quick-actions">
            <el-button type="primary" icon="Plus" @click="createExam">
              创建考试
            </el-button>
            <el-button type="success" icon="UserFilled" @click="addCandidate">
              添加考生
            </el-button>
            <el-button type="warning" icon="Calendar" @click="arrangeSchedule">
              安排日程
            </el-button>
            <el-button type="info" icon="DataAnalysis" @click="viewReports">
              查看报表
            </el-button>
            <el-button icon="Upload" @click="importData">
              批量导入
            </el-button>
            <el-button icon="Download" @click="exportData">
              导出数据
            </el-button>
          </div>
        </el-card>
        
        <el-card style="margin-top: 20px;">
          <template #header>
            <span>系统公告</span>
          </template>
          
          <el-timeline>
            <el-timeline-item
              v-for="(notice, index) in notices"
              :key="index"
              :timestamp="notice.time"
              placement="top"
            >
              <el-card>
                <h4>{{ notice.title }}</h4>
                <p>{{ notice.content }}</p>
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const router = useRouter()

const stats = ref({
  totalCandidates: 1234,
  todayExams: 12,
  passRate: 78.5,
  activeOrgs: 25
})

const recentExams = ref([
  {
    id: 1,
    date: '2025-08-16',
    time: '09:00',
    type: '理论考试',
    candidates: 30,
    status: '待开始'
  },
  {
    id: 2,
    date: '2025-08-16',
    time: '14:00',
    type: '实操基础',
    candidates: 15,
    status: '待开始'
  },
  {
    id: 3,
    date: '2025-08-17',
    time: '09:00',
    type: '实操进阶',
    candidates: 10,
    status: '待开始'
  }
])

const notices = ref([
  {
    title: '系统维护通知',
    content: '系统将于本周末进行维护升级',
    time: '2025-08-15 10:00'
  },
  {
    title: '新功能上线',
    content: '微信小程序签到功能已上线',
    time: '2025-08-14 15:00'
  }
])

const getExamTypeTag = (type) => {
  const typeMap = {
    '理论考试': '',
    '实操基础': 'success',
    '实操进阶': 'warning'
  }
  return typeMap[type] || 'info'
}

const getStatusTag = (status) => {
  const statusMap = {
    '待开始': 'info',
    '进行中': 'warning',
    '已完成': 'success'
  }
  return statusMap[status] || ''
}

const goToSchedules = () => {
  router.push('/schedules')
}

const viewExam = (exam) => {
  router.push(`/exams/${exam.id}`)
}

const manageExam = (exam) => {
  router.push(`/exams/${exam.id}/manage`)
}

const createExam = () => {
  router.push('/exams/create')
}

const addCandidate = () => {
  router.push('/users/create')
}

const arrangeSchedule = () => {
  router.push('/schedules/arrange')
}

const viewReports = () => {
  router.push('/reports')
}

const importData = () => {
  ElMessage.info('打开批量导入对话框')
}

const exportData = () => {
  ElMessage.info('开始导出数据')
}

onMounted(() => {
  // Load dashboard data
})
</script>

<style lang="scss" scoped>
.dashboard-container {
  .stat-card {
    .stat-title {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #909399;
      
      .el-icon {
        font-size: 20px;
      }
    }
  }
  
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .quick-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    
    .el-button {
      width: 100%;
    }
  }
}
</style>