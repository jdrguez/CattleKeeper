import { defineStore } from 'pinia';
import { errorMessages } from 'vue/compiler-sfc';

export const useOrderStore = defineStore('order', {
  state: () => ({
    orders: [] as Array<{
      id: number;
      items: Array<{ id: number; name: string; quantity: number; price: number; }>;
      totalPrice: number;
      createdAt: Date;
    }>,
  }),
  actions: {
    addOrder(cartItems: Array<{ id: number; name: string; quantity: number; price: number; }>, totalPrice: number) {
      const newOrder = {
        id: this.orders.length + 1, 
        items: cartItems,
        totalPrice: totalPrice,
        createdAt: new Date(),
      };
      this.orders.push(newOrder);
    },
    getOrders() {
      return this.orders;
    },
    clearOrders() {
      this.orders = [];
    },
    getTotalOrders(){
        return this.orders.length
    },
    get_order(id:number | any) {
      for (const order of this.orders){
        if (order.id == id){
          return order
        }
      }
    }
  },
});