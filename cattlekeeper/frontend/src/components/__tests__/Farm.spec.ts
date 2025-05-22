import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import Farm from '../farm/Farm.vue'

describe('Farm', () => {
  it('renders properly', () => {
    const wrapper = mount(Farm)
    expect(wrapper.exists()).toBe(true)
  })
})
