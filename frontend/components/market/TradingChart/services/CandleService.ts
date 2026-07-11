const API = "http://127.0.0.1:8000";

export interface Candle {

    time: number;

    open: number;

    high: number;

    low: number;

    close: number;

}

export class CandleService {

    static async getHistory(

        symbol: string,

        timeframe: string

    ): Promise<Candle[]> {

        const response = await fetch(

            `${API}/api/market/history?symbol=${symbol}&timeframe=${timeframe}`

        );

        if (!response.ok) {

            throw new Error(`Error ${response.status}`);

        }

        return await response.json();

    }

}