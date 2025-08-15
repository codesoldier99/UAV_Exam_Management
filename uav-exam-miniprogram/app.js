// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 获取用户信息
    this.getUserInfo()
    
    // 获取系统信息
    this.globalData.systemInfo = wx.getSystemInfoSync()
  },

  getUserInfo() {
    // 查看是否授权
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              this.globalData.userInfo = res.userInfo
              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },

  // 登录
  login() {
    return new Promise((resolve, reject) => {
      wx.login({
        success: res => {
          if (res.code) {
            // 发送 res.code 到后台换取 openId, sessionKey, unionId
            wx.request({
              url: this.globalData.baseUrl + '/api/v1/auth/wechat/login',
              method: 'POST',
              data: {
                code: res.code
              },
              success: res => {
                if (res.statusCode === 200) {
                  this.globalData.token = res.data.access_token
                  this.globalData.userInfo = res.data.user
                  wx.setStorageSync('token', res.data.access_token)
                  wx.setStorageSync('userInfo', res.data.user)
                  resolve(res.data)
                } else {
                  reject(res.data)
                }
              },
              fail: err => {
                reject(err)
              }
            })
          } else {
            reject('登录失败！' + res.errMsg)
          }
        },
        fail: err => {
          reject(err)
        }
      })
    })
  },

  // 检查登录状态
  checkLogin() {
    const token = wx.getStorageSync('token')
    if (!token) {
      wx.redirectTo({
        url: '/pages/login/login'
      })
      return false
    }
    return true
  },

  // 请求封装
  request(options) {
    const token = wx.getStorageSync('token')
    
    return new Promise((resolve, reject) => {
      wx.request({
        ...options,
        url: this.globalData.baseUrl + options.url,
        header: {
          ...options.header,
          'Authorization': token ? `Bearer ${token}` : ''
        },
        success: res => {
          if (res.statusCode === 401) {
            // Token过期，重新登录
            wx.removeStorageSync('token')
            wx.removeStorageSync('userInfo')
            wx.redirectTo({
              url: '/pages/login/login'
            })
            reject('认证失败，请重新登录')
          } else if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve(res.data)
          } else {
            wx.showToast({
              title: res.data?.detail || '请求失败',
              icon: 'none'
            })
            reject(res.data)
          }
        },
        fail: err => {
          wx.showToast({
            title: '网络错误',
            icon: 'none'
          })
          reject(err)
        }
      })
    })
  },

  globalData: {
    userInfo: null,
    token: null,
    baseUrl: 'https://api.uavexam.com', // 生产环境API地址
    // baseUrl: 'http://localhost:8000', // 开发环境API地址
    systemInfo: null
  }
})