<template>
  <div class="page-container">
    <h1 class="page-title">Download PDF Report</h1>
    
    <div class="form-content">
      <div class="form-grid">
        <div class="form-group">
          <label class="form-label">Report Type <span class="text-danger">*</span></label>
          <select v-model="reportType" class="form-select" required>
            <option value="current">Current Period</option>
            <option value="custom">Custom Period</option>
          </select>
        </div>

        <div class="form-group" v-if="reportType === 'custom'">
          <label class="form-label">Month <span class="text-danger">*</span></label>
          <select v-model="selectedMonth" class="form-select" :required="reportType === 'custom'">
            <option v-for="month in months" :value="month.value" :key="month.value">
              {{ month.label }}
            </option>
          </select>
        </div>

        <div class="form-group" v-if="reportType === 'custom'">
          <label class="form-label">Year <span class="text-danger">*</span></label>
          <select v-model="selectedYear" class="form-select" :required="reportType === 'custom'">
            <option v-for="year in years" :value="year" :key="year">
              {{ year }}
            </option>
          </select>
        </div>
      </div>

      <div class="form-actions">
        <button 
          @click="generateReport" 
          class="btn btn-primary"
          :disabled="loading"
        >
          <span v-if="loading">
            <i class="fas fa-spinner fa-spin me-2"></i> Generating...
          </span>
          <span v-else>
            <i class="fas fa-file-pdf me-2"></i> Generate Report
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import api from '@/api/axios'

const toast = useToast()
const loading = ref(false)

const reportType = ref('current')
const selectedMonth = ref((new Date().getMonth() + 1).toString())
const selectedYear = ref(new Date().getFullYear().toString())

const months = ref([
  { value: '1', label: 'January' },
  { value: '2', label: 'February' },
  { value: '3', label: 'March' },
  { value: '4', label: 'April' },
  { value: '5', label: 'May' },
  { value: '6', label: 'June' },
  { value: '7', label: 'July' },
  { value: '8', label: 'August' },
  { value: '9', label: 'September' },
  { value: '10', label: 'October' },
  { value: '11', label: 'November' },
  { value: '12', label: 'December' }
])

const years = ref([])
onMounted(() => {
  const currentYear = new Date().getFullYear()
  for (let i = 0; i < 6; i++) {
    years.value.push((currentYear - i).toString())
  }
})

const generateReport = async () => {
  try {
    loading.value = true
    
    const params = {}
    if (reportType.value === 'custom') {
      params.year = selectedYear.value
      params.month = selectedMonth.value
    }
    
    await api.get('api/stats/report/pdf/', { params })

    toast.success('Report has been sent to your email successfully')
  } catch (error) {
    console.error('Error generating report:', error)
    if (error.response && error.response.status === 402) {
      toast.error('Subscription required to generate reports')
    } else {
      toast.error('Failed to send report. Please try again.')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.page-container {
  margin: 2rem auto;
  background: #fff;
  padding: 2rem 2.5rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2d3a45;
}

.page-title {
  font-size: 2.1rem;
  font-weight: 700;
  border-bottom: 3px solid #28a745;
  padding-bottom: 0.3rem;
  margin-bottom: 1.8rem;
  letter-spacing: 0.03em;
}

.form-content {
  background: #f6f9fc;
  padding: 2rem;
  border-radius: 14px;
  box-shadow: inset 2px 2px 6px #d9e6f0, inset -2px -2px 6px #ffffff;
}

.btn {
  padding: 0.55rem 1.6rem;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: white;
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.5);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #1d4ed8, #2563eb);
  box-shadow: 0 8px 24px rgba(37, 99, 235, 0.8);
}

.text-muted {
  color: #6b7280;
}
.page-container {
  margin: 2rem auto;
  background: #fff;
  padding: 2rem 2.5rem;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2d3a45;
}

.page-title {
  font-size: 2.1rem;
  font-weight: 700;
  border-bottom: 3px solid #28a745;
  padding-bottom: 0.3rem;
  margin-bottom: 1.8rem;
  letter-spacing: 0.03em;
}

.form-content {
  background: #f6f9fc;
  padding: 2rem;
  border-radius: 14px;
  box-shadow: inset 2px 2px 6px #d9e6f0, inset -2px -2px 6px #ffffff;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #34495e;
}

.form-select {
  width: 100%;
  padding: 0.5rem 1rem;
  border: 2px solid #cbd5e1;
  border-radius: 12px;
  background: #f9fafb;
  transition: all 0.3s ease;
}

.form-select:focus {
  outline: none;
  border-color: #28a745;
  box-shadow: 0 0 8px #33d459;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  padding-top: 1rem;
  border-top: 2px solid #d4edda;
}

.btn {
  padding: 0.55rem 1.6rem;
  font-weight: 700;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  color: white;
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.5);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #1d4ed8, #2563eb);
  box-shadow: 0 8px 24px rgba(37, 99, 235, 0.8);
}

.btn-primary:disabled {
  background: #cbd5e1;
  box-shadow: none;
  cursor: not-allowed;
}

.text-danger {
  color: #e53e3e;
}
</style>