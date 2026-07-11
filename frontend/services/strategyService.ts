const API = "http://127.0.0.1:8000";

export async function getStrategies() {

    const res = await fetch(`${API}/strategies`);

    if (!res.ok) {

        throw new Error("No se pudieron cargar las estrategias");

    }

    return res.json();

}