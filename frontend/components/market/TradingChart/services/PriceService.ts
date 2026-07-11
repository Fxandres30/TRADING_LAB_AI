const API = "http://127.0.0.1:8000";

export interface Price {

    bid:number;

    ask:number;

    spread:number;

}

export class PriceService{

    static async getPrice(symbol:string):Promise<Price>{

        const res=await fetch(

            `${API}/api/chart/price?symbol=${symbol}`

        );

        return await res.json();

    }

}