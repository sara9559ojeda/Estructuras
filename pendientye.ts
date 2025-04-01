class Dish {
    private name: string;
    private price: string;
    private description: string;

    constructor(name: string, price: string, description: string) {
        this.name = name;
        this.price = price;
        this.description = description;
    }

    getname(): string {
        return this.name;
    }
}
class Order{
    private dishes: Dish[]=[];
    private isServed: boolean = false;
    private isCanceled: boolean = false;

    createOrder(plato:Dish): void{
        this.dishes.push(plato);
    }
    orderConfirmated(): boolean{
        if (Dish.length==0) {
            
        } else {
            
        }
        return
    }

}


