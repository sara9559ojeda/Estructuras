class Queue{
    private elements: T[]=[]
  
    isEmpty():boolean{
      return this.elements.length ==0;
    }
    enqueue(T:number): void{
      this.elements.push(T);
    }
    dequeue(): number | undefined{
      return this.elements.shift();
    }
    front(): number{
      return this.elements[0];
    }
    rear(): number{
             return this.elements[this.size() -1];
    }
    size(): number{
      return this.elements.length;
    }
  }
  
  const queue = new Queue();
  
  queue.enqueue(10);
  queue.enqueue(20);
  queue.enqueue(30);
  queue.enqueue(40);
  queue.enqueue(50);
  
  console.log('size queue: ', queue.size());
  console.log('size queue: ', queue.front());
  console.log('size queue: ', queue.rear());
  
  console.log('elementos eliminados: ');
  
  
  while(!queue.isEmpty()){
  console.log(queue.dequeue());
  }
  
  console.log('size: ', queue.size());