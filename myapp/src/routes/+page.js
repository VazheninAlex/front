export async function load({ fetch }) {
    let res = await fetch('https://atlasserver-4-h4944389.deta.app/sensor', {
        method: "GET",
        headers: {
            "X-API-Key": "c0Pqf8Wkg92y_U3JHBztTUhD1ZQwVCB78gjVYauoeqXt8"
        }
    })
    if (res.ok) {
        return {
            props: {
                data: await res.json()
            }
        };
    }
    return {
        status: res.status,
        error: new Error()
    };
}