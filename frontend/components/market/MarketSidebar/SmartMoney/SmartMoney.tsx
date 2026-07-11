import "./SmartMoney.css";

export default function SmartMoney() {

    return (

        <section className="market-card">

            <div className="card-header">
                <h3>🧠 Smart Money</h3>
            </div>

            <div className="card-content">

                <div className="info-row">
                    <span>BOS</span>
                    <strong className="green">Detectado</strong>
                </div>

                <div className="info-row">
                    <span>CHoCH</span>
                    <strong>Pendiente</strong>
                </div>

                <div className="info-row">
                    <span>Order Blocks</span>
                    <strong>3</strong>
                </div>

                <div className="info-row">
                    <span>Fair Value Gap</span>
                    <strong>2</strong>
                </div>

                <div className="info-row">
                    <span>Liquidity Sweep</span>
                    <strong className="green">Sí</strong>
                </div>

                <div className="info-row">
                    <span>Mitigation</span>
                    <strong>No</strong>
                </div>

            </div>

        </section>

    );

}