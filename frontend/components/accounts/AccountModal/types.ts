export type Account = {

    broker: string;

    company: string;

    login: number;

    server: string;

    balance: number;

    equity: number;

    currency: string;

    name: string;

    path: string;

    connected: boolean;

};

export type Broker = {

    id: string;

    name: string;

    description: string;

    icon: string;

};