import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ProductionChart from '../dashboard/ProductionChart.vue'

describe('ProductionChart', () => {
  it('renders properly', () => {
    const wrapper = mount(ProductionChart)
    expect(wrapper.exists()).toBe(true)
  })
})
