import { createStore } from "vuex";

let C = 0;
export class MyStore {
	count:number = 0; 
	constructor() { 
		if(this.count<C){
			this.count = C;
		}
	}  
	getCount(){
		return this.count;
	}
	addCount(){
		this.count++;
		if(C<this.count){
			C = this.count;
		}
	}
    
}