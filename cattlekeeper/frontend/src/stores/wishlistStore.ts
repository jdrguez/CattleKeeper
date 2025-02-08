import { defineStore } from 'pinia';

export const useWishlistStore = defineStore({
  id: 'wishlist',
  state: () => ({
    items: [] as Array<{ id: number; name: string; price: number;}>,
  }),
  actions: {
    addItem(item: { id: number; name: string; price:number;}) {
      if (!this.items.find(existingItem => existingItem.id === item.id)) {
        this.items.push(item);
      }
    },
    removeItem(itemId: number) {
      this.items = this.items.filter(item => item.id !== itemId);
    },
    clearWishlist() {
      this.items = [];
    },
    get_total(){
        return this.items.length
    }
  },
  getters: {
    itemCount: (state) => state.items.length,
  },

});