import { API } from "./api";

export async function obtenerDashboard() {

    console.log("API:", API);

    try {

        const res = await fetch(`${API}/system/status`);

        console.log(res);

        if (!res.ok) {
            throw new Error(await res.text());
        }

        return await res.json();

    } catch (e) {

        console.error("ERROR FETCH", e);

        throw e;
    }
}