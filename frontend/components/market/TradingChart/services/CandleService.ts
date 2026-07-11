import { API } from "@/lib/api";

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

    const url =
      `${API}/api/market/history?symbol=${encodeURIComponent(symbol)}&timeframe=${encodeURIComponent(timeframe)}`;

    console.log("GET:", url);

    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(
        `Error ${response.status}: ${await response.text()}`
      );
    }

    return response.json();
  }
}