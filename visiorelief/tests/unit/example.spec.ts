import { mount } from '@vue/test-utils'
import Tab1Page from '../../src/views/Tab1SettingsPage.vue'
import { describe, expect, test } from 'vitest'

describe('Tab1SettingsPage.vue', () => {
  test('renders tab 1 Tab1Page', () => {
    const wrapper = mount(Tab1Page)
    expect(wrapper.text()).toMatch('Tab 1 page')
  })
})
