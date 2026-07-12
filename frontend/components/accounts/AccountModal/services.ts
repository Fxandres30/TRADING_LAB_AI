import { API_URL } from "@/lib/api";

export async function getAccounts() {

    const res = await fetch(`${API_URL}/brokers/discover`);

    if (!res.ok) {
        return [];
    }

    return await res.json();
}

export async function connectAccount(accountId: string) {

    const res = await fetch(`${API_URL}/accounts/connect`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            account_id: accountId,
        }),
    });

    if (!res.ok) {
        throw new Error("No fue posible conectar la cuenta.");
    }

    return await res.json();
}

export function connectBroker(broker: string) {

    switch (broker) {

        case "deriv":
            window.location.href = `${API_URL}/oauth/deriv/login`;
            break;

        case "mt5":
            alert("Selecciona una cuenta MT5 detectada.");
            break;

        case "binance":
            alert("Próximamente");
            break;

        default:
            alert("Broker no disponible");
    }

}