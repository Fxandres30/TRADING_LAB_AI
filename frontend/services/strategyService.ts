import { API } from "../lib/api";
export async function getStrategies() {

    const res = await fetch(`${API}/api/strategies`);

    if (!res.ok) {

        throw new Error("No se pudieron cargar las estrategias");

    }

    return res.json();

}