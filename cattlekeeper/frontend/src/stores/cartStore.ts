import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as Array<{ id: number; name: string; quantity: number }>,
  }),
  actions: {
    addItem(item: { id: number; name: string; quantity: number }) {
      const existingItem = this.items.find(i => i.id === item.id);
      if (existingItem) {
        existingItem.quantity += item.quantity;
      } else {
        this.items.push(item);
      }
    },
    getTotalItems() {
      return this.items.reduce((total, item) => total + item.quantity, 0);
    },
  },
});
