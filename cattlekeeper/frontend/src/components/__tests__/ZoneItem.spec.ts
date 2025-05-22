import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ZoneItem from '../farm/ZoneItem.vue'

describe('ZoneItem', () => {
  it('renders properly', () => {
    const wrapper = mount(ZoneItem)
    expect(wrapper.exists()).toBe(true)
  })
})
