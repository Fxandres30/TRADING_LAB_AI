import { api } from "@/lib/http";

export interface Stats {

    operaciones: number;
    ganadas: number;
    perdidas: number;
    profit: number;
    balance: number;
    equity: number;

}

export interface Trade {

    ticket: number;
    symbol: string;
    type: string;
    volume: number;
    price_open: number;
    price_current: number;
    profit: number;
    sl: number;
    tp: number;

}

export function getStats() {

    return api<Stats>("/operations/stats");

}

export function getOpenTrades() {

    return api<Trade[]>("/operations/open");

}