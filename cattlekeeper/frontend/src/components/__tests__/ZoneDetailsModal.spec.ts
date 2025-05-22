import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ZoneDetailsModal from '../farm/ZoneDetailsModal.vue'

describe('ZoneDetailsModal', () => {
  it('renders properly', () => {
    const wrapper = mount(ZoneDetailsModal)
    expect(wrapper.exists()).toBe(true)
  })
})
