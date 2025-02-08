import { defineStore } from 'pinia';

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [] as Array<{ id: number; name: string; quantity: number; price: number;}>,
  }),
  actions: {
    addItem(item: { id: number; name: string; quantity: number; price:number;}) {
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
    get_price(item: { id: number; name: string; quantity: number; price:number;}){
      return (item.quantity * item.price).toFixed(2);
    },
    getTotalPrice() {
      return this.items.reduce((total, item) => total + (item.quantity * item.price), 0).toFixed(2);
    }
  },
});
