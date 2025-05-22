import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import IncomesBatchChart from '../dashboard/IncomesBatchChart.vue'

describe('IncomesBatchChart', () => {
  it('renders properly', () => {
    const wrapper = mount(IncomesBatchChart)
    expect(wrapper.exists()).toBe(true)
  })
})
