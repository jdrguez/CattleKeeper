import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import NavButton from '../NavButton.vue'

describe('NavButton', () => {
  it('renders properly', () => {
    const wrapper = mount(NavButton)
    expect(wrapper.exists()).toBe(true)
  })
})
