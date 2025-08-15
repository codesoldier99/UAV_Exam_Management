<template>
  <div class="login-container">
    <el-card class="login-card">
      <template #header>
        <div class="card-header">
          <h2>无人机考点管理系统</h2>
          <p>考点运营与流程管理平台</p>
        </div>
      </template>
      
      <el-form
        ref="loginFormRef"
        :model="loginForm"
        :rules="loginRules"
        label-position="top"
        @submit.prevent="handleLogin"
      >
        <el-form-item label="用户名/邮箱" prop="username">
          <el-input
            v-model="loginForm.username"
            placeholder="请输入用户名或邮箱"
            prefix-icon="User"
            size="large"
          />
        </el-form-item>
        
        <el-form-item label="密码" prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            placeholder="请输入密码"
            prefix-icon="Lock"
            size="large"
            show-password
          />
        </el-form-item>
        
        <el-form-item>
          <el-checkbox v-model="rememberMe">记住我</el-checkbox>
        </el-form-item>
        
        <el-form-item>
          <el-button
            type="primary"
            size="large"
            :loading="loading"
            @click="handleLogin"
            style="width: 100%"
          >
            {{ loading ? '登录中...' : '登 录' }}
          </el-button>
        </el-form-item>
      </el-form>
      
      <div class="login-footer">
        <el-divider>测试账号</el-divider>
        <div class="test-accounts">
          <el-tag @click="fillTestAccount('admin')" style="cursor: pointer;">
            超级管理员
          </el-tag>
          <el-tag @click="fillTestAccount('site')" style="cursor: pointer;" type="success">
            考点管理员
          </el-tag>
          <el-tag @click="fillTestAccount('org')" style="cursor: pointer;" type="warning">
            机构管理员
          </el-tag>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessage } from 'element-plus'

const router = useRouter()
const userStore = useUserStore()

const loginFormRef = ref()
const loading = ref(false)
const rememberMe = ref(false)

const loginForm = reactive({
  username: '',
  password: ''
})

const loginRules = {
  username: [
    { required: true, message: '请输入用户名或邮箱', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }
  ]
}

const handleLogin = async () => {
  const valid = await loginFormRef.value.validate()
  if (!valid) return
  
  loading.value = true
  try {
    await userStore.login(loginForm)
    if (rememberMe.value) {
      localStorage.setItem('rememberedUser', loginForm.username)
    }
  } finally {
    loading.value = false
  }
}

const fillTestAccount = (type) => {
  const accounts = {
    admin: { username: 'admin@example.com', password: 'admin123456' },
    site: { username: 'site@example.com', password: 'site123456' },
    org: { username: 'org@example.com', password: 'org123456' }
  }
  
  const account = accounts[type]
  if (account) {
    loginForm.username = account.username
    loginForm.password = account.password
    ElMessage.info(`已填充${type === 'admin' ? '超级管理员' : type === 'site' ? '考点管理员' : '机构管理员'}账号`)
  }
}

// Load remembered username
const rememberedUser = localStorage.getItem('rememberedUser')
if (rememberedUser) {
  loginForm.username = rememberedUser
  rememberMe.value = true
}
</script>

<style lang="scss" scoped>
.login-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  
  .login-card {
    width: 420px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    
    .card-header {
      text-align: center;
      
      h2 {
        margin: 0;
        color: #303133;
        font-size: 24px;
      }
      
      p {
        margin: 8px 0 0;
        color: #909399;
        font-size: 14px;
      }
    }
    
    .login-footer {
      margin-top: 20px;
      
      .test-accounts {
        display: flex;
        justify-content: space-around;
        margin-top: 16px;
      }
    }
  }
}
</style>