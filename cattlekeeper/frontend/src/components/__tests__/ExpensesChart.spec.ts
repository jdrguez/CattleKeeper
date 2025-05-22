import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ExpensesChart from '../dashboard/ExpensesChart.vue'

describe('ExpensesChart', () => {
  it('renders properly', () => {
    const wrapper = mount(ExpensesChart)
    expect(wrapper.exists()).toBe(true)
  })
})
