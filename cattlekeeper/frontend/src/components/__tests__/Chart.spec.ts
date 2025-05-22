import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Chart from '../dashboard/Chart.vue'

describe('Chart', () => {
  it('renders properly', () => {
    const wrapper = mount(Chart)
    expect(wrapper.exists()).toBe(true)
  })
})
