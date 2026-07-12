import { API } from "@/lib/api";

export interface Price {
    bid: number;
    ask: number;
    spread: number;
}

export class PriceService {

    static async getPrice(symbol: string): Promise<Price> {

        const res = await fetch(

            `${API}/api/market/tick/${encodeURIComponent(symbol)}`

        );

        if (!res.ok) {
            throw new Error(await res.text());
        }

        return await res.json();

    }

}